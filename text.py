import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((255, 255), 0, 32)
screen.fill((255,255,255))
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      pressed_array = pygame.mouse.get_pressed()
      for index in range(len(pressed_array)):
        if pressed_array[index]:
          if index == 0:
            print('Pressed LEFT Button!')
          elif index == 1:
            print('The mouse wheel Pressed!')
          elif index == 2:
            print('Pressed RIGHT Button!')
  pygame.display.update()

  too = False
  ot = True
  if ot:
    screen.fill(m_setting.bg_color)  # setting bg
    i_word.dis()  # text
  for event in pygame.event.get():  # check
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      pressed_arr = pygame.mouse.get_pressed()
      if len(pressed_arr) == 1:
        too = True
        ot = False
    elif event.type == pygame.MOUSEBUTTONUP:
      too = False
  while too:
    screen.fill(m_setting.bg_color)
    ship.blitme()
  pygame.display.flip()