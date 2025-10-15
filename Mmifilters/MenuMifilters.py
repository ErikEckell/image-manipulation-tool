from abc import ABC, abstractmethod

class MenuItemFilters(ABC):
    def __init__(self,filename):
        self.filename = filename

    @classmethod
    @abstractmethod
    def get_description(cls) -> str:
        ...

    @classmethod
    @abstractmethod
    def ask_params(cls) -> None:
        ...

    @abstractmethod
    def create_action(self):
        ...