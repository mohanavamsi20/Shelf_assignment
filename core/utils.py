# shape_identifier/utils.py
from .locations import assign_shape_location, \
    divide_grid_middle, divide_grid_vertically, divide_grid_into_quarters


def is_square_submatrix(coordinates):
    # Extract the minimum and maximum coordinates
    min_x = min(coordinates, key=lambda x: x[0])[0]
    max_x = max(coordinates, key=lambda x: x[0])[0]
    min_y = min(coordinates, key=lambda x: x[1])[1]
    max_y = max(coordinates, key=lambda x: x[1])[1]

    # Calculate the size of the potential square sub-matrix
    size = max(max_x - min_x, max_y - min_y) + 1

    # Check if all coordinates within the square sub-matrix are present
    expected_coords = [(r, c) for r in range(min_x, min_x + size)
                       for c in range(min_y, min_y + size)]
    if all(coord in coordinates for coord in expected_coords):
        return True
    else:
        return False


def identify_shapes(coordinates):
    shapes = {}

    # Check if the element forms a square sub-matrix
    if is_square_submatrix(coordinates):
        shapes['shape'] = 'square'

    # Check if the element forms a horizontal rectangle
    elif len(set(coord[0] for coord in coordinates)) == 1 and len(set(coord[1] for coord in coordinates)) >= 2:
        shapes['shape'] = 'horizontal rectangle'

    # Check if the element forms a vertical rectangle
    elif len(set(coord[1] for coord in coordinates)) == 1 and len(set(coord[0] for coord in coordinates)) >= 2:
        shapes['shape'] = 'vertical rectangle'

    # If none of the above conditions are met, consider it a polygon
    else:
        shapes['shape'] = 'polygon'

    return shapes


def get_layout(grid):
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def dfs(x, y, element):
        if not is_valid(x, y) or grid[x][y] != element or visited[x][y]:
            return

        visited[x][y] = True
        connected_elements[element].append((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(x + dx, y + dy, element)

    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    connected_elements = {}
    result = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not visited[row][col]:
                element = grid[row][col]
                connected_elements.setdefault(element, [])
                dfs(row, col, element)
                if len(connected_elements[element]) > 2:
                    for element, coordinates in connected_elements.items():
                        shape_info = identify_shapes(coordinates)
                        quarters = divide_grid_into_quarters(grid)
                        halves = divide_grid_vertically(grid)
                        middle_sections = divide_grid_middle(grid)
                        assign_shape_location(coordinates, shape_info, quarters, halves, middle_sections)
                        result.append({element: shape_info})
                connected_elements = {}
    return result
