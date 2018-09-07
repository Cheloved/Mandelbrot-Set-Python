from PIL import Image
import time 

#xStart = -0.74877
#xEnd =  -0.74872
xStart = -3.16
xEnd = 2.16
xLen = xEnd - xStart

#yStart = 0.065053
#yEnd = 0.065103
yStart = -1.5
yEnd = 1.5
yLen = yEnd - yStart

multiplier = 10000

width = 3840
height = 2160

if width == 0:
    width = int( abs( xLen ) * multiplier )

if height == 0:    
    height = int( abs( yLen ) * multiplier )

image = Image.new('RGB', (width, height), (0,0,0))
pixels = image.load()

iterations = 40
border = 4

startTime = time.time()

for x in range(width):
    for y in range(height):        
        xCurrent = ( ( float(x) * xLen ) / float(width) ) + xStart
        yCurrent = ( ( float(y) * yLen ) / float(height) ) + yStart
        
        c = complex(xCurrent, yCurrent)
        z = c
        
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
            
delay = time.time() - startTime
print('Ready in {0:2f} seconds').format(delay)

image.show()
image.save('MBSet-'+str(time.time())+'.png')
        
        


