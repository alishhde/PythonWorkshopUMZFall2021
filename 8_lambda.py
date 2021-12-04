
def w(n):
    return lambda x : x + n

var = w(10) # This equals to lambda x : x + 10
print(var(3))