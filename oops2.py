class Student:
    '''class to form the data of student'''
    student_name = "KARAN"
    student_id="20BCS1794"       

    # def display(self):
    #     print(f"NAME OF STUDENS IS {self.name}  HAVING UID :{self.id}")

    # def change_age(slf,Cage):
    #     slf.age=Cage


p = Student()
print(f"ATTRIBUTES INITIALLY............\nNAME OF THE STUDENT:{p.student_name} \nUID of the student: {p.student_id}\n")
# print(Student.__dict__)
Student.student_class = "608(A)"
print(f"ATTRIBUTES AFTER ADDING NEW ATTRIBUTE............\nNAME OF THE STUDENT:{p.student_name} \nUID of the student: {p.student_id}\nClass of the student {Student.student_class}\n")
del Student.student_name
print(f"ATTRIBUTES AFTER DELETING AN ATTRIBUTE............\nNAME OF THE STUDENT: DELETED \nUID of the student: {p.student_id}\nClass of the student {Student.student_class}")

 
# print(Student.__dict__)

# p.display() 
# p.change_age(34)
# p.display()

class py_solution:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))
