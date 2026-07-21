"""
visuals.py
Story-based visual fetcher
"""

import os
import random
import re
import requests

PIXABAY_SEARCH_URL = "https://pixabay.com/api/videos/"


def _clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    words = [w for w in text.split() if len(w) > 2]
    return " ".join(words[:4])


def _queries(scene):
    queries = []

    for k in scene.get("keywords", []):
        q = _clean(k)
        if q and q not in queries:
            queries.append(q)

    visual = _clean(scene.get("visual", ""))
    if visual and visual not in queries:
        queries.insert(0, visual)

    return queries


def _find_video(scene):
    for query in _queries(scene):
        r = requests.get(
            PIXABAY_SEARCH_URL,
            params={
                "key": os.environ["PIXABAY_API_KEY"],
                "q": query,
                "video_type": "film",
                "per_page": 10,
            },
            timeout=20,
        )

        if r.status_code != 200:
            continue

        hits = r.json().get("hits", [])
        if not hits:
            continue

        hit = random.choice(hits)
        videos = hit["videos"]

        for tier in ("large", "medium", "small", "tiny"):
            if tier in videos:
                return videos[tier]["url"]

    return None


def _download(url, out_path):
    r = requests.get(url, stream=True, timeout=60)
    r.raise_for_status()

    with open(out_path, "wb") as f:
        for chunk in r.iter_content(1024 * 1024):
            f.write(chunk)


def fetch_visuals_for_script(script, config, workdir):
    os.makedirs(workdir, exist_ok=True)

    paths = []

    for i, scene in enumerate(script["scene_plan"], start=1):
        url = _find_video(scene)

        if not url:
            paths.append(None)
            continue

        out = os.path.join(workdir, f"scene_{i}.mp4")
        _download(url, out)
        paths.append(out)

    return paths
