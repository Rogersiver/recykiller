
import pygame
import serial


pygame.mixer.init()
test_sound = pygame.mixer.Sound('BTSTU2.wav')

try:
    arduino = serial.Serial('COM4', 9600)
except:
    print("Failed to connect on COM4")

while arduino:
    while True:
        print(arduino.read(10))
        # await websocket.send("0|PLAY")
        test_sound.play()
