class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        average = sum(self.marks) / len(self.marks)
        print(f"{self.name} average: {average}")
        return average

    def go_to_school(self):
        print(f"{self.name} is going to school")

    @classmethod
    def go_to_school_class(cls):
        print("I'm going to school")
        print(f"I'm a {cls}")

    @staticmethod
    def go_to_school_static():
        print("I'm going to school")


anna = Student("Anna", "MIT")
anna.marks.append(98)
anna.marks.append(33)
print(anna.marks)

helen = Student("Helen", "MIT")
helen.marks.append(32)
helen.marks.append(55)
print(helen.marks)
print(helen.average())

anna.go_to_school()
print("Class methods")
anna.go_to_school_class()
Student.go_to_school_class()
print("Static methods")
anna.go_to_school_static()
Student.go_to_school_static()

