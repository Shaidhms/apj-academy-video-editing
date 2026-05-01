"""Remove all LumaFusion references from index.html."""
import re

HTML = "/Users/shaid/Documents/Shaid_Works/Nisha/video-editing-guide/index.html"

with open(HTML, "r") as f:
    html = f.read()

# 1) Remove sidebar group for LumaFusion
sidebar_pat = re.compile(
    r'\s*<div class="group-label">LumaFusion</div>\s*'
    r'(?:<a href="#luma-[^"]+">[^<]+</a>\s*)+',
    re.DOTALL,
)
html, n = sidebar_pat.subn("", html)
print(f"sidebar: removed {n} block(s)")

# 2) Update lead text
html = html.replace(
    "VPN setup, CapCut, Clipchamp, and LumaFusion — explained step by step with screenshots, embedded YouTube tutorials, and the secret CapCut Pro export trick (the one from your Tamil reference video).",
    "VPN setup, CapCut, and Clipchamp — explained step by step with screenshots, YouTube tutorials, and the secret CapCut Pro export trick.",
)

# 3) Update hero stat — Tools covered: 4 → 3
html = html.replace(
    '<div class="hero-stat"><div class="num">4</div><div class="label">Tools covered</div></div>',
    '<div class="hero-stat"><div class="num">3</div><div class="label">Tools covered</div></div>',
)

# 4) Update Clipchamp "When NOT to use it" lines
html = html.replace(
    "<li>Complex motion graphics with keyframes — use CapCut or LumaFusion.</li>",
    "<li>Complex motion graphics with keyframes — use CapCut.</li>",
)
html = html.replace(
    "<li>Mobile-first editing on phone — use CapCut Mobile or LumaFusion.</li>",
    "<li>Mobile-first editing on phone — use CapCut Mobile.</li>",
)

# 5) Update HSL callout in Clipchamp section
html = html.replace(
    "<strong>No HSL, no color wheels, no masks</strong>For cinematic color grading you need CapCut or LumaFusion. Use Clipchamp's built-in filters as a quick base look, then fine-tune the sliders.",
    "<strong>No HSL, no color wheels, no masks</strong>For cinematic color grading you need CapCut. Use Clipchamp's built-in filters as a quick base look, then fine-tune the sliders.",
)

# 6) Remove the entire LumaFusion Part 4 block (8 sections)
# Start from <!-- ============================== LUMAFUSION ============================== -->
# End at the next big section comment <!-- ============================== COMPARISON ============================== -->
luma_block_pat = re.compile(
    r"<!-- =+ LUMAFUSION =+ -->.*?(?=<!-- =+ COMPARISON =+ -->)",
    re.DOTALL,
)
html, n = luma_block_pat.subn("", html)
print(f"part4: removed {n} block(s)")

# 7) Remove LumaFusion column from comparison table
# Header
html = html.replace(
    '<thead><tr><th>Feature</th><th>CapCut</th><th>Clipchamp</th><th>LumaFusion</th></tr></thead>',
    '<thead><tr><th>Feature</th><th>CapCut</th><th>Clipchamp</th></tr></thead>',
)

# Each <tr> currently has 4 td's. Trim the last td in every <tr> inside cmp table.
# Find the cmp tbody block and trim each row.
def trim_table(m):
    body = m.group(0)
    # In each <tr> ... </tr>, drop the last <td>...</td>
    rows = re.split(r'(</tr>)', body)
    # For each tr block (the part before </tr>), keep only first 3 td cells
    result = []
    for chunk in rows:
        if '<td>' in chunk:
            # find all <td>...</td>
            cells = re.findall(r'<td>.*?</td>', chunk, re.DOTALL)
            if len(cells) >= 4:
                # rebuild keeping first 3
                # original chunk has stuff before first <td> too; preserve it
                pre = chunk.split('<td>', 1)[0]
                chunk = pre + ''.join(cells[:3])
        result.append(chunk)
    return ''.join(result)


tbody_pat = re.compile(r'<tbody>.*?</tbody>', re.DOTALL)
html, n = tbody_pat.subn(trim_table, html)
print(f"tbody trimmed: {n}")

# 8) Remove "Move to LumaFusion if..." line in recommendations
html = re.sub(
    r"\s*<li>Move to <strong>LumaFusion</strong>[^<]*</li>",
    "",
    html,
)

# 9) Remove entire LumaFusion sources block (h3 + link-list)
sources_pat = re.compile(
    r'\s*<h3>LumaFusion</h3>\s*<div class="link-list">\s*'
    r'(?:<a class="link-card"[^>]*>.*?</a>\s*)+'
    r'</div>',
    re.DOTALL,
)
html, n = sources_pat.subn("", html)
print(f"sources: removed {n} block(s)")

# 10) Strip stat in hero count 25+ if needed - keep 25+ as is; just confirm no luma left
remaining = html.lower().count('lumafusion') + html.lower().count('luma-touch') + html.lower().count('luma_') + html.lower().count('luma ')
print(f"remaining luma mentions: {remaining}")

with open(HTML, "w") as f:
    f.write(html)
print(f"Saved {HTML}")
