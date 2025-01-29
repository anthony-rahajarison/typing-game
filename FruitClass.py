import random
import pygame

class FruitClass :
    def __init__ (self, name) :
        self.name = name
        self.img = "images/fruits/" + name + ".png"
        self.position = (random.randint(100,1000), random.randint(100, 700))

        self.last = pygame.time.get_ticks()
        self.depop_timer = 3000
    
    def sliced(self) :
        return
    
    def depop(self) :
        now = pygame.time.get_ticks()
        if now - self.last >= self.depop_timer:
            self.last = now
            self.sliced()
        