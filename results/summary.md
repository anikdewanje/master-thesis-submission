# Sweep summary

## Runs included

| total | eligible | censored | unscored | invalid_model_binding |
| --- | --- | --- | --- | --- |
| 310 | 310 | 0 | 0 | 0 |

Censored runs were stopped before their flood deadline was decided and cannot be scored without recording the harness's impatience as the system's failure (`evaluation/thresholds.py`, `CENSORING_MARGIN_SIM_S`).

## Recovery-level distribution

| system | model | scenario | n | level_0 | level_1 | level_2 | level_3 | level_4 | median_level | ceiling_below_nominal | mean_completeness_vs_nominal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agentic | deepseek-v4-pro:0813-cloud | agentic_bus1_suspension_capacity_reduction | 10 | 1 | 1 | 6 | 0 | 2 | 2 | 0 | 0.755 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_closed_loop | 10 | 1 | 0 | 3 | 0 | 6 | 4 | 0 | 0.79 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_conflicting_evacuation_orders | 10 | 1 | 2 | 6 | 0 | 1 | 2 | 0 | 0.65 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_medical_emergency_in_flight | 10 | 1 | 1 | 4 | 0 | 4 | 2 | 0 | 0.8 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_road_closure | 10 | 2 | 1 | 4 | 1 | 2 | 2 | 0 | 0.7 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_sc1_partial_capacity_loss | 10 | 2 | 0 | 2 | 0 | 6 | 4 | 0 | 0.74 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_unverified_persons_report | 10 | 0 | 0 | 8 | 0 | 2 | 2 | 0 | 0.69 |
| agentic | glm-5.2:cloud | agentic_bus1_suspension_capacity_reduction | 10 | 0 | 0 | 3 | 2 | 5 | 4 | 0 | 0.85 |
| agentic | glm-5.2:cloud | agentic_closed_loop | 10 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 1.0 |
| agentic | glm-5.2:cloud | agentic_conflicting_evacuation_orders | 10 | 0 | 0 | 3 | 0 | 7 | 4 | 0 | 0.85 |
| agentic | glm-5.2:cloud | agentic_medical_emergency_in_flight | 10 | 0 | 0 | 3 | 0 | 7 | 4 | 0 | 0.85 |
| agentic | glm-5.2:cloud | agentic_road_closure | 10 | 0 | 1 | 2 | 5 | 2 | 3 | 0 | 0.84 |
| agentic | glm-5.2:cloud | agentic_sc1_partial_capacity_loss | 10 | 1 | 0 | 2 | 0 | 7 | 4 | 0 | 0.81 |
| agentic | glm-5.2:cloud | agentic_unverified_persons_report | 10 | 0 | 0 | 4 | 1 | 5 | 4 | 0 | 0.84 |
| agentic | gpt-oss:120b-cloud | agentic_medical_emergency_in_flight | 4 | 2 | 0 | 2 | 0 | 0 | 2 | 0 | 0.375 |
| agentic | kimi-k2.7-code:cloud | agentic_medical_emergency_in_flight | 3 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 0.6667 |
| agentic | kimi-k3:cloud | agentic_medical_emergency_in_flight | 10 | 1 | 0 | 2 | 7 | 0 | 3 | 0 | 0.8 |
| agentic | kimi-k3:cloud | agentic_unverified_persons_report | 1 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0.5 |
| agentic | minimax-m3:cloud | agentic_closed_loop | 10 | 4 | 1 | 4 | 1 | 0 | 2 | 0 | 0.34 |
| agentic | minimax-m3:cloud | agentic_road_closure | 10 | 7 | 0 | 3 | 0 | 0 | 0 | 0 | 0.15 |
| agentic | nemotron-3-ultra:cloud | agentic_closed_loop | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 |
| agentic | qwen3.5:cloud | agentic_bus1_suspension_capacity_reduction | 10 | 0 | 0 | 4 | 1 | 5 | 4 | 0 | 0.92 |
| agentic | qwen3.5:cloud | agentic_closed_loop | 10 | 0 | 0 | 1 | 3 | 6 | 4 | 0 | 0.95 |
| agentic | qwen3.5:cloud | agentic_conflicting_evacuation_orders | 10 | 0 | 0 | 2 | 1 | 7 | 4 | 0 | 0.98 |
| agentic | qwen3.5:cloud | agentic_medical_emergency_in_flight | 10 | 0 | 0 | 2 | 1 | 7 | 4 | 0 | 0.92 |
| agentic | qwen3.5:cloud | agentic_sc1_partial_capacity_loss | 10 | 1 | 1 | 3 | 0 | 5 | 4 | 0 | 0.78 |
| agentic | qwen3.5:cloud | agentic_unverified_persons_report | 10 | 0 | 0 | 4 | 0 | 6 | 4 | 0 | 0.9 |
| baseline |  | baseline_bus1_suspension_capacity_reduction | 10 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 1.0 |
| baseline |  | baseline_closed_loop | 10 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 1.0 |
| baseline |  | baseline_conflicting_evacuation_orders | 10 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 1.0 |
| baseline |  | baseline_medical_emergency_in_flight | 10 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 1.0 |
| baseline |  | baseline_road_closure | 10 | 0 | 0 | 0 | 10 | 0 | 3 | 10 | 0.6 |
| baseline |  | baseline_sc1_partial_capacity_loss | 10 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 1.0 |
| baseline |  | baseline_unverified_persons_report | 10 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 1.0 |

`ceiling_below_nominal` counts runs whose feasibility ceiling fell below 100 because the shelters they heard from declared fewer beds. For those runs `completeness` flatters the outcome, so `mean_completeness_vs_nominal` is reported beside it.

## Stochastic dominance (by model, within scenario)

