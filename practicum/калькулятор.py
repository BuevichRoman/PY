def calculation(s):
    c = []
    while len(s) > 1:
        k = None
        if '*' in s:
            k = s.index('*')
            if (k > 0) and k < len(s) - 1:
                c.append(int(s[k - 1]) * int(s[k + 1]))
                del s[k - 1:k + 2]
                s.insert(k - 1, c[-1])
        if '+' in s and ('-' not in s or s.index('+') < s.index('-')):
            k = s.index('+')
            if (k > 0) and k < len(s) - 1:
                c.append(int(s[k - 1]) + int(s[k + 1]))
                del s[k - 1:k + 2]
                s.insert(k - 1, c[-1])
        if '-' in s and ('+' not in s or s.index('-') < s.index('+')):
            k = s.index('-')
            if (k > 0) and k < len(s) - 1:
                try:
                    left_number = int(s[k - 1])
                except ValueError:
                    left_number = 0
                try:
                    right_number = int(s[k + 1])
                except ValueError:
                    right_number = 0
                c.append(left_number - right_number)
                del s[k - 1:k + 2]
                s.insert(k - 1, c[-1])
    return s[0]


def calc(expression):
    numbers = {
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
        'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
        'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
        'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
        'восемьдесят': 80, 'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400,
        'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900,
        'одна тысяча': 1000, 'две тысячи': 2000, 'три тысячи': 3000, 'четыре тысячи': 4000, 'пять тысяч': 5000,
        'шесть тысяч': 6000, 'семь тысяч': 7000, 'восемь тысяч': 8000, 'девять тысяч': 9000,
    }
    operations_dict = {'плюс': '+', 'минус': '-', 'умножить': '*', 'открывается': '(', 'закрывается': ')'}

    if 'умножить на' in expression:
        expression = expression.replace('умножить на', 'умножить')
    if 'скобка открывается' in expression:
        expression = expression.replace('скобка открывается', 'открывается')
    if 'скобка закрывается' in expression:
        expression = expression.replace('скобка закрывается', 'закрывается')
    if 'минус минус' in expression:
        expression = expression.replace('минус минус', 'плюс')
    if 'плюс минус' in expression:
        expression = expression.replace('плюс минус', 'минус')

    expression = expression.split(' ')
    num = []
    i = 0
    while i < len(expression):
        if i < len(expression) - 1 and expression[i] in numbers and expression[i + 1] in numbers:
            two_digit_num = numbers[expression[i]] + numbers[expression[i + 1]]
            num.append(two_digit_num)
            i += 2
        else:
            if expression[i] in numbers:
                num.append(numbers[expression[i]])
            elif expression[i] in operations_dict:
                num.append(operations_dict[expression[i]])
            else:
                print('Ошибка, неверный формат')
            i += 1

    while '(' in num:
        if ')' not in num:
            print('Ошибка, неверный формат')
            break
        elif ')' in num and '(' not in num:
            print('Ошибка, неверный формат')
            break
        else:
            q1 = num.index('(')
            q2 = num.index(')')
            s_new = num[q1 + 1:q2]
            del num[q1:q2 + 1]
            result = calculation(s_new)
            num.insert(q1, result)

    result = calculation(num)
    if isinstance(result, list):  # проверка типа результата
        result = result[0]  # если список, извлекается только элемент

    numi = ''
    reversed_numbers = {v: k for k, v in numbers.items()}
    if result == 0:
        print(reversed_numbers[0])

    if result < 0:
        numi += 'минус '
        result = abs(result)

    thousands = result // 1000
    if thousands > 0:
        numi += reversed_numbers[thousands * 1000] + ' '
        result %= 1000

    hundreds = result // 100
    if hundreds > 0:
        numi += reversed_numbers[hundreds * 100] + ' '
        result %= 100

    if result in reversed_numbers:
        numi += reversed_numbers[result]
    else:
        dozens = result // 10
        if dozens > 0:
            numi += reversed_numbers[dozens * 10] + ' '
            result %= 10
        if result > 0:
            numi += reversed_numbers[result]
    print(numi)


calc('восемнадцать плюс три')  # 21
calc('двадцать один умножить на двадцать плюс шестнадцать')  # 436
calc('восемнадцать минус минус пять')  # 23
calc('сорок шесть плюс минус тридцать четыре')  # 12
calc('скобка открывается пять плюс два скобка закрывается умножить три')  # 21
calc('десять плюс пять умножить на скобка открывается двадцать минус восемнадцать умножить на семнадцать скобка закрывается')  # -1420
calc('восемнадцать минус девятнадцать плюс сорок девять умножить на три')  # 146
calc('скобка открывается пять минус два умножить на шестнадцать скобка закрывается плюс один')  # -26
