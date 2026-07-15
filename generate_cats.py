import html

# Define the two walking poses of the large cat (8 lines high, ~38 chars wide)
pose_a = [
    r"                 /\_/\                     ",
    r"                / o o \                    ",
    r"               (   \"   )_______            ",
    r"                \         _   _ \___       ",
    r"                /   _   _/ /  / /   \      ",
    r"               /   / \   \/  / /  \  \     ",
    r"              /   /   \   \ /  /   |  |    ",
    r"             (___/     \___/___/   /__/    "
]

pose_b = [
    r"                 /\_/\                     ",
    r"                / o o \                    ",
    r"               (   \"   )_______            ",
    r"                \         _   _ \___       ",
    r"                /   _   _\ \  \ \   \      ",
    r"               /   \ /   /\  \ \  \  \     ",
    r"              /   / \   /  \  \   |  |     ",
    r"             (__/    \_/____\__\   \__\    "
]

# We will generate 16 frames of the cat walking across the page
# Shifting right by 5 characters (approx 39px) in each frame
num_frames = 16
shift_step = 5

out = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="980" height="200" viewBox="0 0 980 200">',
    '<style>',
    '  :root {',
    '    --bg: #0d1117;',
    '    --text: #3fb950; /* Green terminal text */',
    '    --border: #30363d;',
    '  }',
    '  @media (prefers-color-scheme: light) {',
    '    :root {',
    '      --bg: #ffffff;',
    '      --text: #1a7f37; /* Green light-mode text */',
    '      --border: #d0d7de;',
    '    }',
    '  }',
    '  rect.box { fill: var(--bg); stroke: var(--border); stroke-width: 1px; rx: 8px; }',
    '  text.ascii { fill: var(--text); font-family: Consolas, Menlo, monospace; font-size: 14px; font-weight: bold; }',
    '  '
]

# Generate keyframes for each of the 16 frames
for i in range(num_frames):
    start = i * (100.0 / num_frames)
    end = (i + 1) * (100.0 / num_frames) - 0.01
    
    # We construct keyframes to only show the frame during its active slot
    out.append(f'  @keyframes play-{i} {{')
    out.append(f'    0% {{ opacity: {"1" if i == 0 else "0"}; }}')
    if i > 0:
        out.append(f'    {start:.2f}% {{ opacity: 0; }}')
        out.append(f'    {start + 0.01:.2f}% {{ opacity: 1; }}')
    out.append(f'    {end:.2f}% {{ opacity: 1; }}')
    if i < num_frames - 1:
        out.append(f'    {end + 0.01:.2f}% {{ opacity: 0; }}')
        out.append(f'    100% {{ opacity: 0; }}')
    else:
        out.append(f'    100% {{ opacity: 1; }}')
    out.append('  }')
    out.append(f'  .frame-{i} {{ animation: play-{i} 2.0s infinite; }}')

out.append('</style>')

# Outer container box
out.append('  <rect class="box" x="0.5" y="0.5" width="979" height="199"/>')

# Render each frame
for i in range(num_frames):
    shift_spaces = " " * (i * shift_step)
    pose = pose_a if (i % 2 == 0) else pose_b
    
    out.append(f'  <g class="frame-{i}">')
    for l_idx, line in enumerate(pose):
        # We prepend spaces to shift the cat horizontally
        shifted_line = shift_spaces + line
        ly = 45 + l_idx * 16
        out.append(f'    <text class="ascii" x="25" y="{ly}" xml:space="preserve">{html.escape(shifted_line)}</text>')
    out.append('  </g>')

out.append('</svg>')

with open("cats.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote large cat walk cycle to cats.svg")
