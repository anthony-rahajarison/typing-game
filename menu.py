import pygame

pygame.init()

# Page
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slice Odyssey")

# Play music
pygame.mixer.init()
pygame.mixer.music.load(r"music.mp3")
pygame.mixer.music.play(-1)  # Répète la musique en boucle

# Police
font = pygame.font.Font("Police.otf", 36)


# Background
background_image = pygame.image.load(r"./images/background.png")
background_image = pygame.transform.scale(background_image, (1100, 800))

# Banner
banner = pygame.image.load(r"./images/logo.webp")
banner = pygame.transform.scale(banner, (250, 250))

# Boutons
button_play = pygame.image.load(r"./images/buttons/button_play.png")
button_play = pygame.transform.scale(button_play, (300, 300))
rect_button_play = button_play.get_rect(topleft=(100, 400))

button_back = pygame.image.load(r"./images/buttons/button_back.png")
button_back = pygame.transform.scale(button_back, (80, 80))
rect_button_back = button_back.get_rect(topleft=(900, 80))

button_settings = pygame.image.load(r"./images/buttons/button_settings.png")
button_settings = pygame.transform.scale(button_settings, (300, 300))
rect_button_settings = button_settings.get_rect(topleft=(350, 400))

button_difficulty = pygame.image.load(r"./images/buttons/button_difficulty.png")
button_difficulty = pygame.transform.scale(button_difficulty, (300, 300))
rect_button_difficulty = button_difficulty.get_rect(topleft=(600, 400))

button_quit = pygame.image.load(r"./images/buttons/button_quit.png")
button_quit = pygame.transform.scale(button_quit, (300, 300))
rect_button_quit = button_quit.get_rect(topleft=(800, 400))

background_blur = pygame.image.load(r"./images/background_blur.png")
background_blur = pygame.transform.scale(background_blur,(1100, 800) )



current_screen = "menu"  


def display_main_menu():
    screen.blit(background_image, (0, 0))
    screen.blit(banner, (450, 50))
    screen.blit(button_play, rect_button_play.topleft)
    

    if rect_button_play.collidepoint(pygame.mouse.get_pos()):
        text_menu = font.render("JOUER", True, (0, 0, 0))
        screen.blit(text_menu, (530, 350))  

    if rect_button_settings.collidepoint(pygame.mouse.get_pos()):
        text_menu = font.render("Options", True, (0, 0, 0))
        screen.blit(text_menu, (530, 350))  

    if rect_button_difficulty.collidepoint(pygame.mouse.get_pos()):
        text_menu = font.render("Difficultés", True, (0, 0, 0))
        screen.blit(text_menu, (530, 350))  

    if rect_button_quit.collidepoint(pygame.mouse.get_pos()):
        text_menu = font.render("Quitter", True, (0, 0, 0))
        screen.blit(text_menu, (530, 350))  
    
    # Afficher les boutons
    screen.blit(button_settings, rect_button_settings)
    screen.blit(button_difficulty, rect_button_difficulty)
    screen.blit(button_quit, rect_button_quit)
    pygame.display.update()


def display_settings_menu():
    screen.fill((163, 216, 244))
    title_settings = font.render("Options du jeu", True, (0, 0, 0))
    screen.blit(title_settings, (450, 50))
    screen.blit(button_back, rect_button_back.topleft)
    pygame.display.update()

def display_difficulty():
    screen.fill((163,216,244))
    title_difficulty = font.render("Difficultés", True, (0, 0, 0))
    screen.blit(title_difficulty, (450, 50))
    screen.blit(button_back, rect_button_back.topleft)
    pygame.display.update()

def display_game():
    screen.blit(background_blur,(0,0))  
    screen.blit(button_back, rect_button_back.topleft)
    pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "menu":
                if rect_button_play.collidepoint(event.pos):
                    current_screen = "game"
                if rect_button_settings.collidepoint(event.pos):
                    current_screen = "settings"
                if rect_button_difficulty.collidepoint(event.pos):
                    current_screen = "difficulty"
                if rect_button_quit.collidepoint(event.pos):
                    running = False
            elif current_screen in ["game","settings", "difficulty"]:
                if rect_button_back.collidepoint(event.pos):
                    current_screen = "menu"

    if current_screen == "menu":
        display_main_menu()
    elif current_screen == "settings":
        display_settings_menu()
    elif current_screen == "difficulty":
        display_difficulty()
    elif current_screen == "game":
        display_game()

pygame.quit()