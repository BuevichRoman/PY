from random import randint

nums = [1, 2, 3, 4, 5, 6, 7, 8]
letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
dict = {j: nums[i] for i, j in enumerate(letter)}
win = False


def random_s():
    button = [[randint(0, 2) for j in range(8)] for i in range(8)]
    return button


def draw_bord(button):
    for i in range(8):
        print("-" * 30)
        for j in range(8):
            if button[i][j] == 1:
                print(f" * |", end="")
            else:
                print("   |", end="")
        print(f"{nums[i]}")
    print(*[f" {i} " for i in letter])


def steps(step, button):
    if step.isdigit():
        button[int(step) - 1] = [0] * 8
        return button
    elif step in dict.keys():
        for i in range(len(button)):
            for j in range(len(button[i])):
                button[i][dict[step] - 1] = 0
        return button


def check_win(button):
    global win
    win = True
    for i in button:
        if 1 in i:
            win = False
    return win


bt = random_s()
cnt = 1
while not win:
    draw_bord(bt)
    print(f"игрок {cnt} ваш ход:")
    step = input()
    bt = steps(step, bt)
    if check_win(bt):
        continue
    if cnt == 1:
        cnt = 2
    else:
        cnt = 1
print(f" игрок   {cnt} победил")
