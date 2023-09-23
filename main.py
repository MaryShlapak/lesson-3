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