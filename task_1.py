word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
print(f'{word_1} - type {type(word_1)}')
print(f'{word_2} - type {type(word_2)}')
print(f'{word_3} - type {type(word_3)}')

word_1 = list(map(lambda x: ord(x), list(word_1)))
word_2 = list(map(lambda x: ord(x), list(word_2)))
word_3 = list(map(lambda x: ord(x), list(word_3)))

print(f'{word_1} - type {type(word_1[0])}')
print(f'{word_2} - type {type(word_2[0])}')
print(f'{word_3} - type {type(word_3[0])}')