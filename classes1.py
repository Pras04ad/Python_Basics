class sample:
    def disp(self):
        print("Hello World")
o=sample()
o.disp()

class student:
    sno=1
    name='siva'
    gen="M"
    age=28
    def disp(self):
        print("number:",self.sno)
        print("name:",self.name)
        print("gender:",self.gen)
        print("age:",self.age)
o1=student()
o2=student()
o1.disp()
o2.disp()      

class student:
    def getdata(self):
        self.sno=int(input("Number:"))
        self.name=input("Name:")
        self.age=int(input("Age:"))
    def disp(self):
        print("Age is ",self.age)
        print("Number is ",self.sno)
        print("Name is ",self.name)    
o1=student()
o2=student()
o1.getdata()
o2.getdata()
o1.disp()
o2.disp()      


class student:
    def getdata(self,sno,name,age):
        self.sno=sno
        self.name=name
        self.age=age
    def disp(self):
        print("Age is ",self.age)
        print("Number is ",self.sno)
        print("Name is ",self.name)    
o1=student()
o2=student()
o1.getdata(1,'Prudhvi',18)
o2.getdata(2,'Prasad',20)
o1.disp()
o2.disp()  


# class student:
#     def __init__(self,sno,name,age):  #Constructor - (__init__)
#         self.sno=sno
#         self.name=name
#         self.age=age
#     def disp(self):
#         print("Age is ",self.age)
#         print("Number is ",self.sno)
#         print("Name is ",self.name)    
# o1=student(1,'Prudhvi',18)
# o2=student(2,'Prasad',20)
# o1.disp()
# o2.disp()


class emp:
    def getdata(self,eno,name,sal):
        self.eno=eno
        self.name=name
        self.sal=sal

o=emp()
o.getdata(1,'siva',12000)
print("Emplyoee Number: ",getattr(o,'eno'))
print("Emplyoee Name: ",getattr(o,'name'))
print("Emplyoee Salary: ",getattr(o,'sal'))
            # Emplyoee Number:  1
            # Emplyoee Name:  siva
            # Emplyoee Salary:  12000
setattr(o,'eno',2)
setattr(o,'name','ram')
setattr(o,'sal',20000)
print("Emplyoee Number: ",getattr(o,'eno'))
print("Emplyoee Name: ",getattr(o,'name'))
print("Emplyoee Salary: ",getattr(o,'sal'))

print(hasattr(o,'eno'))
print(hasattr(o,'name'))
print(hasattr(o,'sal'))
delattr(o,'eno')
print(hasattr(o,'eno'))

class emp:
    '''Employee class.....'''
    def getdata(self,eno,name,sal):
        self.eno=eno
        self.name=name
        self.sal=sal

o=emp()
o.getdata(1,'siva',12000)
print(o.__dict__)    #prints all variables in a dictionary
print(o.__doc__)    # prints the multi-line comments 
print(o.__module__)
