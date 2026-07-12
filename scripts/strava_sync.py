#!/usr/bin/env python3
"""Sync Strava activity data for the site (used by .github/workflows/strava.yml).

Reads a raw Strava /athlete/activities JSON array on stdin and writes:
  strava.json          - the 5 most recent runs, shape unchanged since 2026-02
  strava-history.json  - compact append-only run history for the mileage graph

Idempotent: running twice on the same input produces byte-identical files.
Test locally: cat sample.json | python3 scripts/strava_sync.py
"""
import json
import pathlib
import sys

METERS_PER_MILE = 1609.34
RECENT_KEYS = ["name", "distance", "moving_time", "start_date_local", "type"]
RECENT_PATH = pathlib.Path("strava.json")
HISTORY_PATH = pathlib.Path("strava-history.json")


def write(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def main():
    activities = json.load(sys.stdin)
    runs = [a for a in activities if a.get("type") == "Run"]

    recent = []
    for a in runs:
        entry = {k: a[k] for k in RECENT_KEYS if k in a}
        entry["polyline"] = a.get("map", {}).get("summary_polyline", "")
        recent.append(entry)
    write(RECENT_PATH, recent[:5])

    # History entries keep only date + miles. Strava's start_date_local carries
    # a fake "Z" suffix (the value is local time, not UTC) - strip it so
    # downstream code is never tempted to UTC-parse it.
    history = json.loads(HISTORY_PATH.read_text()) if HISTORY_PATH.exists() else []
    by_ts = {e["d"]: e for e in history}
    for a in runs:
        ts = (a.get("start_date_local") or "").rstrip("Z")
        if ts:
            by_ts[ts] = {"d": ts, "mi": round(a["distance"] / METERS_PER_MILE, 2)}
    write(HISTORY_PATH, sorted(by_ts.values(), key=lambda e: e["d"]))


if __name__ == "__main__":
    main()
