# Class
# what is class
# In Python, a class serves as a blueprint or a template for creating objects.

# what is __init__ in class
# This is a special method known as the constructor.
# It is automatically called when a new instance of the class is created and is used to initialize the instance's attributes.

# what is self in class
# This parameter is a convention in Python methods and refers to the current instance of the class.
# It must be the first parameter of any method within a class.

# What is attribute in class
# These are variables associated with a class or its instances. They can be:
# Class Variables: Shared by all instances of the class.(val1 = "test")
# Instance Variables: Unique to each individual instance of the class.(self.name)

# 49) write a class to convert tuples in list
mytuples = [(1, 'a', 11), (2, 'b', 12), (3, 'c', 13), (4, 'd', 14)]

class ConverTupleToList:
    # class variable
    test = "testing"

    def __init__(self, mytuple):
        # instance variable
        self.mytuple = mytuple

    def con_tup_list(self):
        myres = []
        for x, y, z in self.mytuple:
            myres.append(x)
            myres.append(y)
            myres.append(z)
        return myres

obj49 = ConverTupleToList(mytuples)
res49 = obj49.con_tup_list()
print(f"Question 49 NORMAL CLASS answer is : {res49}")

# NOTES IMPORTANT READ FIRST AND THEN CODE

# What is Inheritance
# Inheritance in Python is a fundamental concept of Object-Oriented Programming (OOP)
# that allows a new class (called the child class or subclass) to inherit attributes and methods from
# an existing class (called the parent class or superclass).

# What is override in inheritance
# Override methods:
# Provide a new implementation for a method that is already defined in the parent class, effectively changing
# its behavior for instances of the child class.

# Code Reusability:
# Inheritance promotes code reusability by allowing child classes to utilize the functionalities already
# defined in the parent class, avoiding redundant code.

# What is super()
# The super() function is commonly used within the child class's __init__ method to call the parent class's constructor
# and initialize inherited attributes.

# How many inheritance are there in Python?
# The five types of inheritance in Python are single, multiple, multilevel, hierarchical, and hybrid inheritance

# OVERLOADING IN PYTHON
# In many programming languages like C++ or Java, you can define multiple methods with the same name but different parameter lists.
# This concept is called method overloading.
# Python does not support method overloading by default. If you define multiple methods with the same name,
# only the latest definition will be used.
# however, it offers several techniques to simulate method overloading.
# Using Variable Arguments (*args)
# Using Default Arguments (None as default value)
# Using Multiple Dispatch
#  a) Python's multipledispatch library allows true method overloading by dispatching functions based on parameter types and counts.
#  b) Install multipledispatch module using the following command: pip install multipledispatch

# 50) Write a class first for two unequal list and inherit class for three unequal list (normal way)
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]

class TwoUnequalList:
    # class variable
    test= "testing"

    def __init__(self, mylist1, mylist2):
        # Instance variables
        self.mylist1= mylist1
        self.mylist2 = mylist2

    def two_unequal_list(self):
        myres = []
        max1 = max(len(mylist1), len(mylist2))
        for x in range(max1):
            if (len(mylist1)) < max1:
                self.mylist1.append(0)
            if (len(mylist2)) < max1:
                self.mylist2.append(0)
            myres.append((mylist1[x], mylist2[x]))
        return myres

obj50_1 = TwoUnequalList(mylist1, mylist2)
res50_1 = obj50_1.two_unequal_list()
print(f"Question 50 SINGLE INHERITANCE answers are : ")
print(f"    Parent class : {res50_1}")

# Inheritance (single inheritance)
class InheriThreeUnequalList(TwoUnequalList):
    # class variable
    test = "testing"

    def __init__(self, mylist1, mylist2, mylist3):
        super().__init__(mylist1, mylist2)
        self.mylist3 = mylist3

    def three_unequal_list(self):
        myres = []
        max1 = max(len(mylist1), len(mylist2))
        for x in range(max1):
            if (len(mylist1)) < max1:
                self.mylist1.append(0)
            if (len(mylist2)) < max1:
                self.mylist2.append(0)
            if (len(mylist3)) < max1:
                self.mylist3.append(0)
            myres.append((mylist1[x], mylist2[x], mylist3[x]))
        return myres

