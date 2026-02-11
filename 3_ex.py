'''
TODO:
То что нравится Сладкоежкину, записано через пробел в первой строке.
В следующей строке указано натуральное число N - количество друзей Сладкоежкина.
В следующих N строках находятся предпочтения каждого из его друзей.
Определите сколько наименований продуктов нравится только Сладкоежкину
'''
import sys


def slad_like() -> set | None:
    try:
        like = input('What Sladkoeshkin really like?: ').split()
        return {x.lower() for x in like}
    except ValueError as e:
        print(f'Error - {e}. Program finished.')
        sys.exit(1)


def friends_like() -> set | None:
    try:
        like = input('What Sladkoeshkin\'s friend like?: ').split()
        return {x.lower() for x in like}
    except ValueError as e:
        print(f'Error - {e}')
        return None


def main() -> None:
    slad_set = slad_like()
    try:
        n = int(input('How much friend have Sladkoeshkin ->'))
    except ValueError as e:
        print(f'Error - {e}')
        sys.exit(1)
    friends = set()
    for _ in range(n):
        friends = friends.union(friends_like())

    print(f'Only Sladkoeshkin\'s favorit product -> {len(slad_set - friends)}')


if __name__ == '__main__':
    main()
