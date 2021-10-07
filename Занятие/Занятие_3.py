'''
КАК ЕЩЕ РЕЗАТЬ СТРОКИ?
SPLIT
РАЗРЕЗАЕТ ОДНУ СТРОКУ НА НЕСКОЛЬКО ,
ВЫКИДЫВАЯ РАЗДЕЛИТЕЛИ
'''
txt = "welcome to the jungle"
x = txt.split() # пустые () в spit добавляют запятую
print(x)

txt = "hello, my name is Evgeniy, I am 38 years old"
x = txt.split(", ")
print(x)

"""
СИТАКСИС: split(разделитель) 
не напишешь разделитель - порежет по пробелам
"""

txt = 'apple#banana#cherry#orange'
x = txt.split("#")
print(x)

s = "БОЛЬШОЙ БАРЬЕРНЫЙ РИФ"
s1 = "маленький принц"
if s > s1:
    print("Yes")
else:
    print("No")