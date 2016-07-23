import pygame
from pygame import Rect
import random

pygame.init()
pygame.font.init()

w = 800
h = 600

slideDisplay = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
crashed = False
arial_title = pygame.font.SysFont("Arial", 48, bold=True)
arial_text = pygame.font.SysFont("Arial", 36)

slideDisplay.fill((255, 255, 255))

def drawText(surface, text, color, rect, font, aa=False, bkg=None, center=True):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of lie
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        if center:
            surface.blit(image, ((rect.left + ((rect.width - font.size(text[:i])[0]) / 2)), y))
        else:
            surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

sidebar_images = [
    pygame.image.load('assets/Side1.png'),
    pygame.image.load('assets/Side2.png')
]
def draw_corporate_slide_template(side_index=0):
    slideDisplay.fill((255, 255, 255))
    slideDisplay.fill((50,205,50), rect=(0, (h / 20) * 18, w, h/20))
    slideDisplay.blit(sidebar_images[side_index], (0,0))

def draw_corporate_title_slide(text):
    draw_corporate_slide_template(1)
    drawText(slideDisplay, text, (0,0,0), (w * 0.04 + 200, h / 3, w * 0.92 - 200, h / 3), arial_title, aa=True, bkg=(255, 255, 255))

def draw_corporate_bullet_points(title, bullet_points):
    draw_corporate_slide_template(0)
    drawText(slideDisplay, title, (0,0,0), (200 + w*0.04, h*0.04, w*0.92 - 200, h*0.16), arial_title, aa=True, bkg=(255, 255, 255), center=False)
    for i, point in enumerate(bullet_points):
        pygame.draw.circle(slideDisplay, (0,0,0), (int(200 + w*0.04 + 16),  int(h*0.2*(i + 1) + h * 0.04 + 21)), 10)
        drawText(slideDisplay, point, (0,0,0), (250 + w*0.04, h*0.2*(i + 1) + h * 0.04, w*0.92 - 250, h*0.16), arial_text, aa=True, bkg=(255,255,255), center=False)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    draw_corporate_bullet_points("Some Points", ["Exclamation Points!!!!!!!!!!!!!!!!!!!", "Bullet Points", "Point of no return"])
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
