__author__ = 'Ablezgov Andrey'

from random import randint

def linecreate():
    line = []
    list1 = [0, 0, 0, 0, 1, 1, 1, 1, 1]
    j = 0
    while j < 9:
        line.append(list1.pop(randint(0, 8 - j)))
        j += 1
    return line

def lineconvert(boxc):
    boxc.sort()
    linec = linecreate()
    result = ""
    i = 0
    while i < 9:
        if linec[i] == 0:
           result += "   "
        elif linec[i] == 1:
            result += str(boxc.pop(0)).rjust(3)
        i += 1
    return result

box = []
i = 0
while i < 30:
    number = randint(1, 90)
    if number not in box:
        box.append(number)
        i += 1

cardplayer = f'{lineconvert(box[0:5])}\n{lineconvert(box[5:10])}\n{lineconvert(box[10:15])}'
cardcomp = f'{lineconvert(box[15:20])}\n{lineconvert(box[20:25])}\n{lineconvert(box[25:30])}'

print("Сыграем в игру Лото")
print(f'Игрок получил следующую карточку:\n{cardplayer}')
print("\n" + f'Компьютер получил следующую карточку:\n{cardcomp}')

barrel = [itm for itm in range(1, 91)]
playerwincounter = 0
computerwincounter = 0
step = 1

while True:
    number = barrel.pop(randint(0, 90 - step))
    print(f'Ход {step}')
    print(f'Ведущий достает из мешка бочонок номер {number}')

    answer = input("Игрок, зачеркиваешь карточку? (да/нет): ").lower()
    if number in box[0:15] and answer == "да" :
        print("Поздравляю ты успешно зачеркнул карточку!")
        playerwincounter += 1
        step += 1
        if playerwincounter == 15:
            print("Да ты мега крут, поздравляю ты победил в Лото")
            break
    elif number in box[0:15] and answer == "нет":
        print("В карточке же был номер с бочонка! Ты проиграл, в следующий раз будь внимательнее")
        break
    elif number not in box[0:15] and answer == "да":
        print("О нет, тебе показалось, такого номера в карточке нет! Ничего повезет в следующий раз =)")
        break
    elif number in box[15:30]:
        print("Компьютер зачеркнул номер на своей карточке")
        computerwincounter += 1
        step += 1
        if computerwincounter == 15:
            print("Победил компьютер")
            break
    else:
        print("Номер отсутствует в карточках, тащу дальше...")
        step += 1
        continue








