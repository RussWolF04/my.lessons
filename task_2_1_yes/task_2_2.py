# № 2. Запросить у пользователя возраст. Если возраст
# меньше 0 - вывести Wrong input, если меньше 18 -
# вывести CocaCola, иначе - вывести Beer

user = input('How Your name?: ') # Как вас зовут
user_old = int(input("How old are you? " + user)) # Сколько вам лет
if user_old < 18: # если введенный возраст меньше 18
    print("Пей CocaCola " + user) # то выдать это сообщение
elif user_old >= 18: # Если больше
    print("You can drink beer, " + user) # то выдать это сообщение