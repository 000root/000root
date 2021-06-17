import cfg
import sys
import pygame, time

#吓人的结束
def scaend():
    m1 = 'resources\sca.mp3'
    music = pygame.mixer.music.load(m1)
    pygame.mixer.music.play()

    while (1):
        image = 'resources\sca.jpg'
        ball_image = pygame.image.load(image)
        screen = pygame.display.set_mode(cfg.SCREENSIZE)
        screen.blit(ball_image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)

def happyend():
    m1 = 'resources\happy.wav'
    music = pygame.mixer.music.load(m1)
    pygame.mixer.music.play()

    while(1):
        image = 'resources\happy.png'
        ball_image = pygame.image.load(image)
        screen = pygame.display.set_mode(cfg.SCREENSIZE)
        screen.blit(ball_image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
