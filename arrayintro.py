from array import *


arr=array('i',[1,2,3,4,5])
print(arr)
'''
for i in arr:
    print(i)
'''
i=0
while i<len(arr):
    print(arr[i])
    i=i+1

for j in range(len(arr)):
    print(arr[j])

print(arr.typecode)

print(arr.buffer_info())

arr2=array('i',[1,4,6,8,8])

print(arr+arr2)

