import random as ran

def battlefield():
    rows = 10
    col = 10
    matrix=[]
    row = 0
    while row < rows:
        new_row = [0] * col
        matrix.append(new_row)
        row += 1
    for row in matrix:
        print(row)
    




battlefield()