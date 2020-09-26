numbers = [1, 21, 51, 28, 11, 32, 35, 21, 15, 1, 11, 32, 78, 2, 21, 51, 38, 14, 21, 1, 21, 1, 35]
nums_sorted = {}
for num in numbers:
    nums_sorted[num] = numbers.count(num)

if __name__ == '__main__':
    print(nums_sorted)