word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

def encode_decode(word):
    word = word.encode()
    print(word)
    word = word.decode()
    print(word)
    return word

encode_decode(word_1)
encode_decode(word_2)
encode_decode(word_3)
encode_decode(word_4)
