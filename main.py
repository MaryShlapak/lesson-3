###
# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат
###

try:
    num1 = float(input("Enter 1st number:"))
    num2 = float(input("Enter 2nd number:"))
    user_select = input("Enter the operation:")
    match user_select:
        case "+":
            sum = num1 + num2
            print(f"{num1} + {num2} = {sum}")
        case "-":
            sub = num1 - num2
            print(f"{num1} - {num2} = {sub}")
        case "*":
            mul = num1 * num2
            print(f"{num1} * {num2} = {mul}")
        case "/":
            div = num1 / num2
            print(f"{num1} / {num2} = {div}")
        case _ :
            print("Please, enter correct operation symbol")
except ValueError as error:
    print("Enter only numbers please!")
except ZeroDivisionError as error:
    print(f"ZeroDivisionError occurred: {error}")