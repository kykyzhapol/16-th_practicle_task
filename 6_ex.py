'''
Напишите программу для расшифровки равенства ХОД+ХОД+ХОД=МАТ, где буквам должны соответствовать цифры
3*x=y and x!=y and len(x) == len(y) == 3
'''


def main() -> None:
    solution_space = [x for x in range(100, 1000)]
    for x in solution_space:
        for y in solution_space:
            x_num = {x1 for x1 in str(x)}
            y_num = {y1 for y1 in str(y)}
            if 3*x == y and not x_num & y_num:
                print(f'{x}+{x}+{x}={y}')


if __name__ == '__main__':
    main()