# -*- coding: utf-8 -*-
import random
import pygame

story = ['nothing']
story_try = ['nothing']
colors = ['dvd-logo-blue.png', 'dvd-logo-bluelow.png', 'dvd-logo-brown.png', 'dvd-logo-green.png',
          'dvd-logo-orange.png', 'dvd-logo-purple.png', 'dvd-logo-purplelow.png', 'dvd-logo-purplelowlow.png',
          'dvd-logo-red.png', 'dvd-logo-white.png', 'dvd-logo-yellow.png']

pygame.init()
size = width, height = 1000, 600
background = (0, 0, 0)
pygame.display.set_caption('Телевизор из 2000-х')
logo = pygame.image.load('dvd-logo-white.png')
logo = pygame.transform.scale(logo, (150, 75))
logo_size = [150, 75]
screen = pygame.display.set_mode(size)

x = random.randint(1, width - 300)
y = random.randint(1, height - 150)
x_speed = 2.5
y_speed = 2.5

clock = pygame.time.Clock()

running = True
first_page_running = True
count = 0
border = 10
attempts = 150
count1 = -1

while first_page_running:
    screen.fill(pygame.Color('black'))
    for i in range(5000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 4, 1))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            first_page_running = False
        if event.type == pygame.QUIT:
            first_page_running = False
            running = False

while running:
    screen.fill(background)

    if (0 < x < border and 0 < y < border) and story[-1] != 'up-left':
        count += 1
        print(f'Hooray! Счетчик: {count} из {count1 + 1} попыток.')
        story.append('up-left')
    elif (0 < x < border and height - border - logo_size[1] < y < height) \
            and story[-1] != 'down-left':
        count += 1
        print(f'Hooray! Счетчик: {count} из {count1 + 1} попыток.')
        story.append('down-left')
    elif (width - border - logo_size[0] < x < width and 0 < y < border) \
            and story[-1] != 'up-right':
        count += 1
        print(f'Hooray! Счетчик: {count} из {count1 + 1} попыток.')
        story.append('up-right')
    elif (width - border - logo_size[0] < x < width and height - border - logo_size[1] < y < height) \
            and story[-1] != 'down-right':
        count += 1
        print(f'Hooray! Счетчик: {count} из {count1 + 1} попыток.')
        story.append('down-right')

    if (0 < x < attempts and 0 < y < attempts) and story_try[-1] != 'up-left':
        count1 += 1
        story_try.append('up-left')
    elif (0 < x < attempts and height - attempts - logo_size[1] < y < height) and story_try[-1] != 'down-left':
        count1 += 1
        story_try.append('down-left')
    elif (width - attempts - logo_size[0] < x < width and 0 < y < attempts) and story_try[-1] != 'up-right':
        count1 += 1
        story_try.append('up-right')
    elif (width - attempts - logo_size[0] < x < width and height - attempts - logo_size[1] < y < height)\
            and story_try[-1] != 'down-right':
        count1 += 1
        story_try.append('down-right')

    if (x + logo_size[0] >= width) or (x <= 0):
        x_speed = -x_speed
        logo = pygame.image.load(colors[random.randrange(0, len(colors))])
        logo = pygame.transform.scale(logo, (150, 75))
    if (y + logo_size[1] >= height) or (y <= 0):
        y_speed = -y_speed
        logo = pygame.image.load(colors[random.randrange(0, len(colors))])
        logo = pygame.transform.scale(logo, (150, 75))
    x += x_speed
    y += y_speed
    screen.blit(logo, (x, y))
    pygame.display.flip()
    clock.tick(75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
