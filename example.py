import solve

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

solved = solve.Solver(matrix).search()
print(solved)
assert solved == answer.strip()
