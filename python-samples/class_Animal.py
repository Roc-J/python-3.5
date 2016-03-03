class Animal(object):
      def run(self):
            print('Animal is running..')

class Dog(Animal):
      def run(self):
            print('Dog is running..')

      def eat(self):
            print('Eating meat..')

class Cat(Animal):
      def run(self):
            print('Cat is running..')

      def eat(self):
            print('Cat eat fish..')

class Student(object):
      __slots__=('name','age')

class GraduateStudent(Student):
      pass



