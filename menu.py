import pygame
import random
import FruitClass


pygame.init()
clock = pygame.time.Clock()

# Page
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slice Odyssey")

# Play music
pygame.mixer.init()
pygame.mixer.music.load(r"music.mp3")
pygame.mixer.music.play(-1)  # Loops music

# Police
font = pygame.font.Font(None, 36)
font_loose = pygame.font.Font(None,80)
font_fruit_letter = pygame.font.Font(None, 80)


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

button_back_small = pygame.image.load(r"./images/buttons/button_back.png")
button_back_small = pygame.transform.scale(button_back_small, (50, 50))
rect_button_back_small = button_back_small.get_rect(topleft=(5, 5))

image_combo = pygame.image.load(r"./images/combo.png")
image_combo = pygame.transform.scale(image_combo, (200, 200))

button_settings = pygame.image.load(r"./images/buttons/button_settings.png")
button_settings = pygame.transform.scale(button_settings, (300, 300))
rect_button_settings = button_settings.get_rect(topleft=(350, 400))



button_difficulty1 = pygame.image.load(r"./images/buttons/difficulty1.png")
button_difficulty1 = pygame.transform.scale(button_difficulty1, (800, 400))
rect_button_difficulty1 = button_difficulty1.get_rect(topleft=(170, 100))



button_difficulty2 = pygame.image.load(r"./images/buttons/difficulty2.png")
button_difficulty2 = pygame.transform.scale(button_difficulty2, (800, 400))
rect_button_difficulty2 = button_difficulty2.get_rect(topleft=(170, 250))



button_difficulty3 = pygame.image.load(r"./images/buttons/difficulty3.png")
button_difficulty3 = pygame.transform.scale(button_difficulty3, (800, 400))
rect_button_difficulty3 = button_difficulty3.get_rect(topleft=(170, 400))



button_difficulty = pygame.image.load(r"./images/buttons/button_difficulty.png")
button_difficulty = pygame.transform.scale(button_difficulty, (300, 300))
rect_button_difficulty = button_difficulty.get_rect(topleft=(600, 400))

button_quit = pygame.image.load(r"./images/buttons/button_quit.png")
button_quit = pygame.transform.scale(button_quit, (300, 300))
rect_button_quit = button_quit.get_rect(topleft=(800, 400))

background_blur = pygame.image.load(r"./images/background_blur.png")
background_blur = pygame.transform.scale(background_blur,(1100, 800) )

def sound_design_ice():
    pygame.mixer.music.load(r"sound_design/ice.mp3")
    pygame.mixer.music.play(0)

def sound_design_bomb():
    pygame.mixer.music.load(r"sound_design/bomb.mp3")
    pygame.mixer.music.play(0)

def sound_design_sword():
    pygame.mixer.music.load(r"sound_design/sword_sound.mp3")
    pygame.mixer.music.play(0)

# Puts the game on main menu when program is started
current_screen = "menu"  

def combo():
    screen.blit(image_combo,(600,400))

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
    
    # Display buttons
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
    screen.blit(button_difficulty1,rect_button_difficulty1)
    screen.blit(button_difficulty2,rect_button_difficulty2)
    screen.blit(button_difficulty3,rect_button_difficulty3)
    screen.blit(title_difficulty, (500, 50))
    screen.blit(button_back, rect_button_back.topleft)
    pygame.display.update()


# Game Variables
fruit_list = ["banana", "avocado", "strawberry", "pineapple", "lemon","bomb","ice"]
fruit_objects = []
last_spawn_time = 0
spawn_duration = 2000
score = 0


def display_game(last_spawn_time, lives):
    """Game loop"""
    screen.blit(background_blur, (0, 0))
    button_back_small = pygame.transform.scale(button_back, (50, 50))
    rect_button_back_small = button_back_small.get_rect(topleft=(5, 5))
    screen.blit(button_back_small, rect_button_back_small)
    heart = pygame.image.load(r"./images/lives/" + str(lives) + "heart.png")
    heart = pygame.transform.scale(heart,(400,200))
    screen.blit(heart, (800,-50))

    text_score = font.render(f"score : {score}", True, (0, 0, 0))
    screen.blit(text_score, (50, 50))

    now = pygame.time.get_ticks()
    spawn_timer = random.randint(500, 2000)

    # if now < freeze_time:
    #     pygame.display.update()
    #     return last_spawn_time, lives

    # Spawn new fruit if enough time has passed
    if now - last_spawn_time >= spawn_timer:
        last_spawn_time = now
        fruit_name = random.choice(fruit_list)
        new_fruit = FruitClass.FruitClass(fruit_name)
        new_fruit.spawn_time = now 
        fruit_objects.append(new_fruit)

    new_fruit_objects = []
    for fruit in fruit_objects:
        if now - fruit.spawn_time < spawn_duration:
            new_fruit_objects.append(fruit)
        elif fruit.name != "bomb" and fruit.name != "ice":
            lives = lives - 1 
                
    fruit_objects[:] = new_fruit_objects  



    for fruit in fruit_objects:
        try:
            surface_fruit = pygame.image.load(fruit.img)
            surface_fruit = pygame.transform.scale(surface_fruit, (200, 200))
            screen.blit(surface_fruit, (fruit.x, fruit.y))
            key_text = font_fruit_letter.render(fruit.letter , True, (255,255,255))
            screen.blit(key_text, (fruit.x + 75, fruit.y + 10))
            fruit.move()
        except:
            pass

    
    pygame.display.update()
    return last_spawn_time, lives



def message_loose():
    text_loose = font_loose.render("Perdu", True, (0, 0, 0))  
    screen.blit(text_loose, (460, 300))  

freeze_time = 0  # Stores time when freeze starts
freeze_duration = 3000

running = True
while running:
    clock.tick(60)  # Frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "menu":
                if rect_button_play.collidepoint(event.pos):
                    lives = 3
                    current_screen = "game"
                if rect_button_settings.collidepoint(event.pos):
                    current_screen = "settings"
                if rect_button_difficulty.collidepoint(event.pos):
                    current_screen = "difficulty"
                if rect_button_quit.collidepoint(event.pos):
                    running = False
            elif current_screen in ["game", "settings", "difficulty"]:
                if rect_button_back.collidepoint(event.pos) or rect_button_back_small.collidepoint(event.pos):
                    current_screen = "menu"

        # Check for key press events to slice fruits
        if current_screen == "game" and event.type == pygame.KEYDOWN:
            for fruit in fruit_objects:
                if event.key == fruit.key :
                    sound_design_sword()
                    if fruit.name == "bomb":
                        sound_design_bomb()
                        fruit_objects.clear()  
                        message_loose()  
                        pygame.display.update()
                        pygame.time.delay(2000)  
                        current_screen = "menu"
                        break
                    elif fruit.name == "ice" :
                        sound_design_ice()
                        freeze_time = pygame.time.get_ticks() + freeze_duration

                    else:
                        score = score + 1
                        fruit_objects.remove(fruit)
                

    if current_screen == "menu":
        display_main_menu()
    elif current_screen == "settings":
        display_settings_menu()
    elif current_screen == "difficulty":
        display_difficulty()
    elif current_screen == "game":
        last_spawn_time, lives = display_game(last_spawn_time, lives)
        if lives == 0 : # Game Over
            display_game(last_spawn_time, lives)
            fruit_objects.clear() # Clears screen
            message_loose()
            pygame.display.update()
            pygame.time.delay(2000)
            current_screen = "menu"

pygame.quit()