class Employee:
    base_increment = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'__{self.name.lower()}__'

    def __repr__(self):
        return f'Employee({self.name}, {self.age}, {self.salary})'

    def __add__(self, other):
        return self.salary + other.salary

    def increase_age(self):
        self.age += 1

    def increase_salary(self):
        self.salary += self.base_increment

    @classmethod
    def increase_increment(cls, base_increment=0):
        cls.base_increment += base_increment

    @staticmethod
    def is_on_leave(day="monday"):
        if day.lower() == "sunday" or day.lower() == "saturday":
            return True
        return False


class Developer(Employee):

    def __init__(self, name, age, salary, role):
        super().__init__(name, age, salary)
        self.role = role

    def increase_salary(self, percentage):
        self.salary += self.base_increment + 100000 * percentage


class AutomationTester(Employee):

    def __init__(self, name, age, salary, tool):
        super().__init__(name, age, salary)
        self.tool = tool

    def increase_salary(self):
        self.salary += self.base_increment + 50000


if __name__ == "__main__":
    Employee.increase_increment(20000)
    print(Employee.is_on_leave("Tuesday"))

    subhasish = Developer("Subhasish", 30, 3800000, "Fullstack")
    subhasish.increase_age()
    subhasish.increase_salary(3)
    print(subhasish.__dict__)
    print(subhasish.is_on_leave("saturday"))

    piyu = AutomationTester("Piyu", 30, 1800000, "Selenium")
    piyu.increase_age()
    piyu.increase_salary()
    print(piyu.__dict__)
    print(piyu.is_on_leave("sunday"))
    print(piyu.__repr__())

    print(Employee.__name__)
    print(__name__)

    print(subhasish + piyu)
