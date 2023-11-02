# Бинарный поиск
# Используем функциональное программирование, потому что требуется рекурсия для реализации алгоритма, а также структурную и процедурную парадигмы программирования для построения логики и отображения результатов
def find(array, n):
    i = len(array) // 2
    if array[i] == n:
        return i
    elif i == 0:
        return -1
    if array[i] < n:
        return i + find(array[i:], n)
    elif array[i] > n:
        return find(array[0:i], n)
    else:
        return -1
    
print(find([1,2,3,4,5], 4))
print(find([1,2,3,4,5], 1))
print(find([1,2,3,4,5], 3))
print(find([1,2,3,4,5], 0))
print(find([1,3,3,3,5], 3))