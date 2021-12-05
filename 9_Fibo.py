# Ali Shhde



# The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def fib(n):
    if n == 0:      # Terminate loop condition
        return 0 
    elif n == 1:    # Terminate loop condition
        return 1
    elif n == 2:    # Terminate loop condition
        return 1
    else: 
        return fib(n-1) + fib(n-2)

print(fib(1))