# Sweep summary

## Runs included

| total | eligible | censored | unscored | invalid_model_binding |
| --- | --- | --- | --- | --- |
| 34 | 34 | 0 | 0 | 0 |

Censored runs were stopped before their flood deadline was decided and cannot be scored without recording the harness's impatience as the system's failure (`evaluation/thresholds.py`, `CENSORING_MARGIN_SIM_S`).

## Recovery-level distribution

| system | model | scenario | n | level_0 | level_1 | level_2 | level_3 | level_4 | median_level | ceiling_below_nominal | mean_completeness_vs_nominal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agentic | deepseek-v4-pro:0813-cloud | agentic_closed_loop | 3 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 0.9333 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_road_closure | 3 | 1 | 0 | 1 | 1 | 0 | 2 | 0 | 0.5 |
| agentic | glm-5.2:cloud | agentic_closed_loop | 6 | 0 | 0 | 2 | 0 | 4 | 4 | 0 | 0.9 |
| agentic | glm-5.2:cloud | agentic_road_closure | 6 | 1 | 0 | 4 | 1 | 0 | 2 | 0 | 0.5 |
| agentic | minimax-m3:cloud | agentic_closed_loop | 4 | 2 | 0 | 2 | 0 | 0 | 2 | 0 | 0.25 |
| baseline |  | baseline_closed_loop | 6 | 0 | 0 | 0 | 0 | 6 | 4 | 0 | 1.0 |
| baseline |  | baseline_road_closure | 6 | 0 | 0 | 0 | 6 | 0 | 3 | 6 | 0.6 |

`ceiling_below_nominal` counts runs whose feasibility ceiling fell below 100 because the shelters they heard from declared fewer beds. For those runs `completeness` flatters the outcome, so `mean_completeness_vs_nominal` is reported beside it.

## Stochastic dominance (by model, within scenario)

| scenario | a | b | n_a | n_b | dominates |
| --- | --- | --- | --- | --- | --- |
| agentic_closed_loop | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 3 | 6 | glm-5.2:cloud |
| agentic_closed_loop | deepseek-v4-pro:0813-cloud | minimax-m3:cloud | 3 | 4 | deepseek-v4-pro:0813-cloud |
| agentic_closed_loop | glm-5.2:cloud | minimax-m3:cloud | 6 | 4 | glm-5.2:cloud |
| agentic_road_closure | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 3 | 6 | neither |

## Stochastic dominance (agentic vs. baseline)

_(no rows)_

## Gate 1 -- safety

`RD = S_agentic - S_baseline`, paired per disruption under common random numbers, positive favouring the agentic system. On the anticipated arm the test is non-inferiority against the pre-registered `delta_NI` = 0.05; on the novel arm it is superiority with the paired CI excluding zero. `delta_m` is **not** read here -- it is denominated in levels and this is a survival-rate difference; see the H2 effect table below. A verdict of `unregistered` means the margin was withdrawn for this run (`--delta-ni`), which makes the run exploratory and is **not** a pass.

| disruption | model | arm | n_pairs | pairing | rd | ci_low | ci_high | wilcoxon_p | wilcoxon_method | gate1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | deepseek-v4-pro:0813-cloud | anticipated | 3 | replicate | -0.0667 | -0.1 | 0.0 | 0.34578 | normal_approximation | fail |
| closed_loop | glm-5.2:cloud | anticipated | 6 | replicate | -0.1 | -0.2667 | 0.0 | 0.5 | exact | fail |
| closed_loop | minimax-m3:cloud | anticipated | 4 | replicate | -0.75 | -1.0 | -0.5 | 0.09467 | normal_approximation | fail |
| road_closure | deepseek-v4-pro:0813-cloud | anticipated | 3 | replicate | -0.5 | -1.0 | 0.0 | 0.5 | exact | fail |
| road_closure | glm-5.2:cloud | anticipated | 6 | replicate | -0.5 | -0.75 | -0.25 | 0.04771 | normal_approximation | fail |

### H2 effect -- is the novel-arm win worth claiming?

