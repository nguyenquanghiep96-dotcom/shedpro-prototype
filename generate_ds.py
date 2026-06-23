import json

svg_paths = {
    "p197c5200": "M57.9425 28.7474H64.0751C68.6364 28.7474 71.9318 25.882 71.9318 21.2116C71.9318 16.5412 68.6364 13.6983 64.0533 13.6983H57.9425V28.7474ZM61.6963 25.3631V17.0827H64.0751C66.7377 17.0827 68.0908 18.8877 68.0908 21.2116C68.0908 23.4453 66.6067 25.3631 64.0533 25.3631H61.6963Z",
    "p19d42400": "M76.3636 28.7478H80.1113V23.6561H83.641C86.9093 23.6561 88.696 21.4257 88.696 18.7221C88.696 15.996 86.9093 13.7205 83.641 13.7205H76.3636V28.7478ZM84.883 18.6996C84.883 19.7134 84.1422 20.3668 83.1399 20.3668H80.1113V16.9873H83.1399C84.1422 16.9873 84.883 17.6632 84.883 18.6996Z",
    "p25230c00": "M44.8728 28.7474H55.5448V25.4759H48.6265V22.7684H55.392V19.4743H48.6265V16.9699H55.5448V13.6983H44.8728V28.7474Z",
    "p259d0100": "M12.5 5.83333H7.5V0.833333C7.5 0.373099 7.1269 0 6.66667 0C6.20643 0 5.83333 0.373099 5.83333 0.833333V5.83333H0.833333C0.373099 5.83333 0 6.20643 0 6.66667C0 7.1269 0.373099 7.5 0.833333 7.5H5.83333V12.5C5.83333 12.9602 6.20643 13.3333 6.66667 13.3333C7.1269 13.3333 7.5 12.9602 7.5 12.5V7.5H12.5C12.9602 7.5 13.3333 7.1269 13.3333 6.66667C13.3333 6.20643 12.9602 5.83333 12.5 5.83333Z",
    "p29f37d80": "M2.40396 6.50646V2.40396H6.50646V6.50646H2.40396ZM2.40396 11.7627V7.66021H6.50646V11.7627H2.40396ZM7.66021 6.50646V2.40396H11.7627V6.50646H7.66021ZM7.66021 11.7627V7.66021H11.7627V11.7627H7.66021ZM3.65375 5.25646H5.25646V3.65375H3.65375V5.25646ZM8.91021 5.25646H10.5129V3.65375H8.91021V5.25646ZM3.65375 10.5129H5.25646V8.91021H3.65375V10.5129ZM8.91021 10.5129H10.5129V8.91021H8.91021V10.5129ZM1.50646 14.1667C1.08549 14.1667 0.729167 14.0208 0.4375 13.7292C0.145833 13.4375 0 13.0812 0 12.6602V1.50646C0 1.08549 0.145833 0.729167 0.4375 0.4375C0.729167 0.145833 1.08549 0 1.50646 0H12.6602C13.0812 0 13.4375 0.145833 13.7292 0.4375C14.0208 0.729167 14.1667 1.08549 14.1667 1.50646V12.6602C14.1667 13.0812 14.0208 13.4375 13.7292 13.7292C13.4375 14.0208 13.0812 14.1667 12.6602 14.1667H1.50646ZM1.50646 12.9167H12.6602C12.7244 12.9167 12.7831 12.8899 12.8365 12.8365C12.8899 12.7831 12.9167 12.7244 12.9167 12.6602V1.50646C12.9167 1.44229 12.8899 1.38354 12.8365 1.33021C12.7831 1.27674 12.7244 1.25 12.6602 1.25H1.50646C1.44229 1.25 1.38354 1.27674 1.33021 1.33021C1.27674 1.38354 1.25 1.44229 1.25 1.50646V12.6602C1.25 12.7244 1.27674 12.7831 1.33021 12.8365C1.38354 12.8899 1.44229 12.9167 1.50646 12.9167Z",
    "p3ae3bc80": "M1.40893 13.8261L0.973092 13.6467C0.537259 13.4608 0.245037 13.1455 0.0964257 12.7011C-0.0520465 12.2567 -0.0290603 11.8219 0.165384 11.3967L1.40893 8.70756V13.8261ZM5.06288 15.403C4.60455 15.403 4.21219 15.2398 3.8858 14.9134C3.55941 14.587 3.39622 14.1946 3.39622 13.7363V9.58568L5.29997 14.8613C5.34163 14.9639 5.3833 15.059 5.42497 15.1465C5.46663 15.2342 5.52219 15.3196 5.59163 15.403H5.06288ZM8.82559 14.9832C8.49337 15.1123 8.16969 15.0955 7.85455 14.9326C7.53941 14.7696 7.31719 14.5194 7.18788 14.1819L3.47955 4.01526C3.35025 3.6829 3.36143 3.357 3.51309 3.03756C3.6649 2.71825 3.90691 2.49818 4.23913 2.37735L10.5308 0.0856812C10.863 -0.0434854 11.1841 -0.0266106 11.4939 0.136306C11.8038 0.299223 12.0233 0.54943 12.1525 0.88693L15.8608 11.0376C15.9901 11.3752 15.983 11.7051 15.8393 12.0271C15.6956 12.3492 15.4549 12.5707 15.1173 12.6915L8.82559 14.9832ZM7.77205 5.21151C7.93177 5.05179 8.01163 4.85388 8.01163 4.61776C8.01163 4.38165 7.93177 4.18374 7.77205 4.02401C7.61233 3.86429 7.41441 3.78443 7.1783 3.78443C6.94219 3.78443 6.74427 3.86429 6.58455 4.02401C6.42483 4.18374 6.34497 4.38165 6.34497 4.61776C6.34497 4.85388 6.42483 5.05179 6.58455 5.21151C6.74427 5.37124 6.94219 5.4511 7.1783 5.4511C7.41441 5.4511 7.61233 5.37124 7.77205 5.21151ZM8.38663 13.7844L14.6783 11.4928L10.97 1.28443L4.6783 3.5761L8.38663 13.7844Z",
    "p3b2a0980": "M38.2773 28.7474H42.031V13.6983H38.2773V19.3164H32.232V13.6983H28.4782V28.7474H32.232V22.7007H38.2773V28.7474Z",
    "p3d36480": "M98.6878 28.7478H102.98L100.017 23.2281C101.368 22.7324 102.915 21.3356 102.915 18.7221C102.915 15.9284 101.085 13.7205 97.8598 13.7205H90.5824V28.7478H94.3301V23.6561H96.2475L98.6878 28.7478ZM99.1018 18.6771C99.1018 19.7134 98.2738 20.3668 97.2933 20.3668H94.3301V16.9873H97.2933C98.2738 16.9873 99.1018 17.6407 99.1018 18.6771Z",
    "p7084140": "M13.9773 26.6266C15.4395 28.0706 17.491 29.0182 20.4372 29.0182C24.3437 29.0182 26.5043 27.0101 26.5043 23.9868C26.5043 20.5799 23.1871 19.8579 20.7864 19.3389C19.1714 19.0231 18.2766 18.7523 18.2766 17.9626C18.2766 17.3083 18.7568 16.7894 20.0007 16.7894C21.2884 16.7894 22.8815 17.3083 24.1037 18.3462L26.1552 15.571C24.6056 14.1947 22.576 13.4727 20.2408 13.4727C16.5089 13.4727 14.4356 15.6613 14.4356 18.1882C14.4356 21.7531 17.7965 22.3848 20.1972 22.8812C21.7467 23.2197 22.6851 23.5581 22.6851 24.4155C22.6851 25.1374 21.8994 25.7015 20.6118 25.7015C18.6258 25.7015 17.0108 24.799 15.9633 23.716L13.9773 26.6266Z",
    "p88ca800": "M104.465 21.2454C104.465 25.819 107.798 29.0182 112.243 29.0182C116.688 29.0182 120 25.819 120 21.2454C120 16.6719 116.688 13.4727 112.243 13.4727C107.798 13.4727 104.465 16.6719 104.465 21.2454ZM116.187 21.2454C116.187 23.6786 114.64 25.5937 112.243 25.5937C109.825 25.5937 108.278 23.6786 108.278 21.2454C108.278 18.7897 109.825 16.8972 112.243 16.8972C114.64 16.8972 116.187 18.7897 116.187 21.2454Z",
    "pf15ab80": "M17.9091 0L30.3409 6.04945L29.3106 8.20857L17.9091 2.66047L6.82667 8.05326L2.3734 15.5301V35.6033H30.1421V38H0V14.8649L5.15803 6.20477L17.9091 0Z"
}

