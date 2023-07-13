stock = {'101A': ['Brown rice ', 50, 45.50, 41.25],
        '102B': ['Whole wheat ', 30, 27.45, 21.50],
        '102C': ['Tomato sauce ', 25.50, 20.25, 18.70],
        '103D': ['Mustard ', 40, 39.45, 37],
        '104E': ['Barbecue sauce ', 45, 43, 41.50],
        '105F': ['Red-wine vinegar ', 4000, 3800, 3750],
        '106G': ['Salsa ', 200, 189.50, 170],
        '107H': ['Extra virgin olive oil', 500, 478.50, 455.70],
        '108I': ['canola oil ', 200, 180, 118],
        '109J': ['Hot pepper sauce ', 100, 98.5, 91.25],
        '110K': ['Bananas ', 60, 55, 50],
        '111L': ['Apples ', 300, 250, 120],
        '112M': ['Oranges ', 200, 140, 110],
        '113N': ['Mangoes ', 100, 80, 50],
        '114O': ['Strawberries ', 100, 90, 80],
        '115P': ['Blueberries ', 95, 80, 75],
        '116Q': ['Green teas ', 250, 25, 200],
        '117R': ['Sparkling water ', 20, 14.50, 11],
        '118S': ['Dried apricots ', 270, 250, 230],
        '119T': ['Dried figs ', 100, 95, 90],
        '120U': ['Dried prunes ', 90, 85, 80],
        '121V': ['Almonds ', 900, 870, 850],
        '122W': ['Cashews ', 1000, 950, 910],
        '123X': ['Walnuts ', 800, 770, 720],
        '124Y': ['Peanuts ', 400, 380, 360],
        '125Z': ['Pecans ', 350, 320, 300],
        '201A': ['Pistachios ', 1200, 1180, 1160],
        '202B': ['Sunflower seeds ', 150, 112, 50],
        '203C': ['Sesame seeds ', 103.45, 120.50, 110.40],
        '204D': ['Whole flaxseeds ', 95.20, 90.45, 89.20]}
customer = {'9500012345': ['Surian', 'AAA1001'],
            '9500023456': ['Nila', 'AAA1002'],
            '9712300078': ['Arivazhagan', 'AAA1003'],
            '9586233333': ['Nithin Kumar', 'AAA1004'],
            '6931245872': ['Aravind', 'AAA1005']}
b=0
n = int(input('enter the number of items purchased: '))
for i in range(n):
    c = input("enter the item code: ")
    q = int(input('enter the quality of item(1/2/3): '))
    w = float(input('enter the quantity of item: '))
    b+=stock[c][q]*w

cid = input('enter the customer id: ')
na = input('enter the customer name: ')
num = input('enter the number of customer: ')
if (len(num) != 10):
    print('enter a valid name ')

if cid!='':
    if (customer[cid][0]==na and customer[cid][1]==num):
        b = b - 0.012*b

else:
    if(b>10000):
        b = b - 0.01*b
print('your bill amount is: ',b) 
