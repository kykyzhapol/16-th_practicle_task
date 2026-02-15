'''
Program to generate all subsets (power set) of a given set of natural numbers.

The program reads a space-separated string of natural numbers,
then generates and displays all possible subsets of the input set.
'''

import sys


def in_numb() -> set:
    '''
    Read and parse a set of natural numbers from user input.

    Prompts the user to enter space-separated natural numbers,
    converts them to integers, and returns them as a set.
    If input cannot be parsed as integers, prints an error message
    and exits the program.

    Returns:
        set: A set of natural numbers parsed from user input.

    Raises:
        SystemExit: If input cannot be parsed as valid integers.
    '''
    try:
        numbers = map(int, input('Enter a set of natural numbers separated by spaces: ').split())
        return set(numbers)
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def generate_subsets(numbers: set) -> list:
    '''
    Generate all subsets (power set) of the input set using recursion.

    This function implements a recursive backtracking algorithm to generate
    all possible subsets of the input set. The resulting list contains each
    subset as a Python set object.

    Args:
        numbers: Input set of numbers for which to generate subsets.

    Returns:
        list: A list containing all subsets of the input set.
              Each subset is represented as a set.
    '''
    # Convert set to sorted list for consistent indexing
    # Sorting ensures subsets are generated in a predictable order
    numbers_list = sorted(list(numbers))
    result = []

    def recursive_subsets(current_subset: set, index: int):
        '''
        Recursive helper function to build subsets.

        Uses backtracking to explore all possible combinations of elements
        starting from the given index.

        Args:
            current_subset: The subset being built in the current recursion branch
            index: The starting index in numbers_list to consider for adding elements
        '''
        # Add the current subset to the result
        # We create a new set copy to avoid later modifications
        result.append(set(current_subset))

        # Iterate through remaining elements starting from current index
        for i in range(index, len(numbers_list)):
            # Add current element to the subset
            current_subset.add(numbers_list[i])

            # Recursively generate subsets that include this element
            recursive_subsets(current_subset, i + 1)

            # Remove the element (backtracking) to try other combinations
            current_subset.remove(numbers_list[i])

    # Start recursion with empty set and index 0
    recursive_subsets(set(), 0)

    return result


def main() -> None:
    '''
    Main program execution.

    Reads a set of numbers from user input, generates all possible subsets
    (power set), and displays them along with the total count.
    '''
    # Get input set from user
    numbers = in_numb()

    print(f'Original set: {numbers}')

    # Generate all subsets
    subsets = generate_subsets(numbers)

    print(f'\nAll subsets (total {len(subsets)}):')

    # Display each subset
    for subset in subsets:
        if subset:  # Non-empty subset
            # Sort elements for consistent display
            print(sorted(subset))
        else:  # Empty set
            print('∅')  # Empty set symbol


if __name__ == '__main__':
    main()