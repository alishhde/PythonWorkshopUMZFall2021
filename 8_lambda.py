
def w(n):
    return lambda x : x + n

var = w(3)      # This equals to lambda x : x + 3
print(var(3))