icon_set = [
    {"name": "Home", "path": "M3 12L12 3l9 9M5 10v9h5v-5h4v5h5v-9"},
    {"name": "User", "path": "M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2M12 11a4 4 0 100-8 4 4 0 000 8z"},
    {"name": "Settings", "path": "M12 15a3 3 0 100-6 3 3 0 000 6zM19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z"},
    {"name": "Bell", "path": "M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0"},
    {"name": "Search", "path": "M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"},
    {"name": "Filter", "path": "M22 3H2l8 9.46V19l4 2v-8.54L22 3z"},
    {"name": "Edit", "path": "M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"},
    {"name": "Trash", "path": "M3 6h18M19 6l-1 14a2 2 0 01-2 2H8a2 2 0 01-2-2L5 6M10 11v6M14 11v6M9 6V4a1 1 0 011-1h4a1 1 0 011 1v2"},
    {"name": "Plus", "path": "M12 5v14M5 12h14"},
    {"name": "Minus", "path": "M5 12h14"},
    {"name": "Check", "path": "M20 6L9 17l-5-5"},
    {"name": "X", "path": "M18 6L6 18M6 6l12 12"},
    {"name": "Arrow Right", "path": "M5 12h14M12 5l7 7-7 7"},
    {"name": "Arrow Left", "path": "M19 12H5M12 19l-7-7 7-7"},
    {"name": "Download", "path": "M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"},
    {"name": "Upload", "path": "M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"},
    {"name": "Mail", "path": "M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2zM22 6l-10 7L2 6"},
    {"name": "Lock", "path": "M19 11H5a2 2 0 00-2 2v7a2 2 0 002 2h14a2 2 0 002-2v-7a2 2 0 00-2-2zM7 11V7a5 5 0 0110 0v4"},
    {"name": "Info", "path": "M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10zM12 8v4M12 16h.01"},
    {"name": "Alert", "path": "M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0zM12 9v4M12 17h.01"},
    {"name": "Calendar", "path": "M3 4h18v18H3zM16 2v4M8 2v4M3 10h18"},
    {"name": "Clock", "path": "M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10zM12 6v6l4 2"},
    {"name": "Link", "path": "M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"},
    {"name": "Copy", "path": "M20 9H11a2 2 0 00-2 2v9a2 2 0 002 2h9a2 2 0 002-2v-9a2 2 0 00-2-2zM5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"}
]

