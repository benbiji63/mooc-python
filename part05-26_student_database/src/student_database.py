# Write your solution here

# First create a dictionary of dictionaries with name as key, the internal dictionaries consists of
# A list called courses_completed which is made of  a dictionaries with key course name and value grade


def calc_avg_grade(courses_completed: list, no_of_courses: int):
    total_grade = 0
    for course_name, grade in courses_completed.items():
        total_grade += grade
    return total_grade / no_of_courses


def add_student(students: dict, name: str):
    if name not in students:
        students[name] = {"courses_completed": {}, "no_of_courses": 0, "avg_grade": 0}


def print_student(students: dict, name: str):
    if name in students:
        student = students[name]
        # print(student)
        no_of_courses = student["no_of_courses"]
        courses_completed = student["courses_completed"]
        # print(f"{name}:")
        print(f"{name}:")
        if no_of_courses > 0:
            failed_course_count = int(sum(map(lambda x: x == 0, courses_completed)))
            print(f" {no_of_courses-failed_course_count} completed courses:")
            for course_name, course_grade in courses_completed.items():
                if course_grade != 0:
                    print(f"  {course_name} {course_grade}")
            if student["avg_grade"] != 0:
                print(f" average grade {student['avg_grade']}")
        else:
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")


def add_course(students: dict, name: str, course_info: tuple):
    if name not in students:
        add_student(students, name)

    student = students[name]
    courses_completed = student["courses_completed"]
    course_name = course_info[0]
    course_grade = course_info[1]
    if course_grade == 0:
        return
    if course_name not in courses_completed.keys():
        courses_completed[course_name] = course_grade
    else:
        # If a course with same name exist this finds its index
        max_grade = max(course_grade, courses_completed[course_name])
        courses_completed[course_name] = max_grade
        student["no_of_courses"] -= 1
    student["no_of_courses"] = student["no_of_courses"] + 1
    student["avg_grade"] = calc_avg_grade(courses_completed, student["no_of_courses"])


def summary(students: dict):
    no_of_students = len(students)
    most_course_student = ""
    most_course_count = 0
    highest_average_grade_student = ""
    highest_average_grade = 0
    for key in students:
        student = students[key]
        course_count = len(student["courses_completed"])
        average_grade = student["avg_grade"]
        if course_count > most_course_count:
            most_course_student = key
            most_course_count = course_count
        if average_grade > highest_average_grade:
            highest_average_grade_student = key
            highest_average_grade = average_grade
    print(f"students {no_of_students}")
    print(f"most courses completed {most_course_count} {most_course_student}")
    print(f"best average grade {highest_average_grade} {highest_average_grade_student}")


# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# # print_student(students, "Peter")
# summary(students)

# students = {}
# add_student(students, "Emily")
# add_student(students, "Peter")
# add_course(students, "Emily", ("Introduction to Programming", 5))
# add_course(students, "Emily", ("Introduction to Databases", 4))
# add_course(students, "Peter", ("Data Structures and Algorithms", 3))
# print_student(students, "Emily")

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Software Development Methods", 5))
# add_course(students, "Peter", ("Software Development Methods", 1))
# print_student(students, "Peter")


# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Software Development Methods", 1))
# add_course(students, "Peter", ("Software Development Methods", 5))
# print_student(students, "Peter")
