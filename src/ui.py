import pygame

TILE_SIZE_X = 10
TILE_SIZE_Y = 10

class Ui:
    def __init__(self, screen_resolution: tuple, map: dict):
        self.map = map

        # Alustetaan pygame
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        self.clock = pygame.time.Clock()
        self.running = True

        # Pelin silmukka
        while self.running:
            # Käydään läpi käyttäjän syötteet
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Piirretään kartta ja päivitetään ruutu
            self.screen.fill("gray")
            self.draw_map()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

    # Piirtää kartan pelin aikana
    def draw_map(self):
        for coordinate in self.map:
            if self.map[coordinate].get_type() == 1:
                this_rect = pygame.Rect((coordinate[0]*TILE_SIZE_X, coordinate[1]*TILE_SIZE_Y), (TILE_SIZE_X, TILE_SIZE_Y))
                pygame.draw.rect(self.screen, "gray30", this_rect)


    