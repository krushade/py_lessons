num_1 = int(input("x = "))
num_2 = int(input("y = "))
if num_1 < 0 or num_2 < 0:
    raise Exception("Num is incorrect")
sign = input("pls enter /, *, +, -: ")
if sign not in ['/', '*', '+', '-']:
    raise Exception("Sign is incorrect")
if sign == '/':
    try:
        answer = num_1 / num_2
        print(answer)
    except ZeroDivisionError as z:
        print(z)
    finally:
        print("Next time try harder")
elif sign == '*':
    answer = num_1 * num_2
    print(answer)
elif sign == '+':
    answer = num_1 + num_2
    print(answer)
elif sign == '-':
    print(num_1 - num_2)