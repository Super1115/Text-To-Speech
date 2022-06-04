import gtts
from playsound import playsound
import os
file_name = input("Your file name:")
text = input("Text:")
language = input("language(check out language.txt:)")
read = gtts.gTTS(text,lang=language)
read.save(file_name+".mp3")
playsound(file_name+".mp3")
os.system("pause")