file = open("C:\pg.txt", "rt")
words = 0
symbol = 0
f = 0
for i in file:
    f += 1
    for a in i:
        if a not in (' ', '\n', '\t'):
            symbol += 1

    pos = 'out'
    for a in i:
        if a != ' ' and pos == 'out':
            words +=1
            pos = 'in'
        elif a == ' ':
            pos = 'out'
    print("У рядку номер -", f, "кількість слів -", words, "кількість символів -", symbol)
    symbol = 0
    words = 0