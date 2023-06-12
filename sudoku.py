import numpy as np

# EASY (https://www.rd.com/list/printable-sudoku-puzzles/)
easy = np.zeros((9,9), dtype=int)
easy[0, :] = [0, 0, 4, 0, 5, 0, 0, 0, 0] 
easy[1, :] = [9, 0, 0, 7, 3, 4, 6, 0, 0] 
easy[2, :] = [0, 0, 3, 0, 2, 1, 0, 4, 9] 
easy[3, :] = [0, 3, 5, 0, 9, 0, 4, 8, 0] 
easy[4, :] = [0, 9, 0, 0, 0, 0, 0, 3, 0] 
easy[5, :] = [0, 7, 6, 0, 1, 0, 9, 2, 0] 
easy[6, :] = [3, 1, 0, 9, 7, 0, 2, 0, 0] 
easy[7, :] = [0, 0, 9, 1, 8, 2, 0, 0, 3] 
easy[8, :] = [0, 0, 0, 0, 6, 0, 1, 0, 0] 

# MEDIUM (https://www.rd.com/list/printable-sudoku-puzzles/)
medium = np.zeros((9,9), dtype=int)
medium[0, :] = [2, 0, 0, 0, 0, 0, 6, 9, 0] 
medium[1, :] = [0, 5, 0, 0, 0, 3, 0, 0, 0] 
medium[2, :] = [1, 7, 0, 0, 0, 9, 4, 0, 5] 
medium[3, :] = [0, 0, 3, 0, 2, 5, 0, 1, 8] 
medium[4, :] = [0, 0, 0, 0, 4, 0, 0, 0, 0] 
medium[5, :] = [7, 2, 0, 3, 8, 0, 5, 0, 0]  
medium[6, :] = [5, 0, 2, 6, 0, 0, 0, 4, 1] 
medium[7, :] = [0, 0, 0, 5, 0, 0, 0, 7, 0] 
medium[8, :] = [0, 6, 7, 0, 0, 0, 0, 0, 3] 


# HARD (https://www.rd.com/list/printable-sudoku-puzzles/)
hard = np.zeros((9,9), dtype=int)
hard[0, :] = [0, 9, 1, 0, 7, 0, 0, 0, 0] 
hard[1, :] = [2, 0, 3, 0, 0, 0, 0, 5, 0] 
hard[2, :] = [0, 0, 0, 4, 0, 2, 9, 0, 7] 
hard[3, :] = [0, 0, 2, 8, 0, 6, 0, 0, 9] 
hard[4, :] = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
hard[5, :] = [9, 0, 0, 1, 0, 4, 6, 0, 0]  
hard[6, :] = [1, 0, 5, 2, 0, 7, 0, 0, 0] 
hard[7, :] = [0, 8, 0, 0, 0, 0, 5, 0, 1] 
hard[8, :] = [0, 0, 0, 0, 1, 0, 7, 6, 0]

# EXTRA_HARD (https://www.rd.com/list/printable-sudoku-puzzles/)
extra_hard = np.zeros((9,9), dtype=int)
extra_hard[0, :] = [3, 5, 7, 0, 0, 8, 0, 0, 0] 
extra_hard[1, :] = [0, 4, 0, 0, 5, 0, 0, 0, 0] 
extra_hard[2, :] = [0, 0, 1, 7, 0, 0, 0, 0, 0] 
extra_hard[3, :] = [0, 9, 0, 0, 0, 6, 0, 2, 4] 
extra_hard[4, :] = [0, 0, 0, 0, 9, 0, 0, 0, 0] 
extra_hard[5, :] = [2, 1, 0, 3, 0, 0, 0, 5, 0] 
extra_hard[6, :] = [0, 0, 0, 0, 0, 3, 7, 0, 0] 
extra_hard[7, :] = [0, 0, 0, 0, 2, 0, 0, 8, 0] 
extra_hard[8, :] = [0, 0, 0, 9, 0, 0, 6, 1, 5] 

# WORLD_HARDEST (https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku)
world_hardest = np.zeros((9,9), dtype=int)
world_hardest[0, :] = [8, 0, 0, 0, 0, 0, 0, 0, 0] 
world_hardest[1, :] = [0, 0, 3, 6, 0, 0, 0, 0, 0] 
world_hardest[2, :] = [0, 7, 0, 0, 9, 0, 2, 0, 0] 
world_hardest[3, :] = [0, 5, 0, 0, 0, 7, 0, 0, 0] 
world_hardest[4, :] = [0, 0, 0, 0, 4, 5, 7, 0, 0] 
world_hardest[5, :] = [0, 0, 0, 1, 0, 0, 0, 3, 0]  
world_hardest[6, :] = [0, 0, 1, 0, 0, 0, 0, 6, 8] 
world_hardest[7, :] = [0, 0, 8, 5, 0, 0, 0, 1, 0] 
world_hardest[8, :] = [0, 9, 0, 0, 0, 0, 4, 0, 0] 