| scenario | a | b | n_a | n_b | dominates |
| --- | --- | --- | --- | --- | --- |
| agentic_bus1_suspension_capacity_reduction | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_bus1_suspension_capacity_reduction | deepseek-v4-pro:0813-cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_bus1_suspension_capacity_reduction | glm-5.2:cloud | qwen3.5:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_closed_loop | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_closed_loop | deepseek-v4-pro:0813-cloud | minimax-m3:cloud | 10 | 10 | deepseek-v4-pro:0813-cloud |
| agentic_closed_loop | deepseek-v4-pro:0813-cloud | nemotron-3-ultra:cloud | 10 | 2 | deepseek-v4-pro:0813-cloud |
| agentic_closed_loop | deepseek-v4-pro:0813-cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_closed_loop | glm-5.2:cloud | minimax-m3:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_closed_loop | glm-5.2:cloud | nemotron-3-ultra:cloud | 10 | 2 | glm-5.2:cloud |
| agentic_closed_loop | glm-5.2:cloud | qwen3.5:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_closed_loop | minimax-m3:cloud | nemotron-3-ultra:cloud | 10 | 2 | minimax-m3:cloud |
| agentic_closed_loop | minimax-m3:cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_closed_loop | nemotron-3-ultra:cloud | qwen3.5:cloud | 2 | 10 | qwen3.5:cloud |
| agentic_conflicting_evacuation_orders | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_conflicting_evacuation_orders | deepseek-v4-pro:0813-cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_conflicting_evacuation_orders | glm-5.2:cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | gpt-oss:120b-cloud | 10 | 4 | deepseek-v4-pro:0813-cloud |
| agentic_medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | kimi-k2.7-code:cloud | 10 | 3 | neither |
| agentic_medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | kimi-k3:cloud | 10 | 10 | neither |
| agentic_medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_medical_emergency_in_flight | glm-5.2:cloud | gpt-oss:120b-cloud | 10 | 4 | glm-5.2:cloud |
| agentic_medical_emergency_in_flight | glm-5.2:cloud | kimi-k2.7-code:cloud | 10 | 3 | glm-5.2:cloud |
| agentic_medical_emergency_in_flight | glm-5.2:cloud | kimi-k3:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_medical_emergency_in_flight | glm-5.2:cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_medical_emergency_in_flight | gpt-oss:120b-cloud | kimi-k2.7-code:cloud | 4 | 3 | kimi-k2.7-code:cloud |
| agentic_medical_emergency_in_flight | gpt-oss:120b-cloud | kimi-k3:cloud | 4 | 10 | kimi-k3:cloud |
| agentic_medical_emergency_in_flight | gpt-oss:120b-cloud | qwen3.5:cloud | 4 | 10 | qwen3.5:cloud |
| agentic_medical_emergency_in_flight | kimi-k2.7-code:cloud | kimi-k3:cloud | 3 | 10 | neither |
| agentic_medical_emergency_in_flight | kimi-k2.7-code:cloud | qwen3.5:cloud | 3 | 10 | qwen3.5:cloud |
| agentic_medical_emergency_in_flight | kimi-k3:cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_road_closure | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_road_closure | deepseek-v4-pro:0813-cloud | minimax-m3:cloud | 10 | 10 | deepseek-v4-pro:0813-cloud |
| agentic_road_closure | glm-5.2:cloud | minimax-m3:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_sc1_partial_capacity_loss | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_sc1_partial_capacity_loss | deepseek-v4-pro:0813-cloud | qwen3.5:cloud | 10 | 10 | neither |
| agentic_sc1_partial_capacity_loss | glm-5.2:cloud | qwen3.5:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_unverified_persons_report | deepseek-v4-pro:0813-cloud | glm-5.2:cloud | 10 | 10 | glm-5.2:cloud |
| agentic_unverified_persons_report | deepseek-v4-pro:0813-cloud | kimi-k3:cloud | 10 | 1 | deepseek-v4-pro:0813-cloud |
| agentic_unverified_persons_report | deepseek-v4-pro:0813-cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_unverified_persons_report | glm-5.2:cloud | kimi-k3:cloud | 10 | 1 | glm-5.2:cloud |
| agentic_unverified_persons_report | glm-5.2:cloud | qwen3.5:cloud | 10 | 10 | qwen3.5:cloud |
| agentic_unverified_persons_report | kimi-k3:cloud | qwen3.5:cloud | 1 | 10 | qwen3.5:cloud |

## Stochastic dominance (agentic vs. baseline)

_(no rows)_

## Gate 1 -- safety

`RD = S_agentic - S_baseline`, paired per disruption under common random numbers, positive favouring the agentic system. On the anticipated arm the test is non-inferiority against the pre-registered `delta_NI` = 0.05; on the novel arm it is superiority with the paired CI excluding zero. `delta_m` is **not** read here -- it is denominated in levels and this is a survival-rate difference; see the H2 effect table below. A verdict of `unregistered` means the margin was withdrawn for this run (`--delta-ni`), which makes the run exploratory and is **not** a pass.

| disruption | model | arm | n_pairs | pairing | rd | ci_low | ci_high | wilcoxon_p | wilcoxon_method | gate1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bus1_suspension_capacity_reduction | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -0.245 | -0.45 | -0.08 | 0.01198 | normal_approximation | fail |
| bus1_suspension_capacity_reduction | glm-5.2:cloud | novel | 10 | replicate | -0.15 | -0.3 | 0.0 | 0.14891 | normal_approximation | fail |
| bus1_suspension_capacity_reduction | qwen3.5:cloud | novel | 10 | replicate | -0.08 | -0.18 | -0.01 | 0.08897 | normal_approximation | fail |
| closed_loop | deepseek-v4-pro:0813-cloud | anticipated | 10 | replicate | -0.21 | -0.42 | -0.03 | 0.09751 | normal_approximation | fail |
| closed_loop | glm-5.2:cloud | anticipated | 10 | replicate | 0.0 | 0.0 | 0.0 | None | undetermined | pass |
| closed_loop | minimax-m3:cloud | anticipated | 10 | replicate | -0.66 | -0.85 | -0.46 | 0.00797 | normal_approximation | fail |
| closed_loop | nemotron-3-ultra:cloud | anticipated | 2 | replicate | -1.0 | -1.0 | -1.0 | 0.34578 | normal_approximation | fail |
| closed_loop | qwen3.5:cloud | anticipated | 10 | replicate | -0.05 | -0.15 | 0.0 | 1.0 | exact | fail |
| conflicting_evacuation_orders | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -0.35 | -0.55 | -0.17 | 0.00849 | normal_approximation | fail |
| conflicting_evacuation_orders | glm-5.2:cloud | novel | 10 | replicate | -0.15 | -0.3 | 0.0 | 0.14891 | normal_approximation | fail |
| conflicting_evacuation_orders | qwen3.5:cloud | novel | 10 | replicate | -0.02 | -0.05 | 0.0 | 0.34578 | normal_approximation | fail |
| medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -0.2 | -0.42 | -0.04 | 0.03103 | normal_approximation | fail |
| medical_emergency_in_flight | glm-5.2:cloud | novel | 10 | replicate | -0.15 | -0.3 | 0.0 | 0.14891 | normal_approximation | fail |
| medical_emergency_in_flight | gpt-oss:120b-cloud | novel | 4 | replicate | -0.625 | -1.0 | -0.25 | 0.09751 | normal_approximation | fail |
| medical_emergency_in_flight | kimi-k2.7-code:cloud | novel | 3 | replicate | -0.3333 | -0.5 | 0.0 | 0.34578 | normal_approximation | fail |
| medical_emergency_in_flight | kimi-k3:cloud | novel | 10 | replicate | -0.2 | -0.45 | 0.0 | 0.17357 | normal_approximation | fail |
| medical_emergency_in_flight | qwen3.5:cloud | novel | 10 | replicate | -0.08 | -0.21 | 0.02 | 0.5 | exact | fail |
| road_closure | deepseek-v4-pro:0813-cloud | anticipated | 10 | replicate | -0.3 | -0.55 | -0.08 | 0.01991 | normal_approximation | fail |
| road_closure | glm-5.2:cloud | anticipated | 10 | replicate | -0.16 | -0.32 | 0.0 | 0.17357 | normal_approximation | fail |
| road_closure | minimax-m3:cloud | anticipated | 10 | replicate | -0.85 | -1.0 | -0.7 | 0.00416 | normal_approximation | fail |
| sc1_partial_capacity_loss | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -0.26 | -0.52 | -0.03 | 0.09751 | normal_approximation | fail |
| sc1_partial_capacity_loss | glm-5.2:cloud | novel | 10 | replicate | -0.19 | -0.42 | 0.0 | 0.25 | exact | fail |
| sc1_partial_capacity_loss | qwen3.5:cloud | novel | 10 | replicate | -0.22 | -0.44 | -0.03 | 0.14112 | normal_approximation | fail |
| unverified_persons_report | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -0.31 | -0.44 | -0.17 | 0.01187 | normal_approximation | fail |
| unverified_persons_report | glm-5.2:cloud | novel | 10 | replicate | -0.16 | -0.31 | -0.03 | 0.08897 | normal_approximation | fail |
| unverified_persons_report | kimi-k3:cloud | novel | 1 | replicate | -0.5 | -0.5 | -0.5 | 1.0 | exact | fail |
| unverified_persons_report | qwen3.5:cloud | novel | 10 | replicate | -0.1 | -0.23 | 0.0 | 0.27852 | normal_approximation | fail |

