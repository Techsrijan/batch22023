'''
there are siz ways to create an array using numpy
1. array
2. linspace
3. logspace
4. arange
5. zeros
6. ones
'''

# linspace
from numpy import *
arr=linspace(5,50,5)
print(arr)


arr2=logspace(1,50)
print(arr2)

print(arr2[5])

arr3=arange(1,15,2)
print(arr3)

arr5=zeros(100,int)
print(arr5)
print(arr5.dtype)

arr6=ones(20)
print(arr6)