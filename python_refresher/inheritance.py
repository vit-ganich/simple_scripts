class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        average = sum(self.marks) / len(self.marks)
        print(f"{self.name} average: {average}")
        return average

    @classmethod
    def friend(cls, origin, friend_name, *args):
        """returns a new object with a name and the same school"""
        return cls(friend_name, origin.school, *args)


anna = Student("Anna", "Gymn. #14")


##


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent("Anna", "Krakow", 500)
friend = WorkingStudent.friend(anna, "Greg", 55)

print(anna.salary)
print(friend.salary)