### H2 primary -- P(level_agentic >= level_baseline)

The test PREREGISTRATION sec. 5.1 registers as the H2 primary, and the one this table finally reports: an exact (Clopper-Pearson) binomial interval over the `k` agentic runs against the control's constant level. It is one-sample by design -- the baseline runs no model and produces one level per scenario, so a paired two-sample test would misstate it. `p_holm` is the Holm-Bonferroni adjustment across scenarios within the arm, per model (sec. 5.3).

The pre-registration fixes the *interval* but no cut on it, so per EVALUATION_PROTOCOL sec. 3.8 no reading here can constitute a pass. `verdict` therefore reports where the interval sits relative to chance rather than asserting a registered threshold. Read it beside the risk difference above, not instead of it.

| disruption | model | n | baseline_level | successes | p_hat | ci | p_value | verdict | note | p_holm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bus1_suspension_capacity_reduction | deepseek-v4-pro:0813-cloud | 10 | 4 | 2 | 0.2 | [0.0252, 0.5561] | 0.10938 | inconclusive |  | 0.43752 |
| bus1_suspension_capacity_reduction | glm-5.2:cloud | 10 | 4 | 5 | 0.5 | [0.1871, 0.8129] | 1.0 | inconclusive |  | 1.0 |
| bus1_suspension_capacity_reduction | qwen3.5:cloud | 10 | 4 | 5 | 0.5 | [0.1871, 0.8129] | 1.0 | inconclusive |  | 1.0 |
| conflicting_evacuation_orders | deepseek-v4-pro:0813-cloud | 10 | 4 | 1 | 0.1 | [0.0025, 0.445] | 0.02148 | agentic_below_chance |  | 0.1074 |
| conflicting_evacuation_orders | glm-5.2:cloud | 10 | 4 | 7 | 0.7 | [0.3475, 0.9333] | 0.34375 | inconclusive |  | 1.0 |
| conflicting_evacuation_orders | qwen3.5:cloud | 10 | 4 | 7 | 0.7 | [0.3475, 0.9333] | 0.34375 | inconclusive |  | 1.0 |
| medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | 10 | 4 | 4 | 0.4 | [0.1216, 0.7376] | 0.75391 | inconclusive |  | 1.0 |
| medical_emergency_in_flight | glm-5.2:cloud | 10 | 4 | 7 | 0.7 | [0.3475, 0.9333] | 0.34375 | inconclusive |  | 1.0 |
| medical_emergency_in_flight | gpt-oss:120b-cloud | 4 | 4 | 0 | 0.0 | [0.0, 0.6024] | 0.125 | inconclusive |  | 0.125 |
| medical_emergency_in_flight | kimi-k2.7-code:cloud | 3 | 4 | 0 | 0.0 | [0.0, 0.7076] | 0.25 | inconclusive |  | 0.25 |
| medical_emergency_in_flight | kimi-k3:cloud | 10 | 4 | 0 | 0.0 | [0.0, 0.3085] | 0.00195 | agentic_below_chance |  | 0.0039 |
| medical_emergency_in_flight | qwen3.5:cloud | 10 | 4 | 7 | 0.7 | [0.3475, 0.9333] | 0.34375 | inconclusive |  | 1.0 |
| sc1_partial_capacity_loss | deepseek-v4-pro:0813-cloud | 10 | 4 | 6 | 0.6 | [0.2624, 0.8784] | 0.75391 | inconclusive |  | 1.0 |
| sc1_partial_capacity_loss | glm-5.2:cloud | 10 | 4 | 7 | 0.7 | [0.3475, 0.9333] | 0.34375 | inconclusive |  | 1.0 |
| sc1_partial_capacity_loss | qwen3.5:cloud | 10 | 4 | 5 | 0.5 | [0.1871, 0.8129] | 1.0 | inconclusive |  | 1.0 |
| unverified_persons_report | deepseek-v4-pro:0813-cloud | 10 | 4 | 2 | 0.2 | [0.0252, 0.5561] | 0.10938 | inconclusive |  | 0.43752 |
| unverified_persons_report | glm-5.2:cloud | 10 | 4 | 5 | 0.5 | [0.1871, 0.8129] | 1.0 | inconclusive |  | 1.0 |
| unverified_persons_report | kimi-k3:cloud | 1 | 4 | 0 | 0.0 | [0.0, 0.975] | 1.0 | inconclusive |  | 1.0 |
| unverified_persons_report | qwen3.5:cloud | 10 | 4 | 6 | 0.6 | [0.2624, 0.8784] | 0.75391 | inconclusive |  | 1.0 |

Aggregated across scenarios by the sign test sec. 5.1 registers -- one observation per scenario, because pooling runs across scenarios would add incommensurable ceilings, fleets and deadlines. Note the floor: with five novel scenarios a two-sided exact sign test cannot return less than 0.0625 even if every scenario points the same way, so this aggregation can never reach conventional significance in this design.

| model | scenarios | favour_agentic | favour_baseline | ties | p_value | min_possible_p |
| --- | --- | --- | --- | --- | --- | --- |
| deepseek-v4-pro:0813-cloud | 5 | 1 | 4 | 0 | 0.375 | 0.0625 |
| glm-5.2:cloud | 5 | 3 | 0 | 2 | 0.25 | 0.25 |
| gpt-oss:120b-cloud | 1 | 0 | 1 | 0 | 1.0 | 1.0 |
| kimi-k2.7-code:cloud | 1 | 0 | 1 | 0 | 1.0 | 1.0 |
| kimi-k3:cloud | 2 | 0 | 2 | 0 | 0.5 | 0.5 |
| qwen3.5:cloud | 5 | 3 | 0 | 2 | 0.25 | 0.25 |

