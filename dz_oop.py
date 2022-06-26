from hashlib import new


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def av_grade(self):
        stud_list = []
        for grade in self.grades.values():
            stud_list.extend(grade)
        res_3 = round(sum(stud_list) / len(stud_list), 1)
        return res_3

    


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.ending_courses:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.av_grade() < other.av_grade()

     
    def __str__(self):
        res_1 = f' Имя: {self.name}\n class list: {self.class_list()}\n Фамилия:{self.surname}\n Средняя оценка за домашние задания: {self.av_grade()}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'
        return res_1


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
        
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}
        self.ending_courses = []


    def lector_grades(self):
        lec_list = []
        for grade in self.courses_grades.values():
            lec_list.extend(grade)
        res_2 = round(sum(lec_list) / len(lec_list), 1)
        return res_2

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Lector')
            return
        return self.lector_grades() < other.lector_grades()

    
    def __str__(self):
        res = f' Имя: {self.name}\n Фамилия {self.surname}\n Средняя оценка за лекции {self.lector_grades()}'
        return res


  

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f' Имя: {self.name}\n Фамилия: {self.surname}'
        return res
  




rus = Student('Ruslan', 'Prusakov', 'mens')
rus.courses_in_progress += ['Python']
rus.courses_in_progress += ['Git']

ven = Student('Venera', 'Karimova', 'girl')
ven.courses_in_progress += ['Python']
ven.courses_in_progress += ['Git']



first_reviewer = Reviewer('Ven', 'Kar')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']
first_reviewer.rate_hw(rus, 'Python', 10)
first_reviewer.rate_hw(rus, 'Python', 9)
first_reviewer.rate_hw(rus, 'Python', 7)
first_reviewer.rate_hw(rus, 'Git', 4)
first_reviewer.rate_hw(rus, 'Git', 6)
first_reviewer.rate_hw(rus, 'Git', 8)

first_reviewer.rate_hw(ven, 'Python', 6)
first_reviewer.rate_hw(ven, 'Python', 5)
first_reviewer.rate_hw(ven, 'Python', 8)
first_reviewer.rate_hw(ven, 'Git', 3)
first_reviewer.rate_hw(ven, 'Git', 2)
first_reviewer.rate_hw(ven, 'Git', 9)


first_lector = Lecturer('Kar', 'Bik')
first_lector.ending_courses += ['Python']
first_lector.ending_courses += ['Git']
rus.rate_hw(first_lector, 'Python', 6)
rus.rate_hw(first_lector, 'Python', 8)
rus.rate_hw(first_lector, 'Python', 2)
rus.rate_hw(first_lector, 'Git', 10)
rus.rate_hw(first_lector, 'Git', 9)
rus.rate_hw(first_lector, 'Git', 7)

second_lector = Lecturer('Rad', 'Asd')
second_lector.ending_courses += ['Python']
second_lector.ending_courses += ['Git']
rus.rate_hw(second_lector, 'Python', 4)
rus.rate_hw(second_lector, 'Python', 10)
rus.rate_hw(second_lector, 'Python', 9)
rus.rate_hw(second_lector, 'Git', 3)
rus.rate_hw(second_lector, 'Git', 8)
rus.rate_hw(second_lector, 'Git', 5)
# print(rus)
# print()
# print(ven)
# print(rus > ven)
# print()
# print(first_reviewer)
# print()
# print(first_lector)
# print()


        

# print(rus.name)
# print(rus.surname)
# print(rus.courses_in_progress)
# print(rus.finished_courses)

student_list = [rus, ven]

student_list = [rus, ven]
course_name = input("course name? ")

lectors_list = [first_lector, second_lector]


def new_grade_of_student(student_list, course_name):
    new_list = []
    for student in student_list:
        new_list.extend(student.grades.get(course_name, []))
        res = round(sum(new_list) / len(new_list), 1)
    print(res)


def new_grade_of_lectors(lectors_list, course_name):
    new_list_1 = []
    for lector in lectors_list:
        new_list_1.extend(lector.courses_grades.get(course_name, []))
        res = round(sum(new_list_1) / len(new_list_1), 1)
    print(res)



new_grade_of_student(student_list, course_name)
new_grade_of_lectors(lectors_list, course_name)
