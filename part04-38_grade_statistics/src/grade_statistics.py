# Write your solution here


def calc_exercise_points(exercse_count):
    return exercse_count // 10


def calc_total_points(exam_points, exercise_points):
    return exam_points + exercise_points


def calc_grade_points(exam_points, total_points):
    if exam_points < 10 or total_points <= 14:
        return "0"
    elif total_points in range(15, 18):
        return "1"
    elif total_points in range(18, 21):
        return "2"
    elif total_points in range(21, 24):
        return "3"
    elif total_points in range(24, 28):
        return "4"
    elif total_points in range(28, 31):
        return "5"
    else:
        return "0"


def get_marks():
    marks = []

    while True:
        mark = input("Exam points and exercises completed: ")
        if mark == "":
            break
        exam_points, exercise_count = list(map(int, mark.split()))
        marks.append({"exam_points": exam_points, "exercise_count": exercise_count})

    return marks


mark_list = get_marks()
student_count = len(mark_list)
pass_count = 0
sum_of_points = 0
grade_distribution = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0, "0": 0}

for marks in mark_list:

    # Calculate exercise points and total points
    exercise_points = calc_exercise_points(marks["exercise_count"])
    total_points = calc_total_points(marks["exam_points"], exercise_points)
    marks.update(
        {
            "exercise_points": exercise_points,
            "total_points": total_points,
        }
    )

    # Calculating stats
    sum_of_points += marks["total_points"]
    grade = calc_grade_points(marks["exam_points"], marks["total_points"])
    grade_distribution[grade] += 1
    if int(grade) > 0:
        pass_count += 1

points_average = round((sum_of_points / student_count), 1)
pass_percentage = round((pass_count / student_count) * 100, 1)

# print stats

print("Statistics:")
print(f"Points average: {points_average}")
print(f"Pass percentage: {pass_percentage}")
print("Grade distribution:")
for key, value in grade_distribution.items():
    print(f"  {key}: {'*'*value}")
