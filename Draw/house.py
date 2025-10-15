from Draw.draw import Draw
from PIL import Image, ImageDraw

class House(Draw):
    def __init__(self, filename, x, y, r, g, b, size):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.draw = ImageDraw.Draw(self.image)

        self.x = x
        self.y = y
        self.size = size

        self.r = r
        if self.r<0:
            self.r=0
        if self.r>255:
            self.r = 255

        self.g = g
        if self.g<0:
            self.g=0
        if self.g>255:
            self.g = 255

        self.b = b
        if self.b<0:
            self.b=0
        if self.b>255:
            self.b = 255

        self.width = 5

    def action(self):
        
        self.draw.rectangle([(self.x-self.size, self.y-self.size),
                            (self.x+self.size, self.y+self.size)], 
                            fill=None, outline=(self.r,self.g,self.b), 
                            width=self.width)
        
        self.draw.rectangle([(self.x-10, self.y+self.size-40),
                            (self.x+10, self.y+self.size)], 
                            fill=None, outline=(self.r,self.g,self.b), 
                            width=self.width)
        
        self.draw.rectangle([(self.x-35, self.y-35),
                            (self.x-10, self.y-10)], 
                            fill=None, outline=(self.r,self.g,self.b), 
                            width=self.width)
        
        self.draw.line([(self.x-self.size, self.y-self.size),
                        (self.x,self.y-self.size-50)],
                        fill=(self.r,self.g,self.b), 
                        width=self.width)
        
        self.draw.line([(self.x+self.size, self.y-self.size),
                        (self.x,self.y-self.size-50)],
                        fill=(self.r,self.g,self.b), 
                        width=self.width)
        
        
        self.image.show()
        self.image.save("house.jpg")

        return("house.jpg")