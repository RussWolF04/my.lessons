### ПРАКТИКА №_2
"""
                ПРАКТИКА
             Функции строк
1.
Посчитай, сколько денег тебе накаркала ворона, если за 1 кар у
тебя появится мешок денег Вот, как это было «каркаркаркар
каркаркаркаркаркаркаркаркаркар»
2.
Представь, что пользователь маленький ребенок Так вот
программа должна помогать ему исправить ошибки в « малако »,
« каровы » и « харашо »
3.
Пускай компьютер научится считать, больше ли 60(шестидесяти)
символов в тексте То есть это 1 эсэмэска или больше В
результате он должен написать, за сколько эсэмэсок мы платим
"""
# №_1
s = "каркаркаркаркаркаркаркаркаркаркаркаркаркар"
x = len(s)
print(s, + x, + x/3)

# №_2
s = """малако, каровы, харашо"""
s = s.replace("малако", "молоко")
s = s.replace("каровы", "коровы")
s = s.replace("харашо", "хорошо")
print(s)

# №_3
sms = input('Наберите sms: ')
s = len(sms)
#print(s)
if s <= 60:
    print(s, '"1 sms"')
elif s > 60 and s < 90:
    print(s, '"2 sms"')
elif s > 90 and s < 120:
    print(s, '"3 sms"')
else:
    s > 120
    print(s, '"Отправить mms сообщение?"')