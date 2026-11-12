"""Fetch the latest long-form videos from the YouTube channel RSS feed and write videos.js."""
import datetime, json, re, urllib.request, xml.etree.ElementTree as ET

CHANNEL_ID = "UCPnnMdolHLWL_uUo_Ij4QJg"
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015",
      "media": "http://search.yahoo.com/mrss/"}
UA = {"User-Agent": "Mozilla/5.0"}

def is_short(vid):
    req = urllib.request.Request(f"https://www.youtube.com/shorts/{vid}", headers=UA, method="HEAD")
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k): return None
    try:
        return urllib.request.build_opener(NoRedirect).open(req, timeout=20).status == 200
    except Exception:
        return False

def main():
    xml = urllib.request.urlopen(urllib.request.Request(FEED, headers=UA), timeout=30).read()
    root = ET.fromstring(xml)
    videos = []
    for e in root.findall("a:entry", NS):
        vid = e.find("yt:videoId", NS).text
        if is_short(vid):
            continue
        title = e.find("a:title", NS).text or ""
        title = re.sub(r"(\s*#\w+)+\s*$", "", title).rstrip(" |")
        stats = e.find("media:group/media:community/media:statistics", NS)
        videos.append({
            "id": vid,
            "title": title,
            "date": e.find("a:published", NS).text[:10],
            "views": int(stats.get("views", 0)) if stats is not None else 0,
            "duration": "",
            "thumb": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        })
    videos = videos[:12]
    if not videos:
        raise SystemExit("No videos found; keeping existing videos.js")
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).date().isoformat()
    with open("videos.js", "w", encoding="utf-8") as f:
        f.write(f'window.VIDEOS_UPDATED = "{today}";\nwindow.VIDEOS = ')
        f.write(json.dumps(videos, ensure_ascii=False, indent=0))
        f.write(";\n")
    print(f"Wrote {len(videos)} videos")

if __name__ == "__main__":
    main()
