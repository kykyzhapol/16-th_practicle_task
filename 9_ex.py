'''
Program to generate all K-element subsets (combinations) of a given set of natural numbers.

The first line contains a space-separated set of natural numbers (N elements).
The second line contains a natural number K (where K ≤ N).
The program generates and displays all possible K-element subsets.
'''

import sys
from itertools import combinations


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


def generate_all_subsets(numbers: set) -> list:
    '''
    Generate all subsets (power set) of the input set using recursion.

    This function implements a recursive backtracking algorithm to generate
    all possible subsets of the input set. The resulting list contains each
    subset as a Python set object.

    Args:
        numbers: Input set of numbers for which to generate all subsets.

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


def get_k_subsets() -> None:
    '''
    Generate and display all K-element subsets of the input set.

    Reads a set of numbers and a value K from user input,
    then generates all possible combinations of K elements
    from the input set using itertools.combinations.

    Validates that K does not exceed the size of the input set.
    Displays each K-element subset with its index in the list.
    '''
    # Read input data
    numbers = set(map(int, input('Enter a set of numbers separated by spaces: ').split()))
    
    try:
        k = int(input('Enter K (number of elements in each subset): '))
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)

    # Validate that K is not larger than the set size
    if k > len(numbers):
        print(f'Error: K ({k}) is greater than the number of elements ({len(numbers)})')
        return
    
    if k < 0:
        print('Error: K must be a non-negative number')
        return

    # Generate all K-element subsets using combinations from itertools
    # Convert the set to a sorted list for consistent ordering
    numbers_list = sorted(list(numbers))
    
    # combinations returns tuples, convert each to a set
    subsets = [set(combination) for combination in combinations(numbers_list, k)]

    # Display results
    print(f'\nAll {k}-element subsets (total {len(subsets)}):')
    for i, subset in enumerate(subsets, start=1):
        # Sort elements within each subset for consistent display
        print(f'{i}: {sorted(subset)}')


if __name__ == '__main__':
    get_k_subsets()