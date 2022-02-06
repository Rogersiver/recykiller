import pygame
import serial
import mido
import time

lastCryo = time.time()
interval = 9

# names = mido.get_output_names()
# print(names)

out_port = mido.open_output('qlcplus:__QLC__ 128:0')

pygame.mixer.init()
sounds = [
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),
          pygame.mixer.Sound('test.wav'),]

def sendMidiNote(note):
    msg = mido.Message('note_on', note=note, velocity=127, time=1)
    out_port.send(msg)
    msg = mido.Message('note_off', note=note, velocity=127, time=1)
    out_port.send(msg)

try:
    sp = serial.Serial(port="/dev/ttyACM0", baudrate=512000, timeout=None)
except:
    print("Failed to connect on /dev/ttyACM0")

while sp:
    while True:
        nl = sp.read(4).decode('utf8').lstrip().rstrip()
        if int(nl[0]) == 0:
            nl = nl[1]
        for i in range(17):
            if int(nl) == i:
                sounds[i - 1].play()
                note = 100 + i
                sendMidiNote(note)
                if time.time() - lastCryo > interval:
                    sendMidiNote(127)
