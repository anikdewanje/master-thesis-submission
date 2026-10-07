# Sweep summary

## Runs included

| total | eligible | censored | unscored | invalid_model_binding |
| --- | --- | --- | --- | --- |
| 18 | 18 | 0 | 0 | 0 |

Censored runs were stopped before their flood deadline was decided and cannot be scored without recording the harness's impatience as the system's failure (`evaluation/thresholds.py`, `CENSORING_MARGIN_SIM_S`).

## Recovery-level distribution

| system | model | scenario | n | level_0 | level_1 | level_2 | level_3 | level_4 | median_level | ceiling_below_nominal | mean_completeness_vs_nominal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agentic | kimi-k3:cloud | agentic_closed_loop | 3 | 0 | 0 | 1 | 2 | 0 | 3 | 0 | 0.9667 |
| agentic | kimi-k3:cloud | agentic_road_closure | 3 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 0.6667 |
| agentic | nemotron-3-ultra:cloud | agentic_closed_loop | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0.1667 |
| agentic | nemotron-3-ultra:cloud | agentic_road_closure | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0.1667 |
| baseline |  | baseline_closed_loop | 3 | 0 | 0 | 0 | 0 | 3 | 4 | 0 | 1.0 |
| baseline |  | baseline_road_closure | 3 | 0 | 0 | 0 | 3 | 0 | 3 | 3 | 0.6 |

`ceiling_below_nominal` counts runs whose feasibility ceiling fell below 100 because the shelters they heard from declared fewer beds. For those runs `completeness` flatters the outcome, so `mean_completeness_vs_nominal` is reported beside it.

## Stochastic dominance (by model, within scenario)

| scenario | a | b | n_a | n_b | dominates |
| --- | --- | --- | --- | --- | --- |
| agentic_closed_loop | kimi-k3:cloud | nemotron-3-ultra:cloud | 3 | 3 | kimi-k3:cloud |
| agentic_road_closure | kimi-k3:cloud | nemotron-3-ultra:cloud | 3 | 3 | kimi-k3:cloud |

## Stochastic dominance (agentic vs. baseline)

_(no rows)_

## Gate 1 -- safety

`RD = S_agentic - S_baseline`, paired per disruption under common random numbers, positive favouring the agentic system. On the anticipated arm the test is non-inferiority against the pre-registered `delta_NI` = 0.05; on the novel arm it is superiority with the paired CI excluding zero. `delta_m` is **not** read here -- it is denominated in levels and this is a survival-rate difference; see the H2 effect table below. A verdict of `unregistered` means the margin was withdrawn for this run (`--delta-ni`), which makes the run exploratory and is **not** a pass.

| disruption | model | arm | n_pairs | pairing | rd | ci_low | ci_high | wilcoxon_p | wilcoxon_method | gate1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | kimi-k3:cloud | anticipated | 3 | replicate | -0.0333 | -0.1 | 0.0 | 1.0 | exact | pass |
| closed_loop | nemotron-3-ultra:cloud | anticipated | 3 | replicate | -0.8333 | -1.0 | -0.5 | 0.17357 | normal_approximation | fail |
| road_closure | kimi-k3:cloud | anticipated | 3 | replicate | -0.3333 | -0.5 | 0.0 | 0.34578 | normal_approximation | fail |
| road_closure | nemotron-3-ultra:cloud | anticipated | 3 | replicate | -0.8333 | -1.0 | -0.5 | 0.17357 | normal_approximation | fail |

### H2 effect -- is the novel-arm win worth claiming?

Gate 1 above decides *superiority* on survival. This decides whether the win clears the pre-registered minimum effect, and it is read on the DV's own scale: the median paired shift in Recovery-Outcome Level against `delta_m` = one whole level. Both conditions must hold -- the shift **and** first-order stochastic dominance -- so that a median shift cannot hide a lower tail of runs that lost residents. Anticipated-arm rows read `not_this_arm` and are descriptive: H2 is a claim about the novel set only.

| disruption | model | arm | n_pairs | pairing | median_level_shift | delta_m | dominance | h2_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | kimi-k3:cloud | anticipated | 3 | replicate | -1.0 | 1.0 | baseline | not_this_arm |
| closed_loop | nemotron-3-ultra:cloud | anticipated | 3 | replicate | -4.0 | 1.0 | baseline | not_this_arm |
| road_closure | kimi-k3:cloud | anticipated | 3 | replicate | -1.0 | 1.0 | baseline | not_this_arm |
| road_closure | nemotron-3-ultra:cloud | anticipated | 3 | replicate | -3.0 | 1.0 | baseline | not_this_arm |

### Equity

| subgroups_defined | delta_eq | verdict | reason |
| --- | --- | --- | --- |
| False | None | undefined | declared undefined: the resident population is homogeneous and undifferentiated, so a max-min survival difference across vulnerable subgroups is taken over a single group and is identically zero (docs/PREREGISTRATION.md sec. 4) |

## Gate 2 -- speed and flow

Read only over the runs that cleared Gate 1, and `T_q` is a fraction of the feasibility **ceiling**, not of the residents a run happened to save. A quantile a run never reached is censored, counted in `T*_censored`, and never imputed; a cell in which no run cleared Gate 1 shows `--`. Level 4 is Gate 1 AND Gate 2 (`thresholds.LEVEL_4_IS_GATE_1_AND_GATE_2`) -- the one place the ladder blends safety with efficiency.

