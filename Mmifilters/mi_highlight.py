from Mmifilters.MenuMifilters import MenuItemFilters
from Filters.highlight import Highlight

class MIhighlight(MenuItemFilters):
    @classmethod
    def get_description(cls) -> str:
        return "Aplicar destacar un color"

    def ask_params(self) -> None:
        print("Considere que si coloca un valor mayor o menor a los indicados se considerara como maximo y minimo respectivamente")
        self.red = int(input("Considerando un color RGB (0-255), digame el R del color a destacar: "))
        self.green = int(input("Considerando un color RGB (0-255), digame el G del color a destacar: "))
        self.blue = int(input("Considerando un color RGB (0-255), digame el B del color a destacar: "))
        self.tolerance = int(input("Escoja la tolerancia para el color (0-255): "))

    def create_action(self):
        return Highlight(self.filename,self.red,self.green,self.blue,self.tolerance)