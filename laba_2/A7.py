coord11 = int(input('Введите координату 1 первой клетки:' ))
coord12 = int(input('Введите координату 2 первой клетки:' ))
coord21 = int(input('Введите координату 1 второй клетки:' ))
coord22 = int(input('Введите координату 2 второй клетки:' ))

if (coord11 + coord12) % 2 == (coord21 + coord22) % 2:
    print("YES")
    if (coord11 + coord12) % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")
