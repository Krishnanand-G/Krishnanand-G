import html

# Define the 12 cat animations with their frames
# Each animation has a name and a list of frames (each frame is a list of string lines)
animations = [
    {
        "name": "Sleepy Cat",
        "frames": [
            [
                r"   |\---/|",
                r"   | -_- |  z",
                r"    \_^_/  "
            ],
            [
                r"   |\---/|",
                r"   | -_- |   Z",
                r"    \_^_/  "
            ],
            [
                r"   |\---/|",
                r"   | -_- |    z",
                r"    \_^_/  "
            ]
        ]
    },
    {
        "name": "Wiggle Tail",
        "frames": [
            [
                r"  /\_/\  /",
                r" ( ^.^ )/",
                r"  > ^ <"
            ],
            [
                r"  /\_/\  |",
                r" ( ^.^ )|",
                r"  > ^ <"
            ],
            [
                r"  /\_/\  \\",
                r" ( ^.^ )/",
                r"  > ^ <"
            ]
        ]
    },
    {
        "name": "Curious Look",
        "frames": [
            [
                r"  /\_/\ ",
                r" ( >.< )",
                r"  > ^ <"
            ],
            [
                r"  /\_/\ ",
                r" ( <.< )",
                r"  > ^ <"
            ]
        ]
    },
    {
        "name": "Hacker Cat",
        "frames": [
            [
                r"  /\_/\   [key]",
                r" ( o.o )  / \\",
                r"  > ^ <  /   \\"
            ],
            [
                r"  /\_/\   [key]",
                r" ( o.o )  \\ /",
                r"  > ^ <   \\ /"
            ]
        ]
    },
    {
        "name": "Stretching",
        "frames": [
            [
                r"  _._     _,-'\"\"`-._",
                r" (,-.`._,'(       |\\`-/|",
                r"     `-.-' \ )-`( , o o)",
                r"           `-    \\_`\"'-"
            ],
            [
                r"  _._     _,-'\"\"`-._",
                r" (,-.`._,'(       |\\`-/|",
                r"     `---' \ )-`( , - -)",
                r"           `-    \\_`\"'-"
            ]
        ]
    },
    {
        "name": "Shocked Eeey",
        "frames": [
            [
                r"  /\___/\ ",
                r" (  o o  )",
                r"  \  ^  / ",
                r"   )   (  "
            ],
            [
                r"  /\_ _/\ ",
                r" (  O O  )",
                r"  \  ^  / ",
                r"   )   (  "
            ]
        ]
    },
    {
        "name": "Dancing Cat",
        "frames": [
            [
                r"   /\_/\ ",
                r"  ( ^.^ )  ~",
                r"  /| | |\\",
                r"  /  |  \\"
            ],
            [
                r"   /\_/\ ",
                r"  ( ^.^ ) ~",
                r"  \\| | |/",
                r"  /  |  \\"
            ]
        ]
    },
    {
        "name": "Peeking Wall",
        "frames": [
            [
                r"   /\_/\ ",
                r"  ( o.o )",
                r" =========="
            ],
            [
                r"   /\_/\ ",
                r"  ( -.- )",
                r" =========="
            ]
        ]
    },
    {
        "name": "Bouncing",
        "frames": [
            [
                r"  /\_/\ ",
                r" ( o.o )",
                r"  > ^ <"
            ],
            [
                r"  /\_/\ ",
                r" ( o.o )",
                r"  > ^ <"
            ]
        ]
    },
    {
        "name": "Heart Cat",
        "frames": [
            [
                r"  /\_/\  <3",
                r" ( ^.^ )",
                r"  > ^ <"
            ],
            [
                r"  /\_/\   <3",
                r" ( ^.^ )",
                r"  > ^ <"
            ]
        ]
    },
    {
        "name": "Pawing Dot",
        "frames": [
            [
                r"  /\_/\ ",
                r" ( o.o )  .",
                r"  > ^ <  /"
            ],
            [
                r"  /\_/\ ",
                r" ( o.o ) .",
                r"  > ^ <  \\"
            ]
        ]
    },
    {
        "name": "Happy Hop",
        "frames": [
            [
                r"  /\_/\ ",
                r" (=^.^=)",
                r"  (\")(\")"
            ],
            [
                r"  /\_/\ ",
                r" (=^.^=)",
                r"  (\") (\")"
            ]
        ]
    }
]

