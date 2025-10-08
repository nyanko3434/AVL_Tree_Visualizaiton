def compute_positions(root, x, y, x_offset, positions, level_spacing=60):
    if not root:
        return
    positions[root] = (x, y)
    compute_positions(root.left, x - x_offset, y + level_spacing, x_offset / 2, positions)
    compute_positions(root.right, x + x_offset, y + level_spacing, x_offset / 2, positions)