### H2 effect -- is the novel-arm win worth claiming?

Gate 1 above decides *superiority* on survival. This decides whether the win clears the pre-registered minimum effect, and it is read on the DV's own scale: the median paired shift in Recovery-Outcome Level against `delta_m` = one whole level. Both conditions must hold -- the shift **and** first-order stochastic dominance -- so that a median shift cannot hide a lower tail of runs that lost residents. Anticipated-arm rows read `not_this_arm` and are descriptive: H2 is a claim about the novel set only.

| disruption | model | arm | n_pairs | pairing | median_level_shift | delta_m | dominance | h2_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bus1_suspension_capacity_reduction | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -2.0 | 1.0 | baseline | below_delta_m |
| bus1_suspension_capacity_reduction | glm-5.2:cloud | novel | 10 | replicate | -0.5 | 1.0 | baseline | below_delta_m |
| bus1_suspension_capacity_reduction | qwen3.5:cloud | novel | 10 | replicate | -0.5 | 1.0 | baseline | below_delta_m |
| closed_loop | deepseek-v4-pro:0813-cloud | anticipated | 10 | replicate | 0.0 | 1.0 | baseline | not_this_arm |
| closed_loop | glm-5.2:cloud | anticipated | 10 | replicate | 0.0 | 1.0 | identical | not_this_arm |
| closed_loop | minimax-m3:cloud | anticipated | 10 | replicate | -2.5 | 1.0 | baseline | not_this_arm |
| closed_loop | nemotron-3-ultra:cloud | anticipated | 2 | replicate | -4.0 | 1.0 | baseline | not_this_arm |
| closed_loop | qwen3.5:cloud | anticipated | 10 | replicate | 0.0 | 1.0 | baseline | not_this_arm |
| conflicting_evacuation_orders | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -2.0 | 1.0 | baseline | below_delta_m |
| conflicting_evacuation_orders | glm-5.2:cloud | novel | 10 | replicate | 0.0 | 1.0 | baseline | below_delta_m |
| conflicting_evacuation_orders | qwen3.5:cloud | novel | 10 | replicate | 0.0 | 1.0 | baseline | below_delta_m |
| medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -2.0 | 1.0 | baseline | below_delta_m |
| medical_emergency_in_flight | glm-5.2:cloud | novel | 10 | replicate | 0.0 | 1.0 | baseline | below_delta_m |
| medical_emergency_in_flight | gpt-oss:120b-cloud | novel | 4 | replicate | -3.0 | 1.0 | baseline | below_delta_m |
| medical_emergency_in_flight | kimi-k2.7-code:cloud | novel | 3 | replicate | -2.0 | 1.0 | baseline | below_delta_m |
| medical_emergency_in_flight | kimi-k3:cloud | novel | 10 | replicate | -1.0 | 1.0 | baseline | below_delta_m |
| medical_emergency_in_flight | qwen3.5:cloud | novel | 10 | replicate | 0.0 | 1.0 | baseline | below_delta_m |
| road_closure | deepseek-v4-pro:0813-cloud | anticipated | 10 | replicate | -1.0 | 1.0 | neither | not_this_arm |
| road_closure | glm-5.2:cloud | anticipated | 10 | replicate | 0.0 | 1.0 | neither | not_this_arm |
| road_closure | minimax-m3:cloud | anticipated | 10 | replicate | -3.0 | 1.0 | baseline | not_this_arm |
| sc1_partial_capacity_loss | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | 0.0 | 1.0 | baseline | below_delta_m |
| sc1_partial_capacity_loss | glm-5.2:cloud | novel | 10 | replicate | 0.0 | 1.0 | baseline | below_delta_m |
| sc1_partial_capacity_loss | qwen3.5:cloud | novel | 10 | replicate | -1.0 | 1.0 | baseline | below_delta_m |
| unverified_persons_report | deepseek-v4-pro:0813-cloud | novel | 10 | replicate | -2.0 | 1.0 | baseline | below_delta_m |
| unverified_persons_report | glm-5.2:cloud | novel | 10 | replicate | -0.5 | 1.0 | baseline | below_delta_m |
| unverified_persons_report | kimi-k3:cloud | novel | 1 | replicate | -2.0 | 1.0 | baseline | below_delta_m |
| unverified_persons_report | qwen3.5:cloud | novel | 10 | replicate | 0.0 | 1.0 | baseline | below_delta_m |

### Equity

| subgroups_defined | delta_eq | verdict | reason |
| --- | --- | --- | --- |
| False | None | undefined | declared undefined: the resident population is homogeneous and undifferentiated, so a max-min survival difference across vulnerable subgroups is taken over a single group and is identically zero (docs/PREREGISTRATION.md sec. 4) |

## Gate 2 -- speed and flow

Read only over the runs that cleared Gate 1, and `T_q` is a fraction of the feasibility **ceiling**, not of the residents a run happened to save. A quantile a run never reached is censored, counted in `T*_censored`, and never imputed; a cell in which no run cleared Gate 1 shows `--`. Level 4 is Gate 1 AND Gate 2 (`thresholds.LEVEL_4_IS_GATE_1_AND_GATE_2`) -- the one place the ladder blends safety with efficiency.

