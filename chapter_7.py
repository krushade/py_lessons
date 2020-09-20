if __name__ == '__main__':
    # input
    # message = input("input")
    # print(message)

    # name = input("Enter your name: ")
    # print(f"Hi {name}!")

    # message = "First string"
    # message += "\nSecond string. enter any "
    # inpt = input(message)
    # print(inpt)

    # age = input("How old are you? ")
    # age = int(age)
    # if age >= 18:
    #     print("you old")
    # else:
    #     print("you young")

    # num = input("Enter your number for check ")
    # num = int(num)
    # if num % 2 == 0:
    #     print(f"The number {num} is even")
    # else:
    #     print(f"The number {num} is odd")

    # WHILE
    # number = 1
    # while number <= 5:
    #     print(f"{number} is current")
    # #    number = number + 1
    #     number += 1

    # inpt = "Enter 'quit' to end programm. "
    # inpt += "\n\tEnter here: "
    # message = ""
    # while message != 'quit':
    #     message = input(inpt)
    #     if message != 'quit':
    #         print(message)

    # inpt = "Enter 'quit' to end programm. "
    # inpt += "\n\tEnter here: "
    # activation = True
    # while activation:
    #     message = input(inpt)
    #     if message == 'quit':
    #         activation = False
    #     else:
    #         print(message)

    # inpt = "Enter 'quit' to end programm. "
    # inpt += "\n\tEnter here: "
    # while True:
    #     mess = input(inpt)
    #     if mess == 'quit':
    #         break
    #     else:
    #         print(f"You message: {mess}")

    # num = 0
    # while num <= 10:
    #     num += 1
    #     if num % 2 != 0:
    #         continue
    #     print(num)

    # zadanie pizza
    # pizza = {'testo': 'tonkoe', 'dopolnenie': set()}
    # dopolneniya = ['bekon', 'ananas', 'kyritca', 'perec', 'pomidor']
    # tekst = f"Dlya vyhoda vvedite 'exit' \nvybor dopov {dopolneniya}"
    # tekst += "\n\tVvedite dopolnenie k pizza: "
    #
    # while True:
    #     dop = input(tekst)
    #     if dop == 'exit':
    #         print(f"Vash zakaz {pizza}!")
    #         break
    #     elif dop in dopolneniya:
    #         print(f"Dobavleno: {dop}")
    #         pizza['dopolnenie'].add(dop)
    #     else:
    #         print("Nepravilnyi vybor")

    # zadanie ticket:
    # age = input("Введите ваш возраст: ")
    # age = int(age)
    # if age < 3:
    #     price = 0
    # elif age < 12:
    #     price = 10
    # else:
    #     price = 15
    # print(f"Cтоимость билета: {price}$.")

    # unconfirmed_users = ['anna', 'alex', 'marty', 'alice']
    # confirmed_users = []
    # while unconfirmed_users:
    #     current_user = unconfirmed_users.pop()
    #     print(f"Verifing user: {current_user.title()}")
    #     confirmed_users.append(current_user)
    # print("\n confirmed users:")
    # for confirmed_user in confirmed_users:
    #     print(confirmed_user.title())

    # pets = ['cat', 'dog','cat', 'rabbit', 'cat', 'cat', 'cat', 'python', 'cat', ]
    # print(pets)
    # while 'cat' in pets:
    #     pets.remove('cat')
    # print(pets)

    Опрос
    опрос = {}
    активация_опроса =True
    while активация_опроса:
        имя = input("\nВведите ваше имя: ")
        вопрос = input("\nКакая ваша любимая марка авто: ")
        продолжить = input("Вы хотите ввести данные очередного человека: (да/нет)")
        опрос[имя] = вопрос
        if продолжить == 'нет':
            активация_опроса = False
    print("Результаты опроса:")
    for имя, марка in опрос.items():
        print(f"Имя: {имя.title()}, любмая марка авто: {марка.title()} ")