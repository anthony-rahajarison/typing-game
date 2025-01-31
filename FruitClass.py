import random
import pygame
import string


class FruitClass :

    def __init__ (self, name) :
        key_list = {
        "A": pygame.K_a,
        "B": pygame.K_b,
        "C": pygame.K_c,
        "D": pygame.K_d,
        "E": pygame.K_e,
        "F": pygame.K_f,
        "G": pygame.K_g,
        "H": pygame.K_h,
        "I": pygame.K_i,
        "J": pygame.K_j,
        "K": pygame.K_k,
        "L": pygame.K_l,
        "M": pygame.K_m,
        "N": pygame.K_n,
        "O": pygame.K_o,
        "P": pygame.K_p,
        "Q": pygame.K_q,
        "R": pygame.K_r,
        "S": pygame.K_s,
        "T": pygame.K_t,
        "U": pygame.K_u,
        "V": pygame.K_v,
        "W": pygame.K_w,
        "X": pygame.K_x,
        "Y": pygame.K_y,
        "Z": pygame.K_z,
        }

        self.name = name
        self.img = "images/fruits/" + name + ".png"
        self.position = (random.randint(200,900), random.randint(200, 600))

        self.letter, self.key = random.choice(list(key_list.items()))