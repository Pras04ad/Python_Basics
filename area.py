radius = [10,15,20]

def diff(r):
    difference = []

    for i in r:
        difference.append((2*i)**2 - (i*1.414)**2)

    return difference
out = [radius,diff(radius)]
print(out)
