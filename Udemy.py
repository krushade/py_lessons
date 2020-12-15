# игра в палочки на двух игроков
if __name__ == '__main__':
    while True:
        sticks = input("Выберите количество палочек: ")
        if sticks.isdigit() is True:
            sticks_int = int(sticks)
            break
        else:
            print("Неправильный ввод, еще раз: ")

    print(f"Вы выбрали {sticks_int} палочек."
          f"\nИгра начинается.\n")

    while sticks_int > 0:
        while True:
            sticks_p1 = input("Первый игрок тянет палочки: ")
            if sticks_p1.isdigit() is True:
                sticks_p1 = int(sticks_p1)
                if 0 < sticks_p1 <= 3:
                    sticks_int -= sticks_p1
                    if sticks_int <= 0:
                        print("Второй игрок победил")
                        break
                    print(f"Первый игрок взял {sticks_p1}. \n"
                          f"Осталось {sticks_int}")
                    break
                else:
                    print("Неправильный ввод, еще раз: ")
            else:
                print("Неправильный ввод, еще раз: ")

        while True:
            sticks_p2 = input("Второй игрок тянет палочки: ")
            if sticks_p2.isdigit() is True:
                sticks_p2 = int(sticks_p2)
                if 0 < sticks_p2 <= 3:
                    sticks_int -= sticks_p2
                    if sticks_int <= 0:
                        print("Первый игрок победил")
                        break
                    print(f"Первый игрок взял {sticks_p2}. \n"
                          f"Осталось {sticks_int}")
                    break
                else:
                    print("Неправильный ввод, еще раз: ")
            else:
                print("Неправильный ввод, еще раз: ")
