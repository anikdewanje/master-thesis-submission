"""Check every scored run against its event log.

For each run in results/runs.jsonl, recompute the row count and the SHA-256
log checksum from event_log/event_log.jsonl.gz and compare them with the
values the harness recorded when the run finished (n_event_rows,
log_checksum).

The checksum is the one in RescueSim's evaluation/harness/run_one.py
(log_fingerprint): each row is reduced to agent_key, id, kind, subkind,
sim_time, summary and details, serialised as sorted-key JSON and hashed; the
row digests are sorted, concatenated and hashed again. run_id and ts are left
out. Sorting makes the checksum independent of row order.

The harness takes the fingerprint first and then appends one row of its own,
kind run_outcome, which carries the fingerprint. That row cannot cover itself,
so it is left out here, as it was absent when the checksum was taken.

Standard library only. Usage:

    python verify_checksums.py [--runs results/runs.jsonl]
                               [--log event_log/event_log.jsonl.gz]
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
from collections import defaultdict

FIELDS = ("agent_key", "id", "kind", "subkind", "sim_time", "summary", "details")


def row_digest(row: dict) -> str:
    blob = json.dumps(
        {k: row.get(k) for k in FIELDS},
        sort_keys=True,
        default=str,
        ensure_ascii=False,
    )
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--runs", default="results/runs.jsonl")
    ap.add_argument("--log", default="event_log/event_log.jsonl.gz")
    args = ap.parse_args()

    runs = []
    with open(args.runs, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                runs.append(json.loads(line))
    wanted = {r["run_id"] for r in runs}

    digests: dict[str, list[str]] = defaultdict(list)
    with gzip.open(args.log, "rt", encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row["run_id"] in wanted and row["kind"] != "run_outcome":
                digests[row["run_id"]].append(row_digest(row))

    ok = 0
    bad = []
    for r in runs:
        d = digests.get(r["run_id"], [])
        checksum = hashlib.sha256("".join(sorted(d)).encode("ascii")).hexdigest()
        if len(d) == r.get("n_event_rows") and checksum == r.get("log_checksum"):
            ok += 1
        else:
            bad.append((r["run_id"], r.get("n_event_rows"), len(d)))

    print(f"{ok} of {len(runs)} runs match their recorded row count and log checksum")
    for run_id, rec, got in bad:
        print(f"  MISMATCH {run_id}: recorded {rec} rows, found {got}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
