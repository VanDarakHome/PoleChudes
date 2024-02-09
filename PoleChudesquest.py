while True:
    slovarus = list()
    countgame = 1
    slovarus.append('Гидроэлектростанция')
    slovarus.append('Оториноларинголог')
    slovarus.append('Электрокардиографический')
    slovarus.append('Электронейтральный')
    slovarus.append('Достопримечательность')
    print('Hello! This is game: field of miracles!')
    print("Now you can change language to Russian. Type 1 if you need it.")
    print('1) Continue with English language')
    print("2) Change my language to Russian")
    language = input()
    while language != '1' and language != '2':
        print("Please, make a choice")
        language = input()
    if language == '1':
        print('Ok. Do you want to play?')
        print("1) Yes")
        print("2) No")
        choice = input()
        while choice != '1' and choice != '2':
            print('Bro, please write 1 or 2')
            choice = input()
        if choice == '1':
            break
        else:
            countgame = 1
# -----------------------------------------------------
    if language == '1':
        print("Do you want to play one more time?")
        print("1) Yes")
        print("2) No")
        end = input()
        while end != '1' and end != '2':
            print("Please, make a choice")
            end = input()
        if end == '1':
            continue
        else:
            break
    if language == '2':
        print("Хотите ли вы сыграть ещё раз?")
        print("1) Да")
        print("2) Нет")
        end = input()
        while end != '1' and end != '2':
            print("Введи 1 или 2")
            end = input()
        if end == '1':
            continue
        else:
            break
