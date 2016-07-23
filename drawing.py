import pygame
from pygame import Rect
import random
import processing
import time
from image_search import get_image

pygame.init()
pygame.font.init()

w = 800
h = 600

pygame.init()
pygame.font.init()

slideDisplay = pygame.display.set_mode((w, h))
arial_title = pygame.font.SysFont("Arial", 48, bold=True)
arial_text = pygame.font.SysFont("Arial", 36)
times_title = pygame.font.SysFont("Times New Roman", 54, bold=True)
times_text = pygame.font.SysFont("Times New Roman", 36)

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

# =========================
#  Corporate Design Slides
# =========================

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

def draw_corporate_image_search(search_term):
    draw_corporate_slide_template(1)
    drawText(slideDisplay, search_term, (0,0,0), (200 + w*0.04, h*0.04, w*0.92 - 200, h*0.16), arial_title, aa=True, bkg=(255, 255, 255), center=False)
    image = get_image(search_term)
    if image:
        iw, ih = image.get_size()
        slideDisplay.blit(image, ((w - iw + 200) / 2, (h - ih + 100) / 2))

# ===================
#  90s Desgin Slides
# ===================

nineties_bg = pygame.image.load('assets/90sBG.gif')
nineties_divider = pygame.image.load('assets/90sDivider.gif')
def draw_90s_slide_template():
    slideDisplay.blit(nineties_bg, (0,0))

def draw_90s_title_slide(text):
    draw_90s_slide_template()
    drawText(slideDisplay, text, (255,255,255), (w * 0.04, h / 3, w * 0.92, h / 3), times_title, aa=True, bkg=(0,0,0))
    slideDisplay.blit(nineties_divider, (20, (h/20) * 19))

def draw_90s_bullet_points(title, bullet_points):
    draw_90s_slide_template()
    drawText(slideDisplay, title, (255, 255, 255), (w*0.04, h*0.04, w*0.92, h*0.16), times_title, aa=True, bkg=(0,0,0), center=True)
    slideDisplay.blit(nineties_divider, (20, h*0.18))
    for i, point in enumerate(bullet_points):
        pygame.draw.circle(slideDisplay, (255, 255, 255), (int(w*0.04 + 16),  int(h*0.2*(i + 1) + h * 0.04 + 21)), 10)
        drawText(slideDisplay, point, (255, 255, 255), (50 + w*0.04, h*0.2*(i + 1) + h * 0.04, w*0.92 - 50, h*0.16), times_text, aa=True, bkg=(0,0,0), center=False)

def draw_90s_image_search(search_term):
    draw_90s_slide_template()
    drawText(slideDisplay, search_term, (255, 255, 255), (w*0.04, h - 120, w*0.92, 100), times_title, aa=True, bkg=(0,0,0), center=True)
    image = get_image(search_term)
    if image:
        iw, ih = image.get_size()
        slideDisplay.blit(image, ((w - iw) / 2, (h - ih - 100) / 2))

def draw_slide(slide):
    bullet_funcs = [draw_90s_bullet_points, draw_corporate_bullet_points]
    title_funcs = [draw_90s_title_slide, draw_corporate_title_slide]
    picture_funcs = [draw_90s_image_search, draw_corporate_image_search]

    if slide.type == "Bullets":
        bullet_funcs[slide.theme]("Stuff",slide.content)
    elif slide.type == "Heading":
        title_funcs[slide.theme](slide.content)
    elif slide.type == "Picture":
        picture_funcs[slide.theme](slide.content)

def main(to_render):
    clock = pygame.time.Clock()
    crashed = False
    slideDisplay.fill((255, 255, 255))

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            # print(event)

        draw_slide(to_render[0])
        # draw_90s_bullet_points("This is a title", ["FOO", "BAR", "BAZ"])
        pygame.display.update()
        time.sleep(0.1)
        # clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main([processing.Slide("Bullets",1,["FOO","BAR","BAZ"])])
