from num2words import *
from math import sqrt

number_dict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
               'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
               'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
               'двадцать': 20, 'двадцать один': 21, 'двадцать два': 22, 'двадцать три': 23, 'двадцать четыре': 24,
               'двадцать пять': 25, 'двадцать шесть': 26, 'двадцать семь': 27, 'двадцать восемь': 28,
               'двадцать девять': 29, 'тридцать': 30, 'тридцать один': 31, 'тридцать два': 32, 'тридцать три': 33,
               'тридцать четыре': 34, 'тридцать пять': 35, 'тридцать шесть': 36, 'тридцать семь': 37,
               'тридцать восемь': 38, 'тридцать девять': 39, 'сорок': 40, 'сорок один': 41, 'сорок два': 42,
               'сорок три': 43, 'сорок четыре': 44, 'сорок пять': 45, 'сорок шесть': 46, 'сорок семь': 47,
               'сорок восемь': 48, 'сорок девять': 49, 'пятьдесят': 50, 'пятьдесят один': 51, 'пятьдесят два': 52,
               'пятьдесят три': 53, 'пятьдесят четыре': 54, 'пятьдесят пять': 55, 'пятьдесят шесть': 56,
               'пятьдесят семь': 57, 'пятьдесят восемь': 58, 'пятьдесят девять': 59, 'шестьдесят': 60,
               'шестьдесят один': 61, 'шестьдесят два': 62, 'шестьдесят три': 63, 'шестьдесят четыре': 64,
               'шестьдесят пять': 65, 'шестьдесят шесть': 66, 'шестьдесят семь': 67, 'шестьдесят восемь': 68,
               'шестьдесят девять': 69, 'семьдесят': 70, 'семьдесят один': 71, 'семьдесят два': 72, 'семьдесят три': 73,
               'семьдесят четыре': 74, 'семьдесят пять': 75, 'семьдесят шесть': 76, 'семьдесят семь': 77,
               'семьдесят восемь': 78, 'семьдесят девять': 79, 'восемьдесят': 80, 'восемьдесят один': 81,
               'восемьдесят два': 82, 'восемьдесят три': 83, 'восемьдесят четыре': 84, 'восемьдесят пять': 85,
               'восемьдесят шесть': 86, 'восемьдесят семь': 87, 'восемьдесят восемь': 88, 'восемьдесят девять': 89,
               'девяносто': 90, 'девяносто один': 91, 'девяносто два': 92, 'девяносто три': 93, 'девяносто четыре': 94,
               'девяносто пять': 95, 'девяносто шесть': 96, 'девяносто семь': 97, 'девяносто восемь': 98,
               'девяносто девять': 99, 'сто': 100}


def calculator():
    calc = input("какое действие вы хотите выполнить(узнать операции введите ?)  ")

    if calc == "?":
        print(
            "умножение, деление с остатком, сложение, вычитание, выход, деление без остатка,"
            " остаток, корень, квадрат, куб")
        print()
        calculator()

    elif calc == "умножение":
        b = (input("введите первое число  "))
        c = (input("введите второе число  "))
        number1 = 0
        number2 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        for key, value in number_dict.items():
            if c == key:
                number2 = value
        res = number1 * number2
        print(num2words(res, lang="ru"))
        print()
        calculator()

    elif calc == "деление с остатком":
        b = (input("введите первое число  "))
        c = (input("введите второе число  "))
        number1 = 0
        number2 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        for key, value in number_dict.items():
            if c == key:
                number2 = value
        res = number1 / number2
        print(num2words(round(res, 2), lang="ru"))
        print()
        calculator()

    elif calc == "остаток":
        b = (input("введите первое число  "))
        c = (input("введите второе число  "))
        number1 = 0
        number2 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        for key, value in number_dict.items():
            if c == key:
                number2 = value
        res = number1 % number2
        print(num2words(round(res, 2), lang="ru"))
        print()
        calculator()

    elif calc == "деление без остатка":
        b = (input("введите первое число  "))
        c = (input("введите второе число  "))
        number1 = 0
        number2 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        for key, value in number_dict.items():
            if c == key:
                number2 = value
        res = number1 // number2
        print(num2words(res, lang="ru"))
        print()
        calculator()

    elif calc == "сложение":
        b = (input("введите первое число  "))
        c = (input("введите второе число  "))
        number1 = 0
        number2 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        for key, value in number_dict.items():
            if c == key:
                number2 = value
        res = number1 + number2
        print(num2words(res, lang="ru"))
        print()
        calculator()

    elif calc == "вычитание":
        b = (input("введите первое число  "))
        c = (input("введите второе число  "))
        number1 = 0
        number2 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        for key, value in number_dict.items():
            if c == key:
                number2 = value
        res = number1 - number2
        print(num2words(res, lang="ru"))
        print()
        calculator()

    elif calc == "корень":
        b = (input("введите  число  "))
        number1 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        res = sqrt(number1)
        print(num2words(round(res, 2), lang="ru"))
        print()
        calculator()

    elif calc == "квадрат":
        b = (input("введите  число  "))
        number1 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        res = number1 ** 2
        print(num2words(res, lang="ru"))
        print()
        calculator()

    elif calc == "куб":
        b = (input("введите  число  "))
        number1 = 0
        for key, value in number_dict.items():
            if b == key:
                number1 = value
        res = number1 ** 3
        print(num2words(res, lang="ru"))
        print()
        calculator()

    elif calc == "выход":
        exit()

    else:
        print("нормально вводи, не знаешь что вводить, напиши ,?,   !!!!!!!!!!!")
        print()
        calculator()


print()
calculator()
