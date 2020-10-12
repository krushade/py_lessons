nums = []
sqr_nums = []
cub_nums = []
mes = "To exit enter 'q'"
mes += "\nEnter any number: "


def decor(func):
    def wrapper(nums):
        print(f"nums: {nums}")
        for num in nums:
            num = int(num)
            cub_nums.append(num ** 3)
        func(nums)
        print(f"squares: {sqr_nums}")
        print(f"cubs: {cub_nums}")
    return wrapper


# @decor
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
