class Person:
  def __init__(selfs, name, age):
    selfs.name = name
    selfs.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()