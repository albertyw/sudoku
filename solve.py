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
x841xxx93
xx18394xx
39xxx4x81
x459xx3x7
2x9x53xx4
x3xx4x9xx
"""
answer = """
953412678
418567239
726398145
684125793
571839462
392674581
145986327
269753814
837241956
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
tries = []

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


def add_try(grid, try_count=0):
    orig_try_count = try_count
    for x in range(9):
        for y in range(9):
            if grid[x][y] != 'x':
                continue
            possibilities = compute(grid, x, y)
            while possibilities and try_count > 0:
                possibilities = possibilities[1:]
                try_count += 1
            if try_count > 0:
                continue
            new_grid = copy.deepcopy(grid)
            new_grid[x][y] = possibilities[0]
            tries.append([grid, orig_try_count])
            return new_grid


def revert_try():
    old_grid, try_count = tries.pop()
    return add_try(old_grid, try_count=try_count+1)


def compute(grid, cell_x, cell_y):
    cell_possibilities = copy.deepcopy(possibilities)
    # print('compute')
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
    if len(cell_possibilities) == 1:
        print('confirmed: ', cell_possibilities[0])
    return cell_possibilities


while not finished(grid):
    found = False
    for x in range(9):
        for y in range(9):
            if grid[x][y] != 'x':
                continue
            answer = compute(grid, x, y)
            if len(answer) == 0:
                grid = revert_try()
            if len(answer) == 1:
                found = True
                grid[x][y] = answer[0]
    if not found:
        grid = add_try(grid)
        print_grid(grid)
        # raise Exception("cannot advance")
print_grid(grid)
