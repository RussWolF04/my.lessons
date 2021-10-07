import random

number = random.randint(1, 25)
guesses = 0
while guesses < 5:
    print('Угадайте число от 1 до 25:')
    guess = input('Ваше число: ')
    guess = int(guess)
    guesses += 1
    if guess < number:
        print("Слишком маленькое, попробуйте еще раз")
    if guess > number:
        print('Слишком большое, попробуйте еще раз')
    if guess == number:
        print('Вы угадали номер в',  +  str(guesses) +   'попыток!')
        break
else:
    print('Вы не угадали число, он был' + str(number))