obj50_2 = InheriThreeUnequalList(mylist1, mylist2, mylist3)
res50_2 = obj50_2.two_unequal_list()
res50_3 = obj50_2.three_unequal_list()
print(f"    Parent class method called from child/sub/derived class : {res50_2}")
print(f"    child/sub/derived class : {res50_3}")

# Multiple inheritance
# super() function does not able to call particular class in multiple inheritance
# instead we use the class name __init__ constructor for multiple inheritance
# for example
# person.__init__(self, name, age)
# teacher.__init__(self, teacher_name)

# MRO: Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
# Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes.
# So if we have same method name in both the parent clasess, it perform MRO and take the method from the first class we have specified in inheritance class
# for example
# class Student(teacher, person): it will pick from teacher parent class
# class Student(person, teacher): it will pick from person parent class

# 51 write a class for multiple inheritances
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_of(self):
        return f"Name : {self.name}"

class teacher:
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name

    def name_of(self):
        return f"Teacher Name: {self.teacher_name}"

class Student(teacher, person):
    def __init__(self, name, age, teacher_name, score, section):
        person.__init__(self, name, age)
        teacher.__init__(self, teacher_name)
        self.score = score
        self.section = section

    def details_of_student(self):
        return f"Name: {self.name}, age: {self.age}, teacher_name : {self.teacher_name}, Score: {self.score}, Section: {self.section}"


obj51_1 = Student("hammad", 11, "vipin", 100, "4th A")
res51_1 = obj51_1.details_of_student()
res51_2 = obj51_1.name_of()
print(f"Question 51 MULTIPLE INHERITANCE answers are:  ")
print(f"    Calling method from child/dervied/sub class: {res51_1}")
print(f"    Calling name_of methos from parent class: {res51_2}")

# What is ENCAPSULATION

# Encapsulation means hiding internal details of a class and only exposing what’s necessary.
# It helps to protect important data from being changed directly and keeps the code secure and organized.
# Technically, encapsulation is an object-oriented programming principle where data (variables)
# and methods (functions) are bundled together in a class.
# By default in python all are public like instant variable, methods and properties of class
# any one can change the value of instant variable, by creating instance of class they can change the variables.
# for example
# obj1 = student()
# res = obj1.score = 89
# Access specifiers in python: 1) public  2) private(double underscore __) 3) protect(single underscore _)
# We can also use setter and getter functions for variables
# private can used only in only in class
# protector varibale can be used only and only in derived/sub/child inheritance class
# Note: protector variable are still accessible directly.
# Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
# Use a double underscore (__) to define a private method accessible only within class due to name mangling.
# Note: Unlike other programming languages, Python does not enforce access modifiers like public, private or protected at the language level.
# However, it follows naming conventions and uses a technique called name mangling to support encapsulation.

# 52) Write a class which use private variable, so they should not change the value directly

#without Encapsulation

class students:
    def __init__(self, name, age, score):
        self.name = name
        self.age = 9
        self.score = score

    def name_of(self):
        return f"Name : {self.name}, age : {self.age}, score: {self.score}"

obj52_1 = students("hammad", 11, 100)

# directly changing the values
obj52_1.name = "safeer"
obj52_1.age = 43
obj52_1.score = 98
res52_1 = obj52_1.name_of()
print(f"Question 52 ENCAPSULATION answer are: ")
print(f"    after direct changing the value of attribute/instant variable : {res52_1}")


# After Encapsulation private specifiers
class studentsEncap:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = 9
        self.__score = score

    def name_of(self):
        return f"Name : {self.__name}, age : {self.__age}, score: {self.__score}"

obj52_2 = studentsEncap("hammad", 11, 97)
# trying direct access
obj52_2.__name = "safeer"
obj52_2.__age = 40
obj52_2.__score = 76
res52_2 = obj52_2.name_of()
print(f"    After encapsulation private : {res52_2}")

# NOTE: We are not able to change directly after private encapsulation

# Protec specifiers

class studentsEncapProc:
    def __init__(self, name, age, score):
        self._name = name
        self._age = 9
        self._score = score

    def name_of(self):
        return f"Name : {self._name}, age : {self._age}, score: {self._score}"

