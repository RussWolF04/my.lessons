with open('byron.txt', 'r') as file:
    line = file.readlines()
    print(f'Первая строка:\n-1. {line[0]}\nПятая строка:\n-5. {line[4]}')
    print(f'Первые пять строк:\n-1. {line[0]}\n-2. {line[1]}\n-3. {line[2]}\n-4. {line[3]}\n-5. {line[4]}')
    print(f'Строки с 1 по 2:\n-1. {line[:2]}')
    print(line)
file.close()