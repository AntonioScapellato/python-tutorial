#############################################################
#
#  OOP - Object Oriented Programming
#  @author: Antonio Scapellato
#
#  Book: Python - Everything to know to get started
#
#############################################################

# 1

class MyClass:
  age = 100
  Name = "Antonio"


myObject = MyClass()
print(myObject.age)

# 2

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("Antonio", 10000)

print(p1.name)
print(p1.age)


# 3

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Antonio", 1000)
p1.myfunc()