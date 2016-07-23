import pygame
from pygame import Rect

pygame.init()
pygame.font.init()

w = 800
h = 600

slideDisplay = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
crashed = False
arial_title = pygame.font.SysFont("Arial", 48, bold=True)

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

def drawTitleSlide(text):
    drawText(slideDisplay, text, (0,0,0), (w * 0.04, h / 3, w * 0.92, h / 3), arial_title, aa=True, bkg=(255, 255, 255))


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    drawTitleSlide("A Terrible Powerpoint with a long and annoying title that is TOO LONG")
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