Gate 1 above decides *superiority* on survival. This decides whether the win clears the pre-registered minimum effect, and it is read on the DV's own scale: the median paired shift in Recovery-Outcome Level against `delta_m` = one whole level. Both conditions must hold -- the shift **and** first-order stochastic dominance -- so that a median shift cannot hide a lower tail of runs that lost residents. Anticipated-arm rows read `not_this_arm` and are descriptive: H2 is a claim about the novel set only.

| disruption | model | arm | n_pairs | pairing | median_level_shift | delta_m | dominance | h2_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | deepseek-v4-pro:0813-cloud | anticipated | 3 | replicate | -2.0 | 1.0 | baseline | not_this_arm |
| closed_loop | glm-5.2:cloud | anticipated | 6 | replicate | 0.0 | 1.0 | baseline | not_this_arm |
| closed_loop | minimax-m3:cloud | anticipated | 4 | replicate | -3.0 | 1.0 | baseline | not_this_arm |
| road_closure | deepseek-v4-pro:0813-cloud | anticipated | 3 | replicate | -1.0 | 1.0 | baseline | not_this_arm |
| road_closure | glm-5.2:cloud | anticipated | 6 | replicate | -1.0 | 1.0 | baseline | not_this_arm |

### Equity

| subgroups_defined | delta_eq | verdict | reason |
| --- | --- | --- | --- |
| False | None | undefined | declared undefined: the resident population is homogeneous and undifferentiated, so a max-min survival difference across vulnerable subgroups is taken over a single group and is identically zero (docs/PREREGISTRATION.md sec. 4) |

## Gate 2 -- speed and flow

Read only over the runs that cleared Gate 1, and `T_q` is a fraction of the feasibility **ceiling**, not of the residents a run happened to save. A quantile a run never reached is censored, counted in `T*_censored`, and never imputed; a cell in which no run cleared Gate 1 shows `--`. Level 4 is Gate 1 AND Gate 2 (`thresholds.LEVEL_4_IS_GATE_1_AND_GATE_2`) -- the one place the ladder blends safety with efficiency.

| system | model | scenario | n | n_gate1 | gate1_pass_rate | T50 | T50_censored | T90 | T90_censored | T95 | T95_censored | T100 | T100_censored | bus_km | latency_s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agentic | deepseek-v4-pro:0813-cloud | agentic_closed_loop | 3 | 1 | 0.3333 | 10:20 | 0 | 11:08 | 0 | 11:08 | 0 | 11:08 | 0 | 76.81 | 913.59 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_road_closure | 3 | 1 | 0.3333 | 10:39 | 0 | 11:15 | 0 | 11:38 | 0 | 11:38 | 0 | 185.95 | 1739.97 |
| agentic | glm-5.2:cloud | agentic_closed_loop | 6 | 4 | 0.6667 | 10:32 | 0 | 11:14 | 0 | 11:14 | 0 | 11:14 | 0 | 70.41 | 2009.03 |
| agentic | glm-5.2:cloud | agentic_road_closure | 6 | 1 | 0.1667 | 10:20 | 0 | 10:38 | 0 | 10:38 | 0 | 10:38 | 0 | 147.03 | 2699.92 |
| agentic | minimax-m3:cloud | agentic_closed_loop | 4 | 0 | 0.0 | -- | 4 | -- | 4 | -- | 4 | -- | 4 | -- | -- |
| baseline |  | baseline_closed_loop | 6 | 6 | 1.0 | 10:24 | 0 | 11:37 | 0 | 11:37 | 0 | 11:37 | 0 | 60.63 | 0.0 |
| baseline |  | baseline_road_closure | 6 | 6 | 1.0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 83.12 | 0.0 |

## Gate 3 -- adaptability: A(z) over SIM_TIME_SCALE

One series per disruption and model. `Y` is the cell's **median** level, never its mean -- the DV is ordinal. The series are deliberately not pooled across models: a weak model that emits invalid plans would drag a strong one's median and the crossover would then belong to neither.

