import pygame
import serial
import mido
import time
import shelve
lastCryo = time.time()
interval = 59

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

def incrementCanCount():
    s = shelve.open('count.db', writeback=True)
    try:
        s['thursday']['count'] += 1
    finally:
        s.close()
    s = shelve.open('count.db', writeback=True)
    s.close()

try:
    sp = serial.Serial(port="/dev/ttyACM0", baudrate=512000, timeout=None)
    while sp:
        while True:

            teensyOutput = sp.read(4).decode('utf8').lstrip().rstrip()

            if int(teensyOutput[0]) == 0:
                teensyOutput = teensyOutput[1]

            for i in range(17):
                if int(teensyOutput) == i:
                    sounds[i - 1].play()

                    note = 100 + i
                    sendMidiNote(note)
                    incrementCanCount()

                    if time.time() - lastCryo > interval:
                        sendMidiNote(127)
                        lastCryo = time.time()
except:
    print("Failed to connect on /dev/ttyACM0")


