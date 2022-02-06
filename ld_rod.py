
import pygame
import serial
import mido
import time

lastCryo = time.time()
interval = 9

pygame.mixer.init()
test_sound = pygame.mixer.Sound('BTSTU2.wav')
laugh_sound = pygame.mixer.Sound('laugh.wav')
names = mido.get_output_names()
print(names)
out_port = mido.open_output('Midi Through:Midi Through Port-0 14:0')
sounds = [
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('BTSTU2.wav'),
          pygame.mixer.Sound('laugh.wav'),]

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
        print(nl)
        if int(nl[0]) == 0:
            nl = nl[1]
        for i in range(16):
            if int(nl) == i:
                sounds[i - 1].play()
                note = 100 + i
                print("note", note)
                sendMidiNote(100 + i)
                if time.time() - lastCryo > interval:
                    sendMidiNote(100)
