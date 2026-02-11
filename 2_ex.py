def number_of_courses() -> int | None:
    try:
        numb = int(input('Enter number of facultative courses: '))
        return numb
    except ValueError as e:
        print(f'Error - {e}. Program finished')
        return None


def course_set() -> set:
    try:
        courses = input('enter courses: ').split()
        return set(courses)
    except ValueError as e:
        print(f'Error - {e}')
        return set()


def main():
    '''
    В первой строке указывается натуральное число N - количество студентов.
    В последующих N строках указываются факультативные курсы, которые выбрал каждый студент.
    Курсы указываются через пробел. Определите сколько курсов выбрали все студенты
    :return:
    '''
    course_range = number_of_courses()
    all_courses = set()
    if type(course_range) == int:
        for _ in range(course_range):
            all_courses = all_courses.union(course_set())
        print(f'Set all courses: {all_courses}')
    else:
        pass


if __name__ == '__main__':
    main()