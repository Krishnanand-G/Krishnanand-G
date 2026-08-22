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

# Poses above are drawn facing left (tail trails to the right). The frames
# below shift the cat rightward over time, so mirror each pose horizontally
# (reverse the line and swap slash direction) to make it face the direction
# it's walking instead of appearing to walk backward.
def _mirror(lines):
    table = str.maketrans("/\\", "\\/")
    return [line[::-1].translate(table) for line in lines]

pose_1 = _mirror(pose_1)
pose_2 = _mirror(pose_2)
pose_3 = _mirror(pose_3)

# We will generate 18 frames of the cat walking across the page
num_frames = 18
canvas_width = 980

# Approx monospace glyph width at 14px bold, and the widest pose line, so we
# can compute a pixel offset (not a whole-character shift) that starts the
# cat fully off-canvas on the left and ends it fully off-canvas on the right.
char_width_px = 8.4
pose_width_px = max(len(line) for p in (pose_1, pose_2, pose_3) for line in p) * char_width_px
start_x = -pose_width_px
end_x = canvas_width + pose_width_px

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

# Clip the walking frames to the box so the cat is hidden while off-canvas
# instead of spilling past the rounded corners.
out.append('  <defs><clipPath id="walkClip"><rect x="0.5" y="0.5" width="979" height="119" rx="8"/></clipPath></defs>')
out.append('  <g clip-path="url(#walkClip)">')

# Render each frame
for i in range(num_frames):
    frame_x = start_x + i * (end_x - start_x) / (num_frames - 1)

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
        ly = 35 + l_idx * 16
        out.append(f'    <text class="ascii" x="{frame_x:.1f}" y="{ly}" xml:space="preserve">{html.escape(line)}</text>')
    out.append('  </g>')

out.append('  </g>')
out.append('</svg>')

with open("cats.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote classic cat walk cycle to cats.svg")
