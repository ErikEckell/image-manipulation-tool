from abc import ABC, abstractmethod

class MenuItem(ABC):
    @classmethod
    @abstractmethod
    def get_description(cls):
        ...

    @classmethod
    @abstractmethod
    def ask_params(cls):
        ...

    @classmethod
    @abstractmethod
    def create_action(cls):
        ...