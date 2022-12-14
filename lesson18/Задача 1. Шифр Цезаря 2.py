# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
# Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и сделайте так,
# чтобы текст был в одном регистре.

def caesar_cipher(string, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''.join(char_list)
    return new_str


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
user_list = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

result = caesar_cipher(user_list, shift)
print('Зашифрованное сообщение:', result)


# print(ord("а"), ord("я"), ord("ё"), chr(1104))
#
# text = input("Введите текст: ")
# delta = int(input("Введите сдвиг: "))
# alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]  # заполняем список буквами алфавита
# # Думаем над структурой алгоритма: [вариант_1 если условие_1 иначе вариант_2 for буква in текст]
# new_text = [alphabet[(alphabet.index(letter) + delta) % len(alphabet)] if letter in alphabet else letter for letter in text.lower()]
# print(''.join(new_text))
