from PIL import Image
from abc import ABC, abstractmethod

class Filters(ABC):
    @abstractmethod
    def action(self):
        pass