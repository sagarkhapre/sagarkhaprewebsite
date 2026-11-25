# Changelog — sagarkhaprepodcast.in

Every change to the website is recorded here, newest first.

**How releases work**
- Every change is built on its own branch and opened as a pull request (PR). Nothing goes live until Sagar approves it.
- After a release is merged, a snapshot branch `release/vX.Y` is saved, so any version can be restored.
- To undo one change: revert its PR. To go back to an older version: restore the matching `release/` branch.
- Automatic updates (daily YouTube videos in `videos.js`, weekly Instagram reels in `reels.js`) are not listed here one by one; they appear in the GitHub commit history as "Update latest YouTube videos" and "Update Instagram reels".

---

## v1.2.2 — 25 Nov 2026 — Remove highlights video
**Removed**
- "Watch the highlights" section (Willow by Cricbuzz video) from the Vaibhav post, because the video was not rendering on the live site.

## v1.2.1 — 25 Nov 2026 — BCCI photo on the Vaibhav post
**Added**
- BCCI's official X post (celebration photo after the 204) embedded as the main image under the headline, with a credit caption.

**Changed**
- The "52-ball 200 / 204" banner moved into the "The records he broke" section.

## v1.2 — 25 Nov 2026 — Blog redesign and podcast call to action
**Changed**
- Vaibhav Sooryavanshi post rewritten in a cleaner article layout: banner, hook, "My take" moved to second, records comparison bar, one pull quote, BCCI right vs wrong comparison, what he must avoid, short journey summary.
- Menu on blog pages made consistent with the homepage: gold "Blog" link and gold "Be our guest" button on every blog page.
- Author photo (studio picture) shown on the post instead of the logo.

**Added**
- Closing podcast call to action on the post: featured Faiz Fazal episode, Akshay Wakhare and Bhau Kadam episode cards, Subscribe on YouTube, Follow on Instagram, Share on WhatsApp, and follower proof.
- Official highlights video (Willow by Cricbuzz) of the U19 World Cup final 175, as the last section of the post.
- WhatsApp/LinkedIn share image for the post (`blog/vaibhav-sooryavanshi-204/share.jpg`).
- Gold reading progress bar at the top of the post.

## v1.1 — 25 Nov 2026 — Blog section
**Added**
- Blog home page at `/blog/` with category tabs and a featured latest post.
- 8 category pages at `/blog/category/<name>/`: Cricket & Sports, Health & Myths, Ayurveda & Spirituality, Astrology & Numerology, Nagpur & Vidarbha, Business & Startups, Tech & AI, My Take.
- First post: "28-Ball 100, 52-Ball 200 at 15: Is Vaibhav Sooryavanshi the Next Sachin or the Next Prithvi Shaw?" at `/blog/vaibhav-sooryavanshi-204/` (Cricket & Sports), ending with Faiz Fazal and Akshay Wakhare episode cards.
- "Blog" link in the homepage top menu and footer.
- "Latest takes" strip on the homepage showing the 3 newest posts.
- `blog/posts.js` (list of posts and categories) and `scripts/build_blog.py` (builds the blog home, category pages and sitemap).

**Changed**
- `sitemap.xml` now includes the blog home, every post and every category page.

## v1.0 — 25 Nov 2026 — Snapshot before the blog
Saved as branch `release/v1.0`. Contains everything built from 12–13 Nov 2026:
- Homepage with hero, stats, "My art" method, guest posters, episode cards, story timeline and awards.
- "Fresh episodes" section auto-updated daily from YouTube (GitHub Action).
- Instagram reels section with custom cover cards, auto-updated every Monday.
- Google Form for "Be our guest or suggest a guest" in the top-right button.
- Custom domain sagarkhaprepodcast.in, Google Search Console verification, search tags, robots.txt and sitemap.