| system | model | scenario | n | n_gate1 | gate1_pass_rate | T50 | T50_censored | T90 | T90_censored | T95 | T95_censored | T100 | T100_censored | bus_km | latency_s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agentic | deepseek-v4-pro:0813-cloud | agentic_bus1_suspension_capacity_reduction | 10 | 2 | 0.2 | 10:54 | 0 | 11:03 | 0 | 11:25 | 0 | 11:25 | 0 | 82.39 | 1349.4 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_closed_loop | 10 | 6 | 0.6 | 10:59 | 0 | 11:09 | 0 | 11:19 | 0 | 11:19 | 0 | 84.98 | 763.39 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_conflicting_evacuation_orders | 10 | 1 | 0.1 | 11:00 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 63.25 | 914.35 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_medical_emergency_in_flight | 10 | 4 | 0.4 | 10:47 | 0 | 10:58 | 0 | 10:58 | 0 | 10:58 | 0 | 74.42 | 975.65 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_road_closure | 10 | 3 | 0.3 | 10:49 | 0 | 11:24 | 0 | 11:24 | 0 | 11:24 | 0 | 102.45 | 1310.54 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_sc1_partial_capacity_loss | 10 | 6 | 0.6 | 10:52 | 0 | 11:10 | 0 | 11:27 | 0 | 11:27 | 0 | 83.1 | 1009.38 |
| agentic | deepseek-v4-pro:0813-cloud | agentic_unverified_persons_report | 10 | 2 | 0.2 | 10:52 | 0 | 11:13 | 0 | 11:13 | 0 | 11:13 | 0 | 80.5 | 814.92 |
| agentic | glm-5.2:cloud | agentic_bus1_suspension_capacity_reduction | 10 | 7 | 0.7 | 10:58 | 0 | 11:15 | 0 | 11:15 | 0 | 11:15 | 0 | 75.04 | 2528.07 |
| agentic | glm-5.2:cloud | agentic_closed_loop | 10 | 10 | 1.0 | 10:57 | 0 | 11:17 | 0 | 11:17 | 0 | 11:17 | 0 | 75.64 | 1536.97 |
| agentic | glm-5.2:cloud | agentic_conflicting_evacuation_orders | 10 | 7 | 0.7 | 10:44 | 0 | 11:25 | 0 | 11:25 | 0 | 11:25 | 0 | 76.33 | 1468.54 |
| agentic | glm-5.2:cloud | agentic_medical_emergency_in_flight | 10 | 7 | 0.7 | 10:38 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 67.02 | 2051.81 |
| agentic | glm-5.2:cloud | agentic_road_closure | 10 | 7 | 0.7 | 10:40 | 0 | 11:14 | 0 | 11:14 | 0 | 11:14 | 0 | 101.42 | 1643.46 |
| agentic | glm-5.2:cloud | agentic_sc1_partial_capacity_loss | 10 | 7 | 0.7 | 11:07 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 75.07 | 2490.11 |
| agentic | glm-5.2:cloud | agentic_unverified_persons_report | 10 | 6 | 0.6 | 10:44 | 0 | 11:31 | 0 | 11:31 | 0 | 11:31 | 0 | 82.19 | 2226.97 |
| agentic | gpt-oss:120b-cloud | agentic_medical_emergency_in_flight | 4 | 0 | 0.0 | -- | 4 | -- | 4 | -- | 4 | -- | 4 | -- | -- |
| agentic | kimi-k2.7-code:cloud | agentic_medical_emergency_in_flight | 3 | 1 | 0.3333 | 11:15 | 0 | 11:21 | 0 | 11:21 | 0 | 11:21 | 0 | 67.02 | 2311.34 |
| agentic | kimi-k3:cloud | agentic_medical_emergency_in_flight | 10 | 7 | 0.7 | 10:52 | 0 | 11:27 | 0 | 11:27 | 0 | 11:27 | 0 | 58.85 | 3809.52 |
| agentic | kimi-k3:cloud | agentic_unverified_persons_report | 1 | 0 | 0.0 | -- | 1 | -- | 1 | -- | 1 | -- | 1 | -- | -- |
| agentic | minimax-m3:cloud | agentic_closed_loop | 10 | 1 | 0.1 | 10:59 | 0 | 11:30 | 0 | 11:30 | 0 | 11:30 | 0 | 55.2 | 3779.17 |
| agentic | minimax-m3:cloud | agentic_road_closure | 10 | 0 | 0.0 | -- | 10 | -- | 10 | -- | 10 | -- | 10 | -- | -- |
| agentic | nemotron-3-ultra:cloud | agentic_closed_loop | 2 | 0 | 0.0 | -- | 2 | -- | 2 | -- | 2 | -- | 2 | -- | -- |
| agentic | qwen3.5:cloud | agentic_bus1_suspension_capacity_reduction | 10 | 6 | 0.6 | 10:55 | 0 | 11:31 | 0 | 11:31 | 0 | 11:31 | 0 | 100.4 | 1860.95 |
| agentic | qwen3.5:cloud | agentic_closed_loop | 10 | 9 | 0.9 | 10:56 | 0 | 11:13 | 0 | 11:13 | 0 | 11:13 | 0 | 96.39 | 1756.71 |
| agentic | qwen3.5:cloud | agentic_conflicting_evacuation_orders | 10 | 8 | 0.8 | 10:55 | 0 | 11:09 | 0 | 11:09 | 0 | 11:09 | 0 | 86.38 | 1574.61 |
| agentic | qwen3.5:cloud | agentic_medical_emergency_in_flight | 10 | 8 | 0.8 | 10:54 | 0 | 11:15 | 0 | 11:15 | 0 | 11:15 | 0 | 105.27 | 1775.53 |
| agentic | qwen3.5:cloud | agentic_sc1_partial_capacity_loss | 10 | 5 | 0.5 | 10:49 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 92.27 | 1799.32 |
| agentic | qwen3.5:cloud | agentic_unverified_persons_report | 10 | 6 | 0.6 | 11:00 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 104.41 | 2043.56 |
| baseline |  | baseline_bus1_suspension_capacity_reduction | 10 | 10 | 1.0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| baseline |  | baseline_closed_loop | 10 | 10 | 1.0 | 10:24 | 0 | 11:37 | 0 | 11:37 | 0 | 11:37 | 0 | 60.63 | 0.0 |
| baseline |  | baseline_conflicting_evacuation_orders | 10 | 10 | 1.0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| baseline |  | baseline_medical_emergency_in_flight | 10 | 10 | 1.0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| baseline |  | baseline_road_closure | 10 | 10 | 1.0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 83.12 | 0.0 |
| baseline |  | baseline_sc1_partial_capacity_loss | 10 | 10 | 1.0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| baseline |  | baseline_unverified_persons_report | 10 | 10 | 1.0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |

## Gate 3 -- adaptability: A(z) over SIM_TIME_SCALE

One series per disruption and model. `Y` is the cell's **median** level, never its mean -- the DV is ordinal. The series are deliberately not pooled across models: a weak model that emits invalid plans would drag a strong one's median and the crossover would then belong to neither.

