'''
Program to find all prime numbers less than a given natural number n.

This program implements the Sieve of Eratosthenes algorithm using sets
to efficiently find all prime numbers less than a user-specified limit.
'''

import sys


def in_numb() -> int:
    '''
    Read and validate a natural number from user input.

    Prompts the user to enter a natural number greater than 1.
    If the input is invalid or less than or equal to 1, prints an error
    message and exits the program.

    Returns:
        int: A validated natural number greater than 1.

    Raises:
        SystemExit: If input is not a valid integer or is ≤ 1.
    '''
    try:
        numb = int(input('Enter a natural number greater than 1: '))
        
        # Validate that the number is greater than 1
        # (since prime numbers start from 2)
        if numb <= 1:
            print('Number must be greater than 1')
            sys.exit(1)
            
        return numb
        
    except ValueError as e:
        # Handle case when input is not a valid integer
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def sieve_eratosthenes(limit: int) -> set[int]:
    '''
    Find all prime numbers less than the given limit using the Sieve of Eratosthenes.

    Implements the classic Sieve of Eratosthenes algorithm using set operations
    for efficiency. Starting with all numbers from 2 to limit-1, iteratively
    removes multiples of each prime number found.

    Args:
        limit: The upper bound (exclusive) for finding prime numbers.

    Returns:
        set[int]: A set containing all prime numbers less than the limit.
    '''
    # Create a set of all candidate numbers from 2 to limit-1
    # 2 is the first prime number, so we start from there
    numbers = set(range(2, limit))

    # Iterate up to the square root of limit
    # Any composite number ≤ limit will have a factor ≤ sqrt(limit)
    for i in range(2, int(limit ** 0.5) + 1):
        
        # If i is still in the set, it's prime
        if i in numbers:
            # Remove all multiples of i starting from i*i
            # Multiples smaller than i*i have already been removed
            # by smaller prime factors
            multiples = set(range(i * i, limit, i))
            numbers -= multiples  # Set difference operation

    return numbers


def main() -> None:
    '''
    Main program execution.

    Reads a natural number from the user, finds all prime numbers less than it
    using the Sieve of Eratosthenes, and displays the results.
    '''
    # Get the upper limit from user
    n = in_numb()
    
    # Find all prime numbers less than n
    primes = sieve_eratosthenes(n)

    # Display the results in sorted order
    print(f'Prime numbers less than {n}:')
    print(*sorted(primes))


if __name__ == '__main__':
    main()