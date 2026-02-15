'''
Program to generate all unique permutations of a set of natural numbers.

The program reads a space-separated string of natural numbers,
then generates and displays all unique permutations in lexicographic order.
'''

from itertools import permutations


def main() -> None:
    '''
    Generate and display all unique permutations of input numbers.

    Reads a space-separated string of natural numbers from user input,
    converts them to integers, and generates all unique permutations
    in lexicographic (sorted) order.

    The program handles duplicate numbers in input by generating only
    unique permutations, avoiding duplicate output.

    Returns:
        None
    '''
    # Read input string and convert to list of integers
    input_string = input('Enter natural numbers separated by spaces: ')
    numbers = list(map(int, input_string.split()))

    # Generate all permutations and remove duplicates using set
    # Then sort them lexicographically
    unique_perms = sorted(set(permutations(numbers)))

    # Display results
    print('\nAll unique permutations in lexicographic order:')
    for perm in unique_perms:
        # Use * operator to unpack the tuple for printing
        print(*perm)


if __name__ == '__main__':
    main()