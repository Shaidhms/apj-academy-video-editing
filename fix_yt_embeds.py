"""Replace YouTube iframe embeds with clickable thumbnail cards."""
import re
import os

HTML = "/Users/shaid/Documents/Shaid_Works/Nisha/video-editing-guide/index.html"

with open(HTML, "r") as f:
    html = f.read()

# Pattern: <div class="yt-card"><div class="yt-iframe-wrap"><iframe src="https://www.youtube.com/embed/VIDEO_ID" ...></iframe></div><div class="meta"><div class="label">LABEL</div><div class="src">SRC</div></div></div>
pattern = re.compile(
    r'<div class="yt-card">\s*'
    r'<div class="yt-iframe-wrap">\s*'
    r'<iframe src="https://www\.youtube\.com/embed/([^"]+)"[^>]*></iframe>\s*'
    r'</div>\s*'
    r'<div class="meta">\s*'
    r'<div class="label">([^<]+)</div>\s*'
    r'<div class="src">([^<]+)</div>\s*'
    r'</div>\s*'
    r'</div>',
    re.DOTALL
)


def replacer(m):
    vid = m.group(1)
    label = m.group(2)
    src = m.group(3)
    # Strip any URL params from vid
    vid = vid.split('?')[0]
    watch_url = f"https://www.youtube.com/watch?v={vid}"
    thumb_url = f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"
    return (
        f'<a class="yt-card" href="{watch_url}" target="_blank" rel="noopener">'
        f'<div class="yt-thumb">'
        f'<img src="{thumb_url}" alt="{label}" loading="lazy">'
        f'<div class="yt-play"></div>'
        f'</div>'
        f'<div class="meta">'
        f'<div class="label">{label}</div>'
        f'<div class="src">{src}</div>'
        f'</div>'
        f'</a>'
    )


new_html, n = pattern.subn(replacer, html)
print(f"Replaced {n} yt-card iframe embeds with thumbnail cards.")

# Also handle the hero-video and the standalone embed iframes (the big Tamil video at top + Pro section)
# These look like: <div class="hero-video"><iframe src="https://www.youtube.com/embed/Zm4i-YT5M1k"...></iframe></div>
hero_pattern = re.compile(
    r'<div class="hero-video">\s*'
    r'<iframe src="https://www\.youtube\.com/embed/([^"]+)"[^>]*></iframe>\s*'
    r'</div>',
    re.DOTALL
)


def hero_replacer(m):
    vid = m.group(1).split('?')[0]
    watch_url = f"https://www.youtube.com/watch?v={vid}"
    thumb_url = f"https://img.youtube.com/vi/{vid}/maxresdefault.jpg"
    return (
        f'<a class="hero-video-link" href="{watch_url}" target="_blank" rel="noopener" '
        f'style="display:block; position:relative; max-width:720px; margin:32px 0 0; border-radius:16px; overflow:hidden; '
        f'border:1px solid var(--line); aspect-ratio:16/9; background:#000;">'
        f'<img src="{thumb_url}" alt="" '
        f'style="width:100%; height:100%; object-fit:cover; display:block;">'
        f'<div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); '
        f'width:88px; height:88px; border-radius:50%; background:rgba(255,0,0,0.95); '
        f'display:grid; place-items:center; box-shadow:0 12px 40px rgba(0,0,0,0.6);">'
        f'<div style="width:0; height:0; margin-left:7px; '
        f'border-left:30px solid white; border-top:18px solid transparent; border-bottom:18px solid transparent;"></div>'
        f'</div>'
        f'</a>'
    )


new_html, n2 = hero_pattern.subn(hero_replacer, new_html)
print(f"Replaced {n2} hero-video iframes with thumbnail cards.")

with open(HTML, "w") as f:
    f.write(new_html)
print(f"Saved {HTML}")
