# a = [1, -1, 2, 3, 5, -8, 13, 21, -34, 56, 89]
# # for i in a:
# #     i < 0
# #     i += 2
# #     print(i)
# import datetime

# print(60 * 60 * 24 * 7)
# print(2 ** 18)
# print(829 % 72)
# a = float(input("Enter float: "))
# b = float(input("Enter float: "))
# c = a + b
# print(c)

# a = 10
# b = 14
# c = 23
# d = 2
# s = (a + b + c + d) / 4
# print(s)

# rub = float(input("Enter rub: "))
# usd = rub / 78
# eur = rub / 98
# print(f'{rub} rub = {round(usd, 2)} dollars\n{rub}rub = {round(eur, 2)} euro\n')

# tickets = int(input('Enter tickets: '))
# popcorns = int(input('Enter popcorn: '))
# ticket_1 = 10
# popcorn_1 = 5
# sum_tickets = tickets * ticket_1
# sum_popcorns = popcorns * popcorns
# print(f'Билеты {tickets} = {sum_tickets}\nПопкор {popcorns} = {sum_popcorns}\nк оплате {sum_tickets + sum_popcorns} рублей')

# taxi = [2, 3, 4, 5]
# for i in taxi:
#     i <= 2
#     i >= 5
#     print(i * 5)

s = input("Введите строку:")
count_gl = 0
count_sg = 0
gl = set("ёуеыаоэяию")
sg = set("йцкнгшщзхъфвпрлджчсмтьб")
for i in s:
    if i in gl:
        count_gl += 1
    elif i in sg:
        count_sg += 1
print("Количество гласных равно:")
print(count_gl)
print('Количество согласных ровно:')
print(count_sg)
