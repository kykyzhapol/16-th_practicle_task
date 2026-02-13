'''
TODO:
В строке задается множество натуральных чисел, разделенных пробелом.
Получите список всех подмножеств для заданного множества.
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


def main():
    # Получаем множество чисел от пользователя
    numbers = in_numb()

    print(f"Исходное множество: {numbers}")

    # Генерируем все подмножества
    subsets = generate_subsets(numbers)

    print(f"\nВсе подмножества (всего {len(subsets)}):")
    for subset in subsets:
        if subset:  # Если подмножество не пустое
            print(sorted(list(subset)))
        else:  # Пустое множество
            print("∅")  # или можно вывести "[]"


if __name__ == "__main__":
    main()