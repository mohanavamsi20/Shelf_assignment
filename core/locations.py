def divide_grid_into_quarters(grid):
    rows = len(grid)
    cols = len(grid[0])

    half_rows = rows // 2
    half_cols = cols // 2

    result = {}

    top_left = [(i, j) for i in range(half_rows) for j in range(half_cols)]
    top_right = [(i, j) for i in range(half_rows) for j in range(half_cols, cols)]
    bottom_left = [(i, j) for i in range(half_rows, rows) for j in range(half_cols)]
    bottom_right = [(i, j) for i in range(half_rows, rows) for j in range(half_cols, cols)]

    result["top_left"] = top_left
    result["top_right"] = top_right
    result["bottom_left"] = bottom_left
    result["bottom_right"] = bottom_right

    return result


def divide_grid_vertically(grid):
    rows = len(grid)
    cols = len(grid[0])

    half_cols = cols // 2

    result = {}

    left_half = [(i, j) for i in range(rows) for j in range(half_cols)]
    right_half = [(i, j) for i in range(rows) for j in range(half_cols, cols)]

    result["left"] = left_half
    result["right"] = right_half

    return result


def divide_grid_middle(grid):
    rows = len(grid)
    cols = len(grid[0])

    if rows < 4 or cols < 4:
        raise ValueError("Grid dimensions must be at least 4x4 for middle division")

    # Remove the top and bottom rows and the left and right columns to get the middle data
    middle_data = [row[1:-1] for row in grid[1:-1]]

    middle_rows = len(middle_data)
    middle_cols = len(middle_data[0])

    middle_half_cols = middle_cols // 2

    result = {}
    middle_left = [(i + 1, j + 1) for i in range(middle_rows) for j in range(middle_half_cols)]
    middle_right = [(i + 1, j + middle_half_cols + 2) for i in range(middle_rows) for j in range(middle_half_cols)]

    result["middle_left"] = middle_left
    result["middle_right"] = middle_right

    return result


def assign_shape_location(coordinates, shapes, quarters, halves, middle_sections):
    quarter_counts = {section: 0 for section in quarters.keys()}
    half_counts = {section: 0 for section in halves.keys()}
    middle_counts = {section: 0 for section in middle_sections.keys()}
    for coord in coordinates:
        for section, section_coords in quarters.items():
            if coord in section_coords:
                quarter_counts[section] += 1
        for section, section_coords in halves.items():
            if coord in section_coords:
                half_counts[section] += 1
        for section, section_coords in middle_sections.items():
            if coord in section_coords:
                middle_counts[section] += 1
    # print(quarter_counts)

    # Determine the location based on which section covers the most coordinates
    max_quarter_section = max(quarter_counts, key=quarter_counts.get)
    max_half_section = max(half_counts, key=half_counts.get)
    max_middle_section = max(middle_counts, key=middle_counts.get)

    # Assign the locations
    if quarter_counts[max_quarter_section] >= half_counts[max_half_section] and \
            quarter_counts[max_quarter_section] >= middle_counts[max_middle_section]:
        shapes['location'] = [max_quarter_section]
    elif half_counts[max_half_section] >= middle_counts[max_middle_section]:
        shapes['location'] = [max_half_section]
    else:
        shapes['location'] = [max_middle_section]
    return shapes
