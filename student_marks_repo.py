class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __repr__(self):
        return f"Name: {self.name}\nRoll number: {self.roll_no}\nMarks: {self.marks}"


rohan = Student("Rohan Joshi", "32", "89/100")
john = Student("John Smith", "66", "34/100")
print(john.__repr__())
