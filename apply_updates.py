"""Apply: remove Sources, add audio + beat-sync sections, make sidebar collapsible."""
import re

HTML = "/Users/shaid/Documents/Shaid_Works/Nisha/video-editing-guide/index.html"

with open(HTML, "r") as f:
    html = f.read()

# ============== 1. REMOVE SOURCES SECTION ==============
sources_pat = re.compile(
    r'\s*<!-- SOURCES -->\s*<section class="part" id="sources">.*?</section>\s*(?=<footer>)',
    re.DOTALL,
)
html, n = sources_pat.subn('\n\n', html)
print(f"sources section: removed {n}")

# Remove "Sources" reference link from sidebar
html = html.replace('<a href="#sources">Sources</a>\n', '')
# Also remove the "Reference" group label (since Sources was the only other entry; Mistakes still there)
# Actually keep the Reference group since 'mistakes' is still under it.
# Update the credit footer line referencing "Source pages credited above" since we removed sources
html = html.replace(
    'All screenshots reproduced for personal learning reference. Source pages credited above.',
    'All screenshots reproduced for personal learning reference.',
)

# ============== 2. INSERT AUDIO + BEAT SYNC SECTIONS ==============
# Place them after the cc-effects section (before cc-mask) so they sit naturally
# in the workflow: Effects -> Audio -> Beat sync -> Text masking

