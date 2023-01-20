import pygame
from Show_img import main as newimage
import time

pygame.init()
WIDTH, HEIGHT = 900, 460
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
number_font = pygame.font.SysFont('Arial', 350)
text_font = pygame.font.SysFont('Arial', 30)


def main():
    percent = 0
    # constants/start
    WIN.fill((255,255,255))
    clock = pygame.time.Clock()
    FPS = 60
    count = 0
    Red = (255, 127, 127)
    Green = (144, 238, 144)
    # first image
    guess, actual = newimage(int(time.time()) % 10000)
    if guess == actual:
        percent = 1
    total = 1
    # redraw window every 2 seconds
    def redraw():
        # red or green background
        if guess == actual:
            WIN.fill(Green)
        else:
            WIN.fill(Red)
        # loading the images
        image_dis = pygame.image.load("number.png")
        number_text = number_font.render(str(int(guess)) + " " + str(int(actual)), False, (0, 0, 0))
        number_rect = number_text.get_rect(center=((660, 230)))
        guess_actuall = text_font.render("Guess                      Actual", False, (0, 0, 0))
        guess_actuall_rect = guess_actuall.get_rect(center=((660, 60)))
        percent_text = text_font.render(f'{percent*100/total:.2f}% correct', False, (0, 0, 0))
        percent_text_rect = percent_text.get_rect(center=((660, 20)))
        #blitting them
        WIN.blit(image_dis, (20, 20))
        WIN.blit(number_text, number_rect)
        WIN.blit(guess_actuall, guess_actuall_rect)
        WIN.blit(percent_text, percent_text_rect)
        pygame.display.update()
    
    # main loop
    redraw()
    run = True
    while run:

        clock.tick(FPS)

        if count == 120:
            guess, actual = newimage(int(time.time()) % 10000)
            count = 0
            if guess == actual:
                percent += 1
            total += 1
            redraw()
        else:
            count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    pygame.quit()

if __name__ == '__main__':
    main()