obj52_3 = studentsEncapProc("hammad", 11, 97)
# trying direct access
obj52_3._name = "safeer"
obj52_3._age = 40
obj52_3._score = 76
res52_3 = obj52_3.name_of()
print(f"    After encapsulation protect : {res52_3}")

# 53  Write class for private method and protect method

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount             # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()           # Accessing protected method
        else:
            print("Invalid deposit amount!")

print(f"Question 53 ENCAPSULATION PRIVATE PROTECTED METHODS AND ATTRIBUTES answer is : ")
account = BankAccount()
account._show_balance()      # Works, but should be treated as internal
#account.__update_balance(500)  # Error: private method
account.deposit(500)         # Uses both methods internally

# abstract class
# what is ABSTRACT CLASS
# An abstract class in Python is a class that cannot be instantiated directly and serves as a blueprint for other classes(child clasess).
# It defines a common interface and enforces a structure that subclasses must adhere to.
# This approach helps in reducing the complexity and increasing the efficiency of application development.
# Python provides the abc module to define ABC(Abstract base class) and enforce the implementation of abstract methods in subclasses.
# from abc import ABC, abstractmethod
# class goal(abc):
#
#   @abstarctmethod
#   def aim(self):
#   pass
#
#   Full implementation
#   def workhard(self):
#       return f"Learning to achieve the goal"
#
# Note: code/definition/statements in abstract class can be implemented or not Implemented, it is left to user, it is a blueprint.
# We cannot instantiate the class, subclass/derivied/child class will use this abstract class and implement the code.
# Where as in INTERFACE all methods are abstractmethods, it is a blueprint.
# subclass/derivied/child class will use this abstract class and methods to implement the code.
#

# 54) Write a program for abstract class and explain

# import abc module first
from abc import ABC, abstractmethod


class Construction(ABC):
    def __init__(self, owner_name, bricks_quantity, cement_quantity):
        self.owner_name = owner_name
        self.bricks_quantity = bricks_quantity
        self.cement_quantity = cement_quantity

    def bricks_cost(self):
        res= 0
        if self.bricks_quantity > 0:
            res = self.bricks_quantity * 35
            return f"Bricks Quantity is : {self.bricks_quantity}, total cost of bricks: {res}"
        else:
            return f"InValid input of Bricks Quantity: {self.bricks_quantity}"

    @abstractmethod
    def cement_cost(self):
        pass


#constr = Construction("Hammad", 400, 100)
#myval1 = constr.bricks_cost()
#print(myval1)
# We cannot instatinate the abstarct class, get error TypeError: Can't instantiate abstract class Construction with abstract method cement_cost

# Lets use abstract class in derived/subclass/child class

class GroundFloor(Construction):
    def __init__(self, owner_name, bricks_quantity, cement_quantity, msand_quantity):
        super().__init__(owner_name, bricks_quantity, cement_quantity)
        self.msand_quantity = msand_quantity

    def cement_cost(self):
        total =0
        if self.cement_quantity > 0:
            total = self.cement_quantity * 350
            return f"Cement Quantity : {self.cement_quantity}, total Cement cost : {total}"
        else :
            return f"InValid Input of Cement Quantity : {self.cement_quantity}"

    def msand_cost(self):
        total = 0
        if self.msand_quantity > 0:
            total = self.msand_quantity * 650
            return f"Msand Quanity is Tons : {self.msand_quantity}, total cost : {total}"
        else:
            return f"Invalid Input it should be in Tons 1 ton means 1000Kg : {self.msand_quantity}"


groundfloor = GroundFloor("Hammad", 500, 200, 7)
res54_1 = groundfloor.owner_name
res54_2 = groundfloor.bricks_cost()
res54_3 = groundfloor.cement_cost()
res54_4 = groundfloor.msand_cost()

print(f"Question 54 ABSTRACT CLASS answer is : ")
print(f"    Owner_name : {res54_1}")
print(f"    Bricks cost: {res54_2}")
print(f"    Cement Cost: {res54_3}")
print(f"    MSAND cost : {res54_4}")

