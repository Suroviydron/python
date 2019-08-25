__author__ = 'Ablezgov Andrey'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):

    for idx, itm in enumerate(str(number), start=1):
       if itm == ".":
           pointnumb = idx
           break

    i = len(str(number)) - pointnumb
    while i - ndigits > 0:
        number = number * 10**i
        if number % 10 >= 5:
            number = number // 10
            number += 1
            number = number / 10 ** (i-1)
        else:
            number = number // 10
            number = number / 10 ** (i - 1)
        i -= 1
    return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    part1sum = 0
    part2sum = 0
    for idx, itm in enumerate(str(ticket_number)):
        if idx >= 0 and idx <= 2:
            part1sum = part1sum + int(itm)
        else:
            part2sum = part2sum + int(itm)
    if part1sum == part2sum:
        return "Счастливый билет"
    else:
        return "Упс! Ты зря съел этот билет, он оказался несчастливым =)"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
