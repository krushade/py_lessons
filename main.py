message = "Hello Python Crash Course world!"
print(message)

print('\tfirst message')

name = "this is String"
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'aliaksei'
last_name = "markevich"
full_name = first_name + ' ' + last_name
print(full_name)
message = 'Hello, ' + full_name.title() + '!'
print(message)

print('\tTab')
print("Разрывы строк:\n\tString 1\nString 2\n\tString 3")

language = 'python  '
print(language.rstrip() + ' py')

language_1 = "python   "
language_1 = language_1.rstrip()
print(language_1 + "_py")

language_2 = '  python  '
print("'" + language_2.rstrip() + "'")
print("'" + language_2.lstrip() + "'")
print("'" + language_2.strip() + "'")

сложение = 3 + 2
вычитание = 3 - 2
умножение = 3 * 2
деление = 3 / 2
print(сложение + вычитание + умножение + деление)
print(сложение)
print(вычитание)
print(умножение)
print(деление)

example_1 = 3 ** 2
print(example_1)
example_2 = 3 ** 3
print(example_2)
example_3 = 2 + 3 * 4
print(example_3)
example_4 = (2 + 3) * 4
print(example_4)

example_5 = 0.1 + 0.1
print(example_5)
example_6 = 2 * 0.1
print(example_6)

example_7 = 0.2 + 0.1
print(example_7)

age = 28
message = "I'm " + str(age) + " years old"
print(message)

print(4 + 4)
print(2 * 4)
print(16 / 2)
print(10 - 2)

#задание про любимое число
favourite = 13
message = "My favourite number is " + str(favourite)
print(message)

names = ['alex', 'Jools', 'Sergei', 'Jon']
print(names)
print(names[1])
print(names[0].upper())
print(names[-1].lower())
print(names[-2])
message = "My names is " + names[0].title() + '.'
print(message)

message = 'My friend is ' + names[2] + "."
print(message)

message = "My girlfriend is " + names[1]
print(message)

auto = ['audi', 'bmw', 'nissan', 'honda', 'geely']
buy_auto = "I want to buy a " + auto[-2].title()
print(buy_auto)
never_buy = "Never buy a " + auto[1].upper()
print(never_buy)
fast_car = "Very fast car this is " + auto[2].title() + "-GTR R35"
print(fast_car)

cars = ['honda', 'nissan', 'toyota', 'subaru']
print(cars)

cars[2] = 'mitsubishi'
print(cars)

cars.append('toyota')
print(cars)
cars.insert(1, 'ford')
print(cars)

del cars[1]
print(cars)

cars.insert(2, "doodge")
print(cars)

cars.pop()
print(cars)

car_pop = cars.pop(2)
print(cars)
print(car_pop)

last_owner = cars.pop()
message = "The last car I owned was a " + last_owner.title() + "."
print(message)

first_owned = cars.pop(0)
message = "The first car I owned was a " + first_owned.title() + "."
print(message)
print(cars)
cars.remove('mitsubishi')
print(cars)

too_expensive = 'nissan'
cars.remove(too_expensive)
message = "\n A " + too_expensive.title() + " is too expensive for me."
print(cars)
print(message)

#exercise 3-4
guests = ['Jon', 'bob', 'ken']
message = "Invitation message for "
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
# 3-5
guest_del = guests.pop(2)
print("Won't be able to come " + guest_del.title())
print(guests)
guests.insert(2, 'luk')
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
#3-6
guests.insert(0, 'jool')
guests.insert(2, 'tom')
guests.append('jerry')
print(guests)
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
print(message + guests[3].title())
print(message + guests[4].title())
print(message + guests[5].title())
#3-7
jerry = 'jerry'
guests.remove(jerry)
message_sorry = "I was sorry to cancel invitations for you "
print(message_sorry + jerry.title())

luk = 'luk'
guests.remove(luk)
print(message_sorry + luk.title())

last_guest = guests.pop()
print(message_sorry + last_guest.title())

last_guest = guests.pop()
print(message_sorry + last_guest.title())
print(guests)

print(message + guests[0].title())
print(message + guests[-1].title())

del guests[0]
del guests[0]

print(guests)