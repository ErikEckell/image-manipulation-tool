from abc import ABC, abstractmethod

class Draw(ABC):
    @abstractmethod
    def action(self):
        pass