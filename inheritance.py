# class father:
#     fathername = ""
#     def show_father(self):
#             print("Father :",self.fathername)
        
# class son(father):
#     # mothername = ""
#     def show_mother(self):
#             print("Mother :",self.mothername)
        
# class child(father,mother):
#     def show_parent(self):
#         print("father Name :",self.fathername)
#         print("mother Name :",self.mothername)

# c = child()
# c.fathername = "SHABBIR BHAI"
# c.mothername = "KULSUM BEN"
# c.show_parent()

class parent:
    parentname=""
    childname=""
    def show_parentname(self):
        print(self.parentname)
class son(parent):
    def show_child(self):
        print(self.childname)
class daughter(parent):
    def show_child(self):
        print(self.childname)
s1 = son()
s1.parentname="sabbir bhai"
s1.childname="sahil"
s1.show_parentname()
s1.show_child()
d1 = daughter()
d1.childname = "saniya"
d1.parentname="sabbir bhai"
d1.show_parentname()
d1.show_child()