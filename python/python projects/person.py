class Person:
    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return self.fname, self.lname

    def say_hello(self, fname, lname):
        print("hello, my_name is ", fname, lname)


Person.say_hello("abby", "donoghue")

