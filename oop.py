class Student:
    '''Класс студент, запоминает прогресс по курсам и оценки'''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, corses_name):
        self.finished_courses.append(corses_name)
        

class Mentor:
    '''Класс преподователей, запоминает, какой курс ведет и выставляет оценки'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached =[]

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return f'ошибка'            


def main():
    best_student = Student('Василий', 'Пупкин', 'Мужской')
    best_student.finished_courses.append('Git')
    best_student.courses_in_progress.append('Python')
    best_student.grades['Git'] = [10, 10, 10, 10, 10]
    best_student.grades['Python'] = [10, 10]

    print(f'Студент {best_student.name} {best_student.surname}:')
    print(f'Изучил: {best_student.finished_courses}')
    print(f'Проходит сейчас: {best_student.courses_in_progress}')
    print(f'Его оценки: {best_student.grades}')

    cool_mentor = Mentor('Гвидо', 'Ван Россум')
    cool_mentor.courses_attached.append('Python')
    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 9)
    cool_mentor.rate_hw(best_student, 'Python', 10)

    print(f'Преподователь {cool_mentor.name} {cool_mentor.surname} ведет курс {cool_mentor.courses_attached}')
    print(f'Студет {best_student.name} {best_student.surname} получил новые оценки: {best_student.grades}')

if __name__ == '__main__':
    main()