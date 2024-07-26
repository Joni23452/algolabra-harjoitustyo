import random

class Map:
    def __init__(self, size: tuple):
        self.x = size[0]
        self.y = size[1]
        self.coordinates = {}
        for x in range(self.x):
            for y in range(self.y):
                self.coordinates.update({(x,y): Tile()})

    # Sijoittaa kartalle satunnaisesti annetun määrän kohteita kartan jakoa varten. Syötteen tulee olla pienempi kuin kartan leveys*korkeus.
    def place_sites(self, count: int):
        sites_to_place = count
        while sites_to_place > 0:
            site_x = random.randint(0,self.x-1)
            site_y = random.randint(0,self.y-1)
            if not self.coordinates[(site_x, site_y)].is_site():
                self.coordinates[(site_x, site_y)].place_site()
                sites_to_place -= 1

    # Tulostaa terminaaliin lopullisen kartan
    def print_map(self):
        for y in range(self.y):
            y_string = ""
            for x in range(self.x):
                y_string += str(self.coordinates[(x,y)].get_type())
                y_string += " "
            print(y_string)

    def get_map(self):
        return self.coordinates
    
    # Tulostaa terminaaliin kohteet kartalla
    def print_sites(self):
        for y in range(self.y):
            y_string = ""
            for x in range(self.x):
                if self.coordinates[(x,y)].is_site():
                    y_string += "1 "
                else:
                    y_string += "0 "
            print(y_string)


class Tile:
    def __init__(self):
        self.type = 0       # Kartan kohdan tyyppi: 0 = tyhjää, 1 = kiveä
        self.site = False   # Sijaitseeko kohdalla karttaa kohdetta

    def get_type(self):
        return self.type

    def is_site(self):
        return self.site

    def place_site(self):
        self.site = True