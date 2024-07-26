import ui
import tiles

# Tuotettavan kartan koko
MAP_WIDTH = 200
MAP_HEIGHT = 200

# Ikkunan resoluutio
SCREEN_RESOLUTION_X = 1920
SCREEN_RESOLUTION_Y = 1080

test_map = tiles.Map((MAP_WIDTH, MAP_HEIGHT))
test_map.place_sites(4)
test_map_coordinates = test_map.get_map()

game_ui = ui.Ui((SCREEN_RESOLUTION_X, SCREEN_RESOLUTION_Y), test_map_coordinates)