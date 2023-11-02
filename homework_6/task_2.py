# Поиск слиянием
# Используем функциональное программирование, потому что требуется рекурсия для реализации алгоритма, а также структурную и процедурную парадигмы программирования для построения логики и отображения результатов
def sortSplit(array):
    n = len(array)
    if n == 1 or n == 0:
        return array
    n //= 2
    arrLeft = sortSplit(array[0:n])
    arrRight = sortSplit(array[n:])

    leftN = rightN = k = 0
    result = [0] * (len(arrLeft) + len(arrRight))
    while leftN < len(arrLeft) and rightN < len(arrRight):
        if arrLeft[leftN] <= arrRight[rightN]:
            result[k] = arrLeft[leftN]
            leftN += 1
        else:
            result[k] = arrRight[rightN]
            rightN += 1
        k += 1
    while leftN < len(arrLeft):
        result[k] = arrLeft[leftN]
        leftN += 1
        k += 1
    while rightN < len(arrRight):
        result[k] = arrRight[rightN]
        rightN += 1
        k += 1
    return result

print(sortSplit([3,6,1,8,9,8,8]))