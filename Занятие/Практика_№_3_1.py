### ПРАКТИКА №_1

# '+' склеивает текст
'''
1. Представь, что ты известный продюсер и попытайся
   склеить сестер «Джиджи» и «Беллу» Хадид
'''
str = "Джиджи" + "Буллу"
print(str)

# Умножение
'''
2. Умножь «зарплату» в 10 раз
'''
zp = 'зарплата'
print(zp * 10)

# разделитель split()
'''
3. Как картавый человек скажет «тартарары»?
   (по разделителю «р»
'''
s = "тартарары"
r = s.split('р')
print(r)

'''
4.  Преврати « рено » и «внимательность» в «неровность»
'''
s_1 = 'рено'
s_2 = s_1[2::-1]
s_1_1 = s_1[3]
s_1_2 = 'внимательность'
s_2_1 = s_1_2[0]
s_2_2 = s_1_2[9:14]
print(s_2 + s_1_1 + s_2_1 + s_2_2)