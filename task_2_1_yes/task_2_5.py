""""" №_5
Получить на ввод количество рублей и копеек и
вывести в правильной форме, например, 3 рубля, 1
рубль 25 копеек, 3 копейки
"""""
# Получил подсказку от Олега (препода)
# Перепечатаю его код и добавлю сой
# Понял схему. Нужно найти диапозон в котором склонение одинаковое и установить его
"""
хотел создать список с вложенными в него числами по склонениям, но почему то не могу к нему обратиться.
пример kop_1 = [1, 21, 31, 41, 51 ...] если введенное число соответствует имеющемуся в списке то 
вывести на экран соответствующее сообщение столько то рублей, столькото копеек.
"""

rub = int(input("Введите количество рублей: "))
kop = int(input("Введите количество копеек: "))
kop_1 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
kop_2 =[2, 3, 4, 22, 23, 24]
if rub == 1:
    if kop in kop_1:
        print(rub, "рубль", kop, 'копейка')
    elif kop in kop_2: # понял схему!! > 1 и < 5 в этом диапазоне склоняется одинакого
        print(rub, "рубль", kop, 'копейки')
    elif kop == 0 or kop > 4:
        print(rub, 'рубль', kop, 'копеек')
elif rub > 1 and rub < 5:
    if kop == 1:
        print(rub, "рубля", kop, 'копейка')
    elif kop > 1 and kop < 5:
        print(rub, "рубля", kop, 'копейки')
    elif kop == 0 or kop > 4:
        print(rub, 'рубля', kop, 'копеек')
elif rub == 0 or rub > 4:
    if kop == 1:
        print(rub, "рублей", kop, 'копейка')
    elif kop > 1 and kop < 5:
        print(rub, "рублей", kop, 'копейки')
    elif kop == 0 or kop > 4:
        print(rub, 'рублей', kop, 'копеек')