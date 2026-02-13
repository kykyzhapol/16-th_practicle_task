from itertools import permutations
'''
TODO:
В строке задается множество натуральных чисел, разделенных пробелом.
Получите все перестановки этого множества в лексикографическом порядке. 

Подсказка: Найдите и используйте соответствующий метод из модулей Python.
'''


def main() -> None:
    input_string = input("Введите натуральные числа через пробел: ")
    numbers = list(map(int, input_string.split()))

    # Убираем дубликаты перестановок
    unique_perms = sorted(set(permutations(numbers)))

    print("\nВсе уникальные перестановки в лексикографическом порядке:")
    for perm in unique_perms:
        print(*perm)


if __name__ == '__main__':
    main()