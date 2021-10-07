""" № 6
Ввести почтовый адрес. Проверить доменной имя. В
случае если оно gmail.com, вывести на экран имя
почтового ящика. Иначе вывести надпись “
DOMAIN NAME is not supported’
"""
user_mail = input("Введите свой e-mail: ")
if 'gmail.com' in user_mail:
    print(user_mail)
else:
    print("DOMAIN NAME is not supported")
