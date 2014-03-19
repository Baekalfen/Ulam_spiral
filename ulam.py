from PIL import Image,ImageDraw
from math import sin,cos,radians,sqrt

width=700
height=700
im = Image.new('RGB', (width,height), color="white")
im_draw=ImageDraw.Draw(im)

def prime(a):
    if (a==2):
        return True

    if (a%2==0 or a==1):
        return False

    n=3
    while (n<=sqrt(a)):
        if (a%n==0):
            return False
        n+=2
    return True

direction=0
x=width/2
y=height/2
i=1
p=1
# im_draw.point((x,y),"red")
while (abs(x-width/2)<width/2 and abs(y-height/2)<height/2):
    for n in range(2): # try 1 or 2
        for m in range(i):
            if (prime(p)):
                im_draw.point((x,y),(255,0,0))
            else:
                im_draw.point((x,y),(230,230,230))
            if (p==1):
                im_draw.point((x,y),(0,0,0))
            p+=1
            x+=int(cos(radians(direction)))
            y+=int(sin(radians(direction)))
        direction-=90
    i+=1

# im_draw.point((x,y),"black")
im.save("ulam.png")
