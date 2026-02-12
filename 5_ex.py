'''
TODO:
Для заданного натурального числа n определить все простые числа меньшие n.
Для решения задачи использовать алгоритм решета Эратосфена и множества.
'''
import sys


def in_numb() -> int:
    '''
    Function for taking int number from console
    :return:
    numb
    '''
    try:
        numb = int(input('Enter natural number ->'))
        if numb <= 1:
            print('Number must be greater than 1')
            sys.exit(1)
        return numb
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def sieve_eratosthenes(n: int) -> set[int]:
    '''
    Implementation of Sieve of Eratosthenes using sets
    :param n: upper limit
    :return: set of prime numbers less than n
    '''
    # Create a set of all numbers from 2 to n-1
    numbers = set(range(2, n))

    # For each prime number, remove its multiples
    for i in range(2, int(n ** 0.5) + 1):
        if i in numbers:
            # Remove all multiples of i
            multiples = set(range(i * i, n, i))
            numbers -= multiples

    return numbers


def main() -> None:
    n = in_numb()
    primes = sieve_eratosthenes(n)

    print(f"Prime numbers less than {n}:")
    print(*sorted(primes))


if __name__ == "__main__":
    main()
