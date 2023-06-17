from collections import defaultdict
from statistics import mean
def process_students(students):
    students_by_course = defaultdict(list)
    average_score_by_group = defaultdict(lambda: defaultdict(list))
    oldest_student = min(students, key=lambda s: s['birth_year'])
    youngest_student = max(students, key=lambda s: s['birth_year'])
    best_student_by_group = {}

    for student in students:
        students_by_course[student['course']].append(student)
        for subject, grade in student['grades'].items():
            average_score_by_group[student['group']][subject].append(grade)

    for course, students in students_by_course.items():
        students.sort(key=lambda s: (s['surname'], s['name'], s['patronymic']))

    for group, subjects in average_score_by_group.items():
        average_score_by_group[group] = {subject: round(mean(grades), 2) for subject, grades in subjects.items()}

    for group, students in students_by_course.items():
        best_student_by_group[group] = max(students, key=lambda s: mean(s['grades'].values()))

    return {
        "students_by_course": students_by_course,
        "average_score_by_group": average_score_by_group,
        "oldest_student": oldest_student,
        "youngest_student": youngest_student,
        "best_student_by_group": best_student_by_group
    }

students = [
    {'surname': 'Ivanov', 'name': 'Ivan', 'patronymic': 'Ivanovich', 'birth_year': 1999, 'course': 3, 'group': '3A', 'grades': {'math': 5, 'physics': 4, 'history': 3}},
    {'surname': 'Petrov', 'name': 'Petr', 'patronymic': 'Petrovich', 'birth_year': 2000, 'course': 2, 'group': '2B', 'grades': {'math': 4, 'physics': 5, 'history': 4}},
    {'surname': 'Sidorov', 'name': 'Sidor', 'patronymic': 'Sidorovich', 'birth_year': 1998, 'course': 3, 'group': '3A', 'grades': {'math': 3, 'physics': 3, 'history': 5}},
    {'surname': 'Nikolaev', 'name': 'Nikolay', 'patronymic': 'Nikolaevich', 'birth_year': 2001, 'course': 2, 'group': '2B', 'grades': {'math': 5, 'physics': 5, 'history': 5}},
{'surname': 'Kalinin', 'name': 'Nikolay', 'patronymic': 'Nikolaevich', 'birth_year': 2001, 'course': 2, 'group': '2B', 'grades': {'math': 5, 'physics': 5, 'history': 5}},
]

results = process_students(students)

print("Students by course:")
for course, students in results["students_by_course"].items():
    print(f"Course {course}: {[(s['surname'], s['name']) for s in students]}")

print("\nAverage score by group:")
for group, subjects in results["average_score_by_group"].items():
    print(f"Group {group}: {subjects}")

print("\nOldest student:", (results["oldest_student"]['surname'], results["oldest_student"]['name']))
print("Youngest student:", (results["youngest_student"]['surname'], results["youngest_student"]['name']))

print("\nBest student by group:")
for group, student in results["best_student_by_group"].items():
    print(f"Group {group}: {(student['surname'], student['name'])}")