Задача №1: Загрузка на github через git bash.
Переход в указанный каталог
![image](https://github.com/xazerer/Lab_Lesson/assets/98025314/a2732ced-6679-4cc9-82e9-f2549b454ee3)
Добавление файлов в индекс для отслеживания изменений и проверка, чтобы добавить файлы использовались команды:
$git add
$git commit
Чтобы Запушить в git необходимо использовать команду git push
Теперь git начал отслеживать содержимое папки
git status
Просмотреть список имеющихся тегов в Git можно очень просто. Достаточно набрать команду git tag (параметры -l и --list опциональны):

$ git tag
v1.0
v2.0
Создание аннотированного тега в Git выполняется легко. Самый простой способ — это указать -a при выполнении команды tag
Можно так же использовать команду git log для просмотра списков всех коммитов.
Описание кода Задание №2 Вариант №17
17.	Написать функцию, которая принимает в качестве аргумента строку и определяет количество слов в ней
s = "Это наш пример строки"
words = s.split()
num_words = len(words)
print(num_words)
![image](https://github.com/xazerer/Lab_Lesson/assets/98025314/c74f8e8e-b37f-486d-a7da-86026af71403)
15.	Вывести ФИО и дату рождения, самого младшего и самого старшего студента
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

Вывод:
![image](https://github.com/xazerer/Lab_Lesson/assets/98025314/1e459cd3-5e94-4e11-82b0-7440c9c164d5)
![image](https://github.com/xazerer/Lab_Lesson/assets/98025314/1f4ca014-a288-47c7-9dbd-a08f391851c8)

