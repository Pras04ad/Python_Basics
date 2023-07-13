
def count(n,m):
    ducksc = 0
    ducksc = 4*n-m
    ducksc = ducksc/2
    return ducksc

def main():
    n=int(input("Enter number of heads:"))
    m = int(input("Enter the number of legs:"))
    Ducks = count(n,m)    
    print("{}-Ducks".format(int(Ducks)))
    print("{}-Cows".format(int(n-Ducks)))
main()    
