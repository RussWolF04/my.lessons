#задание№3
print('задание№3')

q=int(input('число манет:'))
d=q//25
d1=q-25*d
c=d1//10
c1=d1-10*c
b=c1//5
b1=c1-5*b
a=b1//1
a1=b1-1*4
schet=d+c+b+a
print(f'общее кол-во манет {schet}шт.\nкол-во по 25|{d}шт.\nкол-во по 10|{c}шт.\nкол-во по 5|{b}шт.\nкол-во по 1|{a}шт. ')


n = int(input())