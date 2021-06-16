import sys

try:
    import pygame
except ImportError:
    print('error importing pygame, check installation')

dis = (2560, 1440)
root = pygame.display.set_mode(dis,pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60

MAX_ITER = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def getImage():

    RE_START = -2
    RE_END = 1
    IM_START = -1
    IM_END = 1

    WIDTH = dis[0]
    HEIGHT = dis[1]

    img = pygame.Surface(dis)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):

            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))

            m = mandelbrot(c)

            color = (255 - int(m * 255 / MAX_ITER),255 - int(m * 255 / MAX_ITER),255 - int(m * 255 / MAX_ITER))

            img.set_at((x,y), color)

    return img


def main(argv):

    img = getImage()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        root.fill((0,0,0))

        root.blit(img,(0,0))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        pygame.quit()
        raise e