"""
6. (МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
"""
my_list = input("Введите элементы списка через запятую: ")
my_list_two = input("Введите элементы списка через запятую: ")
my_list = list(my_list)
my_list_two = list(my_list_two)
my_list_3 = list(set(my_list) - set(my_list_two))
my_list_3.sort()
print ("Результат:", ", "''.join(my_list_3))