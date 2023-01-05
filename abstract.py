from abc import ABC, abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
class Triangle(polygon):
    def sides(self,a):
        self.a = a
        print("I have", self.a ,"sides")
class Pentagon(polygon):
    def sides(self):
        print("I have 5 sides")

t = Triangle()
t.sides(3)
p = Pentagon()
p.sides()
