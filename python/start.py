import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import mido
import shelve
from random import randrange
import shutil

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

def increment_can_count():
    s = shelve.open('counter.db', writeback=True)
    try:
        s['key1']['count'] += 1
        val = s['key1']['count']
    except: 
        s['key1'] = {'count': 0}         
    finally:
        s.close()
        return val



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
         print('💀')
         keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e']
         keys_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0 ', 'q ', 'w ', 'e ']
         monst_idx = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
         for i in range(len(keys)):
             try:
                 keys.index(val)
             except:
                 print(f'{val} is not a valid key')
                 break
             if keys[i] == val:
                 sounds[i].play()
                 send_midi_note(101 + i)

                 keys_labels[i] = '\033[92m' + keys_labels[i] + '\033[0m'
                 monst_idx[i] = '\033[92m' + monst_idx[i] + '\033[0m'

                 print(f'⌨️ input: {val}')
                 print(f'🎹 midi note: {100 + i}')
                 print(f'🎵 sound: {sound_labels[i]}')
                 print(f'💀 monster: {monst_idx[i]}')
                 print('📐 can count: ' + str(increment_can_count()))
             pass
         
         print('💀')

         if val == "G":
             send_midi_note(120)
             print('🚀🚀🚀 cryo!!! 🚀🚀🚀')
         if val == "c":
            exit()
# footer
         print('\n\n\n\n')
         print('Press c to exit 🛫. press capital G for 🚀cryo🚀')
         print('\n\n\n\n')
         print(' | '.join(keys_labels))
         print(' | '.join(monst_idx))

except Exception as e:
    print(e)

