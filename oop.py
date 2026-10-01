import time

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

    def rate_lecture(self, lectured, course, grade):
        if isinstance(lectured, Lecturer) and course in self.courses_in_progress and course in lectured.courses_attached:
            if course in lectured.grades:
                lectured.grades[course].append(grade)
            else:
                lectured.grades[course] = [grade]
        else:
            return f'{lectured.name} не преподает этот курс, либо не может получать оценки, так как является ревьювером'   

    def get_average_grade(self):
            if len(self.grades) == 0:
                return 0
    
            grades_list = [grade_lector for grade in self.grades.values() for grade_lector in grade]
            return sum(grades_list) / len(grades_list)

    def __lt__(self, other):
            return self.get_average_grade() < other.get_average_grade()

    def __eq__(self, other):
                return self.get_average_grade() == other.get_average_grade()

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.get_average_grade()} \
            \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}'

                
class Mentor:
    '''Класс преподователей, запоминает курсы'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached =[] 

    def __str__(self):
            return f'Имя: {self.name} \nФамилия: {self.surname}'        


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0

        grades_list = [grade_lector for grade in self.grades.values() for grade_lector in grade]
        return sum(grades_list) / len(grades_list)

    def __str__(self):
        return f'{super().__str__()} \nСредняя оценка за лекции: {self.get_average_grade()}'

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()
     
             
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)       

    def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course].append(grade)
                else:
                    student.grades[course] = [grade]
            else:
                return f'ошибка'       


def main():
    
    student_1 = Student('Иван', 'Иванов', 'м')   
    student_2 = Student('Мария', 'Васильева', 'ж')    

    lectured_1 = Lecturer('Михаил', 'Михайлович')
    lectured_2 = Lecturer('Валентин', 'Сергеевич')

    reviewered_1 = Reviewer('Петр', 'Петрович')
    reviewered_2 = Reviewer('Сергей', 'Сергеевич')

    student_1.finished_courses += ['C#', 'Git']
    student_1.courses_in_progress += ['Python', 'Ruby']
    student_2.finished_courses += ['C#', 'Java']
    student_2.courses_in_progress += ['QA', 'C++']

    student_1.grades['C#'] = [10, 8, 10, 9, 10]
    student_1.grades['Git'] = [7, 10, 10, 9, 10]
    student_2.grades['C#'] = [9, 8, 10, 9, 10]
    student_2.grades['Java'] = [9, 10, 10, 5, 10]

    lectured_1.courses_attached += ['Python', 'C++']
    lectured_2.courses_attached += ['Ruby', 'QA']
    reviewered_1.courses_attached += ['Python', 'QA']
    reviewered_2.courses_attached += ['Ruby', 'C++']

    print(f'Студент {student_1.name} {student_1.surname} идёт на курс по "Python",', end=' ')
    print(f'его общие оценки до начала курса {student_1.grades}, а средний балл {student_1.get_average_grade()}')
    student_1.rate_lecture(lectured_1, 'Python', 10)
    print(f'Студент {student_1.name} {student_1.surname} закончил занятие и поставил оценку лектору', end=' ')
    print(f'{lectured_1.name} {lectured_1.surname} {lectured_1.grades}')
    print(f'Студент {student_2.name} {student_2.surname} идёт на курс по "C++",', end=' ')
    print(f'его общие оценки до начала курса {student_2.grades}, а средний балл {student_2.get_average_grade()}')
    student_2.rate_lecture(lectured_1, 'C++', 8)
    print(f'Студент {student_2.name} {student_2.surname} закончил занятие и поставил оценку лектору', end=' ')
    print(f'{lectured_1.name} {lectured_1.surname} {lectured_1.grades}')
    print(f'Ревьювер {reviewered_1.name} {reviewered_1.surname} проверил домашние задание у студента {student_1.name} {student_1.surname}.')
    reviewered_1.rate_hw(student_1, 'Python', 9)
    reviewered_1.rate_hw(student_1, 'Python', 6)
    print(f'Оценки у студента {student_1.name} {student_1.surname} теперь такие {student_1.grades}')
    print(f'Ревьювер {reviewered_2.name} {reviewered_2.surname} проверил домашние задание у студента {student_2.name} {student_2.surname}.')
    reviewered_2.rate_hw(student_2, 'C++', 9)
    reviewered_2.rate_hw(student_2, 'C++', 10)
    print(f'Оценки у студента {student_2.name} {student_2.surname} теперь такие {student_2.grades}')

    time.sleep(2)

    print('Наступил новый день!')

    print(f'Студент {student_1.name} {student_1.surname} идёт на курс по "Ruby",', end=' ')
    print(f'его общие оценки до начала курса {student_1.grades}, а средний балл {student_1.get_average_grade()}')
    student_1.rate_lecture(lectured_2, 'Ruby', 10)
    print(f'Студент {student_1.name} {student_1.surname} закончил занятие и поставил оценку лектору', end=' ')
    print(f'{lectured_2.name} {lectured_2.surname} {lectured_2.grades}')
    print(f'Студент {student_2.name} {student_2.surname} идёт на курс по "QA",', end=' ')
    print(f'его общие оценки до начала курса {student_2.grades}, а средний балл {student_2.get_average_grade()}')
    student_2.rate_lecture(lectured_2, 'QA', 7)
    print(f'Студент {student_2.name} {student_2.surname} закончил занятие и поставил оценку лектору', end=' ')
    print(f'{lectured_2.name} {lectured_2.surname} {lectured_2.grades}')
    print(f'Ревьювер {reviewered_1.name} {reviewered_1.surname} проверил домашние задание у студента {student_2.name} {student_2.surname}.')
    reviewered_1.rate_hw(student_2, 'QA', 9)
    reviewered_1.rate_hw(student_2, 'QA', 5)
    print(f'Оценки у студента {student_2.name} {student_2.surname} теперь такие {student_2.grades}')
    print(f'Ревьювер {reviewered_2.name} {reviewered_2.surname} проверил домашние задание у студента {student_1.name} {student_1.surname}.')
    reviewered_2.rate_hw(student_1, 'Ruby', 6)
    reviewered_2.rate_hw(student_1, 'Ruby', 10)
    print(f'Оценки у студента {student_1.name} {student_1.surname} теперь такие {student_1.grades}')

    print('Все занятия закончены, пришло время подвести итоге и определить лучших студентов и лучших лекторов!')
    print('В номинации лучший студент побеждает:')
    if student_1 > student_2:
        print(student_1.name, student_1.surname)
    elif student_1 < student_2:
        print(student_2.name, student_2.surname)    
    else:
        print('Оценки у студентов одинаковые, лучшего определить невозможно')    

    print('В номинации лучший лектор побеждает:')
    if lectured_1 > lectured_2:
        print(lectured_1.name, lectured_1.surname)
    elif lectured_1 < lectured_2:
        print(lectured_2.name, lectured_2.surname)    
    else:
        print('Оценки у лекторов одинаковые, лучшего определить невозможно')       


if __name__ == '__main__':
    main()
