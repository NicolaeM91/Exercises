# Homework 1

# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
#
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui

from abc import ABC, abstractmethod


class GeometricForm(ABC):
    Pi = 3.14

    @abstractmethod
    def area(self):
        raise NotImplementedError


class Square(GeometricForm):
    __side = 0

    def __init__(self, side: float):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.getter
    def side(self):
        print(f'The side is {self.__side}.')
        return self.__side

    @side.setter
    def side(self, new_side_value: float):
        print(f'The new side value is {new_side_value}')
        self.__side = new_side_value

    @side.deleter
    def side(self):
        print('I deleted the side.')
        self.__side = None

    def area(self):
        square_area = self.__side * self.__side
        print(f'The square area is {square_area: .2f}.')
        return square_area

    @staticmethod
    def description():
        print('Most likely i have corners.')


class Circle(GeometricForm):
    __radius = 0

    def __init__(self, radius=float):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        print(f'The radius is : {self.__radius}')
        return self.__radius

    @radius.setter
    def radius(self, new_radius_value):
        print(f'The new radius value is {new_radius_value}.')
        self.__radius = new_radius_value

    @radius.deleter
    def radius(self):
        print('I deleted the radius.')
        self.__radius = None

    def area(self):
        circle_area = self.Pi * self.__radius ** 2
        print(f'The circle area is {circle_area: .2f}')
        return circle_area

    @staticmethod
    def description():
        print('I don\'t  have corners.')


the_square_object = Square(side=3.45)
the_square_object.side
the_square_object.side = 5
del the_square_object.side
the_square_object.side
the_square_object.side = 2.33
the_square_object.area()
the_square_object.description()
print('-' * 50)
the_circle_object = Circle(radius=4.5)
the_circle_object.radius
the_circle_object.radius = 2.33
del the_circle_object.radius
the_circle_object.radius
the_circle_object.radius = 2.8
the_circle_object.area()
the_circle_object.description()


# Homework 2

# Description pillars OOP
# 1. Inheritance-  allows us to define a class that inherits all the methods
# and properties from another class.
# 2. Polymorphism-represents two functions that have the same name but are
# used differently.
# 3. Abstraction- it helps us hide unnecessary information.
# The user sees only the information that helps him.
# 4. Encapsulation-  It describes the idea of wrapping data and the methods
# that work on data within one unit.

# 2. create a class called Person, inside the class person cu encapsulation pattern
# add two class variables called hair, is_alive(bool),
# patru metode care: 1. seteaza culoarea parului,
# 2. seteaza bool
# 3. get hair color
# 4. get alive
# initiem clasa, apelam metodele

class Person:
    __hair: str = 'blonde'
    __is_alive:  bool = False

    def the_new_color(self, new_color):
        print(f'The new hair color is {new_color}.')
        self.__hair = new_color

    def get_hair_color(self):
        print(f'The hair color is {self.__hair}.')
        return self.__hair

    def set_the_new_status(self, is_alive: bool):
        print(f'And now - The person is alive - {is_alive}.')
        self.__is_alive = is_alive

    def get_alive(self):
        print(f'The person is alive - {self.__is_alive}.')
        return self.__is_alive

the_person = Person()
the_person.get_hair_color()
the_person.the_new_color(new_color='red')
the_person.get_hair_color()
the_person.get_alive()
the_person.set_the_new_status(is_alive=True)
the_person.get_alive()


