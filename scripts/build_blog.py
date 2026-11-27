"""Generate the blog home page, the category pages and the sitemap from blog/posts.js.

Run from the repository root:  python3 scripts/build_blog.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://sagarkhaprepodcast.in"

def load_js_array(text, name):
    m = re.search(r"window\." + name + r"\s*=\s*(\[.*?\n\]);", text, re.S)
    return json.loads(m.group(1))

def main():
    js = open(os.path.join(ROOT, "blog", "posts.js"), encoding="utf-8").read()
    cats = load_js_array(js, "BLOG_CATEGORIES")
    posts = load_js_array(js, "BLOG_POSTS")
    tpl = open(os.path.join(ROOT, "scripts", "blog_template.html"), encoding="utf-8").read()

    def render(path, title, desc, eyebrow, h1, cat):
        html = (tpl.replace("{{TITLE}}", title).replace("{{DESC}}", desc).replace("{{PATH}}", path)
                   .replace("{{EYEBROW}}", eyebrow).replace("{{H1}}", h1).replace("{{CAT}}", cat))
        out = os.path.join(ROOT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(html)

    render("/blog/", "Blog | My Take by Sagar Khapre | Are Baap Re Podcast",
           "Sagar Khapre's honest take on cricket, health myths, Ayurveda, astrology, Nagpur, business and tech.",
           "The Are Baapre blog", "My <span>take</span>", "all")
    for c in cats:
        name = c["name"]
        render("/blog/category/%s/" % c["slug"], "%s | Sagar Khapre Blog" % name.replace("&", "&amp;"),
               "Sagar Khapre's take on %s." % name.replace("&", "and").lower(),
               "Category", name.replace("&", "<span>&amp;</span>"), c["slug"])

    urls = [("/", "daily", "1.0"), ("/blog/", "weekly", "0.9")]
    urls += [("/blog/%s/" % p["slug"], "monthly", "0.8") for p in posts]
    # Translated versions (e.g. blog/<slug>/hi/) are added when the folder exists.
    urls += [("/blog/%s/%s/" % (p["slug"], lang), "monthly", "0.7") for p in posts for lang in ("hi", "mr")
             if os.path.exists(os.path.join(ROOT, "blog", p["slug"], lang, "index.html"))]
    urls += [("/blog/category/%s/" % c["slug"], "weekly", "0.6") for c in cats]
    latest = max([p["date"] for p in posts] or ["2026-11-12"])
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, freq, pr in urls:
        lines.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>" % (SITE, u, latest, freq, pr))
    lines.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("Built blog home, %d category pages, sitemap with %d URLs" % (len(cats), len(urls)))

if __name__ == "__main__":
    main()
