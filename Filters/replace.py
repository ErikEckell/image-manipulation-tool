from Filters.filters import Filters
from PIL import Image

class Replace(Filters):
    def __init__(self,filename,r,g,b,tolerance,r2,g2,b2):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.pxs = self.image.load()

        self.tolerance = tolerance
        if self.tolerance<0:
            self.tolerance = 0
        if self.tolerance>255:
            self.tolerance=255

        self.r2 = r2
        self.g2 = g2
        self.b2 = b2
        self.rt = r-self.tolerance 
        self.gt = g-self.tolerance
        self.bt = b-self.tolerance 
        self.rt2 = r+self.tolerance
        self.gt2 = g+self.tolerance 
        self.bt2 = b+self.tolerance
        if(self.rt<0):
            self.rt=0
        if(self.gt<0):
            self.gt=0
        if(self.bt<0):
            self.bt=0
        if(self.rt2>255):
            self.rt2=255
        if(self.gt2>255):
            self.gt2=255
        if(self.bt2>255):
            self.bt2=255

    def action(self):

        i = 0
        while i<self.width:
            j = 0
            while j<self.height:
                if((self.pxs[i,j]>=(self.rt,self.gt,self.bt)) and (self.pxs[i,j]<=(self.rt2,self.gt2,self.bt2))):
                    self.pxs[i,j] = (self.r2, self.g2, self.b2)     
                j += 1
            i += 1
        self.image.show()

        self.image.save("replace.jpg")

        return("replace.jpg")