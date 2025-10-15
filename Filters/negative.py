from Filters.filters import Filters
from PIL import Image

class Negative(Filters):
    def __init__(self,filename):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.pxs = self.image.load()

    def action(self):
        i = 0
        while i<self.width:
            j = 0
            while j<self.height:
                self.pxs[i,j] = (255-self.pxs[i,j][0], 255-self.pxs[i,j][1], 255-self.pxs[i,j][2])
                j += 1
            i += 1
        self.image.show()

        self.image.save("negative.jpg")

        return("negative.jpg")