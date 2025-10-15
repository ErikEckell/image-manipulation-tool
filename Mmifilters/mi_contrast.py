from Mmifilters.MenuMifilters import MenuItemFilters
from Filters.contrast import Contrast

class MIcontrast(MenuItemFilters):
    @classmethod
    def get_description(cls) -> str:
        return "Aplicar contraste"

    @classmethod
    def ask_params(cls) -> None:
        pass
   
    def create_action(self):
        return Contrast(self.filename)