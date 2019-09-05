__author__ = 'Ablezgov Andrey'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
from shutil import copy
from sys import argv

def look():
    print(os.listdir(os.getcwd()))

def currentdirectories():
    list1 = os.listdir(os.getcwd())
    for itm in list1:
        currentpath = os.path.join(os.getcwd(), itm)
        if os.path.isdir(currentpath):
            print(itm)

def createdir(pathdir):
    try:
        os.mkdir(pathdir)
        print("Папка успешно создана!")
    except FileExistsError:
        print("Эмм уже создавал такую папку")

def removedir(pathdir):
    try:
        os.rmdir(pathdir)
        print("Папка успешно удалена!")
    except FileNotFoundError:
        print("Файла не существует или он уже удален")

def changedir(pathdir):
    try:
        os.chdir(pathdir)
    except FileNotFoundError:
        print("Файла не существует или он уже удален")

if __name__ == '__main__':
    i = 1
    while i <= 9:
        createdir(os.path.join(os.getcwd(), f'Dir_{i}'))
        i += 1
    look()

    j = 1
    while j <= 9:
        removedir(os.path.join(os.getcwd(), f'Dir_{j}'))
        j += 1
    look()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

if __name__ == '__main__':
    currentdirectories()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == '__main__':
    copy(argv[0], os.path.join(os.getcwd(), "homework_copy.py"))
    look()