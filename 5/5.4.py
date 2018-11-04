#!/usr/bin/env python3

"""
Задание 5.4
Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
"""

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

input_int = int(input("""Введите числа из списка ниже, чтобы узнать индекс последнего вхождения элемента:
[10, 2, 30, 100, 10, 50, 11, 30, 15, 7]:"""))
print(9 - num_list[::-1].index(input_int))
"""
Ещё варинат, без привязки к количеству элементов в списке
print(len(num_list) - num_list[::-1].index(input_int)"""

input_str = input("""Введите слово из списка ниже, чтобы узнать индекс последнего вхождения элемента
['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']:""")
print(7 - word_list[::-1].index(input_str))


"""
Вывод:
13:24 $ ./5.4.py 
Введите числа из списка ниже, чтобы узнать индекс последнего вхождения элемента:
[10, 2, 30, 100, 10, 50, 11, 30, 15, 7]:30
7
Введите слово из списка ниже, чтобы узнать индекс последнего вхождения элемента
['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']:ruby
6
"""
