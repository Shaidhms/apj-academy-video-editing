#!/bin/bash
# Download all screenshots used in the guide
set -u
cd "$(dirname "$0")/images"

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"

dl() {
  local fname="$1"
  local url="$2"
  if [ -s "$fname" ]; then
    echo "skip (have) $fname"
    return
  fi
  curl -sSL -A "$UA" -e "https://www.google.com/" -o "$fname" "$url" || echo "FAIL $fname"
  if [ ! -s "$fname" ]; then
    echo "EMPTY $fname"
    rm -f "$fname"
  fi
}

# ===== CapCut + VPN install (Kripesh Adwani) =====
dl "vpn_01_proton_site.png"     "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/1-Proton-VPN-official-site-1.png"
dl "vpn_02_free.png"            "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/2-Click-on-Proton-VPN-Free.png"
dl "vpn_03_account.png"         "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/3-Create-a-new-account.png"
dl "vpn_04_password.png"        "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/4-Generate-password.png"
dl "vpn_05_download.png"        "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/5-Download-Proton-VPN.png"
dl "vpn_06_install.png"         "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/6-Download-Proton-VPN.png"

dl "capcut_01_site.png"         "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/1-Visit-Capcut-website.png"
dl "capcut_02_download.png"     "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/2-Download-Capcut-app.png"
dl "capcut_03_signup.png"       "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/3-Sign-up-for-a-new-account.png"
dl "capcut_04_create_project.png" "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/4-Create-project-1.png"
dl "capcut_05_import.png"       "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/5-Import-clips.png"
dl "capcut_06_arrange.png"      "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/6-Arrange-clips.png"
dl "capcut_07_effects.png"      "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/7-Edit-video-with-effects-filters.png"
dl "capcut_08_audio.png"        "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/8-Add-audio.png"
dl "capcut_10_export.png"       "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/10-Export-video-for-PC.png"

# Mobile / Android CapCut
dl "capcut_m_01_apk.png"        "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/1-Explore-Capcut-APK-file.png"
dl "capcut_m_02_apk_dl.png"     "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/2-Download-the-Capcut-APK-file.png"
dl "capcut_m_03_signup.png"     "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/3-Sign-up-to-Capcut.png"
dl "capcut_m_04_project.png"    "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/4-Create-project.png"
dl "capcut_m_05_import.png"     "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/5-Import-video-files.png"
dl "capcut_m_07_edit.png"       "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/7-Edit-video.png"
dl "capcut_m_10_export.png"     "https://cdn.kripeshadwani.com/wp-content/uploads/2024/12/10-Export-video-for-mobile.png"

# ===== CapCut color grading & HSL (createthat.ai) =====
dl "capcut_color_01_adjust.png"     "https://createthat.ai/finding-the-adjustment-panel-for-color-grading-in-capcut.png"
dl "capcut_color_02_panels.png"     "https://createthat.ai/the-5-main-color-grading-panels-in-capcut.png"
dl "capcut_color_03_hsl.png"        "https://createthat.ai/hsl-panel-in-capcut.png"
dl "capcut_color_04_curves.png"     "https://createthat.ai/curves-panel-in-capcut.png"
dl "capcut_color_05_wheel.png"      "https://createthat.ai/capcut-color-wheel-panel.png"
dl "capcut_color_06_mask.png"       "https://createthat.ai/capcut-mask-panel.png"

# ===== Clipchamp interface (media.clipchamp.com) =====
dl "clip_01_overview.png"   "https://media.clipchamp.com/clipchamp/2048/5GILE3XwylaZljae3zOEle"
dl "clip_02_uidiagram.png"  "https://media.clipchamp.com/clipchamp/2048/4Epqn9KYYT9MR1vlZPGALA"
dl "clip_03_lefttool.png"   "https://media.clipchamp.com/clipchamp/2048/5YEAIfakHwzL0InTlV0iJS"
dl "clip_04_rightpanel.png" "https://media.clipchamp.com/clipchamp/2048/6J2yF41I32A9G73Y4ss6SU"
dl "clip_05_floating.png"   "https://media.clipchamp.com/clipchamp/2048/4xNbDuaO1h6dzvC4GyMaB"
dl "clip_06_floating2.png"  "https://media.clipchamp.com/clipchamp/2048/3XgmumjUE7o4zvr8ncIfYN"
dl "clip_07_timeline.png"   "https://media.clipchamp.com/clipchamp/2048/2piRAWJwAPBxs6WPZ2pUdy"

# Clipchamp transitions specifically
dl "clip_t_01_heart.png"        "https://media.clipchamp.com/clipchamp/2048/5yci5wbdsipYd05yWkqClX"
dl "clip_t_02_import.png"       "https://media.clipchamp.com/clipchamp/2048/1IEkSEkmvmgyYibBKpFjXA"
dl "clip_t_03_library.png"      "https://media.clipchamp.com/clipchamp/2048/5YvwlirWshf7sO6nQsmuiM"
dl "clip_t_04_drag.png"         "https://media.clipchamp.com/clipchamp/2048/3b5U0p4qkQnhkk8CozXAJD"
dl "clip_t_05_apply.png"        "https://media.clipchamp.com/clipchamp/2048/3l5G5ZCDL7tIy7MlEU8mgv"
dl "clip_t_06_duration.png"     "https://media.clipchamp.com/clipchamp/2048/7HlUjSNSfZvgkAB277g26v"
dl "clip_t_07_export.png"       "https://media.clipchamp.com/clipchamp/2048/6RqsjQ4CeYSLSSEw7hlwJg"

# ===== LumaFusion =====
dl "luma_01_main.png"      "https://www.podfeet.com/blog/wp-content/uploads/2021/01/Screenshot-of-main-screen.png"
dl "luma_02_title.png"     "https://www.podfeet.com/blog/wp-content/uploads/2021/01/Screenshot-of-title-sequence.png"
dl "luma_03_keyframe.png"  "https://www.podfeet.com/blog/wp-content/uploads/2021/01/Screenshot-of-keyframe-example.png"

dl "luma_cb_01.jpg"        "https://cdn.mos.cms.futurecdn.net/4HAeh7QYqLAMaPh5NY6axE.jpg"
dl "luma_cb_02.jpg"        "https://cdn.mos.cms.futurecdn.net/Kq8ckrtQTDauaaCSBHeFc4.jpeg"
dl "luma_cb_03.png"        "https://cdn.mos.cms.futurecdn.net/BMVnXErB33YXc2AqngW8i9.png"

# ===== Proton VPN Android =====
dl "proton_a_01_signup.png"  "https://vpncdn.protonweb.com/image-transformation/?s=a&image=Zr_Cndka_F0_Tc_G_Irj_J_signup_to_a_paid_plan_step_1_6590e801d2.png&width=974&height=408"
dl "proton_a_02_dlogin.png"  "https://vpncdn.protonweb.com/image-transformation/?s=a&image=Zyl_I0a8j_Q_Ar_T0_Lfd_how_to_step_2_download_6e13fb69f1.png&width=974&height=404"
dl "proton_a_03_connect.png" "https://vpncdn.protonweb.com/image-transformation/?s=a&image=Zmf4hpm069_VX_1nt4_step_3_connect_to_a_server_android_85dda1b41a.png&width=974&height=404"
dl "proton_a_04_hero.png"    "https://vpncdn.protonweb.com/image-transformation/?s=a&image=proton_vpn_trusted_and_free_vpn_for_android_37efb32b2c.png&width=1566&height=1090"

echo "===== DONE ====="
ls -la
