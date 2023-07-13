def reverse_words_order_and_swap_cases(sentence):
    str=''
    for i in sentence:
        if i.isspace():
            str+=" "
        else:
            if i.isupper():
                str+=i.lower()
            if i.islower():
                str+=i.upper()
    out=list(reversed(str.split()))
    new = " ".join(out)
    return new                   
    
x=str(input())
result = reverse_words_order_and_swap_cases(x)
print(result)
    
N = int(input())
lis=list()
for i in range(N):
    s=input().strip().split(" ")
    if s[0]=="insert":
        lis.insert(int(s[1]),int(s[2]))
    if s[0]=="print":
        print(lis)
    if s[0]=="remove":
        lis.remove(int(s[1]))
    if s[0]=="append":
        lis.append(int(s[1]))
    if s[0]=="sort":
        lis.sort()
    if s[0]=="pop":
        lis.pop()
    if s[0]=="reverse":
        lis.reverse()
print(lis)

def print_full_name(first, last):
    if(len(first)<=10 and len(last)<=10):
        s=print("Hello %s %s You just delved into python."%(first,last))
    return s    
      

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# You are given a string s and width w .
# Your task is to wrap the string into a paragraph of width .
import textwrap

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result=string[i:i+max_width]
        if len(result)==max_width:
            print(result)
        else:
            return(result)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

# You are given a string .
# Your task is to find out if the string  contains: alphanumeric character,
#  alphabetical characters, digits, lowercase and uppercase characters.

def pot(t):
    if t==1:
        print(True)
    elif t==0:
        print(False)    
if __name__ == '__main__':
    s = input() 
t=0
for i in s:
    if i.isalnum()==True:
        t=1
        break
pot(t)
t=0
for i in s:
    if i.isalpha()==True:
        t=1
        break
pot(t)
t=0
for i in s:
    if i.isdigit()==True:
        t=1
        break
pot(t)
t=0
for i in s:
    if i.islower()==True:
        t=1
        break
pot(t)
t=0
for i in s:
    if i.isupper()==True:
        t=1
        break
pot(t)
    
# Given  sets of integers,  and , print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in 
# either  or  but do not exist in both.
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a1=map(int, input().split(' '))
n=int(input())
b1=map(int, input().split(' '))
a=set(a1)
b=set(b1)
t1=a.difference(b)
t2=b.difference(a)
t3=t1.union(t2)
res=sorted(t3)
for i in res:
    print(i)     
l=[1,2]
p=[4,5]
q=[l,p]
print(q)