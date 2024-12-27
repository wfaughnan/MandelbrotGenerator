import PIL.Image, PIL.ImageDraw
import cmath, math, random

z = 0
maxsteps = 80
c = 0
originx, originy = (0, 0)
scale = 1
scale = scale * (600*0.25)
samplepath = "white600x600.png"

userinput1 = input("Would you like to generate this fractal in 4k? (Takes longer) [y/n]: ")
userinput2 = input("Type a real number (between -2 and 2) for the real part of the c-value of this Julia Set: ")
userinput3 = input("Type a real number (between -2 and 2) for the imaginary part of the c-value of this Julia Set: ")

if userinput1 == "y":
    samplepath = "white4096x4096"

with PIL.Image.open(samplepath) as image1:
    draw = PIL.ImageDraw.Draw(image1)
    x, y = image1.size
    for count1 in range(x):
        for count2 in range(y):
            i = 0
            c = float(userinput2) - float(userinput3)*1j
            c1 = ((count1 - (x/2))/scale) + originx
            c2 = ((count2 - (y/2))/scale) - originy
            z = c1 + c2*1j
            while i <= maxsteps and abs(z) <= 2:
                z = z**2 + c
                i += 1
            if abs(z) <= 2:
                draw.point([count1, count2], (0, 0, 0))
            else:
#                if i >= 70:
#                    color = [255, 0, 0]
#                if i >= 60 and i < 70:
#                    color = [255, 128, 0]
#                if i >= 50 and i < 60:
#                    color = [255, 255, 0]
#                if i >= 40 and i < 50:
#                    color = [128, 255, 0]
#                if i >= 30 and i < 40:
#                    color = [0, 255, 0]
#                if i >= 20 and i < 30:
#                    color = [0, 255, 128]
#                if i >= 10 and i < 20:
#                    color = [0, 255, 255]
#                if i > 0 and i < 10:
#                    color = [255, 255, 255]
#                if i == 0:
#                    color = [255, 255, 255]
#                random.seed(i)
#                color[0] = random.randint(0, 255)
#                random.seed(i*i)
#                color[1] = random.randint(0, 255)
#                random.seed(i*i*i)
#                color[2] = random.randint(0, 255)
                colorconst = (i * 255) / 80
                colorconst = int(colorconst)
                draw.point([count1, count2], (colorconst, colorconst, colorconst))
    try:
        image1.save("Newfrac.png", "PNG")
        print("Saved to Newfrac.png")
    except OSError:
        image1.save("NewfracFailsafe.png", "PNG")
        print("Saved to NewfracFailsafe.png")