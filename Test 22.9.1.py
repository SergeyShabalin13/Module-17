array = [int(x) for x in input('Введите положительные целые числа через пробел: ').split()]
array = (sorted(array))
print(array)

while True:
    try:
        element = int(input('Введите положительное целое число из полученного списка: '))
        if element < min(array) or element > max(array):
            print('Указанное число не входит в диапазон списка')
        if element <= 0:
            raise Exception
        break
    except ValueError:
        print('Нужно ввести целое число')
    except Exception:
        print('Нужно ввести положительное число')

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
print(binary_search(array, element, 0, len(array) - 1))