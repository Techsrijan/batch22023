from numpy import *
arr=array([
    [1,2,3],
    [3,4,5],
    [6,7,8],
    [6,6,6]
])

print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)

# to convert one d array
print(arr.flatten())

b=arr.reshape(3,4)
print(b)


print('3 d array')
# to convert 3 d array
a=arr.reshape(2,2,3)
print(a)
print(a.shape)
print(a.size)
print(a.ndim)