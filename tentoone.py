# i=10
# while i>=1:
#     print(i)
#     i=i-1
#
# k=1
# while k<=10:
#     print(k)
#     k=k+1

start=int(input("enter the start no"))
end=int(input("enter the end no"))

if start<end:
    i=start
    while i<=end:
        print(i)
        i=i+1
else:
    i=start
    while i>=end:
        print(i)
        i=i-1