nums = []
sqr_nums = []
cub_nums = []
mes = "To exit enter 'q'"
mes += "\nEnter any number: "


def decor(func):
    def wrapper(*numbers):
        print(nums)
        numbers = list(numbers)
        for number in numbers:
            number = int(number)
            cub_nums.append(number ** 3)
        func()
    return wrapper


@decor
def square(numbers):
    for number in numbers:
        number = int(number)
        sqr_nums.append(number * number)


if __name__ == '__main__':
    while True:
        num = input(mes)
        if num == 'q':
            break
        elif num.isdigit() is True:
            nums.append(num)
        else:
            print("Wrong data!")

    square(nums)
    print(nums)
    print(sqr_nums)
    print(cub_nums)