| disruption | model | scale | n_agentic | n_baseline | y_agentic | y_baseline | advantage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | deepseek-v4-pro:0813-cloud | 8.4 | 3 | 6 | 2 | 4.0 | -2.0 |
| closed_loop | glm-5.2:cloud | 8.4 | 6 | 6 | 4.0 | 4.0 | 0.0 |
| closed_loop | minimax-m3:cloud | 8.4 | 4 | 6 | 1.0 | 4.0 | -3.0 |
| road_closure | deepseek-v4-pro:0813-cloud | 8.4 | 3 | 6 | 2 | 3.0 | -1.0 |
| road_closure | glm-5.2:cloud | 8.4 | 6 | 6 | 2.0 | 3.0 | -1.0 |

| disruption | model | scales | first_advantage | crossover_low | crossover_high |
| --- | --- | --- | --- | --- | --- |
| closed_loop | deepseek-v4-pro:0813-cloud | 1 | -2.0 | -- | -- |
| closed_loop | glm-5.2:cloud | 1 | 0.0 | -- | -- |
| closed_loop | minimax-m3:cloud | 1 | -3.0 | -- | -- |
| road_closure | deepseek-v4-pro:0813-cloud | 1 | -1.0 | -- | -- |
| road_closure | glm-5.2:cloud | 1 | -1.0 | -- | -- |

The crossover is a **band** and not a point: cron due-ness is evaluated once per wall-second, so every trigger carries +/- `scale` sim-seconds of jitter. A `--` band means the advantage never turned in the sampled range -- read `first_advantage` beside it to tell that from 'there was never an advantage to turn'.

## Reporting template (protocol sec. 10)

| disruption | system | model | n | levels | median_level | survival | gate1_pass_rate | rd | ci | gate1 | never_moved | late | refused | T50 | T50_censored | T90 | T90_censored | T95 | T95_censored | T100 | T100_censored | bus_km | latency_s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | agentic | deepseek-v4-pro:0813-cloud | 3 | 2x2 3x1 | 2 | 0.9333 | 0.3333 | -0.0667 | [-0.1, 0.0] | fail | 3.3 | 3.3 | 0.0 | 10:20 | 0 | 11:08 | 0 | 11:08 | 0 | 11:08 | 0 | 76.81 | 913.59 |
| closed_loop | agentic | glm-5.2:cloud | 6 | 2x2 4x4 | 4.0 | 0.9 | 0.6667 | -0.1 | [-0.2667, 0.0] | fail | 1.7 | 8.3 | 0.0 | 10:32 | 0 | 11:14 | 0 | 11:14 | 0 | 11:14 | 0 | 70.41 | 2009.03 |
| closed_loop | agentic | minimax-m3:cloud | 4 | 0x2 2x2 | 1.0 | 0.25 | 0.0 | -0.75 | [-1.0, -0.5] | fail | 75.0 | 0.0 | 0.0 | -- | 4 | -- | 4 | -- | 4 | -- | 4 | -- | -- |
| closed_loop | baseline | none | 6 | 4x6 | 4.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 10:24 | 0 | 11:37 | 0 | 11:37 | 0 | 11:37 | 0 | 60.63 | 0.0 |
| road_closure | agentic | deepseek-v4-pro:0813-cloud | 3 | 0x1 2x1 3x1 | 2 | 0.5 | 0.3333 | -0.5 | [-1.0, 0.0] | fail | 46.7 | 3.3 | 0.0 | 10:39 | 0 | 11:15 | 0 | 11:38 | 0 | 11:38 | 0 | 185.95 | 1739.97 |
| road_closure | agentic | glm-5.2:cloud | 6 | 0x1 2x4 3x1 | 2.0 | 0.5 | 0.1667 | -0.5 | [-0.75, -0.25] | fail | 41.7 | 8.3 | 0.0 | 10:20 | 0 | 10:38 | 0 | 10:38 | 0 | 10:38 | 0 | 147.03 | 2699.92 |
| road_closure | baseline | none | 6 | 3x6 | 3.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 83.12 | 0.0 |

Sensitivity across the cut points 0.40, 0.50, 0.60 rides on every score record and must be reported beside this table, never after it.
