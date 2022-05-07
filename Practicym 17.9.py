t_array = input('Введите последовательность чисел через пробел (от 0 до 100): ')
s_array = t_array.split()
array = list(map(int, s_array))
n = int(input('Введите контрольное число для поиска: '))
def sort_insert(array):
    for i in range(1, len(array)):
        x = array[i]
        ix = i
        while ix > 0 and array[ix-1] > x:
             array[ix] = array[ix-1]
             ix -= 1
        array[ix] = x
    return array
print('Отсортированная последовательность: ', sort_insert(array))
def binary_search(array, n, left, right):
    if left > right:
        return print('Данного числа нет в последовательности')
    middle = (right+left) // 2
    if array[middle] == n:
        print('Номер позиции элемента, который меньше введенного пользователем числа:', middle-1)
    elif n < array[middle]:
        return binary_search(array, n, left, middle-1)
    else:
        return binary_search(array, n, middle+1, right)
binary_search(array, n, 0, len(array))