def recur_Fibonacci_seq(n):
    if n<=1:
        return n
    else:
        return(recur_Fibonacci_seq(n-1) + recur_Fibonacci_seq(n-2))

a = 4
val = recur_Fibonacci_seq(a)
print(val)