| disruption | model | scale | n_agentic | n_baseline | y_agentic | y_baseline | advantage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bus1_suspension_capacity_reduction | deepseek-v4-pro:0813-cloud | 8.4 | 10 | 10 | 2.0 | 4.0 | -2.0 |
| bus1_suspension_capacity_reduction | glm-5.2:cloud | 8.4 | 10 | 10 | 3.5 | 4.0 | -0.5 |
| bus1_suspension_capacity_reduction | qwen3.5:cloud | 8.4 | 10 | 10 | 3.5 | 4.0 | -0.5 |
| closed_loop | deepseek-v4-pro:0813-cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| closed_loop | glm-5.2:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| closed_loop | minimax-m3:cloud | 8.4 | 10 | 10 | 1.5 | 4.0 | -2.5 |
| closed_loop | nemotron-3-ultra:cloud | 8.4 | 2 | 10 | 0.0 | 4.0 | -4.0 |
| closed_loop | qwen3.5:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| conflicting_evacuation_orders | deepseek-v4-pro:0813-cloud | 8.4 | 10 | 10 | 2.0 | 4.0 | -2.0 |
| conflicting_evacuation_orders | glm-5.2:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| conflicting_evacuation_orders | qwen3.5:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | 8.4 | 10 | 10 | 2.0 | 4.0 | -2.0 |
| medical_emergency_in_flight | glm-5.2:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| medical_emergency_in_flight | gpt-oss:120b-cloud | 8.4 | 4 | 10 | 1.0 | 4.0 | -3.0 |
| medical_emergency_in_flight | kimi-k2.7-code:cloud | 8.4 | 3 | 10 | 2 | 4.0 | -2.0 |
| medical_emergency_in_flight | kimi-k3:cloud | 8.4 | 10 | 10 | 3.0 | 4.0 | -1.0 |
| medical_emergency_in_flight | qwen3.5:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| road_closure | deepseek-v4-pro:0813-cloud | 8.4 | 10 | 10 | 2.0 | 3.0 | -1.0 |
| road_closure | glm-5.2:cloud | 8.4 | 10 | 10 | 3.0 | 3.0 | 0.0 |
| road_closure | minimax-m3:cloud | 8.4 | 10 | 10 | 0.0 | 3.0 | -3.0 |
| sc1_partial_capacity_loss | deepseek-v4-pro:0813-cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| sc1_partial_capacity_loss | glm-5.2:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |
| sc1_partial_capacity_loss | qwen3.5:cloud | 8.4 | 10 | 10 | 3.0 | 4.0 | -1.0 |
| unverified_persons_report | deepseek-v4-pro:0813-cloud | 8.4 | 10 | 10 | 2.0 | 4.0 | -2.0 |
| unverified_persons_report | glm-5.2:cloud | 8.4 | 10 | 10 | 3.5 | 4.0 | -0.5 |
| unverified_persons_report | kimi-k3:cloud | 8.4 | 1 | 10 | 2 | 4.0 | -2.0 |
| unverified_persons_report | qwen3.5:cloud | 8.4 | 10 | 10 | 4.0 | 4.0 | 0.0 |

| disruption | model | scales | first_advantage | crossover_low | crossover_high |
| --- | --- | --- | --- | --- | --- |
| bus1_suspension_capacity_reduction | deepseek-v4-pro:0813-cloud | 1 | -2.0 | -- | -- |
| bus1_suspension_capacity_reduction | glm-5.2:cloud | 1 | -0.5 | -- | -- |
| bus1_suspension_capacity_reduction | qwen3.5:cloud | 1 | -0.5 | -- | -- |
| closed_loop | deepseek-v4-pro:0813-cloud | 1 | 0.0 | -- | -- |
| closed_loop | glm-5.2:cloud | 1 | 0.0 | -- | -- |
| closed_loop | minimax-m3:cloud | 1 | -2.5 | -- | -- |
| closed_loop | nemotron-3-ultra:cloud | 1 | -4.0 | -- | -- |
| closed_loop | qwen3.5:cloud | 1 | 0.0 | -- | -- |
| conflicting_evacuation_orders | deepseek-v4-pro:0813-cloud | 1 | -2.0 | -- | -- |
| conflicting_evacuation_orders | glm-5.2:cloud | 1 | 0.0 | -- | -- |
| conflicting_evacuation_orders | qwen3.5:cloud | 1 | 0.0 | -- | -- |
| medical_emergency_in_flight | deepseek-v4-pro:0813-cloud | 1 | -2.0 | -- | -- |
| medical_emergency_in_flight | glm-5.2:cloud | 1 | 0.0 | -- | -- |
| medical_emergency_in_flight | gpt-oss:120b-cloud | 1 | -3.0 | -- | -- |
| medical_emergency_in_flight | kimi-k2.7-code:cloud | 1 | -2.0 | -- | -- |
| medical_emergency_in_flight | kimi-k3:cloud | 1 | -1.0 | -- | -- |
| medical_emergency_in_flight | qwen3.5:cloud | 1 | 0.0 | -- | -- |
| road_closure | deepseek-v4-pro:0813-cloud | 1 | -1.0 | -- | -- |
| road_closure | glm-5.2:cloud | 1 | 0.0 | -- | -- |
| road_closure | minimax-m3:cloud | 1 | -3.0 | -- | -- |
| sc1_partial_capacity_loss | deepseek-v4-pro:0813-cloud | 1 | 0.0 | -- | -- |
| sc1_partial_capacity_loss | glm-5.2:cloud | 1 | 0.0 | -- | -- |
| sc1_partial_capacity_loss | qwen3.5:cloud | 1 | -1.0 | -- | -- |
| unverified_persons_report | deepseek-v4-pro:0813-cloud | 1 | -2.0 | -- | -- |
| unverified_persons_report | glm-5.2:cloud | 1 | -0.5 | -- | -- |
| unverified_persons_report | kimi-k3:cloud | 1 | -2.0 | -- | -- |
| unverified_persons_report | qwen3.5:cloud | 1 | 0.0 | -- | -- |

The crossover is a **band** and not a point: cron due-ness is evaluated once per wall-second, so every trigger carries +/- `scale` sim-seconds of jitter. A `--` band means the advantage never turned in the sampled range -- read `first_advantage` beside it to tell that from 'there was never an advantage to turn'.

## Reporting template (protocol sec. 14)

