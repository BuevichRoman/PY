from random import randint


def number():
    return randint(1000, 9999)


def bull(q_num, a_num):
    cnt_b = 0
    start = 1000
    for i in range(4):
        if (a_num // start % 10) == (q_num // start % 10):
            cnt_b += 1
        start //= 10
    return cnt_b


def cow(q_num, a_num):
    cnt_c = 0
    for i in range(0, 4):
        if str(a_num)[i] in str(q_num) and str(a_num)[i] != str(q_num)[i]:
            cnt_c += 1
    return cnt_c


game = True
num = number()
while game:
    print("your number?", end=" ")
    digit = int(input())
    bul = bull(digit, num)
    coww = cow(digit, num)
    if digit == num:
        print("you win!!!")
        game = False
        break
    print(f"cow = {coww}, bul = {bul}")
