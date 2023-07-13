import re

data = 'Welcome to Python Programming Course'
x = re.search("^Welcome.*Course$",data)
print(x)                                                     
if x:
    print("matched")
else:
    print("not matched")
 
#<re.Match object; span=(0, 36), match='Welcome to Python Programming Course'>
#matched

data = ' Python Programming welcomes You'
x = re.search("^Welcome.*Course$",data)
print(x)
if x:
    print("matched")
else:
    print("not matched")
#None
#not matched

data = ' Python Programming welcomes You'
x= re.findall('[p-z]',data)
print(x)
#['y', 't', 'r', 'r', 'w', 's', 'u']

x= re.findall('[aeiou]',data)
print(x)
#['o', 'o', 'a', 'i', 'e', 'o', 'e', 'o', 'u']

x= re.findall('[^aeiou]',data)
print(x)
#[' ', 'P', 'y', 't', 'h', 'n', ' ', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g', ' ', 'w', 'l', 'c', 'm', 's', ' ', 'Y']


data = ' Python Programming Editor IDLE 3.7.8 Welcomes You'
x = re.findall('\d',data)
print(x)
#['3', '7', '8']    \d - for numbers

x = re.findall('\D',data)
print(x)                    #\D- for only characters
#[' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'E', 'd', 'i', 't', 'o', 'r', ' ', 'I', 'D', 'L', 'E', ' ', '.', '.', ' ', 'W', 'e', 'l', 'c', 'o', 'm', 'e', 's', ' ', 'Y', 'o', 'u']


data = 'Python Welcomes You'
x = re.findall('Py.*n',data)
print(x)
#['Python']

data = 'Python Programming Welcomes You'
x = re.findall('Wel.?comes',data)
print(x)
#['Welcomes']


data = 'Python Programming Welcomes You'
x = re.findall('Pro.{5}ing',data)
print(x)
#['Programming']

data = 'Python Welcomes You'
x = re.findall('Python|Programming', data)
print(x)
#['Python']


x = re.findall("\APython",data)
print(x)
#['Python']

data = "Python Programming Welcomes You"
x = re.findall(r"\bPy", data)
print(x)
#['Py']

x = re.findall(r"mming\b", data)
print(x)
#['mming']


x = re.findall(r"\Btho", data)
print(x)
#['tho']


data = "Python Programming Welcomes You"
x = re.findall("\w", data)
print(x)
#['P', 'y', 't', 'h', 'o', 'n', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'W', 'e', 'l', 'c', 'o', 'm', 'e', 's', 'Y', 'o', 'u']

data = "Python Programming Welcomes You"
x = re.findall("\W", data)
print(x)
#[' ', ' ', ' ']


data = ' Python Programming Editor IDLE 3.7.8 Welcomes You'
x = re.findall('[a-zA-Z]',data)
print(x)
#['P', 'y', 't', 'h', 'o', 'n', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'E', 'd', 'i', 't', 'o', 'r', 'I', 'D', 'L', 'E', 'W', 'e', 'l', 'c', 'o', 'm', 'e', 's', 'Y', 'o', 'u']

data = "Python Programming Welcomes You 70"
x = re.findall('[0-9][0-9]',data)
print(x)
#['70']

