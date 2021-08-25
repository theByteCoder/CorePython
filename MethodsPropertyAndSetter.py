class Employee:
    def __init__(self, fname, lname, domain):
        self.fname = fname
        self.lname = lname
        self.domain = domain

    def __str__(self):
        return f'{self.fname} {self.lname}'

    def __repr__(self):
        return f'Employee({self.fname}, {self.lname}, {self.domain})'

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@{self.domain}'

    @email.setter
    def email(self, email):
        name, self.domain = email.split('@')
        self.fname, self.lname = name.split('.')

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        # self.email = None


if __name__ == "__main__":
    subhasish = Employee("Subahsish", "Ghosh", "gmail")
    print(subhasish.email)
    subhasish.email = "subh.ghosh@gmail.com"
    print(subhasish.email)
    del subhasish.email
    print(subhasish.email)
