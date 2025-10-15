from Compositions.compositions import Compositions
from PIL import Image

class Join_right(Compositions):
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
        blank_img = Image.new("RGB",(self.width1+self.width2,self.maxheight))
        blank_img.paste(self.image1,(0,0))
        blank_img.paste(self.image2,(self.width1,0))
        blank_img.show()

        blank_img.save("right.jpg")

        return("right.jpg")