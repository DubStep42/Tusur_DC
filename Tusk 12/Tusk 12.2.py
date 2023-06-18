from statistics import mean
from collections import defaultdict
class Year:
    def __init__(self, year):
        self.year = year
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)
class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_grade_group(self):
        return sum(student.average_grade() for student in self.students) / len(self.students)
    def average_grade_stud(self):
        return {student.name: student.average_grade() for student in self.students}
    def problem_subjects(self):
        subjects = defaultdict(list)
        for student in self.students:
            for subject, grade in student.grades.items():
                subjects[subject].append(grade)
        return {subject: sum(grades) / len(grades) for subject, grades in subjects.items() if
                    sum(grades) / len(grades) < 3}

    def students_to_dismiss(self):
        return [student for student in self.students if student.average_grade() < 3]

    def scholarship_students(self):
        return [student for student in self.students if student.average_grade() > 4.8]


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def __str__(self):
        return self.name
    def add_grade(self, course, grade):
        self.grades[course] = grade

    def average_grade(self):
        return round(sum(self.grades.values()) / len(self.grades), 2)


class Deanery:
    def __init__(self):
        self.years = []

    def add_year(self, year):
        self.years.append(year)
    def report(self):

        for year in self.years:
            for group in year.groups:
                # Получение информации о стипендиатах и на студентов на отчисление
                students_to_dismiss = list(map(str, group.students_to_dismiss())) # Студенты на отчисление отбираются из групп с баллом < 3
                scholarship_students = list(map(str, group.scholarship_students())) # Стипендиаты отбираются из групп с баллом  > 4.8
                problem_subjects = group.problem_subjects()  # Предметы, по которым балл  < 3
                average_grades = group.average_grade_stud()  # Определение среднего балла студента в каждой группе

                print(f"Group {group.name}  - average group grade - {group.average_grade_group()}")
                print(f" * Students to dismiss: {students_to_dismiss}")
                print(f" * Scholarship students: {scholarship_students}")
                print(f" * Problem subjects: {problem_subjects if problem_subjects else 'None'}")
                print(f" * Average grades: {average_grades} \n ")


# Создаем объекты групп
group1 = Group("1A")
group2 = Group("2B")

# Создаем объекты студентов
student1 = Student("Ivan")
student2 = Student("Petr")
student3 = Student("Seva")
# Добавляем оценки студентам
student1.add_grade("Math", 2)
student1.add_grade("Physics", 3)
student1.add_grade("Chemistry", 2)

student2.add_grade("Math", 4)
student2.add_grade("Physics", 5)
student2.add_grade("Math", 4)
student2.add_grade("Chemistry", 5)

student3.add_grade("Physics", 5)
# Добавляем студентов в группы
group1.add_student(student1)

group2.add_student(student2)
group2.add_student(student3)
# Создаем объекты годов и добавляем в них группы
year1 = Year(1)
year1.add_group(group1)
year2 = Year(2)
year2.add_group(group2)

# Создаем объект деканата и добавляем в него годы
deanery = Deanery()
deanery.add_year(year1)
deanery.add_year(year2)
deanery.report()