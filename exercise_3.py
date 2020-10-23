numbers = [1, 21, 51, 28, 11, 32, 35, 21, 15, 1, 11, 32,
           78, 2, 21, 51, 38, 14, 21, 1, 21, 1, 35]
numbers_2 = [1, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6, 1, 1, 1, 5]


def sort(nums):
    nums_sorted = {}
    for num in nums:
        nums_sorted[num] = nums.count(num)
    return nums_sorted


if __name__ == '__main__':
    print(sort(numbers))
    print(sort(numbers_2))
