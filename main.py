"""
Case-study #4
Developers:
# Case-study #3
# Developers: Marinkin O. (27%),
# Seledtsov A. (25%),
# Evdischenko M. (85%).
"""

from textblob import TextBlob

text = input('Введите текст: ')
text_blob = TextBlob(text)
detect_language = text_blob.detect_language()


def number_sentences(t):
    k = t.count('.')
    k += t.count('!')
    k += t.count('?')
    return k


def number_words(w):
    w = w.split()
    f = len(w)
    return f


def number_syllables(word):
    vowels = 0
    for let in word:
        if let.isalpha():
            if let.lower() in 'aeiouy':
                vowels += 1
            elif let.lower() in 'ауоыиэяюёе':
                vowels += 1
    return vowels


def average_indicators(sentences, words, syllables):
    asl = words / sentences
    asw = syllables / words
    return asl, asw


def flash(asl2, asw2):
    fre = -1
    if detect_language == 'ru':
        fre = 206.835 - (1.3 * asl2) - (60.1 * asw2)
    elif detect_language == 'en':
        fre = 206.835 - 1.015 * asl2 - 84.6 * asw2
    return fre


def flash_detect(fre2):
    if detect_language == 'ru':
        if fre2 > 80:
            print('Текст очень легко читается (для младших школьников).')
        elif fre2 > 50:
            print('Простой текст (для школьников).')
        elif fre2 > 25:
            print('Текст немного трудно читать (для студентов).')
        elif fre2 <= 25:
            print('Текст трудно читается (для выпускников ВУЗов).')
    elif detect_language == 'en':
        if fre2 >= 100:
            print('Очень легко читается.')
        elif fre2 >= 65:
            print('Простой английский язык.')
        elif fre2 >= 30:
            print('Немного трудно читать.')
        elif fre2 < 30:
            print('Очень трудно читать. ')


def analysis(textb):
    if detect_language == 'ru':
        textb = text_blob.translate(to='en')
    polarity = round(textb.polarity)
    if polarity > 0:
        polarity = 'позитивная'
    elif polarity < 0:
        polarity = 'негативная'
    else:
        polarity = 'нейтральная'
    objectivity = (1 - textb.subjectivity) * 100
    return polarity, objectivity


sent1 = number_sentences(text)
words1 = number_words(text)
syllables1 = number_syllables(text)
asl1, asw1 = average_indicators(sent1, words1, syllables1)
print('Предложений:', sent1)
print('Слов:', words1)
print('Слогов:', syllables1)
print('Средняя длина предложения в словах:', asl1)
print('Средняя длина слова в слогах:', asw1)
fre1 = flash(asl1, asw1)
print('Индекс удобочитаемости Флеша:', fre1)
flash_detect(fre1)
polarit, objectiv = analysis(text_blob)
print('Тональность текста:', polarit)
print('Объективность: ', objectiv, '%', sep=' ')

