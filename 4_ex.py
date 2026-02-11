'''
TODO:
В двух строках представлены элементы двух множеств.
Элементы разделены пробелами. В третьей строке указано одно число.
Определить принадлежит ли значение, расположенное в третьей строке пересечению этих множеств.
'''
import sys


def num_set(n: int) -> set:
    try:
        num = map(float, input(f'Enter the elements of the {n} set ->').split())
        return set(num)
    except ValueError as e:
        print(f'Error - {e}')
        return set()


def reference() -> float:
    try:
        num = float(input('Enter reference number ->'))
        return num
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def main() -> None:
    set_1 = num_set(1)
    set_2 = num_set(2)
    numb = reference()
    set_1_and_2 = set_1 & set_2
    if numb in set_1_and_2:
        print('The reference value belongs to the intersection of sets')
    else:
        print('The reference value does not belong to the intersection of sets')


if __name__ == '__main__':
    main()
