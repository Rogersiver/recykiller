import time
import pygame
import mido
from random import randrange


lastCryo = time.time()
interval = 60


names = mido.get_output_names()
# for name in names:
    # print(name)

out_port = mido.open_output(names[0])

pygame.mixer.init()
sounds = [
          pygame.mixer.Sound('../RW_Sounds/001.wav'), # 1
          pygame.mixer.Sound('../RW_Sounds/002.wav'), # 2
          pygame.mixer.Sound('../RW_Sounds/003.wav'), # 3
          pygame.mixer.Sound('../RW_Sounds/004.wav'), # 4
          pygame.mixer.Sound('../RW_Sounds/005.wav'), # 5
          pygame.mixer.Sound('../RW_Sounds/006.wav'), # 6
          pygame.mixer.Sound('../RW_Sounds/007.wav'), # 7
          pygame.mixer.Sound('../RW_Sounds/008.wav'), # 8
          pygame.mixer.Sound('../RW_Sounds/009.wav'), # 9
          pygame.mixer.Sound('../RW_Sounds/010.wav'), # 10
          pygame.mixer.Sound('../RW_Sounds/011.wav'), # 11
          pygame.mixer.Sound('../RW_Sounds/012.wav'), # 12
          pygame.mixer.Sound('../RW_Sounds/002.wav'), # 13
          pygame.mixer.Sound('../RW_Sounds/test.wav'), # 14
          pygame.mixer.Sound('../RW_Sounds/test.wav'), # 15
          pygame.mixer.Sound('../RW_Sounds/test.wav'),] # 16

def sendMidiNote(note):
    msg = mido.Message('note_on', note=note, velocity=127, time=1)
    out_port.send(msg)
    msg = mido.Message('note_off', note=note, velocity=127, time=1)
    out_port.send(msg)


try:
     while True:
         val = input("Hit: ")
         if val == "1":
             num = randrange(1,13)
             sendMidiNote(100 + num)
             sounds[num - 1].play()
             print(num)

         if val == "2":
             num = randrange(1,13)
             sendMidiNote(100 + num)
             sounds[num - 1].play()
             print(num)
             sendMidiNote(120)
             print('cryo!!!')
             lastCryo = time.time()
except Exception as e:
    print(e)

