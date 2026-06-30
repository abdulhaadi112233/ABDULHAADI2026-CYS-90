r = "r"        # read mode
w = "w"        # write mode
a = "a"        # append mode
b = "b"        # binary mode

f = open("shayan", r)  # open in read mode
content = f.read()
print(content)
f.close()