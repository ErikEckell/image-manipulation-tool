from Mmifilters.MenuMifilters import MenuItemFilters
from Filters.pixelated import Pixelated

class MIpixelated(MenuItemFilters):
    @classmethod
    def get_description(cls) -> str:
        return "Aplicar pixelado"

    def ask_params(self) -> None:
        self.sizep = int(input("Dime el tamaño de los pixeles (2-50):"))
        while self.sizep<2 or self.sizep>50:
            print("Tamaño invalido")
            self.sizep = int(input("Dime el tamaño de los pixeles (2-50):"))

    def create_action(self):
        return Pixelated(self.filename,self.sizep)