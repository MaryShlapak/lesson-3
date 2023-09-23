###
# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1,
# на екрані напис понеділок, 2 — вівторок тощо.
###


try:
    user_number = int(input("Enter the number of the week day (1-7):"))
    if user_number == 1:
        print("Monday")
    elif user_number == 2:
        print("Tuesday")
    elif user_number == 3:
        print("Wednesday")
    elif user_number == 4:
        print("Thursday")
    elif user_number == 5:
         print("Friday")
    elif user_number == 6:
        print("Saturday")
    elif user_number == 7:
        print("Sunday")
    else:
        print("Incorrect number!")
except ValueError as error:
    print("Enter only integer numbers please!")

###
# 2. Користувач вводить два числа. Визначити, чи рівні ці числа,
# і, якщо ні, вивести їх на екран у порядку зростання
###

try:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))


  if num1 == num2:
      print(f"Numbers are equal: {num1} = {num2}")
  elif num1 > num2:
      print(num2, num1)
  elif num2 > num1:
      print(num1, num2)
  else:
      print("Please,enter numbers only")
except ValueError as error:
    print("Enter only numbers please!")