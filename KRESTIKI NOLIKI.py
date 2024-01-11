pole = ["-" for i in range(9)]

def vivod_pole():
    ryad1 = "    0  1  2 "
    ryad2 = " 0  {}  {}  {} ".format(pole[0], pole[1], pole[2])
    ryad3 = " 1  {}  {}  {} ".format(pole[3], pole[4], pole[5])
    ryad4 = " 2  {}  {}  {} ".format(pole[6], pole[7], pole[8])
    print()
    print(ryad1)
    print(ryad2)
    print(ryad3)
    print(ryad4)
    print()

def proverka_pobeda(pole):
    combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in combination:
        if pole[each[0]] == pole[each[1]] == pole[each[2]] == "X":
            return "Победил первый игрок(X)"
        elif pole[each[0]] == pole[each[1]] == pole[each[2]] == "0":
            return "Победил второй игрок(0)"
    if "-" not in pole:
        return "Ничья"
    return None

def vvod1(pole):
    while True:
        vibor1 = int(input("Введите позицию: "))
        if vibor1 in range(1, 10):
            if pole[vibor1 - 1] == "-":
                pole[vibor1 - 1] = "X"
                break
            else:
                print("Занято")
        else:
            print("Неверный номер ввода")

def vvod2(pole):
    while True:
        vibor2 = int(input("Введите позицию: "))
        if vibor2 in range(1, 10):
            if pole[vibor2 - 1] == "-":
                pole[vibor2 - 1] = "0"
                break
            else:
                print("Занято")
        else:
            print("Неверный номер")

def game():
    vivod_pole()

while True:
    vivod_pole()
    vvod1(pole)
    vivod_pole()
    if proverka_pobeda(pole):
        print(proverka_pobeda(pole))
        break
    vvod2(pole)
    vivod_pole()
    if proverka_pobeda(pole):
        print(proverka_pobeda(pole))
        break

game()


