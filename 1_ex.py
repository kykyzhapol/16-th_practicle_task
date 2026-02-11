def set_input() -> set:
    '''
    Correctly take data from console in right format (from TODO)
    :return:
    in_set
    '''
    try:
        in_set = map(int, input('Enter number\'s set throaty space').split())
        return set(in_set)
    except ValueError as e:
        print(f'Error - {e}')
        return set()


def numb_input() -> int | None:
    '''
    Correctly take data from console in right format (from TODO)
    :return:
    in_numb or None
    '''
    try:
        numb = int(input('Enter natural number'))
        return numb
    except ValueError as e:
        print(f'Error - {e}')
        return None


def main():
    '''
    The first line contains a sequence of natural numbers, separated by spaces.
    The second line contains a single number.
    TODO:Check if the number specified in the second line
    belongs to the set of repeating numbers.
    :return:
    '''
    reference_set = set_input()
    numb = numb_input()
    if numb in reference_set:
        print('The number belongs to the set')
    else:
        print('The number does not belong to the set')


if __name__ == '__main__':
    main()