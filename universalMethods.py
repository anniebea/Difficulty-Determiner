def find_empty_cell(puzzle):
    """
    Finds first empty cell in puzzle string
    :param puzzle: Sudoku puzzle string
    :return: Either return position of empty cell or return None
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == '0':
                return row, col
    return None


def is_valid(puzzle, num, row, col):
    for x in range(9):
        if puzzle[row][x] == num or puzzle[x][col] == num:
            return False
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(3):
        for c in range(3):
            if puzzle[start_row + r][start_col + c] == num:
                return False
    return True


def count_givens(puzzle):
    givenCount = 0
    for cell in puzzle:
        if cell != '0':
            givenCount += 1
    return givenCount
