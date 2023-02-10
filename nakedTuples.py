from universalMethods import *
from bruteForce import bruteForce


def get_peers(i, j):
    """
    Get all peers to a cell.
    :param i: column
    :param j: row
    :return: set of cells that are peers of cell at coordinates [i;j]
    """
    peers = set()
    for a in range(9):
        if a != i:
            peers.add((a, j))
        if a != j:
            peers.add((i, a))
    box_x = j // 3
    box_y = i // 3
    for a in range(box_y * 3, box_y * 3 + 3):
        for b in range(box_x * 3, box_x * 3 + 3):
            if (a != i) and (b != j):
                peers.add((a, b))
    return peers


def nakedSingleStep(puzzle, row, col):
    """
    Apply the Naked Single method to a cell, return modified cell.
    :param puzzle: Puzzle that contains solvable cell
    :param row: ID of cell's row
    :param col: ID of cell's column
    :return: Puzzle with potentially solved cell
    """
    puzzle = [list(puzzle[col:col + 9]) for col in range(0, 81, 9)]
    if puzzle[col][row] == '0':
        candidates = set('123456789')
        peers = get_peers(col, row)
        for x, y in peers:  # set actual candidates
            if puzzle[x][y] in candidates:
                candidates.remove(puzzle[x][y])
        if len(candidates) == 1:  # one candidate means the cell is a Naked Single
            puzzle[col][row] = candidates.pop()
    return ''.join([''.join(row) for row in puzzle])


def naked_single(puzzle):
    """
    Calculate solution using a Naked Single method.
    :param puzzle: string of numbers, representing a Sudoku puzzle
    :return: Sudoku string with visible Naked Singles solved (not including ones that are revealed during solve)
    """
    for i in range(9):
        for j in range(9):
            puzzle = nakedSingleStep(puzzle, i, j)
    return puzzle


def naked_double(puzzle):
    puzzle = [list(puzzle[i:i + 9]) for i in range(0, 81, 9)]
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == '0':
                peers = get_peers(i, j)
                peers_with_values = [puzzle[x][y] for x, y in peers if puzzle[x][y] != 0]
                if len(peers_with_values) == 2 and len(set(peers_with_values)) == 2:
                    for x, y in peers:
                        if puzzle[x][y] == 0:
                            puzzle[x][y] = list(set(peers_with_values))[0]
    return ''.join([''.join(row) for row in puzzle])


def naked_triple(puzzle):
    puzzle = [list(puzzle[i:i + 9]) for i in range(0, 81, 9)]
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == '0':
                peers = get_peers(i, j)
                peers_with_values = [puzzle[x][y] for x, y in peers if puzzle[x][y] != 0]
                if len(peers_with_values) == 3 and len(set(peers_with_values)) == 3:
                    for x, y in peers:
                        if puzzle[x][y] == 0:
                            puzzle[x][y] = list(set(peers_with_values))[0]
    return ''.join([''.join(row) for row in puzzle])


def naked_quadruple(puzzle):
    puzzle = [list(puzzle[i:i + 9]) for i in range(0, 81, 9)]
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == '0':
                peers = get_peers(i, j)
                peers_with_values = [puzzle[x][y] for x, y in peers if puzzle[x][y] != '0']
                if len(peers_with_values) == 4 and len(set(peers_with_values)) == 4:
                    for x, y in peers:
                        if puzzle[x][y] == 0:
                            puzzle[x][y] = list(set(peers_with_values))[0]
    return ''.join([''.join(row) for row in puzzle])


def naked_solve(puzzle):
    hasStepped = True
    # while hasStepped:
    #     print('quad step')
    #     solution = naked_quadruple(puzzle)
    #     if solution == puzzle:
    #         hasStepped = False
    #     puzzle = solution
    # print('After Quad:\t\t', puzzle)
    # hasStepped = True
    # while hasStepped:
    #     print('tripple step')
    #     solution = naked_triple(puzzle)
    #     if solution == puzzle:
    #         hasStepped = False
    #     puzzle = solution
    # print('After Tripple:\t', puzzle)
    # hasStepped = True
    # while hasStepped:
    #     print('double step')
    #     solution = naked_double(puzzle)
    #     if solution == puzzle:
    #         hasStepped = False
    #     puzzle = solution
    # print('After Double:\t', puzzle)
    # hasStepped = True
    while hasStepped:
        # print('single step')
        solution = naked_single(puzzle)
        if solution == puzzle:
            hasStepped = False
        puzzle = solution
    # print('After Single:\t', puzzle)
    # print('Adding a brute')
    # puzzle = bruteForce(puzzle)
    return puzzle