colors = [
    {"title": "Primary", "items": [
      {"name": "Primary 500", "hex": "#ff7048", "cssClass": ".bg-primary-500"},
      {"name": "Primary 400", "hex": "#ff8765", "cssClass": ".bg-primary-400"},
      {"name": "Primary 300", "hex": "#ffa58a", "cssClass": ".bg-primary-300"},
      {"name": "Primary 200", "hex": "#ffc3ae", "cssClass": ".bg-primary-200"},
      {"name": "Primary 100", "hex": "#ffe1d7", "cssClass": ".bg-primary-100"}
    ]},
    {"title": "Secondary", "items": [
      {"name": "Secondary 500", "hex": "#2b3b63", "cssClass": ".bg-secondary-500"},
      {"name": "Secondary 400", "hex": "#556282", "cssClass": ".bg-secondary-400"},
      {"name": "Secondary 300", "hex": "#7f8aa1", "cssClass": ".bg-secondary-300"},
      {"name": "Secondary 200", "hex": "#aab1c1", "cssClass": ".bg-secondary-200"},
      {"name": "Secondary 100", "hex": "#d4d8e0", "cssClass": ".bg-secondary-100"}
    ]},
    {"title": "Neutral", "items": [
      {"name": "Neutral 900", "hex": "#2e323d", "cssClass": ".bg-neutral-900"},
      {"name": "Neutral 800", "hex": "#5e6578", "cssClass": ".bg-neutral-800"},
      {"name": "Neutral 700", "hex": "#8e97b3", "cssClass": ".bg-neutral-700"},
      {"name": "Neutral 600", "hex": "#bec9ee", "cssClass": ".bg-neutral-600"},
      {"name": "Neutral 100", "hex": "#f5f5f5", "cssClass": ".bg-neutral-100"}
    ]},
    {"title": "Semantic / Status", "items": [
      {"name": "Danger", "hex": "#f12428", "cssClass": ".bg-danger-900"},
      {"name": "Warning", "hex": "#f09a11", "cssClass": ".bg-warning-900"},
      {"name": "Success", "hex": "#22c55e", "cssClass": ".bg-success-500"},
      {"name": "Info", "hex": "#3b82f6", "cssClass": ".bg-info-500"}
    ]}
]

