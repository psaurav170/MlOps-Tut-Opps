# Single or Basic inheritance:

#Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}!")
    
# # Derived class
# class child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")


# # create an instance of child
# child = child('Saurav')
# child.greet()
# child.play()

# -------------------------------------------------------

# Multilevel Inheritance
#Base class
# class GrandParent:
#     def __init__(self, name):
#         self.name = name
    
#     def tell_story(self):
#         print(f"{self.name} tells a story.")
    
# # Intermediate class
# class Parent(GrandParent):
#     def work(self):
#         print(f"{self.name} is working.")


# # Derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")


# # create an instance of child
# child = Child('Saurav')
# child.tell_story()
# child.work()
# child.play()


# -------------------------------------------------------

# Hierarchial Inheritance

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello my name is {self.name}")
    
# # Derived class 1
# class Child1(Parent):
#     def work(self):
#         print(f"{self.name} is working.")


# # Derived class 2
# class Child2(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")


# # create an instance of child 1 and child 2
# child1 = Child1('Saurav')
# child2 = Child2('Pooja')

# child1.greet()
# child1.work()


# child2.greet()
# child2.play()

# -------------------------------------------------------
# Multiple Inheritance <Dimond Problem>

# Common base class
# class A:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello from A, {self.name}.")
    
# # Intermediate class 1
# class B(A):
#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()


# # Intermediate class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()


# # Derived class
# class D(B,C):
#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()


# # create an instance of D
# d = D('Frank')
# d.greet()

# -------------------------------------------------------
# Multiple Inheritance <Dimond Problem>

# Common base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes sound.")
    
# Intermediate class 1 (Hierarchial)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")


# Intermediate class 2 (Hierarchial)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")


# Derived class (multiple inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")


# create an instance of D
bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()
