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
