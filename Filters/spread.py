from Filters.filters import Filters
from PIL import Image

class Spread(Filters):
    def __init__(self,filename):
        self.image = Image.open(filename).convert("RGB")
        self.width, self.height = self.image.size
        self.pxs = self.image.load()

    def action(self):
        self.image = self.image.effect_spread(15)
        self.image.show()
        self.image.save("spread.jpg")

        return("spread.jpg")