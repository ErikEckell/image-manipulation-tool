from Filters.filters import Filters
from PIL import Image

class Greyscale(Filters):
    def __init__(self,filename):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.pxs = self.image.load()
    
    def action(self):
        i = 0
        while i<self.width:
            j = 0
            while j<self.height:
                average = int((self.pxs[i,j][0]+self.pxs[i,j][1]+self.pxs[i,j][2])/3)
                self.pxs[i,j] = (average, average, average)
                j += 1
            i += 1
        self.image.show()

        self.image.save("greyscale.jpg")

        return("greyscale.jpg")