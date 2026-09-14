"""Verify rendered pages have working local links and no remote script/image dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[1]
site = root / "_site"

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.remote_assets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in ("script", "img") and attrs.get("src", "").startswith(("http:", "https:")):
            self.remote_assets.append(attrs["src"])

pages = [site / "index.html"] + list((site / "worksheets").glob("*.html"))
assert len(pages) == 1 + len(list((root / "worksheets").glob("*.qmd")))
broken = []
for path in pages:
    parser = Links()
    parser.feed(path.read_text(encoding="utf-8"))
    assert not parser.remote_assets, (path, parser.remote_assets)
    for href in parser.links:
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            continue
        target = site / unquote(url.path).lstrip("/") if url.path.startswith("/") else path.parent / unquote(url.path)
        if not target.exists():
            broken.append((path.name, href))
assert not broken, broken
assert '<math display="inline"' in (site / "index.html").read_text(encoding="utf-8")
print(f"PASS {len(pages)} rendered pages: local links, embedded assets and MathML")
