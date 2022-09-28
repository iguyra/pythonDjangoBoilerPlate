

# defining a class
import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@email.com"

    def fullName(self):
        return self.last + " " + self.first

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

        # self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):  # cls is the class itself(Employee)
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "not a workday"
        return "is a workday"


class Developer(Employee):
    pass


empl1 = Developer("trim", "look", 50000)
fName = empl1.fullName()

empl1_dic = empl1.__dict__
print(empl1_dic["first"])

raised = empl1.apply_raise()
# print(f"{empl1.pay}")


my_date = datetime.date(2020, 7, 10)

print(Employee.is_workday(my_date))