# Generate the SVG contents
out = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="920" height="420" viewBox="0 0 920 420">',
    '<style>',
    '  :root {',
    '    --bg: #ffffff;',
    '    --text: #24292f;',
    '    --border: #d0d7de;',
    '    --title: #0969da;',
    '    --label: #57606a;',
    '  }',
    '  @media (prefers-color-scheme: dark) {',
    '    :root {',
    '      --bg: #0d1117;',
      '      --text: #c9d1d9;',
    '      --border: #30363d;',
    '      --title: #58a6ff;',
    '      --label: #8b949e;',
    '    }',
    '  }',
    '  rect.box { fill: var(--bg); stroke: var(--border); stroke-width: 1px; rx: 8px; }',
    '  text.title { fill: var(--title); font-family: sans-serif; font-size: 13px; font-weight: bold; }',
    '  text.ascii { fill: var(--text); font-family: Consolas, Menlo, monospace; font-size: 12px; }',
    '  ',
    '  /* 2-frame animation classes */',
    '  @keyframes play-2f-1 { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }',
    '  @keyframes play-2f-2 { 0%, 49% { opacity: 0; } 50%, 100% { opacity: 1; } }',
    '  .anim-2f-1 { animation: play-2f-1 0.8s infinite; }',
    '  .anim-2f-2 { animation: play-2f-2 0.8s infinite; }',
    '  ',
    '  /* 3-frame animation classes */',
    '  @keyframes play-3f-1 { 0%, 32% { opacity: 1; } 33%, 100% { opacity: 0; } }',
    '  @keyframes play-3f-2 { 0%, 32% { opacity: 0; } 33%, 65% { opacity: 1; } 66%, 100% { opacity: 0; } }',
    '  @keyframes play-3f-3 { 0%, 65% { opacity: 0; } 66%, 100% { opacity: 1; } }',
    '  .anim-3f-1 { animation: play-3f-1 1.2s infinite; }',
    '  .anim-3f-2 { animation: play-3f-2 1.2s infinite; }',
    '  .anim-3f-3 { animation: play-3f-3 1.2s infinite; }',
    '  ',
    '  /* Special Bounce keyframes */',
    '  @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(4px); } }',
    '  .bounce-cat { animation: bounce 0.6s infinite; }',
    '</style>'
]

# Layout: 4 columns x 3 rows
cols = 4
rows = 3
cell_w = 220
cell_h = 120
gap_x = 10
gap_y = 10

for idx, anim in enumerate(animations):
    r = idx // cols
    c = idx % cols
    
    x = 10 + c * (cell_w + gap_x)
    y = 10 + r * (cell_h + gap_y)
    
    # Outer box
    out.append(f'  <rect class="box" x="{x}" y="{y}" width="{cell_w}" height="{cell_h}"/>')
    
    # Label/title
    out.append(f'  <text class="title" x="{x + 12}" y="{y + 22}">{html.escape(anim["name"])}</text>')
    
    num_frames = len(anim["frames"])
    
    # Render frames
    for f_idx, frame in enumerate(anim["frames"]):
        anim_class = ""
        if num_frames == 2:
            anim_class = f"anim-2f-{f_idx + 1}"
        elif num_frames == 3:
            anim_class = f"anim-3f-{f_idx + 1}"
            
        if anim["name"] == "Bouncing" and f_idx == 1:
            anim_class += " bounce-cat"
            
        out.append(f'  <g class="{anim_class}">')
        for l_idx, line in enumerate(frame):
            ly = y + 48 + l_idx * 16
            out.append(f'    <text class="ascii" x="{x + 15}" y="{ly}" xml:space="preserve">{html.escape(line)}</text>')
        out.append(f'  </g>')

out.append('</svg>')

with open("cats.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote cats.svg")
