# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [1, 2, 4, 0]
list2 = [itm**2 for itm in list1]
print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["арбуз", "банан", "яблоко", "персик"]
fruits2 = ["яблоко", "слива", "вишня", "дыня", "арбуз"]
fruits3 = []
fruits3 = [itm for itm in fruits1 if itm in fruits2]
print(fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
list1 = []
i = 0
while i < 10:
    list1.append(random.randint(-10, 10))
    i += 1
print(f'Дан список: {list1}')
list2 = [itm for itm in list1 if itm % 3 == 0 and itm >= 0 and itm % 4 != 0]
print(f'Числа из списка, удовлетворяющие данному условию:{list2}')

