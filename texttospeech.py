from gtts import gTTS
from playsound import playsound

text = gTTS("If you insist on the (slightly) harder way of installing. ka hal ba")
text.save('abc.mp3')
playsound('abc.mp3')
