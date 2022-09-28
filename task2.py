# 2. Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

user_numberN = int(input('Введите целое число N: '))
product_numbers = 1
result_product_numbers = []

for i in range(1, user_numberN+1):
    product_numbers *= i
    result_product_numbers.append(product_numbers)

print(f'N = {user_numberN} -> {result_product_numbers}')

# user_numberN = int(input('Введите целое число N: '))
# index = 1
# product_numbers = 1
# result_product_numbers = []

# while index <= user_numberN:
#     product_numbers *= index
#     result_product_numbers.append(product_numbers)
#     index += 1

# print(f'N = {user_numberN} -> {result_product_numbers}')
