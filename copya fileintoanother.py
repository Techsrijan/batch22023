f=open("hello.txt","r")
f2=open("cello.txt","w")
for data in f:
    print(data)
    f2.write(data)