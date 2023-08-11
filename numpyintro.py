from numpy import *

arr=array([1,2,3,4,5])
print(arr)

i=0
while i<len(arr):
    print(arr[i])
    i=i+1

for j in range(len(arr)):
    print(arr[j])

print(arr.dtype)
print(arr.shape)
print(arr.size)
