# Dataset no https://www.kaggle.com/datasets/rohanrao/sudoku
# Mīklas bez risinājumiem kolonnā 'puzzle'

import pandas as pd
from universalMethods import count_givens
from bruteForce import bruteForce
from nakedTuples import naked_solve

TEST_FILE_1000 = 'sudoku1000.csv'
TEST_FILE_100 = 'sudoku100.csv'


class Cell:
    def __init__(self, ID, number=0):
        self.ID = ID
        self.row = ID / 9
        self.column = ID % 9
        if number != 0:
            self.content = number
            self.isGiven = True
            self.candidates = []
        else:
            self.content = '_'
            self.isGiven = False
            self.candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Board:
    def __init__(self, ID, numString):
        self.ID = ID  # ID from main data file
        self.givenCount = 0
        self.cells = []
        for i, value in enumerate(numString):
            self.cells.append(Cell(i + 1, value))
            if self.cells[i].isGiven:
                self.givenCount += 1

    def getCell(self, ID):
        """Returns a single cell based on ID"""
        for i in self.cells:
            if i.ID == ID:
                return i
        return -1  # should not happen

    def getRow(self, rowNum):
        """Returns an array of cells from the same row"""
        result = []
        for i in self.cells:
            if i.row == rowNum:
                result.append(i)
            if len(result) == 9:
                return result
        return -1  # should not happen

    def getCol(self, colNum):
        result = []
        for i in self.cells:
            if i.column == colNum:
                result.append(i)
            if len(result) == 9:
                return result
        return -1  # should not happen

    def prettyPrint(self):
        print('Puzzle Num:', self.ID)
        for i in range(9):
            print(self.cells[i * 9].content,
                  self.cells[i * 9 + 1].content,
                  self.cells[i * 9 + 2].content, '|',
                  self.cells[i * 9 + 3].content,
                  self.cells[i * 9 + 4].content,
                  self.cells[i * 9 + 5].content, '|',
                  self.cells[i * 9 + 6].content,
                  self.cells[i * 9 + 7].content,
                  self.cells[i * 9 + 8].content)
            if i % 3 == 2 and i != 8:
                print('------+-------+------')


def extractPuzzles(fileName, puzzleCount):
    """Extract random puzzleCount puzzles from a larger csv, place them in file named fileName"""
    inFile = 'sudoku.csv'
    df = pd.read_csv(inFile, delimiter=',', encoding='latin-1')
    allPuzzles = df['puzzle']
    allPuzzles.sample(puzzleCount).to_csv(fileName)


def getPuzzles(fileName):
    """Get all puzzles from a file"""
    df = pd.read_csv(fileName, delimiter=',', encoding='latin-1')
    return df.values.astype('str')


def main():
    # extractPuzzles('sudoku.csv', 100)
    puzzles = getPuzzles(TEST_FILE_100)
    for ID, puzzle in puzzles:
        # board = Board(ID, puzzle)
        # board.prettyPrint()
        print('Given count:\t', count_givens(puzzle))
        print('Before solving:\t', puzzle)
        print('Brute force:\t', bruteForce(puzzle))
        print('Just tuples:\t', naked_solve(puzzle))
        print('')
        # break


if __name__ == '__main__':
    main()
