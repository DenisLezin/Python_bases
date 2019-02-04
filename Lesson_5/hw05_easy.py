
__author__ = 'Лезин Денис Андреевич'
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import re



def create_nine_dir(access = [], fail = []):
    for i in range(9):
        try:
            os.mkdir(os.path.join(os.getcwd(), 'dir_' + str(i + 1)))
            access.append('dir_' + str(i + 1))
        except FileExistsError:
            fail.append('dir_' + str(i + 1))
    print(f'Dir created: {access}\nDir exists: {fail}')

def remove_dir():
    dir_exist = re.findall('dir_[0-9]+', (''.join(os.listdir())))
    for i in dir_exist:
        os.rmdir(os.path.join(os.getcwd(), i))
    print('Done!')

#create_nine_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

def directories():
    directory = [i for i in os.listdir() if not os.path.isfile(os.path.join(os.getcwd(), i))]
    print(directory)

#directories()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

def copy_this_file1():
    base_filename = os.path._getfullpathname(__file__)
    copy_filename = os.path.join(os.getcwd(), os.path.basename(__file__).replace('.', '_copy.'))
    command = f'copy {base_filename} {copy_filename}'

    if os.path.exists(copy_filename):
        print('Copy already exists')
    else:
        os.popen(command)


#copy_this_file1()


def copy_this_file2():
    base_filename = os.path._getfullpathname(__file__)
    copy_filename = os.path._getfullpathname(__file__).replace('.', '_copy.')
    with open(base_filename, 'r', encoding='UTF-8') as f:
        lst = f.readlines()
    with open(copy_filename, 'w', encoding='UTF-8') as f:
        f.writelines(lst)



#copy_this_file2()
os.remove(os.path.join(os.getcwd(), os.path.basename(__file__).replace('.', '_copy.')))