typography = [
    {"name": "Display", "size": "48px / 3rem", "weight": "Bold", "sample": "The quick brown fox", "cssClass": "fs-display fw-bold"},
    {"name": "H1", "size": "32px / 2rem", "weight": "Bold", "sample": "Heading One", "cssClass": "fs-h1 fw-bold"},
    {"name": "H2", "size": "24px / 1.5rem", "weight": "Bold", "sample": "Heading Two", "cssClass": "fs-h2 fw-bold"},
    {"name": "H3", "size": "20px / 1.25rem", "weight": "Bold", "sample": "Heading Three", "cssClass": "fs-h3 fw-bold"},
    {"name": "Body Large", "size": "16px / 1rem", "weight": "Regular", "sample": "Body large text used for paragraphs and main content areas.", "cssClass": "fs-body-lg fw-reg"},
    {"name": "Body", "size": "14px / 0.875rem", "weight": "Regular", "sample": "Standard body text for most UI elements and descriptions.", "cssClass": "fs-body fw-reg"},
    {"name": "Caption", "size": "12px / 0.75rem", "weight": "Medium", "sample": "Caption and label text for supplementary information.", "cssClass": "fs-caption fw-medium"},
    {"name": "Overline", "size": "10px / 0.625rem", "weight": "Medium", "sample": "OVERLINE TEXT — SMALL CAPS LABELS", "cssClass": "fs-overline fw-medium"}
]

# Generate Color HTML
color_html = ""
for group in colors:
    color_html += f'<div class="color-group">\n  <p class="color-group-title">{group["title"]}</p>\n  <div class="color-tiles">\n'
    for color in group["items"]:
        color_html += f'''
    <button class="color-tile" style="background-color: {color["hex"]};" onclick="copyToClipboard('{color["cssClass"]}', this)" title="Copy {color["cssClass"]}">
      <div class="color-tile-content">
        <span class="color-name">{color["name"]}</span>
        <span class="color-class-label">{color["cssClass"]}</span>
      </div>
    </button>'''
    color_html += "\n  </div>\n</div>\n"

# Generate Typography HTML
typo_html = ""
for t in typography:
    typo_html += f'''
<div class="typo-card">
  <div class="typo-meta">
    <span class="typo-name">{t["name"]}</span>
    <span>{t["size"]}</span>
    <span>{t["weight"]}</span>
  </div>
  <p class="typo-sample {t["cssClass"]}">{t["sample"]}</p>
</div>'''

