import pygame


WIDHT = 1300
HEIGHT = 600

SIZE= (WIDHT,HEIGHT)

window = pygame.display.set_mode(SIZE)
background_color = (201,59,253)
window.fill(background_color)
clock = pygame.time.Clock()








game = True
finish = False
while game: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(60)
