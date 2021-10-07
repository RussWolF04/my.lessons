import random

a = [random.randint(1, 40) for i in range(20)]
b = [random.randint(1, 40) for i in range(20)]
if sum(a) > sum(b) and sum(a) != sum(b):
    print(f'Сумма Картежа "а" - {sum(a)} > Суммы Картежа "b" - {sum(b)}')
elif sum(a) < sum(b) and sum(a) != sum(b):
    print(f'Сумма Картежа "а" - {sum(a)} < Суммы Картежа "b" - {sum(b)}')
else:
    print(f'Каржи равны')

print(f'Tuple "a" = {a}\nTuple "b" = {b}')
print(f'Сумма Картежа "а" = {sum(a)}')
print(f'Сумма картежа "b" = {sum(b)}')
print(f'Minimum "a" = {a.index(min(a))}  Maximum "a" = {a.index(max(a))}')
print(f'Minimum "b" = {b.index(min(b))}  Maximum "b" = {b.index(max(b))}')
print(f'Общее произведение Картежа "а" и "b" = {sum(a) * sum(b)}')