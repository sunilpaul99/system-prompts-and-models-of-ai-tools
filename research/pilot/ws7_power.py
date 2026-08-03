#!/usr/bin/env python3
"""WS7 / PROTOCOL §8.2: power realism simulation, lexical family (H1-L).

Question the protocol asks: what is the MINIMUM DETECTABLE RATE RATIO at
n=24 hosts (and the n=18 floor)? If it exceeds 2.0, §8.2 requires design
revision before freeze.

Inputs are pilot-measured, not assumed (DAILY_BRIEF cycle 74, QA-clean):
  - baseline fingerprint rate  : 7.6 / 100k host words
  - host words per episode     : median ~5.0k (interview formats)
  - episodes per host-period   : 5 (PROTOCOL §3.4)  -> ~25k words/period
  - periods                    : 7 pre (2019H1-2022H1), 6 post (2023H2-2026H1)

Model (mirrors PROTOCOL §7): counts ~ NegBin(mu, k) with
  log mu = log(words) + host_effect + period_effect + beta*USE*POST
Inference: randomisation test — permute exposure labels across hosts,
10,000 draws, two-sided, alpha=.05. Power = P(reject) over sims.

Host heterogeneity: the pilot has only TWO interview hosts, so the
observed between-host spread is not a usable variance estimate. We
therefore sweep a range of plausible dispersions and report power as a
function of it, rather than quoting one number from n=2. This is stated
as a limitation, not hidden behind a point estimate.
"""
import json, sys
import numpy as np

BASE_RATE = 7.6e-5          # per host word (QA-clean pilot measurement)
WORDS_PER_PERIOD = 25_000   # 5 episodes x ~5k host words
N_PRE, N_POST = 7, 6

def simulate(n_hosts, rr, sd_host, nb_k, n_sims, n_perm, rng):
    """Return empirical power for a given true rate ratio."""
    half = n_hosts // 2
    rejects = 0
    for _ in range(n_sims):
        use = np.zeros(n_hosts, dtype=bool); use[:half] = True
        host_eff = rng.normal(0, sd_host, n_hosts)
        counts = np.zeros((n_hosts, N_PRE + N_POST))
        for i in range(n_hosts):
            for t in range(N_PRE + N_POST):
                post = t >= N_PRE
                mu = BASE_RATE * WORDS_PER_PERIOD * np.exp(host_eff[i])
                if use[i] and post: mu *= rr
                # negative binomial via gamma-poisson mixture
                lam = rng.gamma(nb_k, mu / nb_k) if nb_k > 0 else mu
                counts[i, t] = rng.poisson(lam)
        stat = did(counts, use)
        null = np.empty(n_perm)
        for p in range(n_perm):
            perm = rng.permutation(n_hosts)
            null[p] = did(counts, use[perm])
        if (np.abs(null) >= abs(stat)).mean() < 0.05:
            rejects += 1
    return rejects / n_sims

def did(counts, use):
    """Difference-in-differences on log rates (offset constant across cells)."""
    pre, post = counts[:, :N_PRE].sum(1), counts[:, N_PRE:].sum(1)
    # +0.5 continuity correction; sparse cells are the whole problem here
    lr = np.log((post + 0.5) / N_POST) - np.log((pre + 0.5) / N_PRE)
    return lr[use].mean() - lr[~use].mean()

def main(n_sims="400", n_perm="600"):
    rng = np.random.default_rng(20260803)
    n_sims, n_perm = int(n_sims), int(n_perm)
    exp_count = BASE_RATE * WORDS_PER_PERIOD
    print(f"Expected fingerprint count per host-period: {exp_count:.2f}")
    print(f"  (baseline {BASE_RATE*1e5:.1f}/100k x {WORDS_PER_PERIOD:,} words)")
    print(f"  pre-period total per host: {exp_count*N_PRE:.1f}, post: {exp_count*N_POST:.1f}\n")
    results = {}
    for n_hosts in (24, 18):
        for sd_host in (0.3, 0.6):
            for nb_k in (5.0,):          # moderate overdispersion
                row = {}
                for rr in (1.5, 2.0, 3.0, 4.0):
                    pw = simulate(n_hosts, rr, sd_host, nb_k, n_sims, n_perm, rng)
                    row[rr] = pw
                results[f"n{n_hosts}_sd{sd_host}"] = row
                cells = " ".join(f"RR={rr}:{p:.2f}" for rr, p in row.items())
                print(f"n={n_hosts}, host SD={sd_host}: {cells}")
    json.dump({"base_rate_per_100k": BASE_RATE*1e5,
               "words_per_period": WORDS_PER_PERIOD,
               "expected_count_per_period": exp_count,
               "power": {k: {str(r): v for r, v in row.items()}
                         for k, row in results.items()}},
              open("ws7_power_results.json", "w"), indent=1)
    print("\nPower >= 0.80 is the conventional bar; §8.2 fails the design if the")
    print("minimum detectable RR exceeds 2.0.")

if __name__ == "__main__":
    main(*sys.argv[1:])
