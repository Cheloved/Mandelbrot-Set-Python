#Libraries
from PIL import Image
import time 

"""
interesting coordinates
xStart = -0.74877
xEnd =  -0.74872
"""
#Field of view on OX
xStart = -3.16
xEnd = 2.16
xLen = xEnd - xStart

"""
interesting coordinates
yStart = 0.065053
yEnd = 0.065103
"""
#Field of view on OY
yStart = -1.5
yEnd = 1.5
yLen = yEnd - yStart

#multiplier for auto set field
multiplier = 10000

#size of output picture
width = 3840
height = 2160

#check for manual size
if width == 0:
    width = int( abs( xLen ) * multiplier )

if height == 0:    
    height = int( abs( yLen ) * multiplier )

#creating image and loading pixels of it
image = Image.new('RGB', (width, height), (0,0,0))
pixels = image.load()

#more iterations = high quality
iterations = 40
border = 4

#timer for speed test
startTime = time.time()

#goes all over the image
for x in range(width):
    for y in range(height):     
        #making coordinates
        xCurrent = ( ( float(x) * xLen ) / float(width) ) + xStart
        yCurrent = ( ( float(y) * yLen ) / float(height) ) + yStart
        
        #making complex number
        c = complex(xCurrent, yCurrent)
        z = c
        
        #this loop is checking if set infinite or not
        #and changing color of pixels
        for i in range(iterations):
            if abs(z) > border:
                color = int((i*255)/iterations)
                if color >= 40:
                    r = color - 40
                    g = color - 40
                else:
                    r = 0
                    g = 0
                pixels[x,y] = (r,g,color)
                break
            z = z**2 + c            
        else:
            pixels[x,y] = (255,255,255)
            
#information about program perfomance
delay = time.time() - startTime
print('Ready in {0:2f} seconds').format(delay)

#showing and saving the image
image.show()
image.save('MBSet-'+str(time.time())+'.png')
        
        


