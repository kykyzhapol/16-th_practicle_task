'''
TODO:
В первой строке задается множество натуральных чисел, разделенных пробелом.
Их количество N. Во второй строке вводится натуральное число K (K≤N).
Получите список всех K-элементных подмножеств для заданного множества.
'''
import sys


def in_numb() -> set:
    '''
    Function for taking int number from console
    :return:
    numb
    '''
    try:
        numb = map(int, input('Enter set of natural number ->').split())
        return set(numb)
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def generate_subsets(nums: set) -> list:
    '''
    Generate all subsets using recursion
    :param nums: input set of numbers
    :return: list of all subsets (each subset is a set)
    '''
    # Преобразуем множество в список для удобства индексации
    nums_list = sorted(list(nums))
    result = []

    def recursive_subsets(current_subset: set, index: int):
        '''
        Recursive helper function
        :param current_subset: current subset being built
        :param index: current index in nums_list
        '''
        # Добавляем текущее подмножество в результат
        # Используем frozenset для хранения, но для вывода преобразуем в set
        result.append(set(current_subset))

        # Проходим по оставшимся элементам
        for i in range(index, len(nums_list)):
            # Добавляем текущий элемент в подмножество
            current_subset.add(nums_list[i])
            # Рекурсивно генерируем подмножества с этим элементом
            recursive_subsets(current_subset, i + 1)
            # Убираем элемент (backtracking)
            current_subset.remove(nums_list[i])

    # Начинаем с пустого множества и индекса 0
    recursive_subsets(set(), 0)
    return result


from itertools import combinations


def get_k_subsets():
    # Ввод данных
    numbers = set(map(int, input("Введите множество чисел: ").split()))
    k = int(input("Введите K: "))

    # Проверка
    if k > len(numbers):
        print(f"Ошибка: K ({k}) больше количества элементов ({len(numbers)})")
        return

    # Генерация всех K-элементных подмножеств
    numbers_list = sorted(list(numbers))
    subsets = [set(combo) for combo in combinations(numbers_list, k)]

    # Вывод результата
    print(f"\nВсе {k}-элементные подмножества:")
    for i, subset in enumerate(subsets, 1):
        print(f"{i}: {sorted(list(*subset))}")


if __name__ == "__main__":
    get_k_subsets()