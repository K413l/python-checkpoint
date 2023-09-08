import random as rand

def battlefield():
    qt_bomb = int(input("Quantas bombas?")) 
    rows = 11
    col = 11
    matrix=[]
    row = 0
    i = 0
    while row < rows:
        new_row = [0] * col
        matrix.append(new_row)
        row += 1
   
    matrix[0][0]= str(' X')
    matrix[0][1]= str(' A')
    matrix[0][2]= str(' B')
    matrix[0][3]= str(' C')
    matrix[0][4]= str(' D')
    matrix[0][5]= str(' E')
    matrix[0][6]= str(' F')
    matrix[0][7]= str(' G')
    matrix[0][8]= str(' H')
    matrix[0][9]= str(' I')
    matrix[0][10]= str(' J')
    matrix[1][0]= str(' 1')
    matrix[2][0]= str(' 2')
    matrix[3][0]= str(' 3')
    matrix[4][0]= str(' 4')
    matrix[5][0]= str(' 5')
    matrix[6][0]= str(' 6')
    matrix[7][0]= str(' 7')
    matrix[8][0]= str(' 8')
    matrix[9][0]= str(' 9')
    matrix[10][0]= str('10')
    
    rows = len(matrix)
    cols = len(matrix[0])

    while i < qt_bomb:
        i += 1
        random_row = rand.randint(1, rows - 1)
        random_col = rand.randint(1, cols - 1)

        matrix[random_row][random_col] = -1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                if i - 1 >= 0 and matrix[i - 1][j] != -1:
                    matrix[i - 1][j] += 1
                if i + 1 < rows and matrix[i + 1][j] != -1:
                    matrix[i + 1][j] += 1
                if j - 1 >= 0 and matrix[i][j - 1] != -1:
                    matrix[i][j - 1] += 1
                if j + 1 < cols and matrix[i][j + 1] != -1:
                    matrix[i][j + 1] += 1

    
    for row in matrix:
        print(row)


