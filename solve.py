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
tries = []

def parse_matrix(matrix):
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
    return grid


def print_grid(grid):
    for x in range(9):
        print(''.join([str(x) for x in grid[x]]))


def hash_grid(grid):
    total = 0
    for x in range(9):
        for y in range(9):
            if grid[x][y] != 'x':
                total += int(grid[x][y])
    return total


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
                try_count -= 1
            if len(possibilities) == 0:
                continue
            new_grid = copy.deepcopy(grid)
            new_grid[x][y] = possibilities[0]
            tries.append([grid, orig_try_count])
            return new_grid
    raise RuntimeError("Cannot add_try")


def revert_try():
    global tries
    old_grid, try_count = tries[0]
    tries = tries[1:]
    try:
        new_grid = add_try(old_grid, try_count=try_count+1)
        return new_grid
    except RuntimeError:
        return revert_try()


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
    return cell_possibilities


def search(grid):
    while not finished(grid):
        found = False
        reset = False
        for x in range(9):
            for y in range(9):
                # print_grid(grid)
                if grid[x][y] != 'x':
                    continue
                cell_possibilities = compute(grid, x, y)
                if len(cell_possibilities) == 0:
                    reset = True
                    break
                if len(cell_possibilities) == 1:
                    found = True
                    grid[x][y] = cell_possibilities[0]
            if reset:
                break
        if reset:
            grid = revert_try()
            continue
        if not found:
            grid = add_try(grid)
            # print_grid(grid)
            # raise Exception("cannot advance")
    print_grid(grid)


search(parse_matrix(matrix))
