class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my anme is', self.name)

p = Person('Yangmal')
p.say_hi()