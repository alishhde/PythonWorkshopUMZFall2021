
def w(n):
    return lambda x : x + n

var = w(3)      # This equals to lambda x : x + 3
print(var(3))

x = lambda r : r * 5

# print(x(5))



# def func(n):
#     return lambda x : x * n

# r = func(3)
# t = func(2)

# print(r(3))
# print(t(3))

