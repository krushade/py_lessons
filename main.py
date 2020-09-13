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
