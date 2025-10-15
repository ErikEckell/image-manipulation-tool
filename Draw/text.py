from Draw.draw import Draw
from PIL import Image, ImageDraw

class Text(Draw):
    def __init__(self, filename,xy,text,r,g,b,size):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.draw = ImageDraw.Draw(self.image)
        self.xy = xy
        self.text = text

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

        self.size = size

    def action(self):
        self.draw.text(self.xy,self.text,fill=(self.r,self.g,self.b),font_size=self.size)
        self.image.show()
        self.image.save("text.jpg")

        return("text.jpg")