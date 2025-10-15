from Mmifilters.MenuMifilters import MenuItemFilters
from Filters.greyscale import Greyscale

class MIgreyscale(MenuItemFilters):
    @classmethod
    def get_description(cls) -> str:
        return "Aplicar escala de grises"

    @classmethod
    def ask_params(cls) -> None:
        pass

    def create_action(self):
        return Greyscale(self.filename)