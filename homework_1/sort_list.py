def sort_list_imperative(numbers):
    # Имеративный код здесь
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def sort_list_declarative(numbers):
    # Декларативный код здесь
    numbers.sort()


my_list = [4, 5, 1, 2, 3]
sort_list_declarative(my_list)
print(my_list)  # [1, 2, 3, 4, 5]

my_list = [4, 5, 1, 2, 3]
my_list = sort_list_imperative(my_list)
print(my_list)  # [1, 2, 3, 4, 5]