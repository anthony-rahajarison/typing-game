import pygame

class TextBox:
    def __init__(self, x, y, width, height, font_size=32):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = (200, 200, 200)
        self.color_active = (0, 0, 0)
        self.color = self.color_inactive
        self.font = pygame.font.Font(None, font_size)
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text  # Retourne la valeur saisie
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None  # Aucun texte validé

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        txt_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(txt_surface, (self.rect.x + 10, self.rect.y + 10))