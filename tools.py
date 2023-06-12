import numpy as np

## board_print copied from : https://medium.com/codex/building-a-simple-sudoku-solver-in-python-with-numpy-1a8ea6f5bff5
def board_print(board):
    """
    Prints 9x9 numpy array input board in an easier to read format.
    """
    
    # Some basic checks
    assert board.shape == (9, 9)
    assert type(board) == np.ndarray
    
    # Convert array elements to strings
    board_str = board.astype(str)
    
    # Our row separator
    row_sep = '-'*25

    # Loop through 9 rows
    for i in range(9):
        
        # At each multiple of 3, print row separator
        if i % 3 == 0:
            print(row_sep)

        # Get row data
        row = board_str[i]

        # Format row of data with pipe separators at each end, and between each sub grid
        print('| '+' '.join(row[0:3])+' | '+' '.join(row[3:6])+' | '+' '.join(row[6:])+' |')

    # Print final row separator at bottom after loops finish
    print(row_sep)

def find_square(i, j, sudoku):
    return sudoku[(i-i%3):(i-i%3)+3, (j-j%3):((j-j%3)+3)]

def find_line(i, j, sudoku):
    return sudoku[i, :]

def find_column(i, j, sudoku):
    return sudoku[:, j]

def compatibility(i, j, value, sudoku):
    square = find_square(i, j, sudoku).flatten()
    line = find_line(i, j, sudoku)
    column = find_column(i, j, sudoku)

    total = np.concatenate((square, line))
    total = np.concatenate((total, column))
    total = np.setdiff1d(total, [0])
    total = np.unique(total)

    if value in total:
        return False
    return True