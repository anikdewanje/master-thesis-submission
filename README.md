# RescueSim evaluation data

Evaluation data for the master thesis *Design and Evaluation of a
Database-Centric Agentic Architecture for Nursing Home Evacuation Coordination
in Storm Surge Scenarios* (Anik Dewanje, TU Ilmenau, 2026).

The thesis compares a database-centric agentic system with a scripted workflow
baseline on a nursing-home evacuation. Every run of both systems writes to one
append-only PostgreSQL table, `event_log`, and one deterministic scorer reads
that table. This repository holds the scored results and a full copy of that
table, so that every number in the thesis can be traced to the rows it came
from.

The code of both systems, the harness and the scorer is in the private
repository `absolutehh/RescuemateEvacuationWithAgents` of Absolute Software
GmbH. Read access is available through the company.

## Layout

| Path | Content |
| --- | --- |
| `results/runs.jsonl` | One record per scored run (310): manifest, outcome, row count `n_event_rows` and `log_checksum` of its event log |
| `results/scores.jsonl` | The scores of the 310 runs, behind the thesis's results tables |
| `results/summary.md` | The summary tables produced by `python -m evaluation summarize` |
| `results/rubric.jsonl`, `results/rubric.md` | The held-out decision rubric, 218 novel-arm runs (secondary, descriptive) |
| `results/logs/<run_id>/` | Each agent's process log for one run, gzipped |
| `results/pilot/`, `results/screening*/`, `results/block-nemotron/`, `results/smoke/` | Pilot, model screening and smoke runs. Exploratory, never pooled with the scored runs |
| `results/campaign/`, `results/novel/` | Sweep logs of the anticipated arm and the novel arm |
| `results/discrimination*/` | The negative-control check (2026-09-14) and the exploratory re-check (2026-09-22) |
| `results/equivalence/` | Evidence that the post-reveal baseline change left its behaviour unchanged (pre-registration Amendment 6) |
| `results/v2/` | Exploratory process measures of Protocol v2 (Amendment 16) |
| `results/archive/` | Runs set aside: the invalid headless pilot, a partial gemma4 pilot, and pilot baseline runs from a dirty working tree |
| `event_log/event_log.sql.gz` | `pg_dump` of the `event_log` table, with its append-only trigger |
| `event_log/event_log.jsonl.gz` | The same table as JSON Lines, one row per line in insertion order |
| `verify_checksums.py` | Checks every scored run against its event log (standard library only) |
| `SHA256SUMS` | Checksums of the two event-log files |

`results/` is an unchanged copy of `evaluation/results/` in the RescueSim
repository. That folder is not tracked in the RescueSim repository.

The event log holds 135,293 rows from 1,114 runs. Besides the 310 scored runs,
it includes the pilot, screening, smoke and test runs. Join on `run_id` to
select the scored ones.

## Check the logs against the scored runs

```sh
sha256sum -c SHA256SUMS
python verify_checksums.py
```

The script recomputes each run's row count and SHA-256 checksum from
`event_log.jsonl.gz` and compares them with the values the harness recorded in
`results/runs.jsonl` when the run ended. The expected output is

```text
310 of 310 runs match their recorded row count and log checksum
```

The checksum is the harness's own (`evaluation/harness/run_one.py`,
`log_fingerprint`). Each row is reduced to `agent_key`, `id`, `kind`,
`subkind`, `sim_time`, `summary` and `details` and hashed. The row hashes are
sorted, joined and hashed again, so row order does not matter. The harness
takes the checksum before it appends its own `run_outcome` row, which carries
the checksum, so the script leaves that row out.

## Restore the table into PostgreSQL

```sh
createdb rescuesim
gunzip -c event_log/event_log.sql.gz | psql -d rescuesim
```

The dump was taken from PostgreSQL 16. It creates the `event_log` table, its
indexes and the trigger that rejects every `UPDATE` and `DELETE`.

## Score the runs again

With the RescueSim repository checked out and its `DATABASE_URL` pointing at
the restored database:

```sh
python -m evaluation score-all --results results/runs.jsonl --out scores.jsonl
python -m evaluation summarize --scores scores.jsonl --out-dir . \
  --novel medical_emergency_in_flight unverified_persons_report \
          conflicting_evacuation_orders bus1_suspension_capacity_reduction \
          sc1_partial_capacity_loss
python -m evaluation rubric-all --results results/runs.jsonl --out rubric.jsonl
```

The scorer reads its thresholds from `evaluation/thresholds.py`. Every scored
run records the file's SHA-256 (`d08c1e35…`) in its manifest. The hash was
taken over the file with Windows (CRLF) line endings, so a checkout with LF
line endings hashes differently.

## Reference points in the RescueSim repository

| Tag | Commit | Meaning |
| --- | --- | --- |
| `eval-day-2026-09-10` | `67a14f8` | Baseline freeze, before the novel disruptions were revealed |
| `prereg-v1` | `7a4d7cc` | Pre-registration, 2026-09-12 |
| `prereg-amendment-1` | `7a4d7cc` | Amendment 1, same commit |

Amendments 2 to 16 are appended to `docs/PREREGISTRATION.md` without a tag.
A diff of that file against `prereg-v1` contains only added lines.

## Provenance

The event log was exported on 2026-10-07 from the PostgreSQL database the
campaign wrote to. A restore of `event_log.sql.gz` into an empty database was
compared with the source table and matched on all 135,293 rows.
