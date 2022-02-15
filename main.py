import pygame
import pandas as pd
import math
import random

pygame.init()

width = 1600
height = 1000
screen = pygame.display.set_mode( (width, height) )

running = True

xls = pd.ExcelFile(
    "independent_work/Comparison-experimental/data/data.xlsx"
)
data = pd.read_excel( xls, "one-million-reddit-confessions-" )

def return_circle(center, radius):
    theta = random.uniform( 0, 2 * math.pi )
    x = math.cos( theta )
    y = math.sin( theta )

    scale = random.uniform( 0, radius )
    x *= scale
    y *= scale

    return( center[0] + x, center[1] + y )


def return_lines(message, width, font):
    words = message.split()
    lines = []

    line_text = ""
    for word in words:
        line_width = font.size( " ".join(line_text + word) )[0]

        if line_width > width:
            lines.append(line_text)
            line_text = ""
            line_text = word + " "
        else:
            line_text = line_text + word + " "

    lines.append(line_text)
    return lines

def chunk_text( message, position):
    font = pygame.font.Font( "freesansbold.ttf", 32 )

    lines = return_lines( message, 1000, font )

    lines.reverse()
    height = font.size( "test" )[1]
    total_height = (len(lines) * height) / 2

    for i in range(0, len(lines)):
    
        y = position[1] + ((height + 2) * i) - total_height
        draw_text(lines[i], ( position[0], y ), font)
    
def draw_text(message, position, font):

    text = font.render(message, True, (255, 146,141))
    textRect = text.get_rect()
    textRect.center = ( position[0], height - position[1] )
    screen.blit( text, textRect )

def render_all_messages():
    for message in data["selftext"]:
        if message=="[removed]":
            chunk_text(message, return_circle( (300, 500), 200 )  )
        else:
            chunk_text(message, return_circle( (1000, 500), 300 )  )

back = pygame.image.load( "./independent_work/Comparison-experimental/extra/back.png")
back = pygame.transform.scale( back, ( width, height ) )
screen.blit( back, (0, 0) )

render_all_messages()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    pygame.display.flip()

pygame.quit()