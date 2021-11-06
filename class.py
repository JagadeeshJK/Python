class Employee:
    perc_raise = 1.5
    def __init__(self, first, last, salary):
        self.fname = first
        self.lname = last
        self.sal = salary
        self.email = first + '.' + last + "@gmail.com"

    def fullname(self):
        return '{}{}'.format(self.fname, self.lname)
    def apply_raise(self):
        self.sal = int(self.sal*1.5)

emp_1 = Employee("Ramesh", "Suresh", 400000)
emp_2 = Employee("Mani", "harish", 700000)

print(emp_1.sal)
emp_1.apply_raise()
print(emp_1.sal)
print(getattr(emp_1, 'sal'))

