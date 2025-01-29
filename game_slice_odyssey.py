import pygame
import subprocess

pygame.init()

# Page
Screen_width = 1100
Screen_height = 800
ecran = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Slice Odyssey")

# Police
font = pygame.font.Font(None, 36)
TextPolice = pygame.font.Font("Police.otf", 50)

#image_background
background_blur = pygame.image.load(r"Background_blur.png")
background_blur = pygame.transform.scale(background_blur, (1100, 800))

def display_main_menu():
    ecran.blit(background_blur, (0, 0))
    pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_main_menu()

pygame.quit()
