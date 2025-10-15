from Compositions.compositions import Compositions
from PIL import Image

class Fusion(Compositions):
    def __init__(self,filename1, filename2):

        self.image1 = Image.open(filename1).convert("RGB")
        self.image2 = Image.open(filename2).convert("RGB")

        self.width1, self.height1 = self.image1.size
        self.width2, self.height2 = self.image2.size

        self.pxs1 = self.image1.load()
        self.pxs2 = self.image2.load()

        self.maxwidth = max(self.width1,self.width2)
        self.maxheight = max(self.height1, self.height2)
        self.minwidth = min(self.width1,self.width2)
        self.minheight = min(self.height1, self.height2)
    
    def action(self):
        i = 0
        while i<self.minwidth:
            j = 0
            while j<self.minheight:
                r = int((self.pxs1[i,j][0]+self.pxs2[i,j][0])/2)
                g = int((self.pxs1[i,j][1]+self.pxs2[i,j][1])/2)
                b = int((self.pxs1[i,j][2]+self.pxs2[i,j][2])/2)
                self.pxs1[i,j] = (r,g,b)
                j += 1
            i += 1
        self.image1.show()

        self.image1.save("image_fusion.jpg")

        return("image_fusion.jpg")