audio_block = """

<!-- AUDIO & VOICEOVER -->
<section class="part" id="cc-audio">
  <h2>Adding audio, music, and voiceovers</h2>
  <p>Sound is half the video. CapCut PC has one unified <strong>Audio</strong> tab that handles music, sound effects, voiceovers, and AI text-to-speech. Open it from the top toolbar.</p>

  <figure><img src="images/audio_voice_4_panel.jpg"><figcaption>The Audio tab on the top toolbar — your sound command center</figcaption></figure>

  <h3>Adding background music or a soundtrack</h3>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><h4>Open the Audio tab</h4><p>Click <strong>Audio</strong> in the top-left toolbar.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><h4>Pick a category</h4><p>Sub-tabs: <strong>Music</strong> (CapCut's library), <strong>Sound Effects</strong>, <strong>Extract</strong> (rip from any video file), <strong>Voiceover</strong>, <strong>Text to Speech</strong>.</p></div></div>
    <div class="step"><div class="num">3</div><div class="body"><h4>Hover &amp; preview</h4><p>Hover any track to hear it. Click the download icon, then click + to add to timeline. Or drag it directly onto the audio track below your video.</p></div></div>
    <div class="step"><div class="num">4</div><div class="body"><h4>Trim and position</h4><p>Drag the edges of the audio bar to trim. Drag the bar left/right to align with visuals.</p></div></div>
  </div>

  <h3>Importing your own music file</h3>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><p>Press <kbd>Ctrl</kbd>+<kbd>I</kbd> and pick the .mp3, .wav, .aac, or .flac file.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><p>Drag from the Media bin onto the audio track.</p></div></div>
  </div>

  <div class="callout warn">
    <div class="icon">©️</div>
    <div class="ct"><strong>Use copyright-safe music for social posts</strong>CapCut's built-in library is licensed for personal use, but check before commercial use. For YouTube/Reels avoid copyrighted commercial tracks — use Epidemic Sound, Artlist, or YouTube's free library.</div>
  </div>

  <h3>Recording a voiceover live in CapCut</h3>

  <figure><img src="images/audio_voice_3_overview.jpg"><figcaption>The full voiceover workflow in CapCut</figcaption></figure>

  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><h4>Position the playhead</h4><p>Move it to the moment in your video where you want narration to start.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><h4>Click Audio → Voiceover</h4><p>It's the third option in the Audio sub-tabs.</p></div></div>
    <div class="step"><div class="num">3</div><div class="body"><h4>Pick your microphone</h4><p>From the dropdown, choose your built-in mic or any USB mic you have plugged in.</p></div></div>
  </div>
  <figure><img src="images/audio_voice_5_record.jpg"><figcaption>Voiceover recording panel — mic dropdown, level meter, big record button</figcaption></figure>

  <div class="steps">
    <div class="step"><div class="num">4</div><div class="body"><h4>Hit Record</h4><p>Click the big red button. A 3-second countdown begins. Speak naturally as the video plays.</p></div></div>
    <div class="step"><div class="num">5</div><div class="body"><h4>Stop &amp; save</h4><p>Click stop. The recording lands as a new audio track at the playhead position.</p></div></div>
    <div class="step"><div class="num">6</div><div class="body"><h4>Trim and clean up</h4><p>Use <kbd>Ctrl</kbd>+<kbd>B</kbd> to split out breaths, mistakes, and long pauses → delete those segments.</p></div></div>
  </div>
  <figure><img src="images/audio_voice_8_split.jpg"><figcaption>Split the voiceover at unwanted breaths or mistakes, then delete</figcaption></figure>

  <h3>Importing a pre-recorded voiceover</h3>
  <p>If you record on your phone or in another app, just import the file via <kbd>Ctrl</kbd>+<kbd>I</kbd> and drag onto the timeline.</p>
  <figure><img src="images/audio_voice_6_import.jpg"><figcaption>Drag pre-recorded voiceover audio onto the timeline</figcaption></figure>

  <h3>AI Text-to-Speech voiceover</h3>
  <p>Don't want to use your own voice? CapCut has a built-in TTS engine with multiple voices and accents.</p>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><p>Add a <strong>Text</strong> layer on the timeline with your script.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><p>Select the text → in the right panel scroll to <strong>Text to speech</strong>.</p></div></div>
    <div class="step"><div class="num">3</div><div class="body"><p>Pick a voice (English, Hindi, kid, deep narrator, etc.).</p></div></div>
    <div class="step"><div class="num">4</div><div class="body"><p>Click <strong>Generate</strong>. CapCut creates an audio track from your text.</p></div></div>
  </div>
  <figure><img src="images/audio_voice_7_tts.jpg"><figcaption>Text-to-Speech — type once, get an AI voiceover</figcaption></figure>

  <h3>Mixing voice with background music — volume ducking</h3>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><h4>Set base levels</h4><p>Voice peaks around <strong>-6 dB</strong>. Music around <strong>-18 dB</strong>.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><h4>Manual ducking with keyframes</h4><p>On the music track, add a Volume keyframe at 0 dB just before the voice starts → another keyframe at -10 dB right after voice begins → reverse on the way out. Music dips while voice is speaking.</p></div></div>
    <div class="step"><div class="num">3</div><div class="body"><h4>Or use Auto Volume</h4><p>Right-click the music track → Auto Volume. CapCut auto-ducks the music whenever it detects speech on another track.</p></div></div>
  </div>

  <figure><img src="images/audio_voice_9_place.jpg"><figcaption>Voiceover, music, and SFX stacked on multiple audio tracks</figcaption></figure>

  <div class="callout tip">
    <div class="icon">🎙️</div>
    <div class="ct"><strong>Better voice in 30 seconds</strong>Record in a small room with soft surfaces (carpet, curtains, bed) — bathrooms and big rooms echo. Stand 6 inches from the mic. Speak slightly louder than normal conversation. After recording, in the right panel apply <strong>Voice enhance</strong> for a one-click cleanup.</div>
  </div>

  <div class="yt-grid">
    <a class="yt-card" href="https://www.youtube.com/watch?v=nFZsK6YkZDM" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/nFZsK6YkZDM/hqdefault.jpg" alt="Add Audio in CapCut PC — Music, SFX, Voiceover" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Add Audio in CapCut PC — Music, SFX &amp; Voiceover</div><div class="src">YouTube</div></div></a>
    <a class="yt-card" href="https://www.youtube.com/watch?v=bW0bbmvR-cE" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/bW0bbmvR-cE/hqdefault.jpg" alt="How to Record and Add Voiceover in CapCut PC" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Record and Add Voiceover in CapCut PC</div><div class="src">YouTube</div></div></a>
    <a class="yt-card" href="https://www.youtube.com/watch?v=nI-NLiSh_nw" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/nI-NLiSh_nw/hqdefault.jpg" alt="Voiceover in CapCut PC — Lesson 34" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Voiceover in CapCut PC — Lesson 34</div><div class="src">YouTube</div></div></a>
  </div>
</section>


<!-- BEAT SYNC -->
<section class="part" id="cc-beat">
  <h2>Beat sync — match images and clips to music</h2>
  <p>Beat-sync is the single biggest reason short-form videos feel "professional." When your cuts hit on the beat, the brain reads it as polished. CapCut PC has automatic beat detection (yellow markers on the timeline) that does the hard work for you.</p>

  <div class="banner-row">
    <span class="pill ok">Auto-detection works</span>
    <span class="pill info">PC + Mobile</span>
    <span class="pill warn">Needs music track first</span>
  </div>

  <h3>Step 1 — Drop your music on the timeline first</h3>
  <p>Beat detection only works on a track that exists. Bring in your song before adding clips.</p>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><p>Audio tab → pick a track, or <kbd>Ctrl</kbd>+<kbd>I</kbd> to import your own.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><p>Drag onto the audio row below your video timeline.</p></div></div>
  </div>

  <h3>Step 2 — Run automatic beat detection</h3>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><h4>Select the audio track</h4><p>Click on your music track on the timeline.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><h4>Click Auto-Beat (or right-click → Beat Detection)</h4><p>On the toolbar above the timeline you'll see <strong>Auto-Beat</strong>. Or right-click the audio → <strong>Beat Detection</strong>.</p></div></div>
    <div class="step"><div class="num">3</div><div class="body"><h4>Pick Beat 1 or Beat 2</h4><p><strong>Beat 1</strong> = main beats only (sparse, dramatic cuts). <strong>Beat 2</strong> = every beat including off-beats (faster, busier). Pick based on the energy you want.</p></div></div>
    <div class="step"><div class="num">4</div><div class="body"><h4>Yellow dots appear</h4><p>CapCut scans the audio and drops a yellow marker at every detected beat. Zoom into the timeline to see them clearly.</p></div></div>
  </div>

  <div class="callout note">
    <div class="icon">⌨️</div>
    <div class="ct"><strong>Manual beat marking — press M</strong>If auto-detection misses subtle beats, you can tap them yourself. Play the song and press <kbd>M</kbd> on every beat you hear. Each press drops a manual marker. Mix this with auto-detection for hybrid control.</div>
  </div>

  <h3>Step 3 — Snap photos / clips to the beats</h3>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><h4>Drop your photos or clips</h4><p>Drag your images / clips onto the video track above the music. Each one becomes a separate segment.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><h4>Trim each clip to the beat</h4><p>Drag the right edge of each photo/clip until its end snaps to the next yellow beat marker. CapCut snaps automatically when you get close.</p></div></div>
    <div class="step"><div class="num">3</div><div class="body"><h4>Set default photo duration to match</h4><p>If you have many photos, click File → Settings → Editing → Default photo duration → set to a value that matches your average beat interval (e.g. 0.5 sec for fast music).</p></div></div>
    <div class="step"><div class="num">4</div><div class="body"><h4>Add transitions on the beat</h4><p>Drop a transition (Whip, Zoom, Glitch) between two clips. Position it directly on a beat marker. The transition itself becomes the beat hit.</p></div></div>
  </div>

  <h3>Step 4 — Add visual punch on the drops</h3>
  <p>For the big drops, layer effects keyframed to the beat:</p>
  <ul>
    <li><strong>Scale punch</strong> — keyframe Scale 100% just before the beat, 110% on the beat, back to 100% right after. Adds a heartbeat pulse.</li>
    <li><strong>Shake</strong> — apply the Shake video effect for a few frames around the drop.</li>
    <li><strong>Flash</strong> — drop a white solid for 1-2 frames on the heaviest beat.</li>
    <li><strong>Speed ramp</strong> — slow down before the drop, snap to normal speed on the drop.</li>
  </ul>

  <h3>Photo slideshow workflow (montage style)</h3>
  <div class="steps">
    <div class="step"><div class="num">1</div><div class="body"><p>Music first → run beat detection.</p></div></div>
    <div class="step"><div class="num">2</div><div class="body"><p>Select all your photos in the Media bin → drag them all to the timeline at once.</p></div></div>
    <div class="step"><div class="num">3</div><div class="body"><p>Trim each to the beat (or set a uniform duration that matches the BPM).</p></div></div>
    <div class="step"><div class="num">4</div><div class="body"><p>Apply Ken Burns — for each photo, add a Scale keyframe (100% start, 110% end). Adds movement to static images.</p></div></div>
    <div class="step"><div class="num">5</div><div class="body"><p>Add transitions on every cut. Same transition (right-click → Apply to all) keeps it consistent.</p></div></div>
    <div class="step"><div class="num">6</div><div class="body"><p>Color-grade so all photos feel like they belong to the same set.</p></div></div>
  </div>

  <div class="callout tip">
    <div class="icon">🎯</div>
    <div class="ct"><strong>Pick songs with clear beats</strong>Mumbling lo-fi or ambient pads will not auto-detect well. Use songs with prominent kicks and snares — EDM, hip-hop, dance, drum-led pop. The clearer the beat, the better the auto-detection.</div>
  </div>

  <div class="yt-grid">
    <a class="yt-card" href="https://www.youtube.com/watch?v=GJJXYa2ktaI" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/GJJXYa2ktaI/hqdefault.jpg" alt="Auto Beat Feature in CapCut PC — Lesson 26" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Auto Beat Feature in CapCut PC — Lesson 26</div><div class="src">YouTube</div></div></a>
    <a class="yt-card" href="https://www.youtube.com/watch?v=eHYWEwuIW2Y" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/eHYWEwuIW2Y/hqdefault.jpg" alt="How to Auto Sync Beats in CapCut" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">How to Auto Sync Beats in CapCut</div><div class="src">YouTube</div></div></a>
    <a class="yt-card" href="https://www.youtube.com/watch?v=4X64-bWRZ2Y" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/4X64-bWRZ2Y/hqdefault.jpg" alt="Cut to Music Beat using Mark Beats AI — Lesson 98" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Cut to Music Beat with Mark Beats AI — Lesson 98</div><div class="src">YouTube</div></div></a>
    <a class="yt-card" href="https://www.youtube.com/watch?v=wn_MDrlFJL0" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/wn_MDrlFJL0/hqdefault.jpg" alt="Sync Photos to Music Beat" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Sync Photos to Music Beat — Tutorial</div><div class="src">YouTube</div></div></a>
    <a class="yt-card" href="https://www.youtube.com/watch?v=aLPAKKqYZY4" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/aLPAKKqYZY4/hqdefault.jpg" alt="Sync Photos and Videos with Beats — CapCut PC" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Sync Photos &amp; Videos with Beats — CapCut PC</div><div class="src">YouTube</div></div></a>
    <a class="yt-card" href="https://www.youtube.com/watch?v=ar6YrudFdxY" target="_blank" rel="noopener"><div class="yt-thumb"><img src="https://img.youtube.com/vi/ar6YrudFdxY/hqdefault.jpg" alt="Image Slideshows That Match Music Beats" loading="lazy"><div class="yt-play"></div></div><div class="meta"><div class="label">Image Slideshows That Match Music Beats</div><div class="src">YouTube</div></div></a>
  </div>
</section>

"""

