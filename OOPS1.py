
class Student:
    name = "karan"             #class variables
    std = 12
    course = "COMPUTER"
    def __init__(self,nam,kilas,kors) :           # here self = name of the object
        self.name = nam
        self.std = kilas
        self.course = kors

    def details(self):
        print(f"Name is {self.name} Standard is {self.std} Course is {self.course}")

    @classmethod
    def change_course(cls,new_course):             #here cls = name of the class 
        cls.course = new_course

    @classmethod
    def from_dash(cls , string):
        spl = string.split("-")
        return    cls(spl[0],spl[1],spl[2])


p = Student("karan","608(B)","pyhton")
p.details()
print(p.__dict__)
# a = Student()
# b= Student()
# print(b.name)
# Student.name = "RAJAN"     # changwe the value of class variable by class_name.variable_name 
# a.name = "AMAN"        #this will not change the 'name' variable in class but a new instance variable called 'name' will be created for 'a' object
# a.uid = "238982"    #instance variable
# print(f"{a.course} {a.name} {a.std} {a.course} {a.uid}") 
# a.change_course("PYT")    #fuction to change the class variable
# print(a.course)
# print(Student.course)
# print(f"{a.course} {a.name} {a.std} {a.course} {a.uid}") 
 
# print(b.name)
# print(a.__dict__)
# print(Student.__dict__)  #print dictionary of elements of Student Class
# a.details()
 
a= Student("FATIM",11,"LEARNING")        #calling the constructor that takes 3 arguments and change the instance variable values
a.details()  


# b= Student.from_dash("RASHMI-10-CRITICAL THINKING")        #calling the classs method that takes 1 arguments and cahnge the instance variables
# b.details() 

print(Student.name)                #class variables are as it is

print(id(a))





