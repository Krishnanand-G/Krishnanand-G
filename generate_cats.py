import html

# Define the three walking poses of the classic ASCII cat (4 lines high)
pose_1 = [
    r"          /\_/\___  ",
    r"         = o_o =__\_",
    r"           \   _   \_",
    r"            \ / \ / "
]

pose_2 = [
    r"          /\_/\___  ",
    r"         = o_o =__\_",
    r"           \   _   \_",
    r"            | | | | "
]

pose_3 = [
    r"          /\_/\___  ",
    r"         = o_o =__\_",
    r"           \   _   \_",
    r"            / \ / \ "
]

# We will generate 18 frames of the cat walking across the page
# Shifting right by 4 characters in each frame
num_frames = 18
shift_step = 4

out = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="980" height="120" viewBox="0 0 980 120">',
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

# Generate keyframes for each of the 18 frames
for i in range(num_frames):
    start = i * (100.0 / num_frames)
    end = (i + 1) * (100.0 / num_frames) - 0.01
    
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
out.append('  <rect class="box" x="0.5" y="0.5" width="979" height="119"/>')

# Render each frame
for i in range(num_frames):
    shift_spaces = " " * (i * shift_step)
    
    # Cycle poses: 1 -> 2 -> 3 -> 2 -> 1 ...
    cycle_idx = i % 4
    if cycle_idx == 0:
        pose = pose_1
    elif cycle_idx == 1 or cycle_idx == 3:
        pose = pose_2
    else:
        pose = pose_3
        
    out.append(f'  <g class="frame-{i}">')
    for l_idx, line in enumerate(pose):
        shifted_line = shift_spaces + line
        ly = 35 + l_idx * 16
        out.append(f'    <text class="ascii" x="25" y="{ly}" xml:space="preserve">{html.escape(shifted_line)}</text>')
    out.append('  </g>')

out.append('</svg>')

with open("cats.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote classic cat walk cycle to cats.svg")
