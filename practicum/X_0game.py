field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

5
def draw_field():
    for i in range(3):
        print("|", field[i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")


def win():
    for each in wins:
        if (field[each[0] - 1]) == (field[each[1] - 1]) == (field[each[2] - 1]):
            return field[each[1] - 1]
    else:
        return False


def shoot(player):
    while True:
        value = input("your number " + player + " ?")
        value = int(value)
        if str(field[value - 1]) in "X0":
            print("занято")
            continue
        field[value - 1] = player
        break


def main():
    cnt = 0
    while True:
        draw_field()
        if cnt % 2 == 0:
            shoot("x")
        else:
            shoot("0")
        if cnt > 3:
            winner = win()
            if winner:
                draw_field()
                print(winner, "you win")
                break
        cnt += 1
        if cnt > 8:
            print("no one")
            break


main()
