s = input("list of string ")
items = s.split()
ls = [eval(value) for value in items]
print(ls)
