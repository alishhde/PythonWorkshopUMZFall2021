
print("Enter a sequence of comma separated number: ")
inp = input()
lst = list(inp.split(","))
tp = tuple(inp.split(","))
print(lst, tp, sep=" ===> ")