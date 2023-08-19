f=open("test.gif","rb")
f2=open("best.gif","wb")
for data in f:
    print(data)
    f2.write(data)