'''
Program to check if a value belongs to the intersection of two sets.

The first two lines contain elements of two sets (space-separated).
The third line contains a single number.
The program determines if the number from the third line belongs to the
intersection of the two sets.
'''

import sys


def num_set(set_number: int) -> set:
    '''
    Read and parse a set of numbers from user input.

    Prompts the user to enter space-separated elements for a specified set,
    converts them to floating-point numbers, and returns them as a set.
    If input cannot be parsed as numbers, returns an empty set and prints
    an error message.

    Args:
        set_number: The number identifier of the set (1 or 2) for display purposes.

    Returns:
        set: A set of floating-point numbers parsed from user input,
             or an empty set if input validation fails.
    '''
    try:
        # Read space-separated numbers and convert to float
        numbers = map(float, input(f'Enter the elements of set {set_number}: ').split())
        return set(numbers)
    except ValueError as e:
        # Handle case when input contains non-numeric values
        print(f'Error - {e}')
        return set()


def reference() -> float:
    '''
    Read and parse a reference number from user input.

    Prompts the user to enter a single floating-point number.
    If the input cannot be parsed as a number, prints an error message
    and exits the program.

    Returns:
        float: The parsed reference number.

    Raises:
        SystemExit: If input cannot be parsed as a valid number.
    '''
    try:
        reference_num = float(input('Enter reference number: '))
        return reference_num
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def main() -> None:
    '''
    Main program execution.

    Reads two sets of numbers and a reference number from user input,
    then checks if the reference number belongs to the intersection
    of the two sets.
    
    The first two lines should contain space-separated numbers.
    The third line should contain a single number to check.
    
    Prints whether the reference number is in the intersection of the two sets.
    '''
    # Read the two sets from user input
    set_1 = num_set(1)
    set_2 = num_set(2)
    
    # Read the reference number to check
    reference_num = reference()
    
    # Calculate the intersection of the two sets
    # Using the & operator as a shorthand for set.intersection()
    set_intersection = set_1 & set_2
    
    # Check membership in the intersection and display result
    if reference_num in set_intersection:
        print('The reference value belongs to the intersection of sets')
    else:
        print('The reference value does not belong to the intersection of sets')


if __name__ == '__main__':
    main()