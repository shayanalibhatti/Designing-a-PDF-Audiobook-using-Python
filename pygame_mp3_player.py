import pygame
from pygame import mixer
# import pygame.pygame.movie
import os
path = '/home/shayan/Desktop/pdf_audio.mp3'
pygame.init()
mixer.init()
mixer.music.load(os.path.realpath(path))
mixer.music.play()
pygame.event.wait()