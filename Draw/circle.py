from Draw.draw import Draw
from PIL import Image, ImageDraw

class Circle(Draw):
    def __init__(self, filename, xy, r, g, b, size, width):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.draw = ImageDraw.Draw(self.image)
        self.xy = xy
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
        self.width = width

    def action(self):
        self.draw.ellipse((self.xy,(self.xy[0]+self.size,self.xy[1]+self.size)), fill=None, outline=(self.r,self.g,self.b),width=self.width)
        self.image.show()
        self.image.save("circle.jpg")

        return("circle.jpg")