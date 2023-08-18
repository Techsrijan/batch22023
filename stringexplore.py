'''
st="python  the best  programing language"
print(st)
print(st.endswith('g'))
print(st.find('is'))



print(st.upper())
print(st.lower())
print(st.title())
print(st.capitalize())
print(st[0:])
print(st[0::2])


name=input("enter your name")
print(name)
if name.isalpha():
    print(name)
else:
    print("bhai name sahi do")

age = input("enter your age")
print(age)
if age.isdigit():
    print(age)
else:
    print("bhai age sahi do")



name = input("enter your enrollment no")
print(name)
if name.isalnum():
    print(name)
else:
    print("bhai enrollment sahi do")

'''

st1='her name is tamanna and tamanna is good girl'

print(st1.replace('tamanna','sonia',1))

name=input("enter your name")
print(name,end='')
print("thank you")

print(name.rstrip(),end='')   #strip rstrip lstrip
print("thank you")