| system | model | scenario | n | n_gate1 | gate1_pass_rate | T50 | T50_censored | T90 | T90_censored | T95 | T95_censored | T100 | T100_censored | bus_km | latency_s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agentic | kimi-k3:cloud | agentic_closed_loop | 3 | 2 | 0.6667 | 11:11 | 0 | 11:22 | 0 | 11:22 | 0 | 11:22 | 0 | 51.74 | 3817.45 |
| agentic | kimi-k3:cloud | agentic_road_closure | 3 | 1 | 0.3333 | 10:55 | 0 | 11:08 | 0 | 11:08 | 0 | 11:08 | 0 | 76.78 | 3757.86 |
| agentic | nemotron-3-ultra:cloud | agentic_closed_loop | 3 | 0 | 0.0 | -- | 3 | -- | 3 | -- | 3 | -- | 3 | -- | -- |
| agentic | nemotron-3-ultra:cloud | agentic_road_closure | 3 | 0 | 0.0 | -- | 3 | -- | 3 | -- | 3 | -- | 3 | -- | -- |
| baseline |  | baseline_closed_loop | 3 | 3 | 1.0 | 10:24 | 0 | 11:37 | 0 | 11:37 | 0 | 11:37 | 0 | 60.63 | 0.0 |
| baseline |  | baseline_road_closure | 3 | 3 | 1.0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 83.12 | 0.0 |

## Gate 3 -- adaptability: A(z) over SIM_TIME_SCALE

One series per disruption and model. `Y` is the cell's **median** level, never its mean -- the DV is ordinal. The series are deliberately not pooled across models: a weak model that emits invalid plans would drag a strong one's median and the crossover would then belong to neither.

| disruption | model | scale | n_agentic | n_baseline | y_agentic | y_baseline | advantage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | kimi-k3:cloud | 8.4 | 3 | 3 | 3 | 4 | -1 |
| closed_loop | nemotron-3-ultra:cloud | 8.4 | 3 | 3 | 0 | 4 | -4 |
| road_closure | kimi-k3:cloud | 8.4 | 3 | 3 | 2 | 3 | -1 |
| road_closure | nemotron-3-ultra:cloud | 8.4 | 3 | 3 | 0 | 3 | -3 |

| disruption | model | scales | first_advantage | crossover_low | crossover_high |
| --- | --- | --- | --- | --- | --- |
| closed_loop | kimi-k3:cloud | 1 | -1 | -- | -- |
| closed_loop | nemotron-3-ultra:cloud | 1 | -4 | -- | -- |
| road_closure | kimi-k3:cloud | 1 | -1 | -- | -- |
| road_closure | nemotron-3-ultra:cloud | 1 | -3 | -- | -- |

The crossover is a **band** and not a point: cron due-ness is evaluated once per wall-second, so every trigger carries +/- `scale` sim-seconds of jitter. A `--` band means the advantage never turned in the sampled range -- read `first_advantage` beside it to tell that from 'there was never an advantage to turn'.

## Reporting template (protocol sec. 10)

| disruption | system | model | n | levels | median_level | survival | gate1_pass_rate | rd | ci | gate1 | never_moved | late | refused | T50 | T50_censored | T90 | T90_censored | T95 | T95_censored | T100 | T100_censored | bus_km | latency_s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| closed_loop | agentic | kimi-k3:cloud | 3 | 2x1 3x2 | 3 | 0.9667 | 0.6667 | -0.0333 | [-0.1, 0.0] | pass | 3.3 | 0.0 | 0.0 | 11:11 | 0 | 11:22 | 0 | 11:22 | 0 | 11:22 | 0 | 51.74 | 3817.45 |
| closed_loop | agentic | nemotron-3-ultra:cloud | 3 | 0x2 2x1 | 0 | 0.1667 | 0.0 | -0.8333 | [-1.0, -0.5] | fail | 66.7 | 16.7 | 0.0 | -- | 3 | -- | 3 | -- | 3 | -- | 3 | -- | -- |
| closed_loop | baseline | none | 3 | 4x3 | 4 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 10:24 | 0 | 11:37 | 0 | 11:37 | 0 | 11:37 | 0 | 60.63 | 0.0 |
| road_closure | agentic | kimi-k3:cloud | 3 | 2x2 3x1 | 2 | 0.6667 | 0.3333 | -0.3333 | [-0.5, 0.0] | fail | 33.3 | 0.0 | 0.0 | 10:55 | 0 | 11:08 | 0 | 11:08 | 0 | 11:08 | 0 | 76.78 | 3757.86 |
| road_closure | agentic | nemotron-3-ultra:cloud | 3 | 0x2 2x1 | 0 | 0.1667 | 0.0 | -0.8333 | [-1.0, -0.5] | fail | 70.0 | 13.3 | 0.0 | -- | 3 | -- | 3 | -- | 3 | -- | 3 | -- | -- |
| road_closure | baseline | none | 3 | 3x3 | 3 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 83.12 | 0.0 |

Sensitivity across the cut points 0.40, 0.50, 0.60 rides on every score record and must be reported beside this table, never after it.
