class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name): # Добавляем курсы в завершенные курсы
        self.finished_courses.append(course_name)

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Mistake'

    def average_grade_of_student(self):
        grades = self.grades
        list_courses = []
        for courses in grades:
            list_courses.append(courses)
        print(f'Имеющиеся курсы: {list_courses}')
        course_name = input(
            f'''\nВведите название курса для просмотра средней оценки по этому курсу или введите "Все" для просмотра средней оценки по всем курсам'''
        )
        if course_name != 'Все':
            list_grades = grades.get(course_name)
            sum_grade = 0
            for grade in list_grades:
                sum_grade += grade
            average = sum_grade / len(list_grades)
            return round(average, 1)
        else:
            all_grades = []
            for count in grades:
                all_grades += grades.get(count)
            sum_grade = 0
            for grade in all_grades:
                sum_grade += grade
            average = sum_grade / len(all_grades)
            return round(average, 1)

    def __str__(self):
        courses = self.courses_in_progress
        finish = self.finished_courses
        return f'''\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade_of_student()}\nКурсы в процессе изучения: {",".join(courses)}\nЗавершенные курсы: {",".join(finish)}'''

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Можно сравнивать только студентов!')
        elif self.average_grade_of_student() > other.average_grade_of_students():
            return f'\n{self.name} {self.surname} имеет среднюю оценку за домашние задания выше чем {other.name} {other.surname}'
        else:
            return f'\n{other.name} {other.surname} имеет среднюю оценку за домашние задания выше чем {self.name} {self.surname}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname,):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def average_grade_of_lecturer(self):
        grades = self.grades
        list_courses = []
        for courses in grades:
            list_courses.append(courses)
        print(f'Имеющиеся курсы: {list_courses}')
        course_name = input(f'''\nВведите название курса для просмотра средней оценки по этому курсу или введите "Все" для просмотра средней оценки по всем курсам: ''')
        if course_name != 'Все':
            list_grades = grades.get(course_name)
            sum_grade = 0
            for grade in list_grades:
                sum_grade += grade
            average = sum_grade / len(list_grades)
            return round(average, 1)
        else:
            all_grades = []
            for count in grades:
                all_grades += grades.get(count)
            sum_grade = 0
            for grade in all_grades:
                sum_grade += grade
            average = sum_grade / len(all_grades)
            return round(average, 1)

    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_of_lecturer()}'''

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Можно сравнивать только лекторов!')
        elif self.average_grade_of_lecturer() > other.average_grade_of_lecturer():
            return f'{self.name} {self.surname} имеет среднюю оценку за лекции выше чем {other.name} {other.surname}'
        else:
            return f'{other.name} {self.surname} имеет среднюю оценку за лекции выше чем {self.name} {self.surname}'


class Reviewer(Mentor):
    def rate_hw(self, student, lecturer, course, grade):
        if isinstance(student, Student) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Mistake'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

good_student = Student('Luke', 'Skywalker', 'male')
good_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

super_mentor = Mentor('Rocky', 'Balboa')
super_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

smart_lecturer = Lecturer('Albus', 'Dumbledore')
smart_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')

fair_reviewer = Reviewer('Thanos', 'Semenov')

best_student.rate_lection(cool_lecturer, 'Python', 10)
best_student.rate_lection(cool_lecturer, 'Python', 9)
best_student.rate_lection(cool_lecturer, 'Python', 6)

good_student.rate_lection(smart_lecturer, 'Python', 10)
good_student.rate_lection(smart_lecturer, 'Python', 9)
good_student.rate_lection(smart_lecturer, 'Python', 10)

cool_reviewer.rate_hw(best_student, cool_lecturer, 'Python', 10)
cool_reviewer.rate_hw(best_student, cool_lecturer, 'Python', 9)
cool_reviewer.rate_hw(best_student, cool_lecturer, 'Python', 7)

fair_reviewer.rate_hw(good_student, smart_lecturer, 'Python', 10)
fair_reviewer.rate_hw(good_student, smart_lecturer, 'Python', 10)
fair_reviewer.rate_hw(good_student, smart_lecturer, 'Python', 9)

def course_average_grade_prsns(prsn_list, course_name):
    course_grade_list = []

    for prsn in prsn_list:
        if course_name in prsn.grades:
            course_grade_list += prsn.grades.get(course_name)

    sum_of_grades = 0
    for grade in course_grade_list:
        sum_of_grades += grade
    average = sum_of_grades / len(course_grade_list)

    return round(average, 1)


list_of_students = [best_student, good_student]
list_of_lecturers = [cool_lecturer, smart_lecturer]


print(course_average_grade_prsns(list_of_students,"Python"))
print(course_average_grade_prsns(list_of_lecturers,"Python"))
print(cool_lecturer > smart_lecturer)
print(best_student > good_student)
print(best_student)
print(cool_lecturer)
print(cool_reviewer)





