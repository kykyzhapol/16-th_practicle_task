'''
Program to solve the cryptarithmetic puzzle: ХОД + ХОД + ХОД = МАТ

Each letter represents a unique digit (0-9). The equation means 3 * X = Y,
where X and Y are three-digit numbers, and they share no common digits.
'''


def main() -> None:
    '''
    Solve the cryptarithmetic puzzle ХОД + ХОД + ХОД = МАТ.

    The program iterates through all possible three-digit numbers for X (ХОД)
    and Y (МАТ), checking two conditions:
    1. 3 * X equals Y
    2. X and Y have no digits in common (each letter represents a unique digit)

    Prints all valid solutions where both conditions are satisfied.
    '''
    # Generate all possible three-digit numbers (100 to 999)
    solution_space = [x for x in range(100, 1000)]

    # Iterate through all possible values for X and Y
    for x in solution_space:
        for y in solution_space:
            # Convert numbers to sets of their digits for comparison
            # Example: 123 becomes {'1', '2', '3'}
            x_digits = {digit for digit in str(x)}
            y_digits = {digit for digit in str(y)}

            # Check both conditions:
            # 1. Three times X equals Y (3 * ХОД = МАТ)
            # 2. X and Y have no common digits (all letters represent different digits)
            if 3 * x == y and not (x_digits & y_digits):
                print(f'{x}+{x}+{x}={y}')


if __name__ == '__main__':
    main()