
f=open("hello.txt",'r')
print(f)

#print(f.read())
for data in f:
    print(data)
f.close()

f=open("hello.txt",'a')
print(f)
msg=input("enter the text u want to write in a file")
print(msg)
f.write("\n"+msg)
f.close()

