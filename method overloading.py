class overload:
    def multiply(self,a,b):
        print(a*b)
    def multiply(self,a,b,c):
        print(a*b*c)
m = overload()
m.multiply(5, 6, 10)

# NOTE : Python does not allow method overloading based on type,number or sequence of 
# parameters. 
# In Python,method overloading is a technique to define a method in such a way that there
# are more than way to call it.
# This is different from other programming languages.