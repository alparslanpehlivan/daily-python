#import re

#f = open("element.txt", "r")

for line in open("element.txt", "r"):
    data = line.split("Elem ID = ",1)[1]

    file1 = open("id.txt", "a")
    file1.write(data[0:9])
    file1.close()

#for i in f:
#    stringafterword = re.f.readlines(int((i)[0:9]))('\\bElem ID = \\b',line)[-1]
#    print(f"String: {stringafterword}")

#f.close()