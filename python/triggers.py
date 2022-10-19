import time
import pygame
import mido
from random import randrange

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

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

keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd']

try:
     while True:

         val = getch()
         print(f'input: {val}')
         for i in range(len(keys)):
             if keys[i] == val:
                 sendMidiNote(101 + i)
                 print(f'midi note: {100 + i}')
                 sounds[i].play()
                 print(f'sound: {i}')
             if val == "2":
                 sendMidiNote(120)
                 print('cryo!!!')
                 lastCryo = time.time()
             pass
         if val == "c":
            exit()

except Exception as e:
    print(e)

