# @Author: Manuel Rodriguez <valle>
# @Date:   13-Jan-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 09-Apr-2018
# @License: Apache license vesion 2.0

'''
import pyttsx

from os import system
#system('say hello world')
system('say -v Alex hello world')
'''

from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("open good.mp3")