| disruption | system | model | n | levels | median_level | survival | gate1_pass_rate | rd | ci | gate1 | never_moved | late | refused | unaccounted | T50 | T50_censored | T90 | T90_censored | T95 | T95_censored | T100 | T100_censored | bus_km | latency_s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bus1_suspension_capacity_reduction | agentic | deepseek-v4-pro:0813-cloud | 10 | 0x1 1x1 2x6 4x2 | 2.0 | 0.755 | 0.2 | -0.245 | [-0.45, -0.08] | fail | 22.5 | 2.0 | 1.5 | 1 | 10:54 | 0 | 11:03 | 0 | 11:25 | 0 | 11:25 | 0 | 82.39 | 1349.4 |
| bus1_suspension_capacity_reduction | agentic | glm-5.2:cloud | 10 | 2x3 3x2 4x5 | 3.5 | 0.85 | 0.7 | -0.15 | [-0.3, 0.0] | fail | 15.0 | 0.0 | 0.0 | 0 | 10:58 | 0 | 11:15 | 0 | 11:15 | 0 | 11:15 | 0 | 75.04 | 2528.07 |
| bus1_suspension_capacity_reduction | agentic | qwen3.5:cloud | 10 | 2x4 3x1 4x5 | 3.5 | 0.92 | 0.6 | -0.08 | [-0.18, -0.01] | fail | 2.0 | 6.0 | 0.0 | 0 | 10:55 | 0 | 11:31 | 0 | 11:31 | 0 | 11:31 | 0 | 100.4 | 1860.95 |
| bus1_suspension_capacity_reduction | baseline | none | 10 | 4x10 | 4.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| closed_loop | agentic | deepseek-v4-pro:0813-cloud | 10 | 0x1 2x3 4x6 | 4.0 | 0.79 | 0.6 | -0.21 | [-0.42, -0.03] | fail | 11.0 | 10.0 | 0.0 | 0 | 10:59 | 0 | 11:09 | 0 | 11:19 | 0 | 11:19 | 0 | 84.98 | 763.39 |
| closed_loop | agentic | glm-5.2:cloud | 10 | 4x10 | 4.0 | 1.0 | 1.0 | 0.0 | [0.0, 0.0] | pass | 0.0 | 0.0 | 0.0 | 0 | 10:57 | 0 | 11:17 | 0 | 11:17 | 0 | 11:17 | 0 | 75.64 | 1536.97 |
| closed_loop | agentic | minimax-m3:cloud | 10 | 0x4 1x1 2x4 3x1 | 1.5 | 0.34 | 0.1 | -0.66 | [-0.85, -0.46] | fail | 36.0 | 30.0 | 0.0 | 0 | 10:59 | 0 | 11:30 | 0 | 11:30 | 0 | 11:30 | 0 | 55.2 | 3779.17 |
| closed_loop | agentic | nemotron-3-ultra:cloud | 2 | 0x2 | 0.0 | 0.0 | 0.0 | -1.0 | [-1.0, -1.0] | fail | 100.0 | 0.0 | 0.0 | 0 | -- | 2 | -- | 2 | -- | 2 | -- | 2 | -- | -- |
| closed_loop | agentic | qwen3.5:cloud | 10 | 2x1 3x3 4x6 | 4.0 | 0.95 | 0.9 | -0.05 | [-0.15, 0.0] | fail | 5.0 | 0.0 | 0.0 | 0 | 10:56 | 0 | 11:13 | 0 | 11:13 | 0 | 11:13 | 0 | 96.39 | 1756.71 |
| closed_loop | baseline | none | 10 | 4x10 | 4.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 0 | 10:24 | 0 | 11:37 | 0 | 11:37 | 0 | 11:37 | 0 | 60.63 | 0.0 |
| conflicting_evacuation_orders | agentic | deepseek-v4-pro:0813-cloud | 10 | 0x1 1x2 2x6 4x1 | 2.0 | 0.65 | 0.1 | -0.35 | [-0.55, -0.17] | fail | 19.0 | 16.0 | 0.0 | 0 | 11:00 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 63.25 | 914.35 |
| conflicting_evacuation_orders | agentic | glm-5.2:cloud | 10 | 2x3 4x7 | 4.0 | 0.85 | 0.7 | -0.15 | [-0.3, 0.0] | fail | 15.0 | 0.0 | 0.0 | 0 | 10:44 | 0 | 11:25 | 0 | 11:25 | 0 | 11:25 | 0 | 76.33 | 1468.54 |
| conflicting_evacuation_orders | agentic | qwen3.5:cloud | 10 | 2x2 3x1 4x7 | 4.0 | 0.98 | 0.8 | -0.02 | [-0.05, 0.0] | fail | 2.0 | 0.0 | 0.0 | 0 | 10:55 | 0 | 11:09 | 0 | 11:09 | 0 | 11:09 | 0 | 86.38 | 1574.61 |
| conflicting_evacuation_orders | baseline | none | 10 | 4x10 | 4.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| medical_emergency_in_flight | agentic | deepseek-v4-pro:0813-cloud | 10 | 0x1 1x1 2x4 4x4 | 2.0 | 0.8 | 0.4 | -0.2 | [-0.42, -0.04] | fail | 13.0 | 10.0 | 0.0 | 1 | 10:47 | 0 | 10:58 | 0 | 10:58 | 0 | 10:58 | 0 | 74.42 | 975.65 |
| medical_emergency_in_flight | agentic | glm-5.2:cloud | 10 | 2x3 4x7 | 4.0 | 0.85 | 0.7 | -0.15 | [-0.3, 0.0] | fail | 10.0 | 5.0 | 0.0 | 0 | 10:38 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 67.02 | 2051.81 |
| medical_emergency_in_flight | agentic | gpt-oss:120b-cloud | 4 | 0x2 2x2 | 1.0 | 0.375 | 0.0 | -0.625 | [-1.0, -0.25] | fail | 50.0 | 12.5 | 0.0 | 0 | -- | 4 | -- | 4 | -- | 4 | -- | 4 | -- | -- |
| medical_emergency_in_flight | agentic | kimi-k2.7-code:cloud | 3 | 2x2 3x1 | 2 | 0.6667 | 0.3333 | -0.3333 | [-0.5, 0.0] | fail | 33.3 | 0.0 | 0.0 | 0 | 11:15 | 0 | 11:21 | 0 | 11:21 | 0 | 11:21 | 0 | 67.02 | 2311.34 |
| medical_emergency_in_flight | agentic | kimi-k3:cloud | 10 | 0x1 2x2 3x7 | 3.0 | 0.8 | 0.7 | -0.2 | [-0.45, 0.0] | fail | 20.0 | 0.0 | 0.0 | 0 | 10:52 | 0 | 11:27 | 0 | 11:27 | 0 | 11:27 | 0 | 58.85 | 3809.52 |
| medical_emergency_in_flight | agentic | qwen3.5:cloud | 10 | 2x2 3x1 4x7 | 4.0 | 0.92 | 0.8 | -0.08 | [-0.21, 0.02] | fail | 5.0 | 0.0 | 8.0 | 1 | 10:54 | 0 | 11:15 | 0 | 11:15 | 0 | 11:15 | 0 | 105.27 | 1775.53 |
| medical_emergency_in_flight | baseline | none | 10 | 4x10 | 4.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| road_closure | agentic | deepseek-v4-pro:0813-cloud | 10 | 0x2 1x1 2x4 3x1 4x2 | 2.0 | 0.7 | 0.3 | -0.3 | [-0.55, -0.08] | fail | 16.0 | 14.0 | 0.0 | 0 | 10:49 | 0 | 11:24 | 0 | 11:24 | 0 | 11:24 | 0 | 102.45 | 1310.54 |
| road_closure | agentic | glm-5.2:cloud | 10 | 1x1 2x2 3x5 4x2 | 3.0 | 0.84 | 0.7 | -0.16 | [-0.32, 0.0] | fail | 6.0 | 10.0 | 0.0 | 0 | 10:40 | 0 | 11:14 | 0 | 11:14 | 0 | 11:14 | 0 | 101.42 | 1643.46 |
| road_closure | agentic | minimax-m3:cloud | 10 | 0x7 2x3 | 0.0 | 0.15 | 0.0 | -0.85 | [-1.0, -0.7] | fail | 85.0 | 0.0 | 0.0 | 0 | -- | 10 | -- | 10 | -- | 10 | -- | 10 | -- | -- |
| road_closure | baseline | none | 10 | 3x10 | 3.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 11:12 | 0 | 83.12 | 0.0 |
| sc1_partial_capacity_loss | agentic | deepseek-v4-pro:0813-cloud | 10 | 0x2 2x2 4x6 | 4.0 | 0.74 | 0.6 | -0.26 | [-0.52, -0.03] | fail | 16.0 | 10.0 | 0.0 | 0 | 10:52 | 0 | 11:10 | 0 | 11:27 | 0 | 11:27 | 0 | 83.1 | 1009.38 |
| sc1_partial_capacity_loss | agentic | glm-5.2:cloud | 10 | 0x1 2x2 4x7 | 4.0 | 0.81 | 0.7 | -0.19 | [-0.42, 0.0] | fail | 14.0 | 5.0 | 0.0 | 0 | 11:07 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 75.07 | 2490.11 |
| sc1_partial_capacity_loss | agentic | qwen3.5:cloud | 10 | 0x1 1x1 2x3 4x5 | 3.0 | 0.78 | 0.5 | -0.22 | [-0.44, -0.03] | fail | 2.5 | 25.5 | 4.0 | 2 | 10:49 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 92.27 | 1799.32 |
| sc1_partial_capacity_loss | baseline | none | 10 | 4x10 | 4.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |
| unverified_persons_report | agentic | deepseek-v4-pro:0813-cloud | 10 | 2x8 4x2 | 2.0 | 0.69 | 0.2 | -0.31 | [-0.44, -0.17] | fail | 21.0 | 10.0 | 0.0 | 0 | 10:52 | 0 | 11:13 | 0 | 11:13 | 0 | 11:13 | 0 | 80.5 | 814.92 |
| unverified_persons_report | agentic | glm-5.2:cloud | 10 | 2x4 3x1 4x5 | 3.5 | 0.84 | 0.6 | -0.16 | [-0.31, -0.03] | fail | 10.0 | 6.0 | 0.0 | 0 | 10:44 | 0 | 11:31 | 0 | 11:31 | 0 | 11:31 | 0 | 82.19 | 2226.97 |
| unverified_persons_report | agentic | kimi-k3:cloud | 1 | 2x1 | 2 | 0.5 | 0.0 | -0.5 | [-0.5, -0.5] | fail | 50.0 | 0.0 | 0.0 | 0 | -- | 1 | -- | 1 | -- | 1 | -- | 1 | -- | -- |
| unverified_persons_report | agentic | qwen3.5:cloud | 10 | 2x4 4x6 | 4.0 | 0.9 | 0.6 | -0.1 | [-0.23, 0.0] | fail | 4.0 | 3.0 | 8.0 | 1 | 11:00 | 0 | 11:19 | 0 | 11:19 | 0 | 11:19 | 0 | 104.41 | 2043.56 |
| unverified_persons_report | baseline | none | 10 | 4x10 | 4.0 | 1.0 | 1.0 | ref | ref | ref | 0.0 | 0.0 | 0.0 | 0 | 10:39 | 0 | 11:52 | 0 | 11:52 | 0 | 11:52 | 0 | 60.63 | 0.0 |

