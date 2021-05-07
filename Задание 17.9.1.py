a = input('Введите последовательность чисел через пробел:').split()
array = list(map(int, a))
left = 1
right = len(array)


def sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def binary_search(array, numb, left, right):
    middle = (right + left) // 2
    if array[middle] == numb:
    elif numb < array[middle]:
        return binary_search(array, numb, left, middle - 1)
    else:
        return binary_search(array, numb, middle + 1, right)

    x = array[: middle]
    for i in x:
        if i == numb:
            x.remove(numb)
    index_1 = (len(x) - 1)
    y = array[middle:]
    for n in y:
        if n <= numb and len(y) > 1:
            y.remove(n)
    f = y[0]
    index_2 = array.index(f)
    if index_1 < 0:
        print(index_2)
    elif index_2 > len(array) - 1:
        print(index_1)
    else:
        print(index_1, index_2)
        return index_1, index_2

