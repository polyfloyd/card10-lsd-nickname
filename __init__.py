# Made by polyfloyd at CCCamp2019
# Pick your favorite OSI license

import display
import leds
import utime
from urandom import randrange, choice

gs = 160
led_colors  = [ ((i>>2)*gs, (i>>1&1)*gs, (i&1)*gs) for i in range(1, 8) ]
disp_colors = [ ((i>>2)*0xff, (i>>1&1)*0xff, (i&1)*0xff) for i in range(1, 8) ]

nick = 'sample text'
try:
    with open('/nickname.txt') as f:
        nick = f.read()
except:
    pass

while True:
    with display.open() as d:
        for k in range(4):
            (x1, y1) = (randrange(159), randrange(79))
            (x2, y2) = (min(x1+randrange(40), 159), min(y1+randrange(40), 79))
            try:
                d.rect(x1, y1, x2, y2, col=choice(disp_colors), filled=True)
            except:
                pass
        fg = choice(disp_colors)
        nx = 80-round(len(nick)/2 * 14)
        d.print(nick, fg=fg, bg=[0xff-c for c in fg], posx=(nx-8)+randrange(16), posy=22+randrange(16))
        d.update()
        d.close()
    leds.set(randrange(11), choice(led_colors))
    leds.set_rocket(randrange(3), randrange(32))
    utime.sleep(0.001)
