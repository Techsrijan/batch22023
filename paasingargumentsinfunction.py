'''
pass an agument to function
1. positional argument
2. keyword argument
3. default argument
4. variable length argument (*)
5. keyword variable length argumnent
'''

def person(name,age):
    print("name=",name)
    #age=age+10
    print("age=",age)

#1. positional argument
person('rohan',22)

#2. keyword argument
person(age=66,name='mohan')
person(name='rohit',age=25)

#3. default argument
def person2(name,age=18,school='techsrijan'):
    print("name=",name)
    #age=age+10
    print("age=",age)

person2("sohan",22)

def light(from2='suraj'):
    print(from2)
light('china suraj')

#4. variable length argument (*)

def add(a,*b):
    print(a)
    print(b,type(b))
    sum=a
    for i in b:
        sum=sum+i
    print(sum)
add(1,2,4,434,434,5)



def add2(*b):
    print(b,type(b))
    sum=0
    for i in b:
        sum=sum+i
    print(sum)
add2(1,2,4,434,434,5)

#5. keyword variable length argumnent
def persondata(**data):
    print(data)
    for i,j in data.items():
        print(i,"=",j)

persondata(name='ashwani',age=33,city='gkp',pin=273007,phone=9956477677)