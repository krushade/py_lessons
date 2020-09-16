if __name__ == '__main__':
    all_nums = [num for num in range(100, 1001)]
    even_nums = []
    def even():
        for even_num in all_nums:
            if even_num % 2 == 0:
                even_nums.append(even_num)
        return even_nums
    print(even())