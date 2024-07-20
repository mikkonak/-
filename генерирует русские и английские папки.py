import os
import string
import subprocess
import platform

def create_folders(start_letter, end_letter, alphabet):
    # Выбор алфавита
    if alphabet == 'english':
        letters = string.ascii_lowercase
    elif alphabet == 'russian':
        letters = ''.join(chr(i) for i in range(ord('а'), ord('я') + 1))
    else:
        raise ValueError("Invalid alphabet. Choose 'english' or 'russian'.")

    # Найти индексы начальной и конечной буквы
    start_index = letters.index(start_letter.lower())
    end_index = letters.index(end_letter.lower()) + 1

    # Создание папки для хранения алфавитных папок
    parent_folder = 'Alphabet_Folders'
    os.makedirs(parent_folder, exist_ok=True)

    # Создание папок для каждой буквы
    for letter in letters[start_index:end_index]:
        folder_name = os.path.join(parent_folder, letter.upper())
        os.makedirs(folder_name, exist_ok=True)
        print(f'Folder {folder_name} created')

    # Открытие созданной папки
    system_name = platform.system()
    if system_name == 'Windows':
        subprocess.run(['explorer', parent_folder])
    elif system_name == 'Darwin':  # macOS
        subprocess.run(['open', parent_folder])
    else:  # Linux
        subprocess.run(['xdg-open', parent_folder])

# Пример использования:
# Создание папок для английского алфавита от A до Z
create_folders('A', 'Z', 'english')

# Создание папок для русского алфавита от А до Я
create_folders('А', 'Я', 'russian')
