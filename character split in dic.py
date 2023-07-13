def charcount(a):
    a=a.lstrip("'")
    a=a.rstrip("'")
    words=a.split()
    d1={}
    for i in words:
        d2={}
        for j in i:
            x=i.count(j)
            d2[j]=x
        d1[i]=d2
    return d1
def main():
    a=input("Enter a sentence:")
    z=charcount(a)
    print(z)
main()
