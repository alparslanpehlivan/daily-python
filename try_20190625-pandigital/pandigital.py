num=input("Value:")
k=[]
mylist=[]
for i in str(num):
    print(i)
    k.append(i)
mylist = list(dict.fromkeys(k)) #remove duplicates from list
print(mylist)

if "1" in mylist and "2" in mylist and "3" in mylist and "4" in mylist and \
    "5" in mylist and "6" in mylist and "9" in mylist and "8"  in mylist and "7" in mylist:
    print("ok")
else:
    print("dok")