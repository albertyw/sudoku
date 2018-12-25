import copy

matrix = """
xx3x1xxxx
4xx56x2x9
7xxxx81xx
x8x1xxxx3
xx18x94xx
3xxxx4x8x
xx59xxxx7
2x9x53xx4
xxxx4x9xx
"""
matrix = """
9x3x1xxxx
4xx56x2x9
7xxxx814x
x841x5x93
xx18394xx
39xxx4x81
x459xx3x7
2x9x53xx4
x3xx4x9xx
"""
possibilities = range(1, 10)
squares = {
    0: range(0, 3),
    1: range(0, 3),
    2: range(0, 3),
    3: range(3, 6),
    4: range(3, 6),
    5: range(3, 6),
    6: range(6, 9),
    7: range(6, 9),
    8: range(6, 9),
}
grid = []

row = []
for i in matrix:
    if not i.strip():
        continue
    if i != 'x':
        i = int(i)
    row.append(i)
    if len(row) == 9:
        grid.append(row)
        row = []


def print_grid(grid):
    for x in range(9):
        print(''.join([str(x) for x in grid[x]]))


def finished(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 'x':
                return False
    return True


def compute(grid, cell_x, cell_y):
    cell_possibilities = copy.deepcopy(possibilities)
    print('compute')
    # remove row
    x = cell_x
    for y in range(9):
        if grid[x][y] not in cell_possibilities:
            continue
        # print(grid[x][y])
        cell_possibilities.remove(grid[x][y])
    # remove column
    y = cell_y
    for x in range(9):
        if grid[x][y] not in cell_possibilities:
            continue
        # print(grid[x][y])
        cell_possibilities.remove(grid[x][y])
    # remove square
    for x in squares[cell_x]:
        for y in squares[cell_y]:
            if grid[x][y] not in cell_possibilities:
                continue
            # print(grid[x][y])
            cell_possibilities.remove(grid[x][y])
    if not cell_possibilities:
        raise Exception("need to backtrack")
    if len(cell_possibilities) == 1:
        print('confirmed: ', cell_possibilities[0])
        return cell_possibilities[0]
    return None


while not finished(grid):
    found = False
    for x in range(9):
        for y in range(9):
            if grid[x][y] != 'x':
                continue
            answer = compute(grid, x, y)
            if answer:
                found = True
                grid[x][y] = answer
    if not found:
        print_grid(grid)
        raise Exception("cannot advance")
print_grid(grid)