# Insert just before <!-- TEXT MASKING --> section
mask_marker = "<!-- TEXT MASKING -->"
html = html.replace(mask_marker, audio_block + mask_marker)

# Add sidebar links for the new sections (after PIP overlay link, before Text masking)
sidebar_pip_link = '<a href="#cc-effects">Effects &amp; PIP overlay</a>'
sidebar_new = (
    sidebar_pip_link
    + '\n    <a href="#cc-audio">Audio &amp; voiceover</a>'
    + '\n    <a href="#cc-beat">Beat sync editing</a>'
)
html = html.replace(sidebar_pip_link, sidebar_new)

# ============== 3. SIDEBAR COLLAPSIBLE ==============
# Replace the existing sidebar opening + add toggle button
# Update CSS: add transition, allow collapsed state
new_css_block = """
/* ===== SIDEBAR TOGGLE ===== */
.sidebar-toggle {
  position: fixed; top: 16px; left: 16px; z-index: 100;
  width: 42px; height: 42px; border-radius: 10px;
  background: var(--bg-card); border: 1px solid var(--line);
  display: grid; place-items: center; cursor: pointer;
  transition: all 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
.sidebar-toggle:hover { background: var(--bg-elev); border-color: var(--accent); }
.sidebar-toggle .bar { width: 18px; height: 2px; background: var(--text); margin: 2px 0; transition: all 0.2s; border-radius: 2px; }
body.sidebar-open .sidebar-toggle .bar:nth-child(1) { transform: translateY(6px) rotate(45deg); }
body.sidebar-open .sidebar-toggle .bar:nth-child(2) { opacity: 0; }
body.sidebar-open .sidebar-toggle .bar:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }
body:not(.sidebar-open) .sidebar { transform: translateX(-100%); }
.sidebar { transition: transform 0.3s ease; z-index: 50; }
.wrap { display: block !important; max-width: 1100px; }
main { padding: 0; max-width: 100%; transition: margin-left 0.3s; }
body.sidebar-open .sidebar { transform: translateX(0); }
body.sidebar-open .sidebar { position: fixed; top: 0; left: 0; width: 280px; }
@media (min-width: 921px) { body.sidebar-open main { margin-left: 280px; } }
@media (max-width: 920px) { body.sidebar-open main { margin-left: 0; } body.sidebar-open .sidebar { box-shadow: 8px 0 30px rgba(0,0,0,0.5); } }

/* ===== END SIDEBAR TOGGLE ===== */
"""
# Inject the new CSS before the </style> tag
html = html.replace("</style>", new_css_block + "</style>")

# Inject the toggle button right after <body>
toggle_btn = """
<button class="sidebar-toggle" id="sidebarToggle" aria-label="Toggle sidebar">
  <div class="bar"></div>
  <div class="bar"></div>
  <div class="bar"></div>
</button>
"""
html = html.replace("<body>", "<body>\n" + toggle_btn, 1)

# Inject toggle JS before </body>
toggle_js = """
<script>
const tog = document.getElementById('sidebarToggle');
const body = document.body;
tog.addEventListener('click', () => body.classList.toggle('sidebar-open'));
// Close sidebar on link click (mobile-style behavior)
document.querySelectorAll('.sidebar nav a').forEach(a => {
  a.addEventListener('click', () => { if (window.innerWidth < 921) body.classList.remove('sidebar-open'); });
});
</script>
"""
html = html.replace("</body>", toggle_js + "\n</body>")

with open(HTML, "w") as f:
    f.write(html)
print("Updates applied:")
print(" - Sources section removed")
print(" - Audio + voiceover section added")
print(" - Beat sync section added")
print(" - Sidebar toggle button + collapsible behavior added")
