# Pilot sizing -- P(H1 rule passes) per k

Rule: pass iff the paired mean `RD > -0.05` (PREREGISTRATION sec. 5.1). Each cell resamples its own pilot differences (empirical, no shift). 10000 simulations per entry at seed 20260904; `±` is the Monte Carlo standard error. This is the probability of the implemented verdict, not an alpha-controlled power.

| disruption | model | n_pilot | pilot_rd | pilot_verdict | share_losing | p_k3 | p_k6 | p_k10 | p_k20 | p_k30 | p_k50 | p_k100 | p_k200 | k_for_0.80 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | deepseek-v4-pro:0813-cloud | 3 | -0.0667 | fail | 0.667 | 0.262+/-0.004 | 0.098+/-0.003 | 0.080+/-0.003 | 0.038+/-0.002 | 0.022+/-0.001 | 0.006+/-0.001 | 0.000+/-0.000 | 0.000 | > 200 |
| closed_loop | glm-5.2:cloud | 6 | -0.1 | fail | 0.333 | 0.518+/-0.005 | 0.302+/-0.005 | 0.160+/-0.004 | 0.094+/-0.003 | 0.052+/-0.002 | 0.018+/-0.001 | 0.001+/-0.000 | 0.000 | > 200 |
| closed_loop | minimax-m3:cloud | 4 | -0.75 | fail | 1.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | > 200 |
| road_closure | deepseek-v4-pro:0813-cloud | 3 | -0.5 | fail | 0.667 | 0.033+/-0.002 | 0.001+/-0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | > 200 |
| road_closure | glm-5.2:cloud | 6 | -0.5 | fail | 0.833 | 0.005+/-0.001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | > 200 |
