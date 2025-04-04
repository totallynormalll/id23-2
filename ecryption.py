def break_cipher(text):
    import string

    # Создаем множество допустимых символов для русского языка
    russian_letters = set(
        'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' +
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' +
        string.punctuation + string.whitespace + '0123456789'
    )

    max_score = 0
    decrypted_text = ''
    probable_key = 0

    for k in range(65536):
        # Дешифруем текст с текущим ключом
        attempted_text = ''.join(
            [chr((ord(c) - k) % 65536) for c in text]
        )

        # Считаем количество допустимых символов в расшифрованном тексте
        score = sum(char in russian_letters for char in attempted_text)

        # Если счет выше максимального, обновляем максимальный счет и сохраняем текст
        if score > max_score:
            max_score = score
            decrypted_text = attempted_text
            probable_key = k

        # Опционально: вывести прогресс каждые N итераций
        # if k % 10000 == 0:
        #     print(f"Проверено ключей: {k}")

        # Если максимально возможный счет достигнут, можно прервать цикл
        if score == len(text):
            break

    print(f"Найденный ключ: {probable_key}")
    return decrypted_text

# Пример использования функции
cipher_text = input("Введите зашифрованный текст: ")
original_text = break_cipher(cipher_text)
print("Расшифрованный текст:", original_text)