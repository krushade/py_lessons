if __name__ == '__main__':
    # lesson_1
    cars = ['honda', 'subaru', 'bmw', 'toyota', 'mazda']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())
    print("\n")

    for car in cars:
        if car.lower() == 'honda':
            print(f"This car is {car.title()}.")
    print("\n")

    for car in cars:
        if car.lower() == 'bmw':
            print(f"{car.upper()} is not Honda")
        elif car.lower() != 'honda':
            print(f"{car.title()} is not Honda")
        else:
            print(f"This is {car.title()}")
    print("\n")

    num = 19
    if num != 18:
        print(f"{num} is False")
    else:
        print(f"{num} is True")
    print('\n')

    # if num > 5 and num <= 15:
    if 5 < num <= 15:
        print(f"Number {num} is suitable.")
    else:
        print(f"Number {num} is not suitable.")
    print('\n')

    num_2 = 35
    if num > 15 or num_2 < 50:
        print('+')
    else:
        print('-')
    print('\n')

    games = ['doom', 'rocket league', 'gta 5', 'watch dogs', 'horizon']
    if 'horizon' in games:
        print("Horizon in list")
    else:
        print('Horizon not in list')
    if 'doom' not in games:
        print('Doom not in list')
    else:
        print('Doom in list')

    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

    text = "moon"
    print('moon' in text)
    print('rocket league' in games)

    # lesson_2
    print('\n')

    car = {'honda': 28, 'toyota': 5, 'ford': 17}
    for name, age in car.items():
        if age >= 10:
            print(f"Your {name.title()} is old")
        else:
            print(f"Your {name.title()} is new")

    print('\n')
    peoples = {'jon': 15, 'kenny': 18, 'peter': 10, 'max': 3, 'marty': 25}
    for name, age in peoples.items():
        if age < 4:
            price = 0
        elif age < 18:
            price = 5
        else:
            price = 10
        print(f"{name.title()}, your admission cost is {price}$.")

    alien_color = "red"
    if "green" in alien_color:
        print("\nYou got 5 points")
    else:
        print("\nYou got 10 points")

    if "green" in alien_color:
        print("You got 5 points")
    elif "yellow" in alien_color:
        print("You got 10 points")
    elif "red" in alien_color:
        print("You got 15 points")
    else:
        print("You got 0 points")

    print('\n')
    available_colors = ['green', 'yellow', 'red', 'black', 'white']
    requested_colors = ['blue', 'orange', 'red', 'pink', 'black']
    for requested_color in requested_colors:
        if requested_color in available_colors:
            print(f"{requested_color.title()} in available")
        else:
            print(f"{requested_color.title()} is not available")