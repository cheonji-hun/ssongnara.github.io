#!/usr/bin/env python3
"""
Tistory RSS → sitemap.xml  자동 변환 스크립트
© 2025 지훈
"""
import feedparser, datetime, xml.etree.ElementTree as ET, pathlib, sys

# --- 설정 -----------------------------
FEED_URL      = "https://ssongnara.com/rss"        # 티스토리 RSS
OUTPUT_FILE   = pathlib.Path("sitemap.xml")        # GitHub Pages 루트에 생성
CHANGEFREQ    = "weekly"
PRIORITY      = "0.8"
# --------------------------------------

def add_url(urlset, loc, lastmod):
    u  = ET.SubElement(urlset, "url")
    ET.SubElement(u, "loc").text        = loc
    ET.SubElement(u, "lastmod").text    = lastmod
    ET.SubElement(u, "changefreq").text = CHANGEFREQ
    ET.SubElement(u, "priority").text   = PRIORITY

feed = feedparser.parse(FEED_URL)
if feed.bozo:
    sys.exit(f"RSS 파싱 오류: {feed.bozo_exception}")

urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for entry in feed.entries:
    loc      = entry.link
    lastmod  = datetime.datetime(*entry.published_parsed[:3]).isoformat()
    add_url(urlset, loc, lastmod)

# ▲ 필요 시 pages.ssongnara.com 내부 URL도 추가로 append 가능

ET.ElementTree(urlset).write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)
print(f"✅  {OUTPUT_FILE} 생성 완료 — {len(feed.entries)}개 URL 포함")
