with open('test_file.txt', 'w') as t:
    t.write('сетевое программирование')
    t.write('сокет')
    t.write('декоратор')

with open('test_file.txt', 'r', encoding='utf-8') as p:
    print(p.read())         # сетевое программированиесокетдекоратор

with open('test_file.txt', 'r', encoding='ASCII') as q:
    print(p.read())         # ValueError: I/O operation on closed file.
