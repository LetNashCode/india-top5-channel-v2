import os
import requests

API_URL = "https://freesound.org/apiv2/search/text/"


def _search(api_key, query):

    params = {
        "query": query,
        "fields": "id,name,previews",
        "filter": "tag:music duration:[20 TO 300]",
        "sort": "score",
        "token": api_key,
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=60,
    )

    response.raise_for_status()

    return response.json().get("results", [])


def download_music(script, workdir):

    os.makedirs(workdir, exist_ok=True)

    api_key = os.environ["FREESOUND_API_KEY"]

    searches = [
        script.get("music_search", ""),
        "cinematic",
        "epic",
        "orchestral",
        "suspense",
        "ambient",
        "horror",
        "dramatic",
        "trailer",
    ]

    music = None

    for query in searches:

        if not query:
            continue

        print("=" * 80)
        print("🎵 Searching Freesound")
        print(query)
        print("=" * 80)

        try:
            results = _search(api_key, query)

            if results:
                music = results[0]
                break

        except Exception as e:
            print(e)

    if music is None:
        print("⚠️ No background music found.")
        return None

    preview_url = (
        music.get("previews", {}).get("preview-hq-mp3")
        or music.get("previews", {}).get("preview-lq-mp3")
    )

    if not preview_url:
        print("⚠️ Music preview unavailable.")
        return None

    print(f"Selected: {music['name']}")

    path = os.path.join(
        workdir,
        "background.mp3",
    )

    audio = requests.get(
        preview_url,
        timeout=120,
    )

    audio.raise_for_status()

    with open(path, "wb") as f:
        f.write(audio.content)

    print(f"Saved: {path}")

    return path
