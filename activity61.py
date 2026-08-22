import pygame
def main():
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Moving color sprite")

    colors = {
        "white": pygame.color ("white"),
        "red": pygame.color ("red"),
        "green": pygame.color ("green"),
        "blue": pygame.color ("blue"),
        "yellow": pygame.color ("yellow")

    }

    current_color=colors["white"]
    x=200
    y=200
    width=50
    height=50

    clock = pygame.timeclock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_LEFT]:
        x-=5
        if Keys[pygame.K_RIGHT]:
        x+=
