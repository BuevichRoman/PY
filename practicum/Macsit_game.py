from random import shuffle

numers = [1, 2, 3]
letter = ["a", "b", "c"]
my_dict = {j: numers[i] for i, j in enumerate(letter)}

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(nums)


def draw_field():
    print("", nums[0], "|", nums[1], "|", nums[2], "|", " 1\n",
          nums[3], "|", nums[4], "|", nums[5], "|", " 2\n",
          nums[6], "|", nums[7], "|", nums[8], "|", " 3")
    print(" 1", "  2", "  3")


def game():
    draw_field()
    cnt1 = 0
    cnt2 = 0
    count = 1
    while count != 10:
        number = int(input("выбери номер клетки:"))
        if count % 2 != 0:
            cnt1 += nums[number - 1]
            nums[number - 1] = 0
        else:
            cnt2 += nums[number - 1]
            nums[number - 1] = 0
        print(f"счет игрока 1: {cnt1}, счет игрока 2: {cnt2}")
        count += 1
        draw_field()
        if count % 2 != 0:
            if number == 1 or number == 4 or number == 7:
                print("выбирай клетку из 1 столбца")
            if number == 2 or number == 5 or number == 8:
                print("выбирай клетку из 2 столбца")
            if number == 3 or number == 6 or number == 9:
                print("выбирай клетку из 3 столбца")
        if count % 2 == 0:
            if number == 1 or number == 2 or number == 3:
                print("выбирай клетку из 1 строки")
            if number == 4 or number == 5 or number == 6:
                print("выбирай клетку из 2 строки")
            if number == 7 or number == 8 or number == 9:
                print("выбирай клетку из 3 строки")
    if cnt1 > cnt2:
        print("победил игрок 1")
    if cnt2 > cnt1:
        print("победил игрок 2")
    if cnt1 == cnt2:
        print("ничья")


game()
