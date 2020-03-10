class Student:
    def __init__(self, fullname, age, major):
        self.fullname = fullname
        self.age = age
        self.major = major

    def __str__(self):
        return f'name: {self.fullname}, age: {self.age}, major: {self.major}'


Steve = Student('Steven Schultz', 23, 'English')
print(Steve)
Johny = Student('Jonathan Rosenberg', 24, 'Biology')
print(Johny)