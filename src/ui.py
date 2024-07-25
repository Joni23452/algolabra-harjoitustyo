import pygame

RESOLUTION_X = 1920
RESOLUTION_Y = 1080

class Ui:
    def __init__(self):
        # Alustetaan pygame
        pygame.init()
        self.screen = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y))
        self.clock = pygame.time.Clock()
        self.running = True

        # Pelin silmukka
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill("purple")

            pygame.display.flip() # Päivittää ruudun
            self.clock.tick(60)
        
        pygame.quit()

    def add_map(self, map_coordinates: dict):
        pass

ui = Ui()

    