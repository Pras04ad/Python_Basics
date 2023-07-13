'''
print("before exception")
b=[1,2,3,4,5]
try:
    try:
        a=10/0
        print(a)
    except ArithmeticError as o1:
        print("Error 1 : ",o1)
    try:
        print(b[5])
    except IndexError as o2:
        print("Error 2 :",o2)
except Exception as o3:
    print("Error 3: ",o3)
else:
    print("Else block")
print("Rest of CODE")        

'''
print("Before Exception")
age=int(input("Enter your age:"))
if(age>18):
    print("eligible for vote")
else:
    try:
        raise ValueError("UnderAge") 
    except Exception as o:
        print(o)
print("Rest Of Code")