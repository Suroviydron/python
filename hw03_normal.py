__author__ = 'Ablezgov Andrey'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    i = 0
    fib = [1, 1]
    while i < m:
         fib.append(fib[i] + fib[i+1])
         i += 1
    result = fib[n-1:m]
    return result
print(fibonacci(1, 9))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(olist):
    i = len(olist)
    while i > 0:
        j = 0
        while j < i-1:
            if olist[j+1] < olist[j]:
                olist[j], olist[j+1] = olist[j+1], olist[j]
            j += 1
        i -= 1
    return olist

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, olist):
    for itm in olist[:]:
        if func(itm) == False:
            olist.remove(itm)
    return olist

print(my_filter(lambda x:x < 10, [1, 2, 3, 33, 14, 7, 45]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("Введите верхние стороны параллелограмма")
A1 = [int(input("Введите x:")), int(input("Введите y:"))]
print(f' Точка 1: {A1}')
A2 = [int(input("Введите x:")), int(input("Введите y:"))]
print(f' Точка 2: {A2}')
print("Введите нижние стороны параллелограмма")
A3 = [int(input("Введите x:")), int(input("Введите y:"))]
print(f' Точка 3: {A3}')
A4 = [int(input("Введите x:")), int(input("Введите y:"))]
print(f' Точка 4: {A4}')

if A3[0] + A4[0] == A1[0] + A2[0] and A1[1] - A3[1] == A2[1] - A4[1]:
    print("Данные точки являются вершинами параллелограмма")
else:
    print("Не являются вершинами параллелограмма")