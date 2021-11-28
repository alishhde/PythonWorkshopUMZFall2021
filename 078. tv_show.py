

tv = ["show1", "show2", "show3", "show4"]
for i in tv:
    print(i)

newtv = input("Enter another TV SHOW: ")
position = int(input("Enter a number between 0 and 3: "))
tv.insert(position, newtv)
for i in tv:
    print(i)