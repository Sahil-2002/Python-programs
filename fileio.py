f = open("practice.txt","r")

data = f.read()
print(data)

hello = data.endswith("learning")
print(hello)

newdata = data.replace("java","python")
print(newdata)

f = open("practice.txt","w")

f.write(newdata)


f = open("practice.txt","a")

f.write("\n sahil")


f = open("practice.txt","w")

f.write("newdata")