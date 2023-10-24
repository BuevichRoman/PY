sp = [[" " for i in range(10)] for j in range(10)]
my_dict = {1: "*", 2: "&"}
score = 0


def draw_field():
    cnt = 0
    print("  1    2    3    4    5    6    7    8    9    10")
    for i in sp:
        cnt += 1
        print("-" * 50)
        for j in i:
            print(f"  {j} ", end="|")
        print(" ", cnt)
    print("-" * 50,
          f"\t длинна самой большой цепочки: {score}")


def make_step(line, row, player):
    sp[line][row] = my_dict[player]
    check(line, row)


def finish():
    global score
    for i in sp:
        if " " not in i:
            return False
        if score == 3:
            return False
        return True


def game():
    global score
    while finish():
        draw_field()
        x = int(input("введите ккординату строки")) - 1
        y = int(input("введите координату столбца")) - 1
        player = int(input("введите ваш номер игрока"))
        if sp[x][y] == " ":
            make_step(x, y, player)
        else:
            print()
        finish()
        you_win(x, y, player)


def check(line, row):
    global score
    cnt1 = 1
    cnt2 = 1
    cnt3 = 1
    cnt4 = 1
    if (sp[line][row] != " " and sp[line][row - 1] != " ") or (sp[line][row] != " " and sp[line][row + 1] != " "):
        cnt1 += 1
    if (sp[line][row] != " " and sp[line + 1][row] != " ") or (sp[line][row] != " " and sp[line - 1][row] != " "):
        cnt2 += 1
    if (sp[line][row] != " " and sp[line + 1][row - 1] != " ") or (sp[line][row] != " " and sp[line - 1][row + 1] != " "):
        cnt3 += 1
    if (sp[line][row] != " " and sp[line + 1][row + 1] != " ") or (sp[line][row] != " " and sp[line - 1][row - 1] != " "):
        cnt4 += 1
    if ((sp[line][row] != " " and sp[line][row - 1] != " " and sp[line][row + 1] != " ") or
            (sp[line][row] != " " and sp[line][row - 1] != " " and sp[line][row - 2] != " ") or
             (sp[line][row] != " " and sp[line][row + 1] != " " and sp[line][row + 2] != " ")):
        score = 3
    if ((sp[line][row] != " " and sp[line + 1][row] != " " and sp[line - 1][row] != " ") or
            (sp[line][row] != " " and (sp[line + 1][row] != " " and sp[line + 2][row] != " ") or
             (sp[line][row]) != " " and sp[line - 1][row] != " " and sp[line - 2][row] != " ")):
        score = 3
    if ((sp[line][row] != " " and sp[line + 1][row - 1] != " " and sp[line - 1][row + 1] != " ") or
            (sp[line][row] != " " and sp[line + 1][row - 1] != " " and sp[line + 2][row - 2] != " ") or
            (sp[line][row] != " " and sp[line - 1][row + 1] != " " and sp[line - 2][row + 2] != " ")):
        score = 3
    if ((sp[line][row] != " " and sp[line - 1][row - 1] != " " and sp[line + 1][row + 1] != " ") or
            (sp[line][row] != " " and sp[line - 1][row - 1] != " " and sp[line - 2][row - 2] != " ") or
            (sp[line][row] != " " and sp[line + 1][row + 1] != " " and sp[line + 2][row + 2] != " ")):
        score = 3
    score = max(cnt1, cnt2, cnt3, cnt4, score)


def you_win(line, row, player):
    global score
    if score == 3:
        if sp[line][row] == my_dict[player]:
            print(f"проиграл игрок: {player}")


game()