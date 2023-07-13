email = str(input())
base_price = int(input())

ex = ''
for i in email:
    if(i.isdigit()):
        ex+=i
print(email)
print(ex)
ex1 = int(ex)
if ex1%400==0:
    discount = 0.18*base_price
else:
    discount = 0.1*base_price

Cgst = 0.15*base_price
Sgst = 0.18*base_price
Ot = 0.05*base_price
price = base_price + Cgst + Sgst + Ot - discount     

rate = 14
r = rate/100
n = 12  #months
emi = (price*r*((1+r)**n)) / (100*(((1+r)**n)-1))
emi1 = round(emi,2)
print(emi1)