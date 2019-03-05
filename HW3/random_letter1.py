import random
s = ['самовар','весна','чайник']
word = random.choice(s)
letter = random.choice(word)
word_symb = list(word)
word_symb[word.index(letter)] = '?'
word_q = ''.join(word_symb)
print(word_q)
letter_user = input('Введите букву: ')
if letter_user == letter:
    print('Победа!')
else:
    print('Увы! Попробуйте в другой раз...\nСлово:',word)
