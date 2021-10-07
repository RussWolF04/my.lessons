# Калькулятор
a = float(input("Введите число: "))
c = input('Выбирите "/", "*", "+", "-": ')
b = float(input("Введите число: "))
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b == 0: # Исключаем деление на "0"
        print("Ошибка, на 0 делить нельзя!!!")
    print(a / b)