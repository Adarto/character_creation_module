# def we_crash_all(name: str) -> str:    
#    return 'Привет, ' + name + ', мы всё сломали!'

# print(we_crash_all('Наташа'))

# import math

# Спросим, что хорошего в этой библиотеке.
# print(print.__doc__)

# Будет напечатано:
# This module provides access to the mathematical functions
# defined by the C standard.

'''
class Sword:

    def __init__(self, name, material, blade_length, grip):
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        print(f'Новый меч {name} выкован!')
    
    def slashing_blow(self):
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')

    def piercing_strike(self):
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.')

# Создаём экземпляр класса Sword.
first_sword = Sword('Тренировочный',
                    'Кора железного дуба',
                    1.2, 'хват одной рукой')

print('Перед вами манекен, опробуйте удары на нём.')
# Вызвать метод рубящего удара.
print(first_sword.slashing_blow())
# Вызвать метод пронзающего удара.
print(first_sword.piercing_strike())
print('Обслуженное оружие никогда не подведёт.')
# Вызвать метод заточки меча.
print(first_sword.sharpen())
'''

'''
class Sword:

    def __init__(self, name, blade_length, grip, material='сталь'):
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        self.strength = 10
        print(f'Новый меч {name} выкован!')
    
    def slashing_blow(self):
        self.strength -= 10
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')

    def piercing_strike(self):
        self.strength -= 5
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        self.strength = 100
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.')
    
    # Вот он — новый метод! Именно в нём описывается то, что должно выводиться
    # при печати объекта.
    def __str__(self):
        # Можно задать любую строку, например
        # «Не печатай меня, ведь я — объект!».
        # Но лучше пусть при печати выводится что-то осмысленное,
        # например имя объекта и его основные параметры.
        return (
            f'Меч — «{self.name}». ' 
            f'Выкован из материала {self.material}, '
            f'длина клинка — {self.blade_length}, '
            f'прочность — {self.strength}.'
        )


katana = Sword('Верный', 1.5,
               'хват двумя руками')
classic_sword = Sword('Дежурный', 1.2,
                      'хват одной рукой')

# Печатаем созданные объекты.
print(katana)
print(classic_sword)
'''

'''
import datetime as dt
import time

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time:
            return 'С этим испытанием вы уже справились.'
        self.start_time = dt.datetime.now()
        return f'Начало квеста "{self.name}" положено.'

    def pass_quest(self):
        if not self.start_time:
            return 'Нельзя завершить то, что не имеет начала!'
        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return (f'Квест "{self.name}" окончен.'
                f' Время выполнения квеста: {completion_time}')

    # Напишите код метода __str__.
    def __str__(self):
        if self.end_time:
            return (f'Цель квеста {self.name} - {self.goal} Квест завершён.')
        if self.start_time:
            return (f'Цель квеста {self.name} - {self.goal} Квест выполняется.')
        return (f'Цель квеста {self.name} - {self.goal}.')


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = 
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.

new_quest = Quest(quest_name, quest_description, quest_goal) 

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

# Печатаем объекта класса Quest:
print(new_quest)
'''

'''
class MeleeWeapon:

    def __init__(self, name):
        # Задаём свойство, в котором будет храниться значение имени объекта.
        # Это свойство будет передаваться при создании объектов класса.
        self.name = name
        # Задаём свойство, в котором будет храниться значение прочности
        # создаваемых объектов.
        self.strength = 100
    
    # Объявляем метод рубящего удара.
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность оружия на 10.
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'
    
    # Объявляем метод заточки оружия.
    def sharpen(self):
        # При заточке восстанавливаем стартовую прочность.
        self.strength = 100
        return (f'Оружие "{self.name}" заточено.')

# Создаём объект класса MeleeWeapon.
blade = MeleeWeapon('Клинок')
# Вызываем метод объекта класса MeleeWeapon.
blade.slashing_blow()

class Axe(MeleeWeapon):

    def __init__(self, name, material):
        super().__init__(name)
        self.material = material
   
    # Объявляем собственный для класса Axe метод.
    def slashing_blow(self):
        # Описываем логику работы метода дочернего класса.
        print('СОКРУШИТЕЛЬНЫЙ УДАР!')
        # Возвращаем результат выполнения метода slashing_blow() в родительском классе.
        return super().slashing_blow()  

brodex = Axe('Верный', 'железо')

print(brodex.slashing_blow())
'''

'''
class MeleeWeapon:

    def __init__(self, name):
        self.name = name
        self.strength = 100
    
    # Метод родительского класса.
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'
    
    def sharpen(self):
        self.strength = 100
        return (f'Оружие "{self.name}" заточено.')


class Sword(MeleeWeapon):

    # Переопределяем метод родительского класса...
    def slashing_blow(self):
        # ...меняем значение снижения прочности...
        self.strength -= 5
        # ...и меняем сообщение.
        return f'Мечом {self.name} был нанесен рубящий удар.'

# Этот класс-наследник полностью наследует все методы и свойства
# родительского класса.
class Axe(MeleeWeapon):
    ...

brodex = Axe('Верный')
xiphos = Sword('Разящий')

# Для класса Sword будет вызыван переопределённый метод.
print(xiphos.slashing_blow())
# Для класса Axe будет вызван метод родительского класса.
print(brodex.slashing_blow())
# Исходное значение прочности для класса Sword будет уменьшено
# на переопределённое значение.
print(f'Запас прочности меча: {xiphos.strength}')
# Исходное значение просности для класса Axe будет уменьшено
# на значение, указанное в родительском классе.
print(f'Запас прочности топора: {brodex.strength}')
'''

'''
class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
        
    def describe(self, full=False):
        if full == True:
            return (f'Попугай {self.name} — заметная птица, '
                    f'окрас её перьев — {self.color}, а размер — {self.size}.')
        else:
            return print(super().describe())


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
    
    def describe(self, full=False):
        if full == True:
            return print((f'Размер пингвина {self.name} из рода {self.genus} —'
                    f' {self.size}. Интересный факт: однажды группа'
                    f' геологов-разведчиков похитила пингвинье яйцо, и'
                    f' их принялась преследовать вся стая, не пытаясь, '
                    f'впрочем, при этом нападать. Посовещавшись, '
                    f'похитители вернули птицам яйцо, и те отстали.'))
        else:
            return print(super().describe())

kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe()
kowalski.describe(True)
'''

class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    def ask_question(self, someone, question):
        print(f'{someone.name}, {question}')
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку	


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса

# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)
    

class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')