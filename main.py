from textblob import TextBlob

text = input('Введите текст: ')
text_blob = TextBlob(text)


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


sent1 = number_sentences(text)
words1 = number_words(text)
syllables1 = number_syllables(text)
asl1, asw1 = average_indicators(sent1, words1, syllables1)

print('Предложений:', sent1)
print('Слов:', words1)
print('Слогов:', syllables1)
print('Средняя длина предложения в словах:', asl1)
print('Средняя длина слова в слогах:', asw1)


def flash(text1, asl2, asw2):
    fre = -1
    if text1.detect_language() == 'ru':
        fre = 206.835 - (1.3 * asl2) - (60.1 * asw2)
    elif text1.detect_language() == 'en':
        fre = 206.835 - 1.015 * asl2 - 84.6 * asw2
    return fre


print('Индекс удобочитаемости Флеша:', flash(text_blob, asl1, asw1))