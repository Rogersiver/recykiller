import pygame
import serial
import mido
import time

lastCryo = time.time()
interval = 59

names = mido.get_output_names()
# for name in names:
    # print(name)

out_port = mido.open_output(names[0])

pygame.mixer.init()
sounds = [
          pygame.mixer.Sound('test.wav'), # 1
          pygame.mixer.Sound('test.wav'), # 2
          pygame.mixer.Sound('test.wav'), # 3
          pygame.mixer.Sound('test.wav'), # 4
          pygame.mixer.Sound('test.wav'), # 5
          pygame.mixer.Sound('test.wav'), # 6
          pygame.mixer.Sound('test.wav'), # 7
          pygame.mixer.Sound('test.wav'), # 8
          pygame.mixer.Sound('test.wav'), # 9
          pygame.mixer.Sound('test.wav'), # 10
          pygame.mixer.Sound('test.wav'), # 11
          pygame.mixer.Sound('test.wav'), # 12
          pygame.mixer.Sound('test.wav'), # 13
          pygame.mixer.Sound('test.wav'), # 14
          pygame.mixer.Sound('test.wav'), # 15
          pygame.mixer.Sound('test.wav'),] # 16

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

        teensyOutput = sp.read(4).decode('utf8').lstrip().rstrip()

        if int(teensyOutput[0]) == 0:
            teensyOutput = teensyOutput[1]

        for i in range(17):
            if int(teensyOutput) == i:
                sounds[i - 1].play()

                note = 100 + i
                sendMidiNote(note)

                if time.time() - lastCryo > interval:
                    sendMidiNote(127)
