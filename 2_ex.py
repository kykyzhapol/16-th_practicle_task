def number_of_courses() -> int | None:
    '''
    Read and parse the number of facultative courses from user input.

    Prompts the user to enter an integer representing the number of courses.
    If the input cannot be parsed as an integer, returns None and prints
    an error message.

    Returns:
        int or None: The parsed number of courses if successful, None otherwise.
    '''
    try:
        numb = int(input('Enter number of facultative courses: '))
        return numb
    except ValueError as e:
        print(f'Error - {e}. Program finished')
        return None


def course_set() -> set:
    '''
    Read and parse a set of course names from user input.

    Prompts the user to enter course names separated by spaces.
    Returns a set of the entered course names. If input cannot be parsed,
    returns an empty set and prints an error message.

    Returns:
        set: A set of course names from user input, or an empty set
             if input validation fails.
    '''
    try:
        courses = input('Enter courses separated by spaces: ').split()
        return set(courses)
    except ValueError as e:
        print(f'Error - {e}')
        return set()


def main() -> None:
    '''
    Main program execution.

    Reads the number of students and their chosen facultative courses,
    then determines the set of all courses selected by all students.

    The first line of input contains a natural number N - the number of students.
    The next N lines contain facultative courses chosen by each student,
    with courses separated by spaces.

    Prints the complete set of all courses selected across all students.
    '''
    # Get the number of students from first line of input
    course_range = number_of_courses()

    # Initialize empty set to store all courses
    all_courses = set()

    # Process each student's course selections if valid input was received
    if isinstance(course_range, int):
        for _ in range(course_range):
            # Add current student's courses to the overall set
            all_courses = all_courses.union(course_set())

        # Display the final set of all courses
        print(f'Set of all courses: {all_courses}')
    else:
        # Silently exit if number of courses couldn't be parsed
        pass


if __name__ == '__main__':
    main()