import PIL.Image, PIL.ImageDraw
import cmath, math, numpy, random

z = 0
maxsteps = 80
c = 0
originx, originy = (0, 0)
scale = 1
scale = scale * (600*0.25)
samplepath = "white600x600.png"

userinput1 = input("Would you like to generate this fractal in 4k? (Takes longer) [y/n]: ")
userinput2 = input("Would you like to generate the burning ship fractal? [y/n]: ")

if userinput1 == "y":
    samplepath = "white4096x4096"

with PIL.Image.open(samplepath) as image1:
    draw = PIL.ImageDraw.Draw(image1)
    x, y = image1.size
    for count1 in range(x):
        for count2 in range(y):
            i = 0
            z = 0
            c1 = ((count1 - (x/2))/scale) + originx
            c2 = ((count2 - (y/2))/scale) - originy
            c = c1 + c2*1j
            if userinput2 == "y":
                while i <= maxsteps and abs(z) <= 2:
                    z = (abs(z.real) + 1j*abs(z.imag))**2 + c
                    i += 1
            else:
                while i <= maxsteps and abs(z) <= 2:
                    z = z**2 + c
                    i += 1
            if abs(z) <= 2:
                draw.point([count1, count2], (0, 0, 0))
            else:
                #if i >= 70:
                #    color = [255, 0, 0]
                #if i >= 60 and i < 70:
                #    color = [255, 128, 0]
                #if i >= 50 and i < 60:
                #    color = [255, 255, 0]
                #if i >= 40 and i < 50:
                #    color = [128, 255, 0]
                #if i >= 30 and i < 40:
                #    color = [0, 255, 0]
                #if i >= 20 and i < 30:
                #    color = [0, 255, 128]
                #if i >= 10 and i < 20:
                #    color = [0, 255, 255]
                #if i > 0 and i < 10:
                #    color = [255, 255, 255]
                #if i == 0:
                #    color = [255, 255, 255]
                #random.seed(i)
                #color[0] = random.randint(0, 255)
                #random.seed(i*i)
                #color[1] = random.randint(0, 255)
                #random.seed(i*i*i)
                #color[2] = random.randint(0, 255)
                #color[0] = int((color[0] * i) / 30)
                #color[1] = int((color[1] * i) / 30)
                #color[2] = int((color[2] * i) / 30)

                #colortup = (color[0], color[1], color[2])
                colorconst = (i*255)/80
                #colorconst2 = ((i-40)*255)/80
                #colorconst3 = ((i-20)*255)/80
                colorconst = int(colorconst)
                #colorconst2 = int(colorconst2)
                #colorconst3 = int(colorconst3)
                draw.point([count1, count2], (colorconst, colorconst, colorconst))
    try:
        image1.save("Newfrac.png", "PNG")
        print("Saved to Newfrac.png")
    except OSError:
        image1.save("NewfracFailsafe.png", "PNG")
        print("Saved to NewfracFailsafe.png")