#Задачи на циклы и оператор условия------
#-------------------
'''
Задача 1.
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# с
# for i in range(1, 6):
 #   print(f'{i} :', '000000000')

'''
Задача 2.
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
#print('Задача 2')
#five = 0
#for i in range(10):
#    answer = int(input('Введите любую цифру: '))
 #   if answer == 5:
  #      five += 1
#
#print('Количество цифр 5 равно', five)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# print ('Задача 3')
# sum = 0
# for i in range(1,101):
#    sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# print ('Задача 4')
# n = 1
# for i in range(2, 11):
#     n *= i
# print('Произведение ряда чисел от 1 до 10 равно', n)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
# print ('Задача 5')
# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# print ('Задача 6')
# number = 876396
# integer_number = 876396
# sum = 0
# while integer_number > 0:
#    sum += integer_number % 10
#    integer_number = integer_number // 10
# print('Сумма цифр числа', number, 'равно', sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# print ('Задача 7')
# number = 8764567
# integer_number = 8764567
# proizv = 1
# while integer_number>0:
#    proizv *= integer_number%10
#    integer_number = integer_number//10
# print('Произведение цифр числа', number, 'равно', proizv)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# print ('Задача 8')
# number = 4678385
# integer_number = 4678385
# while integer_number>0:
#     if integer_number%10 == 5:
#        print('В числе', number, 'есть цифра 5!')
#        break
#    integer_number = integer_number//10
# else: print('В числе', number, 'нет цифры 5!')

'''
Задача 9
Найти максимальную цифру в числе
'''
# print ('Задача 9')
# integer_number = 765936
# max = 0
# while integer_number>0:
#    if integer_number%10 >= max:
#        max = integer_number%10
#    integer_number = integer_number//10
# print('В данном числе максимальная цифра -', max)


'''
Задача 10
Найти количество цифр 5 в числе
'''
# print ('Задача 10')
# integer_number = 764983
# sum = 0
# while integer_number>0:
#    if integer_number%10 == 5:
#        sum += 1
#    integer_number = integer_number//10
# print('Количество цифр 5 в числе равно -', sum)
