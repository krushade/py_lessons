nums = []
sqr_nums = []
cub_nums = []
mes = "To exit enter 'q'"
mes += "\nEnter any number: "


def decor(func):
    def wrapper(d_nums):
        print(f"nums: {d_nums}")
        for d_num in d_nums:
            d_num = int(d_num)
            cub_nums.append(d_num ** 3)
        func(d_nums)
        print(f"squares: {sqr_nums}")
        print(f"cubs: {cub_nums}")
        with open(input("Enter your file name: ") + ".txt", "w") as file:
            file.write(f"numbers: \t{d_nums}\n"
                       f"square numbers: \t{sqr_nums}\n"
                       f"cube numbers: \t{cub_nums}")
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
