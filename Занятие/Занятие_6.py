# ikea = [1, 1, 1, 1]
# my_ikea = [1, 1, 1]
# # for i in my_ikea:
# #     if i in ikea:
# #         print(i)
# for i in my_ikea:
#     if i - my_ikea:
#         print(i)
# my_list = [0, 0]
# pos_1 = input('вверх/вних/вправо/влево: ')
# while pos_1 != 'стоп':
#     if pos_1 == 'вверх':
#         my_list[0] += 1
#     if pos_1 == 'вниз':
#         my_list[0] -= 1
#     if pos_1 == 'вправо':
#         my_list[1] += 1
#     if pos_1 == 'влево':
#         my_list[1] -= 1
#     print(my_list)
#     pos_1 = input('вверх/вних/вправо/влево: ')
# print(my_list)

from random import randint, choice

my_list = ["Трутьнев", "Машков", "Кулаков", "Крючков", "Тарощин"]
my_marks = [i for i in range(10)]
for i in my_list:
    print(f'{i} - {choice(my_marks)}')


# my_spisok = ["Трутьнев", "Машков", "Кулаков", "Крючков", "Тарощин"]
# print(f'{choice(my_spisok)} - {choice(randint(1,10))}')

# my_second_list = [i ** 2 for i in range(21)]
# print(my_second_list)

# xlList = [[1,2,3], [4,5,6], [7,8,9]]
# myList = [item for sList in xlList for item in sList]
# print(myList)
