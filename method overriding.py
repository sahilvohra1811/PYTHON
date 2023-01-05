class a:
    def display(self):
        print("This is super class")

class b(a):
    def display(self):
        print("This is sub class")
        super().display()
ob = b()
ob.display()
ob1 = a()
ob1.display()