# Generate Icons HTML
icon_html = ""
for i in icon_set:
    icon_html += f'''
<button class="icon-card" data-name="{i["name"].lower()}" onclick="copyToClipboard('{i["name"]}', this)" title='Copy "{i["name"]}"'>
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="icon-svg">
    <path d="{i["path"]}" />
  </svg>
  <span class="icon-label">{i["name"]}</span>
</button>'''

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Design System</title>
    <link rel="icon" href="/Favicon.png" sizes="32x32">
    <link rel="icon" href="/Favicon.png" sizes="192x192">
    <link rel="apple-touch-icon" href="/Favicon.png">
    
    <!-- Google Fonts for Proxima Nova equivalent (Inter or modern sans-serif) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --primary: #ff7048;
            --secondary: #2b3b63;
            --bg-body: #f5f5f5;
            --bg-white: #ffffff;
            --border-color: #ededed;
            --text-dark: #2b3b63;
            --text-gray: #5e6578;
            --text-light-gray: #8e97b3;
            --hover-bg: #f9fafb;
            --active-bg: #ffdbd1;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-body);
            color: var(--text-dark);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        /* Navbar */
        .navbar {{
            background-color: var(--bg-white);
            border-bottom: 1px solid var(--border-color);
            height: 65px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 48px;
            flex-shrink: 0;
        }}

        .navbar-brand {{
            display: flex;
            align-items: center;
            gap: 40px;
        }}

        .logo {{
            height: 38px;
            width: 120px;
            position: relative;
        }}

        .ds-title {{
            font-weight: 700;
            color: var(--secondary);
            font-size: 14px;
            letter-spacing: 0.05em;
        }}

        .nav-links {{
            display: flex;
            gap: 24px;
        }}

        .nav-link {{
            font-weight: 700;
            font-size: 14px;
            color: var(--secondary);
            text-decoration: none;
            cursor: pointer;
            background: none;
            border: none;
            transition: color 0.2s;
        }}

        .nav-link:hover {{
            color: var(--primary);
        }}

        .nav-link.active {{
            color: var(--primary);
        }}

        /* Layout */
        .main-container {{
            display: flex;
            flex: 1;
            gap: 24px;
            padding: 24px;
            overflow: hidden;
        }}

        /* Sidebar */
        .sidebar {{
            background-color: var(--bg-white);
            border: 1px solid var(--border-color);
            border-radius: 0 12px 12px 12px;
            width: 267px;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }}

        .sidebar-content {{
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .menu-section-btn {{
            width: 100%;
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 10px 12px;
            background: var(--bg-white);
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s;
        }}

        .menu-section-btn:hover {{
            background-color: var(--hover-bg);
        }}

        .menu-icon {{
            width: 20px;
            height: 20px;
            flex-shrink: 0;
        }}

        .menu-text {{
            flex: 1;
            text-align: left;
            font-weight: 700;
            color: var(--text-gray);
            font-size: 16px;
        }}

        .menu-indicator {{
            width: 16px;
            height: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .menu-indicator-line {{
            width: 13px;
            height: 1.5px;
            background-color: var(--text-gray);
            border-radius: 2px;
        }}

        .menu-items {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .menu-item {{
            width: 100%;
            text-align: left;
            padding: 10px 12px;
            border-radius: 6px;
            border: none;
            background: var(--bg-white);
            color: var(--text-gray);
            font-weight: 500;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .menu-item:hover {{
            background-color: var(--hover-bg);
        }}

        .menu-item.active {{
            background-color: var(--active-bg);
            color: var(--primary);
        }}

        /* Content Area */
        .content-area {{
            flex: 1;
            min-width: 0;
            overflow-y: auto;
            padding-right: 12px;
        }}

        .page-header {{
            font-weight: 700;
            color: var(--secondary);
            font-size: 24px;
            margin-bottom: 24px;
        }}

        /* Pages */
        .page {{
            display: none;
            flex-direction: column;
            gap: 24px;
        }}

        .page.active {{
            display: flex;
        }}

        /* Color Page */
        .color-grid {{
            display: grid;
            grid-template-columns: repeat(1, 1fr);
            gap: 24px;
        }}

        @media (min-width: 640px) {{ .color-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (min-width: 1024px) {{ .color-grid {{ grid-template-columns: repeat(4, 1fr); }} }}

        .color-group {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .color-group-title {{
            font-weight: 700;
            color: var(--text-gray);
            font-size: 14px;
        }}

        .color-tiles {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .color-tile {{
            width: 100%;
            text-align: left;
            border-radius: 6px;
            border: none;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.2s;
            position: relative;
        }}

        .color-tile:hover {{
            transform: scale(1.02);
        }}

        .color-tile-content {{
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 24px;
            min-height: 90px;
        }}

        .color-name {{
            font-weight: 700;
            font-size: 14px;
            color: white;
        }}

        .color-class-label {{
            font-family: monospace;
            font-size: 10px;
            color: white;
            opacity: 0.9;
        }}

        .color-tile:hover .color-class-label {{
            opacity: 1;
        }}

        /* Typography Page */
        .typo-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .typo-card {{
            background-color: var(--bg-white);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .typo-meta {{
            display: flex;
            align-items: center;
            gap: 16px;
            font-family: monospace;
            font-size: 12px;
            color: var(--text-light-gray);
        }}

        .typo-name {{
            font-weight: 700;
            color: var(--text-gray);
            font-size: 14px;
            width: 112px;
        }}

        .typo-sample {{
            color: var(--text-dark);
            margin: 0;
        }}

        /* Typography utilities */
        .fs-display {{ font-size: 48px; line-height: 3rem; }}
        .fs-h1 {{ font-size: 32px; line-height: 2rem; }}
        .fs-h2 {{ font-size: 24px; line-height: 1.5rem; }}
        .fs-h3 {{ font-size: 20px; line-height: 1.25rem; }}
        .fs-body-lg {{ font-size: 16px; line-height: 1rem; }}
        .fs-body {{ font-size: 14px; line-height: 0.875rem; }}
        .fs-caption {{ font-size: 12px; line-height: 0.75rem; }}
        .fs-overline {{ font-size: 10px; line-height: 0.625rem; letter-spacing: 0.1em; text-transform: uppercase; }}
        
        .fw-bold {{ font-weight: 700; }}
        .fw-medium {{ font-weight: 500; }}
        .fw-reg {{ font-weight: 400; }}

        /* Icons Page */
        .search-input {{
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 14px;
            color: var(--text-dark);
            background-color: var(--bg-white);
            width: 100%;
            max-width: 320px;
            outline: none;
        }}

        .search-input:focus {{
            border-color: var(--primary);
        }}

        .icons-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }}

        @media (min-width: 640px) {{ .icons-grid {{ grid-template-columns: repeat(6, 1fr); }} }}
        @media (min-width: 1024px) {{ .icons-grid {{ grid-template-columns: repeat(8, 1fr); }} }}

        .icon-card {{
            background-color: var(--bg-white);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .icon-card:hover {{
            border-color: var(--primary);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }}

        .icon-svg {{
            width: 28px;
            height: 28px;
            stroke: var(--text-gray);
            transition: stroke 0.2s;
        }}

        .icon-card:hover .icon-svg {{
            stroke: var(--primary);
        }}

        .icon-label {{
            font-size: 10px;
            font-weight: 500;
            color: var(--text-gray);
            transition: color 0.2s;
        }}

        .icon-card:hover .icon-label {{
            color: var(--primary);
        }}

        /* Prototype Page Placeholder */
        .prototype-placeholder {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            gap: 16px;
            padding: 96px 0;
        }}

        .prototype-icon-box {{
            width: 64px;
            height: 64px;
            border-radius: 16px;
            background-color: var(--active-bg);
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .prototype-icon-box svg {{
            width: 32px;
            height: 32px;
            stroke: var(--primary);
        }}

        .prototype-title {{
            font-weight: 700;
            color: var(--secondary);
            font-size: 20px;
        }}

        .prototype-desc {{
            color: var(--text-gray);
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="navbar">
        <div class="navbar-brand">
            <div class="logo">
                <svg class="logo-svg" style="width: 100%; height: 100%; position: absolute; inset: 0;" fill="none" preserveAspectRatio="none" viewBox="0 0 120 38">
                    <g>
                        <g>
                            <path d="{svg_paths["p19d42400"]}" fill="#2B3B63" />
                            <path d="{svg_paths["p3d36480"]}" fill="#2B3B63" />
                            <path d="{svg_paths["p88ca800"]}" fill="#2B3B63" />
                        </g>
                        <path clip-rule="evenodd" d="{svg_paths["pf15ab80"]}" fill="#2B3B63" fill-rule="evenodd" />
                        <g>
                            <path d="{svg_paths["p7084140"]}" fill="#2B3B63" />
                            <path d="{svg_paths["p3b2a0980"]}" fill="#2B3B63" />
                            <path d="{svg_paths["p25230c00"]}" fill="#2B3B63" />
                            <path d="{svg_paths["p197c5200"]}" fill="#2B3B63" />
                        </g>
                    </g>
                </svg>
            </div>
            <span class="ds-title">DESIGN SYSTEM</span>
        </div>
        <div class="nav-links">
            <button class="nav-link" onclick="switchMainPage('3d')">3D Prototype</button>
            <button class="nav-link" onclick="switchMainPage('ops')">OPSHub Prototype</button>
        </div>
    </div>

    <div class="main-container">
        <aside class="sidebar">
            <div class="sidebar-content">
                <!-- Style Section -->
                <button class="menu-section-btn" onclick="toggleMenuSection('style-menu')">
                    <span class="menu-icon">
                        <svg style="width: 100%; height: 100%;" fill="none" viewBox="0 0 16 16">
                            <path d="{svg_paths["p3ae3bc80"]}" fill="#5E6578" />
                        </svg>
                    </span>
                    <span class="menu-text">Style</span>
                    <span class="menu-indicator">
                        <span class="menu-indicator-line"></span>
                    </span>
                </button>
                <div class="menu-items" id="style-menu">
                    <button class="menu-item active" onclick="switchTab('color', this)">Color</button>
                    <button class="menu-item" onclick="switchTab('typography', this)">Typography</button>
                    <button class="menu-item" onclick="switchTab('icons', this)">Icons</button>
                </div>

                <!-- Component Section -->
                <button class="menu-section-btn" onclick="toggleMenuSection('component-menu')">
                    <span class="menu-icon">
                        <svg style="width: 100%; height: 100%;" fill="none" viewBox="0 0 14.17 14.17">
                            <path d="{svg_paths["p29f37d80"]}" fill="#5E6578" />
                        </svg>
                    </span>
                    <span class="menu-text">Component</span>
                    <span class="menu-indicator">
                        <svg style="width: 100%; height: 100%;" fill="none" viewBox="0 0 13.33 13.33">
                            <path d="{svg_paths["p259d0100"]}" fill="#5E6578" />
                        </svg>
                    </span>
                </button>
                <div class="menu-items" id="component-menu" style="display: none;">
                    <button class="menu-item">Buttons</button>
                    <button class="menu-item">Inputs</button>
                    <button class="menu-item">Cards</button>
                    <button class="menu-item">Modals</button>
                    <button class="menu-item">Tables</button>
                </div>
            </div>
        </aside>

        <main class="content-area">
            <!-- Style Pages -->
            <div id="page-design" class="page active">
                <div id="tab-color" class="page active">
                    <h1 class="page-header">Colors</h1>
                    <div class="color-grid">
                        {color_html}
                    </div>
                </div>

                <div id="tab-typography" class="page">
                    <h1 class="page-header">Typography</h1>
                    <div class="typo-list">
                        {typo_html}
                    </div>
                </div>

                <div id="tab-icons" class="page">
                    <h1 class="page-header">Icons</h1>
                    <input type="text" class="search-input" placeholder="Search icons…" oninput="filterIcons(this.value)">
                    <div class="icons-grid" id="icons-grid">
                        {icon_html}
                    </div>
                </div>
            </div>

            <!-- Prototype Pages -->
            <div id="page-3d" class="page prototype-placeholder">
                <div class="prototype-icon-box">
                    <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5">
                        <rect x="3" y="3" width="18" height="18" rx="3" />
                        <path d="M9 9h6M9 12h6M9 15h4" />
                    </svg>
                </div>
                <h2 class="prototype-title">3D Prototype</h2>
                <p class="prototype-desc">This prototype view is coming soon.</p>
            </div>

            <div id="page-ops" class="page prototype-placeholder">
                <div class="prototype-icon-box">
                    <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5">
                        <rect x="3" y="3" width="18" height="18" rx="3" />
                        <path d="M9 9h6M9 12h6M9 15h4" />
                    </svg>
                </div>
                <h2 class="prototype-title">OPSHub Prototype</h2>
                <p class="prototype-desc">This prototype view is coming soon.</p>
            </div>

        </main>
    </div>

    <script>
        function toggleMenuSection(id) {{
            const el = document.getElementById(id);
            if (el.style.display === 'none') {{
                el.style.display = 'flex';
            }} else {{
                el.style.display = 'none';
            }}
        }}

        function switchMainPage(pageId) {{
            // Deactivate all nav links
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            event.target.classList.add('active');

            // Hide sidebar
            document.querySelector('.sidebar').style.display = 'none';

            // Hide all pages
            document.querySelectorAll('main > .page').forEach(p => p.classList.remove('active'));
            
            // Show target page
            document.getElementById('page-' + pageId).classList.add('active');
        }}

        // If clicking on "DESIGN SYSTEM" logo, go back to design page
        document.querySelector('.navbar-brand').addEventListener('click', function() {{
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            document.querySelector('.sidebar').style.display = 'flex';
            document.querySelectorAll('main > .page').forEach(p => p.classList.remove('active'));
            document.getElementById('page-design').classList.add('active');
        }});

        function switchTab(tabId, btn) {{
            // Deactivate all menu items
            const menuItems = document.getElementById('style-menu').querySelectorAll('.menu-item');
            menuItems.forEach(item => item.classList.remove('active'));
            
            // Activate clicked
            btn.classList.add('active');

            // Hide all style tabs
            document.getElementById('tab-color').classList.remove('active');
            document.getElementById('tab-typography').classList.remove('active');
            document.getElementById('tab-icons').classList.remove('active');

            // Show target
            document.getElementById('tab-' + tabId).classList.add('active');
        }}

        function copyToClipboard(text, btn) {{
            navigator.clipboard.writeText(text).then(() => {{
                // Find the label element inside the button
                let labelEl;
                let originalText;
                
                if(btn.classList.contains('color-tile')) {{
                    labelEl = btn.querySelector('.color-class-label');
                }} else if(btn.classList.contains('icon-card')) {{
                    labelEl = btn.querySelector('.icon-label');
                }}
                
                if(labelEl) {{
                    originalText = labelEl.innerText;
                    labelEl.innerText = "Copied!";
                    setTimeout(() => {{
                        labelEl.innerText = originalText;
                    }}, 1500);
                }}
            }});
        }}

        function filterIcons(query) {{
            query = query.toLowerCase();
            const icons = document.querySelectorAll('.icon-card');
            icons.forEach(icon => {{
                const name = icon.getAttribute('data-name');
                if (name.includes(query)) {{
                    icon.style.display = 'flex';
                }} else {{
                    icon.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>
'''

target_path = '/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html'
with open(target_path, 'w') as f:
    f.write(html_content)

print("Generated design-system.html successfully.")
