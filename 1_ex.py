def set_input() -> set:
    '''
    Read and parse a set of integers from user input.

    Prompts the user to enter a sequence of numbers separated by spaces,
    then converts them to a set of integers. If the input cannot be parsed
    as integers, returns an empty set and prints an error message.

    Returns:
        set: A set of integers parsed from user input, or an empty set
             if input validation fails.
    '''
    try:
        # Read space-separated numbers and convert to integers
        in_set = map(int, input('Enter numbers separated by spaces: ').split())
        return set(in_set)
    except ValueError as e:
        # Handle case when input contains non-numeric values
        print(f'Error - {e}')
        return set()


def numb_input() -> int | None:
    '''
    Read and parse a single natural number from user input.

    Prompts the user to enter a single integer. If the input cannot be
    parsed as an integer, returns None and prints an error message.

    Returns:
        int or None: The parsed integer if successful, None otherwise.
    '''
    try:
        numb = int(input('Enter a natural number: '))
        return numb
    except ValueError as e:
        # Handle case when input is not a valid integer
        print(f'Error - {e}')
        return None


def main() -> None:
    '''
    Main program execution.

    Reads a set of numbers and a single number from user input,
    then checks if the single number belongs to the set.

    The first line of input should contain natural numbers separated by spaces.
    The second line should contain a single natural number.

    Prints whether the number belongs to the set of numbers from first line.
    '''
    # Get the set of numbers from first line of input
    reference_set = set_input()

    # Get the single number to check from second line of input
    numb = numb_input()

    # Check membership and display result
    if numb in reference_set:
        print('The number belongs to the set')
    else:
        print('The number does not belong to the set')


if __name__ == '__main__':
    main()