#!/usr/bin/env python3
"""Build github.json from the GitHub API (used by .github/workflows/github.yml).

Writes github.json: the 6 repos with the most recent commits AUTHORED BY the
site owner. Bot commits (the Strava/Letterboxd data pipelines in this repo)
are excluded by the author filter, so the file only changes when Noah
actually ships something - keeping only-if-changed commits meaningful.

The 30-day commit window is anchored to each repo's newest authored commit,
not the wall clock, so output is deterministic for a given repo state.

Auth: set GH_TOKEN (optional locally, required on Actions runners whose
shared IPs exhaust the unauthenticated rate limit).
Test locally: GH_TOKEN=$(gh auth token) python3 scripts/build_github_json.py
"""
import json
import os
import pathlib
import sys
import urllib.request
from datetime import datetime, timedelta

USER = "noahfoster2174"
OUT_PATH = pathlib.Path("github.json")
WINDOW = timedelta(days=30)
MAX_REPOS = 6


def api(path):
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def parse(ts):
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def main():
    repos = api(f"/users/{USER}/repos?sort=pushed&per_page=20&type=owner")
    out = []
    for repo in repos:
        if repo.get("fork") or repo.get("archived"):
            continue
        if len(out) >= MAX_REPOS + 2:  # small buffer before the final sort/cut
            break
        try:
            commits = api(f"/repos/{repo['full_name']}/commits?author={USER}&per_page=30")
        except Exception as e:
            print(f"skip {repo['full_name']}: {e}", file=sys.stderr)
            continue
        if not commits:
            continue
        newest = commits[0]["commit"]["committer"]["date"]
        cutoff = parse(newest) - WINDOW
        recent = sum(1 for c in commits if parse(c["commit"]["committer"]["date"]) >= cutoff)
        out.append({
            "repo": repo["name"],
            "url": repo["html_url"],
            "last_commit": newest,
            "commits_30d": recent,
            "latest": commits[0]["commit"]["message"].splitlines()[0][:80],
        })

    out.sort(key=lambda r: r["last_commit"], reverse=True)
    OUT_PATH.write_text(json.dumps(out[:MAX_REPOS], indent=2) + "\n")


if __name__ == "__main__":
    main()
