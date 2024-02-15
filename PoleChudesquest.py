from random import choice
WORDS = ("собака", "игра", "программирование", 'гидроэлектростанция', 'оториноларинголог', 'электрокардиографический', 'электронейтральный', 'достопримечательность')
word = choice(WORDS)
word_len = "-" * len(word)
mistakes = 0
x = list()
alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',]
while word_len != word:
    print("\nВы использовали следующие буквы:\n", x)
    print("\nНа данный момент слово выглядит так:\n", word_len)
    print("\nВ слове все буквы русские, маленькие(не заглавные)")
    answer = input()
    while answer not in alphavit:
        print("Такой буквы нет в алфавите!")
        answer = input()
    while answer in x:
        print("Вы уже вводили букву", answer)
        answer = input("Введите свое предположение: ")
    x.append(answer)
    if answer in word:
        print("\nДа!", answer, "есть в слове!")
        new = ""
        for i in range(len(word)):
            if answer == word[i]:
                new += answer
            else:
                new += word_len[i]
        word_len = new
    else:
        print("\nИзвините, буквы \"" + answer + "\" нет в слове.")
        mistakes += 1
print("Поздравляю! Вы смогли угадать слово! Ваше количество ошибок: " + mistakes)
