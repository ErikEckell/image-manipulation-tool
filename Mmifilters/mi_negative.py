from Mmifilters.MenuMifilters import MenuItemFilters
from Filters.negative import Negative

class MInegative(MenuItemFilters):
    @classmethod
    def get_description(cls) -> str:
        return "Aplicar negativo"

    @classmethod
    def ask_params(cls) -> None:
        pass

    def create_action(self):
        return Negative(self.filename)