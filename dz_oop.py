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
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        res = round(sum(new_list) / len(new_list), 1)
        return res

    


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'




    def __str__(self):
        res_1 = f' Имя: {self.name}\n Фамилия:{self.surname}\n Средняя оценка за домашние задания: {self.av_grade()}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'
        return res_1


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
        
        



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}
        self.finished_courses = []


    def lector_grades(self):
        new_list = []
        for grade in self.courses_grades.values():
            new_list.extend(grade)
        res = round(sum(new_list) / len(new_list), 1)
        return res

    
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
  


 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)

rus = Student('Ruslan', 'Prusakov', 'mens')
rus.courses_in_progress += ['Python']
rus.courses_in_progress += ['Git']



first_reviewer = Reviewer('Ven', 'Kar')
first_reviewer.rate_hw(rus, 'Python', 10)
first_reviewer.rate_hw(rus, 'Python', 9)
first_reviewer.rate_hw(rus, 'Python', 7)
first_reviewer.rate_hw(rus, 'Git', 4)
first_reviewer.rate_hw(rus, 'Git', 6)
first_reviewer.rate_hw(rus, 'Git', 8)

first_lector = Lecturer('Kar', 'Bik')
first_lector.finished_courses += ['Python']
first_lector.finished_courses += ['Git']
rus.rate_hw(first_lector, 'Python', 6)
rus.rate_hw(first_lector, 'Python', 8)
rus.rate_hw(first_lector, 'Python', 2)
rus.rate_hw(first_lector, 'Git', 10)
rus.rate_hw(first_lector, 'Git', 9)
rus.rate_hw(first_lector, 'Git', 7)

print(first_lector.courses_grades)
print(first_lector.finished_courses)




# print(rus)
# print(first_reviewer)
# print(first_lector)


# brus = Reviewer ('Papa', 'Djons')
# brus.courses_attached += ['Python']
# brus.rate_hw(rus, 'Phyton', 10)

# brus.courses_attached += ['Git']
# brus.rate_hw(rus, 'Git', 8)

# brus.courses_attached += ['OOP']
# brus.rate_hw(rus, 'OOP', 6)






# print(rus.name)
# print(rus.surname)
# print(rus.courses_in_progress)
# print(rus.finished_courses)
# print(rus.grades)






