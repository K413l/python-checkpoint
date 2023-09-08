import random

def criar_tabuleiro(linhas, colunas, num_minas):
    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    posicoes_minas = random.sample(range(linhas * colunas), num_minas)

    for posicao in posicoes_minas:
        linha = posicao // colunas
        coluna = posicao % colunas
        tabuleiro[linha][coluna] = '*'

    return tabuleiro

def mostrar_tabuleiro(tabuleiro, reveladas):
    for i in range(len(tabuleiro)):
        linha_mostrada = []
        for j in range(len(tabuleiro[i])):
            if reveladas[i][j]:
                linha_mostrada.append(tabuleiro[i][j])
            else:
                linha_mostrada.append(' ')
        print(" ".join(linha_mostrada))
    print()

def contar_minas_adjacentes(tabuleiro, linha, coluna):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    contador = 0

    for dl, dc in direcoes:
        l, c = linha + dl, coluna + dc
        if 0 <= l < linhas and 0 <= c < colunas and tabuleiro[l][c] == '*':
            contador += 1

    return contador

def revelar_casa(tabuleiro, reveladas, linha, coluna):
    if reveladas[linha][coluna] or tabuleiro[linha][coluna] == '*':
        return

    reveladas[linha][coluna] = True
    if tabuleiro[linha][coluna] == ' ':
        for dl in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                l, c = linha + dl, coluna + dc
                if 0 <= l < len(tabuleiro) and 0 <= c < len(tabuleiro[0]):
                    revelar_casa(tabuleiro, reveladas, l, c)

def jogar_jogo(linhas, colunas, num_minas):
    tabuleiro = criar_tabuleiro(linhas, colunas, num_minas)
    reveladas = [[False for _ in range(colunas)] for _ in range(linhas)]
    jogo_acabou = False

    while not jogo_acabou:
        mostrar_tabuleiro(tabuleiro, reveladas)
        linha = int(input(f"Digite a linha (0 a {linhas - 1}): "))
        coluna = int(input(f"Digite a coluna (0 a {colunas - 1}): "))

        if tabuleiro[linha][coluna] == '*':
            print("Fim de Jogo! Você acertou uma mina!")
            jogo_acabou = True
        else:
            contador = contar_minas_adjacentes(tabuleiro, linha, coluna)
            reveladas[linha][coluna] = True
            if contador == 0:
                revelar_casa(tabuleiro, reveladas, linha, coluna)

        if all(reveladas[i][j] or tabuleiro[i][j] == '*' for i in range(linhas) for j in range(colunas)):
            print("Parabéns! Você ganhou!")
            jogo_acabou = True

if __name__ == "__main__":
    linhas = 10
    colunas = 10
    num_minas = 20
    jogar_jogo(linhas, colunas, num_minas)
