class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}"\tAge: "{}"'.format(self.name, self.age), end="\t")
    
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t1 = Teacher('Mrs. Shrividya', 40, 130000)
t2 = Teacher('Mr. Sony', 30, 230000)
t3 = Teacher('Miss. Lim', 50, 330000)
t4 = Teacher('Mr. Yangmal', 570, 430000)
s1 = Student('Swaroop', 25, 75)
s2 = Student('Haricane', 26, 80)
s3 = Student('Sunny', 27, 85)
s4 = Student('한글이름', 28, 90)

print("***")

members = [t1, t2, t3, t4, s1, s2, s3, s4]
for member in members:
    member.tell()