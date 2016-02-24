from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if (x1 < x0):
        draw_line(screen, x1, y1, x0, y0, color);

    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    
    
    if (y1 > y0):
        d = (2*A) + B
        if (A < B):
            while (x < x1):
                plot(screen,color,x,y)
                if (d > 0):
                    y += 1
                    d = d + (2*B)
                x += 1
                d = d + (2*A)
        else:
            while (y < y1):
                plot(screen,color,x,y)
                if (d < 0):
                    x += 1
                    d = d + (2*A)
                y += 1
                d = d + (2*B)
    else:
        d = (2*A) - B
        if (A > B):
            while (x < x1):
                plot(screen,color,x,y)
                if (d < 0):
                    y -= 1
                    d = d - (2*B)
                x += 1
                d = d + (2*A)
        else:
            while (y > y1):
                plot(screen,color,x,y)
                if (d > 0):
                    x += 1
                    d = d + (2*A)
                y -= 1
                d = d - (2*B)
            
