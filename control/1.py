# Вариант 14
import time


class Person:
    def __init__(self, famil, date):
        self.famil = famil
        self.date = date

    def print_info(self):
        print(f'Фамилия: {self.famil}\nДата рождения: {self.date}')

    @classmethod
    def new_pers(cls, surname, old):
        return cls(surname, old)


class Entrant(Person):
    def __init__(self, famil, date, fac):
        super().__init__(famil, date)
        self.fac = fac

    def print_info(self):
        print(f'Фамилия: {self.famil}\nДата рождения: {self.date}\nФакультет: {self.fac}')


class Student(Entrant):
    def __init__(self, famil, date, fac, curs):
        super().__init__(famil, date, fac)
        self.curs = curs

    def print_info(self):
        print(f'Фамилия: {self.famil}\nДата рождения: {self.date}\nФакультет: {self.fac}\nКурс: {self.curs}')


class Teacher(Entrant):
    def __init__(self, famil, date, fac, post, experience):
        super().__init__(famil, date, fac)
        self.post = post
        self.experience = experience

    def print_info(self):
        print(f'Фамилия: {self.famil}\nДата рождения: {self.date}\nФакультет: {self.fac}\nДолжность: {self.post}\n'
              f'Стаж: {self.experience} лет')


n = int(input("Количество людей: "))
list_of_pers = []

for i in range(n):
    pers1 = Person.new_pers(input('Новая фамилия: '),  (input('Дата рождения: ')))
    if 2022 - int(pers1.date[-4:]) >= 18:
        list_of_pers.append(pers1)  # Добалвяем если старше 18
    print('Записываем в базу...')
    time.sleep(1.2)

print()
print('Вот что хранится в базе: ')
print("Люди, которым больше 18")
time.sleep(1.2)
for pers in list_of_pers:
    pers.print_info()
    print()
    time.sleep(1.2)

print('Покажем функционирование всех всех команд')
time.sleep(1.2)
print('Абитуриент')
entrant1 = Entrant('Колобков', '1.1.1999', 'сисадмин')
entrant1.print_info()
time.sleep(1.2)
print()
print('Студент')
student1 = Student('Полохов', '12.11.2003', 'Прогер', 1)
student1.print_info()
time.sleep(1.2)
print()
print('Учитель')
teacher1 = Teacher('Бобченок', '6.1.1990', 'Программирование', 'Лучший препод по питону', 1000)
teacher1.print_info()
time.sleep(1.2)
print()
