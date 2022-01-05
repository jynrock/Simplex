from PIL import Image # Depends on the Pillow lib

import opensimplex as simplex

WIDTH = 512
HEIGHT = 512
FEATURE_SIZE = 24.0


def main():
    print('Generating 2D image...')
    im = Image.new('L', (WIDTH, HEIGHT))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            value = simplex.noise2(x / FEATURE_SIZE, y / FEATURE_SIZE)
            color = int((value + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise2d.png')
if __name__ == '__main__':
    main()