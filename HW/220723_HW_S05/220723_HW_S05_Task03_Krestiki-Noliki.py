# Создайте программу для игры в ""Крестики-нолики"".


def printField(pf):
    s = ""
    for x in range(0, len(pf)):
        s += "\n\n\n"
        for y in range(len(pf[x])):
            if pf[x][y] == 0:
                s += "-\t"
            elif pf[x][y] == 1:
                s += "X\t"
            else:
                s += "O\t"
    print(s + "\n")

def scoring(pf):
    sum_diagonal_1 = 0
    sum_diagonal_2 = 0
    score = 0
    for x in range(0, len(pf)): 
        sum_row = 0
        sum_column = 0
        for y in range(0, len(pf[x])):
            sum_row += pf[x][y]
            sum_column += pf[y][x]
            if x == y:
                sum_diagonal_1 += pf[x][y]
            if len(pf) - 1 - x == y:
                sum_diagonal_2 += pf[x][y]    
        if abs(score) < abs(sum_row): score = sum_row
        if abs(score) < abs(sum_column): score = sum_column
    if abs(score) < abs(sum_diagonal_1): score = sum_diagonal_1
    if abs(score) < abs(sum_diagonal_2): score = sum_diagonal_2
    return score

def play(pf):
    move = 9
    player = -1
    while move > 0:
        if player == -1:
            player = 1
        else:
            player = -1
        x = int(input((f"{'X' if player == 1 else 'O'}, задайте кооодинаты \n \t Строка (сверху) = "))) - 1
        y = int(input(f"\t столбец (слева) = ")) - 1
        pf[x][y] = player
        printField(pf)
        if abs(scoring(pf)) == 3:
            print(f"Игрок {'X' if player == 1 else 'O'} выиграл!")
            break
        move -= 1
    if abs(scoring(pf)) < 3: print(f'Ничья.')    


pf = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # play field
printField(pf)
play(pf)