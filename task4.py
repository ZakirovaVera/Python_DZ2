# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число.
import random
user_numberN = int(input('Введите целое число N: '))
lst_numbers = []
sum = 0

while len(lst_numbers) < user_numberN:
    lst_numbers.append(random.randrange(-user_numberN, user_numberN+1))

print(lst_numbers)

with open("text.txt", "r") as file:
    nums = file.read().splitlines()
    print(f'Данные с файла {nums}')
    index = 0
    while index < len(nums):
        position = int(nums[index])
        # print(len(lst_numbers))
        if position > len(lst_numbers):
            sum +=0
        else:
            sum += lst_numbers[position]
            print(f'На {position} позиции -> {lst_numbers[position]}')
        index+=1
file.close()    
print(f'Сумма этих позиций = {sum}')
    
