import math
def totalarea(d,w):
    return 2*math.pi*(d/2)*w*2.54*2.54
def totalcost(a):
    return a*75
diameter = [15,16,17,18]
width = [6,7,8,9]
dic = {}
for i in range(len(diameter)):
    a = totalarea(diameter[i],width[i])
    dic[a] = [diameter[i],width[i]]
for i in dic:
    print("cost:",round(totalcost(i),2) ,    "size:",dic[i])
s  = int(input("enter diameter:"))  
w = 6
if (s>15): 
    w = w+(s-15)
area = round(totalarea(s,w),2)
cost = round(totalcost(area),2)
l = [{area:[s,w]},{cost:[s,w]}]
print(l)
