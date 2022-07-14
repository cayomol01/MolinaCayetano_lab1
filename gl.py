#Programa para crear una ventana de Graficos que se represente a través de un mapa de bits
#El programa fue creado con la ayuda del catedrático Carlos Alonso y es casi una copia de lo hecho en clase



import struct

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h', w)

def dword(d):
    return struct.pack('=l', d)

def color(r,g,b):
    return bytes([int(b*255),int(g*255),int(r*255)])

class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clearColor = color(1, 1, 1)
        self.currColor = color(1, 1, 1)
        
        self.glClear()
        self.glViewPort(0, 0, self.width, self.height)
        
    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)] for x in range(self.width)]
        
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)
        
    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)
        
    def glPoint(self, x, y, clr = None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor
            
    def glViewPort(self, posX, posY, width, height):
        self.vpx = posX
        self.vpy = posY
        self.vpwidth = width
        self.vpheight = height
        
    def glClearViewport(self, clr = None):
        for x in range(self.vpx, self.vpx + self.vpwidth):
            for y in range(self.vpy, self.vpy + self.vpheight):
                self.glPoint(x,y,clr)
                
    def glPoint_vp(self, ndcX, ndcY, clr = None):
        if ndcX < -1 or ndcX > 1 or ndcY < -1 or ndcY > 1:
            return

        x = (ndcX + 1) * (self.vpwidth / 2) + self.vpx
        y = (ndcY + 1) * (self.vpheight / 2) + self.vpy

        x = int(x)
        y = int(y)
        
        self.glPoint(x,y,clr)
    
        
        
        
        
    def glFinish(self, filename):
        with open(filename, "wb") as file:
            #header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))
            
            
            #info header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            
            #Color Tables
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
                    
            