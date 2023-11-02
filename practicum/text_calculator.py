def calculator():
    calc = input("какое действие вы хотите выполнить(узнать операции ,?,)  ")

    if calc == "?":
        print("множение(*), деление(/), сложение(+), вычитание(-), выход(exit)")
        print()
        calculator()

    elif calc == "*":
        number1 = int(input("введите первое число  "))
        number2 = int(input("введите второе число  "))
        print(number1 * number2)
        print()
        calculator()

    elif calc == "/":
        number1 = int(input("введите первое число  "))
        number2 = int(input("введите второе число  "))
        print(number1 / number2)
        print()
        calculator()

    elif calc == "+":
        number1 = int(input("введите первое число  "))
        number2 = int(input("введите второе число  "))
        print(number1 + number2)
        print()
        calculator()

    elif calc == "-":
        number1 = int(input("введите первое число  "))
        number2 = int(input("введите второе число  "))
        print(number1 - number2)
        print()
        calculator()

    elif calc == "exit":
        exit()

    else:
        print("нормально вводи, не знаешь что вводить, напиши ,?,   !!!!!!!!!!!")
        print()
        calculator()


print()
calculator()
