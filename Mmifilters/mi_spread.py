from Mmifilters.MenuMifilters import MenuItemFilters
from Filters.spread import Spread

class MIspread(MenuItemFilters):
    @classmethod
    def get_description(cls) -> str:
        return "Aplicar difuminado"

    @classmethod
    def ask_params(cls) -> None:
        pass

    def create_action(self):
        return Spread(self.filename)