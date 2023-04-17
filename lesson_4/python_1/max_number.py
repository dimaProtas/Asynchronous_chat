# Вариант №2
def f_max(a, b, c):
    result = max([a, b, c])
    return result


if __name__ == '__main__':
    namber1 = int(input('Введите первое числоэ: '))
    namber2 = int(input('Введите второе числоэ: '))
    namber3 = int(input('Введите третье числоэ: '))

    print(max(namber1, namber2, namber3))


    result = f_max(1, 5, 6)
    print(result)
