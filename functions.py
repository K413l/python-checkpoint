import random as rand



def battlefield():
    
    rows = 11
    col = 11
    row = 0
    i = 0
    matrix = []
    matrixjog = []
    game_over = False
    qt_bomb = int(input("Quantas bombas:"))
    X= 0
    Y= 0
    while row < rows:
        new_row = [0] * col
        matrix.append(new_row)
        row += 1
   
    matrix[0][0]= str(' x')
    matrix[0][1]= str('a')
    matrix[0][2]= str('b')
    matrix[0][3]= str('c')
    matrix[0][4]= str('d')
    matrix[0][5]= str('e')
    matrix[0][6]= str('f')
    matrix[0][7]= str('g')
    matrix[0][8]= str('h')
    matrix[0][9]= str('i')
    matrix[0][10]= str('j')
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
                if i - 1 >= 0 and matrix[i - 1][j] != -1 and type(matrix[i - 1][j]) != str:
                    matrix[i - 1][j] += 1
                if i + 1 < rows and matrix[i + 1][j] != -1 and type(matrix[i + 1][j]) != str:
                    matrix[i + 1][j] += 1
                if j - 1 >= 0 and matrix[i][j - 1] != -1 and type(matrix[i][j - 1]) != str:
                    matrix[i][j - 1] += 1
                if j + 1 < cols and matrix[i][j + 1] != -1 and type(matrix[i][j + 1]) != str:
                    matrix[i][j + 1] += 1

    rows = len(matrix)
    cols = len(matrix[0])

    matrixjog = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0 or matrix[i][j] == -1:
                matrixjog[i][j] = '   '
            else:
                matrixjog[i][j] = '  ' + str(matrix[i][j])

    for row in matrixjog:
        print(row)

    lin = int(input("escolha uma linha"))
    colu = str(input("escolha uma coluna"))
    if colu == "a":
            C = 1
    if colu == "b":
            C = 2
    if colu == "c":
            C = 3
    if colu == "d":
            C = 4
    if colu == "e":
            C = 5
    if colu == "f":
            C = 6
    if colu == "g":
            C = 7
    if colu == "h":
            C = 8
    if colu == "i":
            C = 9
    if colu == "j":
            C = 10
    
   
    while game_over != True:    
        escolha = matrix[lin][C]
        if escolha == -1:
            print("Pisou em uma bomba,vc perdeu o jogo")
            game_over = True
        else:
             print("continue jogando")

    return matrix
    return matrixjog

def mostrarcamp(matrixjog):
     for row in matrixjog:
        print(row)




battlefield()
