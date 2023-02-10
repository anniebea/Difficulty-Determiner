from universalMethods import *


def bruteForce(puzzle):
    puzzle = [list(puzzle[i:i + 9]) for i in range(0, 81, 9)]
    empty = find_empty_cell(puzzle)
    if empty is None:
        return ''.join([''.join(row) for row in puzzle])
    row, col = empty
    for num in "123456789":
        if is_valid(puzzle, num, row, col):
            puzzle[row][col] = num
            solution = bruteForce(''.join([''.join(row) for row in puzzle]))
            if solution:
                return solution
    return None
