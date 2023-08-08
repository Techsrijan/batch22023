from random import *
from gtts import gTTS
from playsound import playsound

n=randint(2,99)
#print(n)

num=int(input("enter any number between 2 to 99"))
if num==n:
    print("Jeet gaye")
    text = gTTS("Jeet gaye")
    text.save('abc.mp3')
    playsound('abc.mp3')

else:
    print("Har gaye")
    text = gTTS("har gaye")
    text.save('abc.mp3')
    playsound('abc.mp3')