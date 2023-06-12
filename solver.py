from tools import board_print, compatibility
import sudoku
import time

## CHOOSE THE SUDOKU YOU WANT TO RESOLVE ##
sudoku = sudoku.extra_hard
## ------------------------------------- ##

# SOLVE
start = time.time()

zeros_position = []
for i in range(9):
    for j in range(9):
        if sudoku[i, j] == 0 :
            zeros_position.append((i, j))

x = 0
z = 0

while 0 in sudoku:
    i = zeros_position[x][0]
    j = zeros_position[x][1]

    for k in range(sudoku[i, j]+1, 11):
        if k == 10 : # Pas de chiffres valide trouvé on revient un en arrière
            sudoku[i, j] = 0
            x -= 1
            break
        elif compatibility(i, j, k, sudoku): # Chiffres valide trouvé k
            sudoku[i, j] = k
            x += 1
            break

    z += 1

board_print(sudoku)
print(f"Elapsed time : {time.time()-start} seconds\nIteration : {z}")