`unaccounted` counts the runs in the cell whose three loss channels do not reconcile with the shortfall. Anything but 0 means the log recorded more dropoffs than the ceiling admits -- read it before the cell's `never_moved`, which is floored at zero.

### Sensitivity across the cut points

Protocol sec. 14 item 1: the headline may not be reported without this, so it sits beside the table above rather than after it. Each column re-reads the cell's median level with `LEVEL_1_2_CUT` moved to that cut. **These are not the published levels** -- the level-4 promotion is applied after the sensitivity map is built, so a cell reading 3 here can publish a median of 4. Compare the cuts against each other. `stable` is true when the cell reads the same at all three, which is the claim the headline actually needs.

| disruption | system | model | n | median@0.40 | median@0.50 | median@0.60 | stable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bus1_suspension_capacity_reduction | agentic | deepseek-v4-pro:0813-cloud | 10 | 2.0 | 2.0 | 2.0 | True |
| bus1_suspension_capacity_reduction | agentic | glm-5.2:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| bus1_suspension_capacity_reduction | agentic | qwen3.5:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| bus1_suspension_capacity_reduction | baseline | none | 10 | 3.0 | 3.0 | 3.0 | True |
| closed_loop | agentic | deepseek-v4-pro:0813-cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| closed_loop | agentic | glm-5.2:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| closed_loop | agentic | minimax-m3:cloud | 10 | 2.0 | 1.5 | 1.0 | False |
| closed_loop | agentic | nemotron-3-ultra:cloud | 2 | 0.0 | 0.0 | 0.0 | True |
| closed_loop | agentic | qwen3.5:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| closed_loop | baseline | none | 10 | 3.0 | 3.0 | 3.0 | True |
| conflicting_evacuation_orders | agentic | deepseek-v4-pro:0813-cloud | 10 | 2.0 | 2.0 | 2.0 | True |
| conflicting_evacuation_orders | agentic | glm-5.2:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| conflicting_evacuation_orders | agentic | qwen3.5:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| conflicting_evacuation_orders | baseline | none | 10 | 3.0 | 3.0 | 3.0 | True |
| medical_emergency_in_flight | agentic | deepseek-v4-pro:0813-cloud | 10 | 2.0 | 2.0 | 2.0 | True |
| medical_emergency_in_flight | agentic | glm-5.2:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| medical_emergency_in_flight | agentic | gpt-oss:120b-cloud | 4 | 1.0 | 1.0 | 1.0 | True |
| medical_emergency_in_flight | agentic | kimi-k2.7-code:cloud | 3 | 2 | 2 | 1 | False |
| medical_emergency_in_flight | agentic | kimi-k3:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| medical_emergency_in_flight | agentic | qwen3.5:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| medical_emergency_in_flight | baseline | none | 10 | 3.0 | 3.0 | 3.0 | True |
| road_closure | agentic | deepseek-v4-pro:0813-cloud | 10 | 2.0 | 2.0 | 2.0 | True |
| road_closure | agentic | glm-5.2:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| road_closure | agentic | minimax-m3:cloud | 10 | 0.0 | 0.0 | 0.0 | True |
| road_closure | baseline | none | 10 | 3.0 | 3.0 | 3.0 | True |
| sc1_partial_capacity_loss | agentic | deepseek-v4-pro:0813-cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| sc1_partial_capacity_loss | agentic | glm-5.2:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| sc1_partial_capacity_loss | agentic | qwen3.5:cloud | 10 | 2.5 | 2.5 | 2.5 | True |
| sc1_partial_capacity_loss | baseline | none | 10 | 3.0 | 3.0 | 3.0 | True |
| unverified_persons_report | agentic | deepseek-v4-pro:0813-cloud | 10 | 2.0 | 2.0 | 1.5 | False |
| unverified_persons_report | agentic | glm-5.2:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| unverified_persons_report | agentic | kimi-k3:cloud | 1 | 2 | 2 | 1 | False |
| unverified_persons_report | agentic | qwen3.5:cloud | 10 | 3.0 | 3.0 | 3.0 | True |
| unverified_persons_report | baseline | none | 10 | 3.0 | 3.0 | 3.0 | True |
