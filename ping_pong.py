from pygame import *

win_width = 700
win_lenght = 500
window = display.set_mode((win_width, win_lenght))
display.set_caption("Пинг Понг")
background = transform.scale(image.load("background.jpg"), (win_width, win_lenght))

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0,0))
    
    display.update()
    time.delay(50)