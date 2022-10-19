import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import mido
from random import randrange
import shutil

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

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
          pygame.mixer.Sound('./RW_Sounds/001.wav'), # 1
          pygame.mixer.Sound('./RW_Sounds/002.wav'), # 2
          pygame.mixer.Sound('./RW_Sounds/003.wav'), # 3
          pygame.mixer.Sound('./RW_Sounds/004.wav'), # 4
          pygame.mixer.Sound('./RW_Sounds/005.wav'), # 5
          pygame.mixer.Sound('./RW_Sounds/006.wav'), # 6
          pygame.mixer.Sound('./RW_Sounds/007.wav'), # 7
          pygame.mixer.Sound('./RW_Sounds/008.wav'), # 8
          pygame.mixer.Sound('./RW_Sounds/009.wav'), # 9
          pygame.mixer.Sound('./RW_Sounds/010.wav'), # 10
          pygame.mixer.Sound('./RW_Sounds/011.wav'), # 11
          pygame.mixer.Sound('./RW_Sounds/012.wav'), # 12
          pygame.mixer.Sound('./RW_Sounds/002.wav'), # 13
          pygame.mixer.Sound('./RW_Sounds/test.wav'), # 14
          pygame.mixer.Sound('./RW_Sounds/test.wav'), # 15
          pygame.mixer.Sound('./RW_Sounds/test.wav'),] # 16

sound_labels = ['thank_you', 'snort_burp', 'snort_gulp', 'rarara_burp', 'thank_you_come_again', 'shove_it_more', 'more_shove_it', 'dolphin.wav', 'mm_tasty', 'mm_yummy', 'gulp_raaaa', 'glugglug_burp', 'snort_burp']

def send_midi_note(note):
    msg = mido.Message('note_on', note=note, velocity=127, time=1)
    out_port.send(msg)
    msg = mido.Message('note_off', note=note, velocity=127, time=1)
    out_port.send(msg)

keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e']
keys_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0 ', 'q ', 'w ', 'e ']
monst_idx = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
val = '1'

first = True

try:
     while True:
         if first == False:
             val = getch()
         if first == True:
            val = '1'
            first = False
         os.system('cls' if os.name == 'nt' else 'clear')
         print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
         print_centre('💀')
         for i in range(len(keys)):
             if keys[i] == val:
                 print_centre(f'⌨️ input: {val}')
                 send_midi_note(101 + i)
                 print_centre(f'🎹 midi note: {100 + i}')
                 sounds[i].play()
                 print_centre(f'🎵 sound: {sound_labels[i]}')
                 print_centre(f'💀 monster: {monst_idx[i]}')
             pass
         print_centre('💀')
         if val == "G":
             send_midi_note(120)
             print_centre('🚀🚀🚀 cryo!!! 🚀🚀🚀')
             lastCryo = time.time()
         if val == "c":
            exit()
         print('\n\n\n\n')
         print_centre('Press c to exit 🛫. press capital G for 🚀cryo🚀')
         print('\n\n\n\n')
         print_centre(' | '.join(keys_labels))
         print_centre(' | '.join(monst_idx))
except Exception as e:
    print(e)

