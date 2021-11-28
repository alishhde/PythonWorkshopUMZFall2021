from time import sleep

# First Let's read the Documentation of the print method
print(print.__doc__) 
"""
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
"""

# # Example 1 - separate 
# print("This", "is", "going", "to", "be", "Fun", sep="----")

# # Example 2 - end
# for i in range(5):
# print("This", "is", "going", "to", "be", "Fun", sep=" ", end=" ")
# print("this is")

# # Example 3 - 
# for i in range(5):
#     print("This", "is", "going", "to", "be", "Fun", sep=" ", end=" ")
#     sleep(1)
    
# # Example 3
# for i in range(5):
#     print("This", "is", "going", "to", "be", "Fun", sep=" ", end=" ", flush=True)
#     sleep(1)
