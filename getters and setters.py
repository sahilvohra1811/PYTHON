class a:
    def __init__(self):
        self.name = None
        self.age = 0
    
    #GETTER
    def get_name(self):
        return self.name
    #SETTER
    def set_name(self,x):
        self.name = x

object = a()
object.set_name("sahil")
print(object.get_name())