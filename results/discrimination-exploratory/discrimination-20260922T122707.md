# Instrument discrimination -- PASS

No-replan control vs. the doctrine (EVALUATION_PROTOCOL sec. 5.4). PASS iff a **gate** row's no-replan level is strictly below the doctrine's. Note rows are descriptive and never enter the verdict. Both variants are scored without a clean-run reference, so both cap at level 3.

commit `a15c1c5a0dec8fade1631d311397d82cc832bb97` · thresholds `d08c1e35380f`

| role | scenario | world | orders identical | doctrine L (C) | no-replan L (C) | doctrine km | no-replan km | discriminates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gate | evaluation/fixtures/baseline_shelter_closure.json | yes | no | 3 (1.0) | 0 (0.0) | 83.122 | 38.139 | yes |
| note | scenarios/baseline_medical_emergency_in_flight.json | yes | yes | 3 (1.0) | 3 (1.0) | 60.63 | 60.63 | no |
| note | scenarios/baseline_unverified_persons_report.json | yes | yes | 3 (1.0) | 3 (1.0) | 60.63 | 60.63 | no |
| note | scenarios/baseline_conflicting_evacuation_orders.json | yes | yes | 3 (1.0) | 3 (1.0) | 60.63 | 60.63 | no |
| note | scenarios/baseline_bus1_suspension_capacity_reduction.json | yes | yes | 3 (1.0) | 3 (1.0) | 60.63 | 60.63 | no |
| note | scenarios/baseline_sc1_partial_capacity_loss.json | yes | yes | 3 (1.0) | 3 (1.0) | 60.63 | 60.63 | no |
| note | scenarios/baseline_closed_loop.json | yes | yes | 3 (1.0) | 3 (1.0) | 60.63 | 60.63 | no |
| note | scenarios/baseline_road_closure.json | no | no | 3 (1.0) | 3 (1.0) | 83.122 | 38.139 | no |

Run ids:

- discrimination-baseline_shelter_closure-ic-20260922T122707 · discrimination-baseline_shelter_closure-no_replan-20260922T122707
- discrimination-baseline_medical_emergency_in_flight-ic-20260922T122707 · discrimination-baseline_medical_emergency_in_flight-no_replan-20260922T122707
- discrimination-baseline_unverified_persons_report-ic-20260922T122707 · discrimination-baseline_unverified_persons_report-no_replan-20260922T122707
- discrimination-baseline_conflicting_evacuation_orders-ic-20260922T122707 · discrimination-baseline_conflicting_evacuation_orders-no_replan-20260922T122707
- discrimination-baseline_bus1_suspension_capacity_reduction-ic-20260922T122707 · discrimination-baseline_bus1_suspension_capacity_reduction-no_replan-20260922T122707
- discrimination-baseline_sc1_partial_capacity_loss-ic-20260922T122707 · discrimination-baseline_sc1_partial_capacity_loss-no_replan-20260922T122707
- discrimination-baseline_closed_loop-ic-20260922T122707 · discrimination-baseline_closed_loop-no_replan-20260922T122707
- discrimination-baseline_road_closure-ic-20260922T122707 · discrimination-baseline_road_closure-no_replan-20260922T122707
