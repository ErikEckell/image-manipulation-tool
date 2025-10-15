from Mmifilters.MenuMifilters import MenuItemFilters
from Filters.replace import Replace

class MIreplace(MenuItemFilters):
    @classmethod
    def get_description(cls) -> str:
        return "Reemplazar un color por otro "

    def ask_params(self) -> None:
        print("Considere que si coloca un valor mayor o menor a los indicados se considerara como maximo y minimo respectivamente")
        self.red = int(input("Considerando un color RGB (0-255), digame el R del color a reemplazar: "))
        self.green = int(input("Considerando un color RGB (0-255), digame el G del color a reemplazar: "))
        self.blue = int(input("Considerando un color RGB (0-255), digame el B del color a reemplazar: "))
        self.tolerance = int(input("Escoja la tolerancia para el color (0-255): "))
        self.red2 = int(input("Considerando un color RGB (0-255), digame el R del color a colocar: "))
        self.green2 = int(input("Considerando un color RGB (0-255), digame el G del color a colocar: "))
        self.blue2 = int(input("Considerando un color RGB (0-255), digame el B del color a colocar: "))

    def create_action(self):
        return Replace(self.filename,self.red,self.green,self.blue,self.tolerance,self.red2,self.green2,self.blue2)