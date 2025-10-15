from Filters.filters import Filters
from PIL import Image

class Contrast(Filters):
    def __init__(self,filename):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.pxs = self.image.load()

    def action(self):    
        i = 0
        while i<self.width:
            j = 0
            while j<self.height:
                rt = int(self.pxs[i,j][0]*1.6)
                gt = int(self.pxs[i,j][1]*1.6)
                bt = int(self.pxs[i,j][2]*1.6)
                if(rt>255):
                    rt=255
                if(gt>255):
                    gt=255
                if(bt>255):
                    bt=255
                self.pxs[i,j] = (rt, gt, bt)
                j += 1
            i += 1
        self.image.show()

        self.image.save("contrast.jpg")

        return("contrast.jpg")

     