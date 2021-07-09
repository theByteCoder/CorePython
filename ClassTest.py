class ClassTest:
    val = "coding is great"

    def __init__(self, user, pwd, host, db):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.db = db
        print(ClassTest.val, user, pwd, host, db)

    def my_func(self):
        return self.user


ClassTest_obj = ClassTest('rgr1', '****', 'ibm01', 'vtest191')
print(ClassTest_obj.my_func())
print(ClassTest_obj.val)