# INTERFACE
# Interfaces (using Abstract Base Classes)
# In Python, an "interface" is typically implemented as an abstract base class where all methods are abstract.
# This means the class defines a contract that any implementing subclass must adhere to, without providing any default implementations.
# Python provides the abc module to define ABC(Abstract base class) and enforce the implementation of abstract methods in subclasses.
# from abc import ABC, abstractmethod
# class goal(abc):
#
#   @abstarctmethod
#   def aim(self):
#       pass
#
#   @abstarctmethod
#   def workhard(self):
#       pass
#
#   @abstarctmethod
#   def skils(self)
#       pass
# Note: code/definition/statements in Interface class not Implemented, it is a blueprint.
# We cannot instantiate the class, subclass/derivied/child class will use this abstract/interface class and implement the code.
# Where as in INTERFACE all methods are abstractmethods, it is a blueprint.
# subclass/derivied/child class will use this abstract/interface class and methods to implement the code.

# 55) Write a program for Interface class:

# import abc module first
from abc import ABC, abstractmethod


class ConstructionCost(ABC):
    def __init__(self, owner_name, bricks_quantity, cement_quantity):
        self.owner_name = owner_name
        self.bricks_quantity = bricks_quantity
        self.cement_quantity = cement_quantity

    @abstractmethod
    def bricks_cost(self):
        pass

    @abstractmethod
    def cement_cost(self):
        pass

    @abstractmethod
    def msand_cost(selfself):
        pass

#constr = ConstructionCost("Hammad", 400, 100)
#myval1 = constr.bricks_cost()
#print(myval1)
# We cannot instatinate the abstarct class, get error TypeError: Can't instantiate abstract class Construction with abstract method cement_cost

# Lets use Interface class in derived/subclass/child class

class FirstFloor(ConstructionCost):
    def __init__(self, owner_name, bricks_quantity, cement_quantity, msand_quantity):
        super().__init__(owner_name, bricks_quantity, cement_quantity)
        self.msand_quantity = msand_quantity

    def bricks_cost(self):
        res = 0
        if self.bricks_quantity > 0:
            res = self.bricks_quantity * 35
            return f"Bricks Quantity is : {self.bricks_quantity}, total cost of bricks: {res}"
        else:
            return f"InValid input of Bricks Quantity: {self.bricks_quantity}"

    def cement_cost(self):
        total =0
        if self.cement_quantity > 0:
            total = self.cement_quantity * 350
            return f"Cement Quantity : {self.cement_quantity}, total Cement cost : {total}"
        else :
            return f"InValid Input of Cement Quantity : {self.cement_quantity}"

    def msand_cost(self):
        total = 0
        if self.msand_quantity > 0:
            total = self.msand_quantity * 650
            return f"Msand Quanity is Tons : {self.msand_quantity}, total cost : {total}"
        else:
            return f"Invalid Input it should be in Tons 1 ton means 1000Kg : {self.msand_quantity}"


firstfloor = FirstFloor("Hammad", 500, 200, 7)
res55_1 = firstfloor.owner_name
res55_2 = firstfloor.bricks_cost()
res55_3 = firstfloor.cement_cost()
res55_4 = firstfloor.msand_cost()

print(f"Question 55 INTERFACE answer is : ")
print(f"    Owner_name : {res55_1}")
print(f"    Bricks cost: {res55_2}")
print(f"    Cement Cost: {res55_3}")
print(f"    MSAND cost : {res55_4}")

# What is Polymorphism in Python?
# The term polymorphism refers to a function or method taking different forms in different contexts.
# Since Python is a dynamically typed language, polymorphism in Python is very easily implemented.
# If a method in a parent class is overridden with different business logic in its different child classes,
# the base class method is a polymorphic method.

# Ways of implementing Polymorphism in Python
# There are four ways to implement polymorphism in Python −

# Duck Typing
# Operator Overloading
# Method Overriding
# Method Overloading

# Duck Typing
# Duck typing is a concept where the type or class of an object is less important than the methods it defines.
# Using this concept, you can call any method on an object without checking its type, as long as the method exists.
# This term is defined by a very famous quote that states: Suppose there is a bird that walks like a duck,
# swims like a duck, looks like a duck, and quaks like a duck then it probably is a duck.
# We can pass any class or method from function/method.

# 56 write a program for duck typing

class Duck:
    def sound(self):
        return "Quack Quack"

