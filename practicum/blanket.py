sp = [[" " for j in range(4)] for i in range(5)]
my_dict = {1: "*", 2: "&", 3: "@"}
score_dict = {1: 0, 2: 0, 3: 0}


def draw_field():
    cnt = 0
    print("  1    2    3    4 ")
    for i in sp:
        cnt += 1
        print("-" * 20)
        for j in i:
            print(f"  {j} ", end="|")
        print(" ", cnt)
    print("-" * 20,
          f"\tСчет штрафов 1 игрока : {score_dict[1]}\t Счет штрафов 2 игрока : {score_dict[2]}\t Счет штрафов 3 игрока: {score_dict[3]}")


def make_step(line, row, sign):
    sp[line][row] = my_dict[sign]
    check_win(line, row, sign)


def finish_game():
    for i in sp:
        if " " in i:
            return True
    return False


def make_game():
    while finish_game():
        draw_field()
        x = int(input("введите ккординату строки")) - 1
        y = int(input("введите координату столбца")) - 1
        player = int(input("введите ваш номмер игрока"))
        if sp[x][y] == " ":
            make_step(x, y, player)
        else:
            print()
        finish_game()
        you_win()


def check_win(line, row, player):
    minimal_line = line
    maximal_line = line
    maximal_row = row
    minimal_row = row
    if line > 0:
        minimal_line = line - 1
    if line < 3:
        maximal_line = line + 1
    if row > 0:
        minimal_row = row - 1
    if row < 4:
        maximal_row = row + 1
    for i in range(minimal_line, maximal_line + 1):
        for j in range(minimal_row, maximal_row):
            if (sp[i][j] != "") and (sp[i][j] == sp[line][row]) and (i != line or j != row):
                score_dict[player] += 1


def you_win():
    if score_dict[1] < score_dict[2] and score_dict[1] < score_dict[3]:
        print("выйграл игрок 1")
    if score_dict[2] < score_dict[1] and score_dict[2] < score_dict[3]:
        print("выйграл игрок 2")
    if score_dict[3] < score_dict[2] and score_dict[3] < score_dict[1]:
        print("выйграл игрок 1")


make_game()
