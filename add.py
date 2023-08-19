#a,b=5,6 this is single line comment
'''
this program is made for tutorial purpose
in this we can add by user input
this is multiline comment
'''
import pyttsx3
a=int(input("enter first number"))
b=int(input("enter second Number"))
c=a+b
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)
print("sum=",c)
engine.say(c)
engine.runAndWait()