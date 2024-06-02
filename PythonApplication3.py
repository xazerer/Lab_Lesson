from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    subjects: List[str] = field(default_factory=list)
    exam_dates: List[str] = field(default_factory=list)
    teachers: List[str] = field(default_factory=list)

    def add_subject(self, subject: str, exam_date: str, teacher: str):
        self.subjects.append(subject)
        self.exam_dates.append(exam_date)
        self.teachers.append(teacher)

@dataclass
class Group:
    students: List[Student] = field(default_factory=list)

    def add_student(self, student: Student):
        self.students.append(student)

    def print_group(self):
        for student in self.students:
            print(f"{student.first_name} {student.last_name}:")
            print(f"  Birth date: {student.birth_date}")
            print(f"  Subjects: {' '.join(student.subjects)}")
            print(f"  Exam dates: {' '.join(student.exam_dates)}")
            print(f"  Teachers: {' '.join(student.teachers)}\n")

# Создание списка студентов
students = [
    Student("Иван", "Иванов", "1998-04-15","Math","19.07.2024","Сидоров А.А"),
    Student("Алексей", "Алексеев", "1997-03-15","History","17.07.2024","Пальцев М.С."),
    Student("Андрей", "Андреев", "1998-02-16","Programming","15.07.2024","Федорова М.А."),
    Student("Василий", "Васильев", "1998-01-10","Cyber security","10.07.2024","Петрова К.А,"),
    Student("Александр", "Прокопьев", "1996-03-07","jurisprudence","09.07.2024","Сидорчук С.С."),
    # Добавьте столько студентов, сколько необходимо
]

# Создание группы и добавление студентов
group = Group()
for student in students:
    group.add_student(student)

# Вывод информации о группе
group.print_group()
# Предположим, что данные о студентах хранятся в списке словарей, где каждый словарь содержит информацию о студенте
students = [
    {"first_name": "Иван", "last_name": "Иванов", "birth_date": "1998-04-15"},
    {"first_name": "Алексей", "last_name": "Сидоров", "birth_date": "1999-03-15"},
    {"first_name": "Андрей", "last_name": "Андреев", "birth_date": "1998-02-16"},
    {"first_name": "Василий", "last_name": "Васильев", "birth_date": "1998-01-10"},
    {"first_name": "Александр", "last_name": "Прокопьев", "birth_date": "1996-03-07"},
    # Добавьте сюда остальные студенты
]

# Функция для сортировки студентов по дате рождения
def sort_students_by_birth_date(students):
    return sorted(students, key=lambda x: x['birth_date'])

# Получаем отсортированный список студентов
sorted_students = sort_students_by_birth_date(students)

# Находим самого младшего и самого старшего студента
youngest_student = sorted_students[0]
oldest_student = sorted_students[-1]

# Выводим результаты
print(f"Самый младший студент: {youngest_student['first_name']} {youngest_student['last_name']}, дата рождения: {youngest_student['birth_date']}")
print(f"Самый старший студент: {oldest_student['first_name']} {oldest_student['last_name']}, дата рождения: {oldest_student['birth_date']}")