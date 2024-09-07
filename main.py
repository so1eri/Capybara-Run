from os import environ
environ ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import sys
import pygame
from pygame.locals import QUIT

pygame.init()
FPS = 30
WIDTH = 500
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Capys and Computers')
clock = pygame.time.Clock()

class Player():
  def __init__(self):
    self.rect = pygame.rect.Rect(100,350,30,30)
  def draw(self):
    pygame.draw.rect(screen, (0,0,0), self.rect)

class PC():
  def __init__(self):
    self.rect = pygame.rect.Rect(470,350,30,30)
  def draw (self):
    pygame.draw.rect(screen, (0,0,0), self.rect)
    
player = Player()
pc = PC()

def main():
  while True:
    handle_events()
    update()
    draw()

def update():
  clock.tick(FPS)

def handle_events():
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()

def draw():
  screen.fill((255, 255, 255))
  pygame.draw.line(screen, (0,0,0),(0,382), (500, 382), width = 6)
  player.draw()
  pc.draw()
  pygame.display.update()

main()