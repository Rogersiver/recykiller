import time
import pygame
import mido
from random import randrange

lastHit = time.time()
hitInterv = 20

lastCryo = time.time()
cryoInterv = 300

names = mido.get_output_names()
# for name in names:
    # print(name)

out_port = mido.open_output(names[0])

pygame.mixer.init()
sounds = [
          pygame.mixer.Sound('001.wav'), # 1
          pygame.mixer.Sound('002.wav'), # 2
          pygame.mixer.Sound('003.wav'), # 3
          pygame.mixer.Sound('004.wav'), # 4
          pygame.mixer.Sound('005.wav'), # 5
          pygame.mixer.Sound('006.wav'), # 6
          pygame.mixer.Sound('007.wav'), # 7
          pygame.mixer.Sound('008.wav'), # 8
          pygame.mixer.Sound('009.wav'), # 9
          pygame.mixer.Sound('010.wav'), # 10
          pygame.mixer.Sound('011.wav'), # 11
          pygame.mixer.Sound('012.wav'), # 12
          pygame.mixer.Sound('002.wav'), # 13
          pygame.mixer.Sound('test.wav'), # 14
          pygame.mixer.Sound('test.wav'), # 15
          pygame.mixer.Sound('test.wav'),] # 16

def sendMidiNote(note):
    msg = mido.Message('note_on', note=note, velocity=127, time=1)
    out_port.send(msg)
    msg = mido.Message('note_off', note=note, velocity=127, time=1)
    out_port.send(msg)

try:
        while True:
            if time.time() - lastHit > hitInterv:
                num = randrange(13)
                print(num)
                sounds[num - 1].play()
                sendMidiNote(100 + num)
                lastHit = time.time()
            if time.time() - lastCryo > cryoInterv:
                sendMidiNote(120)
                lastCryo = time.time()
except Exception as e:
    print(e)

