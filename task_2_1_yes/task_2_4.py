# № 4.
# Ввести число, проверить на то что было ведено именно число. Везвести его в куб
# Проверять будем с помощью функции type()

a = int(input("Введите число: "))
if type(a) == int: # делаем проверку на то что int является числом
    print(a ** 3)
else:
    print('Вы ввели не число!')