if __name__ == "__main__":
    all_nums = [num for num in range(100, 1001)]
    def even(numbers):
        even_nums = []
        for even_num in numbers:
            if even_num % 2 == 0:
                even_nums.append(even_num)
        even_nums.reverse()
        return even_nums
    print(even(all_nums))