"""
5. (МОДУЛЬ 2) создать модуль 2seq.py. Задание:
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
Вывести новый список на экран
Порядок цифр в новом списке не важен
Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
Результат: 2, 4, 6, 9
(Дополнительно*) Предусмотреть что пользователь может использовать один из 3-х разделителей:
запятую, точку с запятой, слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя

"""
my_list = input("Введите элементы списка через запятую: ")
my_list_one =[]
for i in my_list:
    if i==";" or i=="/" or i==",":
        my_list = my_list.replace(";", "")
        my_list = my_list.replace("/", "")
        my_list = my_list.replace(",", "")
for j in my_list:
    if my_list.count(j) == 1:
        my_list_one.append((j))
my_list = list(my_list)
print ("Результат:", ", "''.join(my_list_one))