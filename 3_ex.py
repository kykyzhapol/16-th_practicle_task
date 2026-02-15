'''
Program to find food items that only Sladkoeshkin likes.

The first line contains Sladkoeshkin's preferences (space-separated).
The second line contains a natural number N - the number of Sladkoeshkin's friends.
The next N lines contain preferences of each friend.
The program determines how many food items are liked only by Sladkoeshkin.
'''

import sys


def slad_like() -> set | None:
    '''
    Read and parse Sladkoeshkin's food preferences from user input.

    Prompts the user to enter Sladkoeshkin's favorite foods separated by spaces.
    Converts all items to lowercase for case-insensitive comparison.
    If input cannot be parsed, prints an error message and exits the program.

    Returns:
        set | None: A set of lowercase food items that Sladkoeshkin likes,
                   or None if the program exits due to an error.
    '''
    try:
        like = input('What does Sladkoeshkin really like?: ').split()
        # Convert to lowercase for case-insensitive comparison
        return {x.lower() for x in like}
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def friends_like() -> set | None:
    '''
    Read and parse a single friend's food preferences from user input.

    Prompts the user to enter one friend's favorite foods separated by spaces.
    Converts all items to lowercase for case-insensitive comparison.
    If input cannot be parsed, prints an error message and returns None.

    Returns:
        set | None: A set of lowercase food items that the friend likes,
                   or None if input validation fails.
    '''
    try:
        like = input('What does Sladkoeshkin\'s friend like?: ').split()
        # Convert to lowercase for case-insensitive comparison
        return {x.lower() for x in like}
    except ValueError as e:
        print(f'Error - {e}')
        return None


def main() -> None:
    '''
    Main program execution.

    Reads Sladkoeshkin's preferences, the number of friends,
    and each friend's preferences. Then calculates and displays
    how many food items are liked exclusively by Sladkoeshkin.
    '''
    # Get Sladkoeshkin's preferences
    slad_set = slad_like()
    
    # Get number of friends
    try:
        n = int(input('How many friends does Sladkoeshkin have? -> '))
    except ValueError as e:
        print(f'Error - {e}')
        sys.exit(1)
    
    # Collect all friends' preferences using union
    friends = set()
    for _ in range(n):
        friend_preferences = friends_like()
        if friend_preferences is not None:
            friends = friends.union(friend_preferences)
    
    # Calculate and display items liked only by Sladkoeshkin
    # Set difference: items in slad_set but not in friends
    only_slad_items = slad_set - friends
    print(f'Number of products only Sladkoeshkin likes -> {len(only_slad_items)}')


if __name__ == '__main__':
    main()