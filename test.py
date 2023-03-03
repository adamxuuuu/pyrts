import pygame

from entity.tile import Tile, TileType

def tile_test():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tile Demo')

    # Create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    tiles = pygame.sprite.Group()
    tt = TileType.GRASS_32x32
    for y in range(0, 600, tt.value[3]):
        for x in range(0, 800, tt.value[2]):
            tile = Tile(x, y, tt)
            tiles.add(tile)
            background.blit(tile.image, tile.rect)

    clock = pygame.time.Clock()
    # game loop
    running = True
    while running:

        # check for events (keyboard, mouse, etc.)
        for event in pygame.event.get():

            # check if the user closed the window
            if event.type == pygame.QUIT:

                # if so, end the game loop
                running = False

        # update all game logic here

        # draw/render
        # Blit everything to the screen
        screen.blit(background, (0, 0))

        # after drawing everything, flip the display
        pygame.display.flip()

        # run at 60 fps
        clock.tick(60)

    # quit pygame and close the window when done
    pygame.quit()