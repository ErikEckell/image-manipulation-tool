from Filters.filters import Filters
from PIL import Image

class Pixelated(Filters):
    def __init__(self,filename,size):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.pxs = self.image.load()
        self.size = size

    def action(self):
        for i in range(0, self.width, self.size):
            for j in range(0, self.height, self.size):
                    counter_red,counter_green,counter_blue = (0,0,0)
                    total_pxs = 0

                    for o in range(i, min(i+self.size, self.width)):
                        for u in range(j, min(j+self.size, self.height)):
                            counter_red += self.pxs[o,u][0]
                            counter_green += self.pxs[o,u][1]
                            counter_blue += self.pxs[o,u][2]
                            total_pxs += 1
                    
                    for o in range(i, min(i+self.size, self.width)):
                        for u in range(j, min(j+self.size, self.height)):
                            self.pxs[o,u] = (int(counter_red/total_pxs), int(counter_green/total_pxs), int(counter_blue/total_pxs))
        self.image.show()

        self.image.save("pixelated.jpg")

        return("pixelated.jpg")