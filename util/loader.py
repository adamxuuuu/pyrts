import os
from pygame.image import load

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join("sprites", name)
    try:
        image = load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()