class Student:
    def __init__(self,name:str,age:int,adress:str,marks:int):
        self.name=name 
        self.age=age
        self.adress =adress 
        self.marks=marks
        
class studentManagementSystem:
    def __init__(self):
        self.students=[]
    def add_student(self):
        try :
            name=str(input("enter name : " ))
        except Exception:
            print("enter a valid input")
        try :
            age=int(input("enter your age : "))
        except Exception:
            print("enter a valid input")
        try :
            adress=str(input("enter your adress : "))
        except Exception:
            print("enter a valid input")
        try :
            marks=int(input("enter your marks : "))
        except Exception:
            print("enter a valid input")
        
        student=Student(name,age,adress,marks)
        self.students.append(student)
        print("student sucessfully added ")
        return Student
    def viewStudents(self):
        if len(self.students)==0:
            print("no students found")
        else:
            view_type = input(" all students or onr student ? (all/one): ")
            if view_type=="all": 
                for student in self.students:
                    print(f"name: {student.name}, \nage:{student.age},\nadress : {student.adress}\nmarks: {student.marks}%")
            if view_type=="one":
                name=input("enter the name of student you want to see : ")
                for student in self.students:
                    if student.name==name:
                        print(f"name: {student.name}, \nage:{student.age},\n adress : {student.adress}\n marks: {student.marks}%")
    def delete_students(self):
        name=input("enter the student you want to delete") 
        for student in self.students:
                    if student.name==name:
                        self.students.remove(student)
        print("student sucessfully deleted")           
        return Student
    def update_student(self):
        name=input("\nenter the name you wamt to update : ")
        for student in self.students:
            if student.name==name:
                print("\nWhat you want to update ?")
                print("\n1. To edit name")    
                print("2. To edit age")    
                print("3. To to edit address")    
                print("4. To edit the marks")
                print("5. To exit \n")
                try:
                    choice=int(input("enter your choice : "))
                except Exception:
                    print("enter a integer value")
                if choice==1:    
                    student.name=input("enter name : ")
                    print("student sucessfully updated \n")
                    return Student
                if choice==2:
                    student.age=int(input("enter your age : "))
                    print("student sucessfully updated \n")
                    return Student
                if choice==3:
                    student.adress=input("ente your adress : ")
                    print("student sucessfully updated \n")
                    return Student
                if choice==4:
                    student.marks=int(input("enter your marks : "))
                    print("student sucessfully updated \n")
                    return Student
                if choice==5:
                    break
        print("student not found")
                          
print("\n------------------------------------")
print("Welcome to student management system")
system =studentManagementSystem()
try:
    while True:

        print("\n\n1. Add student")
        print("2. Delete Student")
        print("3. update student")
        print("4. View student")
        print("5. exit student\n\n")
    
        choice=int(input(" enter your choice : "))
        
        if choice==1:
            system.add_student()
        if choice==2:
            system.delete_students()
        if choice==3:
            system.update_student()
        if choice==4:
            system.viewStudents()
        if choice==5:
            print("exited successfully !")
            break
        
except Exception:
    print("something went wrong try again")