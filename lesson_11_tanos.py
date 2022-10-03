# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
from string import ascii_lowercase as alphabet
import random


def create_directory(dirname: str) -> None:
    os.makedirs(dirname, exist_ok=True)
    # try:
    #     os.mkdir(dirname)
    # except FileExistsError:
    #     pass


def create_files(dirname: str) -> None:
    for symbol in alphabet:
        filename = os.path.join(dirname, f"{symbol}.txt")  # better way
        # filename = f"{dirname}/{symbol}.txt"
        create_file_from_symbol(filename, symbol)


def create_file_from_symbol(filename: str, symbol: str) -> None:
    data = alphabet.replace(symbol, symbol.upper())
    with open(filename, 'w') as file:
        file.write(data)


def do_tanos_click(dirname: str) -> None:
    listdir = os.listdir(dirname)
    random.shuffle(listdir)
    for filename in listdir[:len(listdir) // 2]:
        os.remove(os.path.join(dirname, filename))


print(__name__)
if __name__ == "__main__":
    dirname = "alphabet"
    create_directory(dirname)
    create_files(dirname)
    do_tanos_click(dirname)

    # alph = "".join([chr(idx) for idx in range(ord('а'), ord('я') + 1)])
    # print(alph)