class Bird:
    def sound(self):
        return "I am Similar to Duck"

def make_sounds(myval):
    print(myval.sound())

# Create instances for class

duck = Duck()
bird = Bird()

# Call function/method with instances
print("Question 56 POLYMORPHISM DUCK TYPE answer : ")
make_sounds(duck)
make_sounds(bird)


# Method Overriding in Python
# In method overriding, a method defined inside a subclass has the same name as a method in its superclass
# but implements a different functionality.

# 57 Write a program for Method Overriding
from abc import ABC, abstractmethod
class Shapes(ABC):
    @abstractmethod
    def draw(self):
        return

# Shapes class in abstract/interface blueprint, we need to inherit in subclass/child class and implement is function
# draw method will be overriding with different busniness logic/code

class Circle(Shapes):
    def draw(self):
        super().draw()
        print(" Draw a Circle")
        return

class Rectangle(Shapes):
    def draw(self):
        super().draw()
        print(f" Draw a Rectangle")
        return

circle = Circle()
rect = Rectangle()

print(f"Question 57 Method Overriding answer is: ")
for x in [circle, rect]:
    x.draw()

# Operators overloading
# Operator Overloading means giving extended meaning beyond their predefined operational meaning.
# For example operator + is used to add two integers as well as join two strings and merge two lists.
# It is achievable because '+' operator is overloaded by int class and str class.
# You might have noticed that the same built-in operator or function shows different behavior for objects of different classes,
# this is called Operator Overloading.
# + Operator perform addition of integer, same operator perform concatenation of string,
# * Operator perform multiplication of integer, same operator perform repeatation of word ("greek"*4)
# Note: __str__ Operator will return the values

# 58 Write a program for Operator Overloading

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "point({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x, y)

p1= point(3, 4)
p2 = point(3, 4)
print(f"Question 58 OPERATOR OVERLOADING answer is : ")
print(p1 + p2)

# METHOD OVERLOADING
# When a class contains two or more methods with the same name but different number of parameters or datatypes
# then this scenario can be termed as method overloading.
# Python does not allow overloading of methods by default, however,
# we can use the techniques like argument lists, multiple dispatch and default parameters to achieve this.
# For multiple dispatch we need to install pip install multipledispatch
# for example len() function/method will get len info for list, tuples, dictionary and strings, this is method overloading

# 59 Write a program for method overloading

# argument techniques

def add(*args):
    return sum(args)

num = add(2, 3)
num1 = add(4, 4, 2)
print(f"Question 59 METHOD OVERLOADING answer are : ")
print(f"    ARGS techniques : {num}, {num1}")

# default None techiques

def add(x=None, y=None, z=None):
    r = 0
    if x != None and y != None and z != None:
        r = x+y+z
    elif x != None and y !=None and z==None:
        r = x+y
    return r

obj = add(2, 2, 6)
obj1 = add(10, 20)
print(f"    DEFAULT NONE technique : {obj}, {obj1}")

# multipledispatch
# install pip install multipledispatch

from multipledispatch import dispatch
class example:
   @dispatch(int, int)
   def add(self, a, b):
      x = a+b
      return x
   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a+b+c
      return x

ex = example()
obj = ex.add(10, 20 , 30)
obj1 = ex.add(10, 20)
print(f"    MULTIPLEDISPATCH technique : {obj}, {obj1}")

# WRAPPER IN PYTHON

# Function wrappers, also known as decorators, are a powerful and useful feature in Python
# that allows programmers to modify the behavior of a function or class without changing its actual code.
# means calling function under another function.
# Decorators enable wrapping another function to extend or alter its behavior dynamically at runtime.

# 60 write the program for WRAPPER Function or Class

def div(a, b):
    print(a/b)

# Above the actually function/method, we dont want to alter its code to swap the values.
# Cos we have imported or inbuilt function.
# So we can write the decorators/wrappers to alert the function behaviuor in different function
# So we can function under function

# let's write the decorator function

def smart_div(func):
    def inner_func(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner_func

div = smart_div(div)
print(f"Question 60 DECORATOR/WRAPPER answer is : ")
div(2, 4)

# calling using decorator
@smart_div
def sub(a, b):
    print(a - b)

sub(2, 5)
