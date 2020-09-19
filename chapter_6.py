if __name__ == '__main__':
    # lesson_1
    car_0 = {}
    car_0['color'] = 'black'
    car_0['speed'] = 290
    car_0['pos_x'] = 25
    car_0['pos_y'] = 40
    print(car_0['color'])
    print(car_0['speed'])
    car_0['model'] = 'honda'
    print(car_0)
    model = car_0['model']
    print(f"This is {model.title()}!")
    print(f"Before painting: {car_0['color'].title()}")
    car_0['color'] = 'green'
    print(f"After painting: {car_0['color'].title()}")

    def x_position(x):
        if x == 280:
            offset_x = 50
        elif x == 290:
            
            offset_x = 70
        elif x == 300:
            offset_x = 90
        x = x + offset_x
        return f"New {car_0['model'].title()} position X is {x}"
    print(x_position(car_0['speed']))
    car_0['speed'] = 300
    print(x_position(car_0['speed']))

    del car_0['pos_y']
    print(car_0)

    favourite_car = {
        'alex': 'honda',
        'jool': 'audi',
        'peter': 'subaru',
        'marty': 'mira',
        'moog': 'nissan',
        }
    print(f"Moog's favourite car is {favourite_car['moog'].title()}.")

    # lesson_2
    user_00 = {
        'username': 'moog',
        'first': 'marty',
        'last': 'reen',
        'city': 'minsk',
        'age': 28,
        }
    def information(usr):
        for key, value in usr.items():
            return f"key: {key} \nvalue: {value}\n"
    print(information(user_00))

    for key, value in user_00.items():
        print(f"key: {key}\nvalue: {value}\n")
    for name, car in favourite_car.items():
        print(f"{name.title()} like {car.title()}.\n")
    for name in favourite_car.keys():
        print(name.title())
    for name in favourite_car:
        print(name.title())

    favourite_car = {
        'alex': 'honda',
        'jool': 'audi',
        'peter': 'subaru',
        'marty': 'mira',
        'moog': 'nissan',
    }
    print('\n')
    friends = ['moog', 'alex', 'fred', 'tod']
    for name in favourite_car.keys():
        print(name.title())
        if name in friends:
            print(f"   Hi {name.title()}, I see u like {favourite_car[name].title()}")

    if 'fred' not in favourite_car.keys():
        print("Fred go away")

    for name in sorted(favourite_car.keys()):
            print(f"{name.title()} in list")
    print('\n')
    favourite_car['ron'] = 'nissan'
    for model in favourite_car.values():
        print(f"{model.title()} in list")
    print('\n')
    for model in set(favourite_car.values()):
        print(f"{model.title()} in list.")
    print('\n')
    # exercise

    favourite_car = {
        'alex': 'honda',
        'peter': 'subaru',
        'moog': 'nissan',
    }
    peoples = ['peter', 'jool', 'moog', 'ted', 'marty', 'alex', 'ken']
    for people in peoples:
        if people in favourite_car.keys():
            print(f"{people.title()} in list.")
        else:
            print(f"{people.title()} not in list.")

    car_01 = {'model': 'subaru', 'color': 'red', 'max_speed': 350}
    car_02 = {'model': 'toyota', 'color': 'blue', 'max_speed': 320}
    car_03 = {'model': 'honda', 'color': 'white', 'max_speed': 340}
    cars = [car_01, car_02, car_03]
    for car in cars:
        print(car)
    print('\n')

    cars =[]
    for car_number in range(30):
        new_car = {'model': 'subaru', 'color': 'red', 'max_speed': 350}
        cars.append(new_car)
    for car in cars[3:6]:
        print(car)
    print(f"Total number of cars {len(cars)}")
    for car in cars[2:5]:
        if car['model'] == 'subaru':
            car['model'] = 'honda'
            car['color'] = 'black'
            car['max_speed'] = 320
    for car in cars[:7]:
        print(car)

    favourite_car = {
        'alex': ['honda', 'nissan'],
        'jool': ['audi'],
        'peter': ['subaru', 'honda', 'toyota'],
        'marty': ['mira'],
        'moog': ['nissan'],
    }
    for name, cars in favourite_car.items():
        if len(cars) == 1:
            print(f"{name.title()}'s favourite car is:")
        else:
            print(f"{name.title()}'s favourite cars are:")
        for car in cars:
            print(f" {car.title()}")
    print('\n')

    users = {
        'klayton': {
            'first_name': 'mike',
            'last_name': 'shinoda',
            'location': 'california',
            },
        'cameroon': {
            'first_name': 'chester',
            'last_name': 'benington',
            'location': 'texas',
            },
        }
    for username, user_info in users.items():
        print(f"User name: {username.title()}")
        print(f"\tFull name: {user_info['first_name'].title()} {user_info['last_name'].title()}")
        print(f"\tLocation: {user_info['location'].title()}")