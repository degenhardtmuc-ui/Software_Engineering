class Student:
    def __init__(self, name, fach):
        self.name = name
        self.fach = fach
        
    def x(self):
        print("ich bin die Methode x in Student")
        
    def y(self):
        print("Ich bin die Methode y in Student")
===========
class Lehrkraft:
      def __init__(self, vorlesung):
        self.vorlesung = vorlesuung
        
    def x(self):
        print("ich bin die Methode x in Lehrkraft")
        
    def y(self):
        print("Ich bin die Methode y in Lehrkraft")
class HiWi(Student, Lehrkraft): # x Student, x Lehrkraft?
    pass

====================================================================
import random
animals = []
for i in range(10):
    zufalls_zahl = random.randint(0, 1)
    
    if zufalls_zahl == 0:
        animals.append(Dog())
    elif zufalls_zahl == 1:
        animals.append(Cat())

for animal in animals:
    animal.make_sound()
========
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Abstrakte Methode: eine Methode ohne Implementation"""
        pass

=====================================================================

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Abstrakte Methode: eine Methode ohne Implementation"""
        pass

import random
animals = []
for i in range(10):
    zufalls_zahl = random.randint(0, 1)
    
    if zufalls_zahl == 0:
        animals.append(Dog())
    elif zufalls_zahl == 1:
        animals.append(Cat())

for animal in animals:
    animal.make_sound()
========
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Abstrakte Methode: eine Methode ohne Implementation"""
      pass

==========================================================

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print("I am an Animal")
=========
class Lion(Animal):
    
    def make_sound(self):
       super().make_sound()
    
    def eat(self):
        print("I am eating something")