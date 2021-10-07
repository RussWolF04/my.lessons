print('''
Ведьмак принимает только чеканные монеты
наминалом 25, 10, 5, 1
Узнайте какое количество и наминал Вам нужно 
дать Ведьмаку Геральду!!!
''')
money = int(input('Введите сумму: '))
if money == 0:
    print("Делайте свою грязную работу сами. Я умываю руки!!!")
elif money >= 0:
    money_25 = money // 25
    money_10 = money % 25 // 10
    money_5 = money % 10 // 5
    money_1 = money % 5 // 1
    wedmack = money_25 + money_10 + money_5 + money_1
    print("Всего монет нужно", wedmack)
    print(
        f'Монет_25 - {money_25} шт.\n Монет_10 - {money_10} шт.\n Монет_5 - {money_5} шт.\n Монет_1 - {money_1} шт.\n')
