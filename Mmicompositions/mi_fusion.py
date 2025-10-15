from Mmicompositions.MenuMicompositions import MenuItemComp
from Compositions.fusion import Fusion
from PIL import Image

class MIfusion(MenuItemComp):
    @classmethod
    def get_description(cls) -> str:
        return "Fusionar imagenes"

    def ask_params(self) -> None:
        self.image_name2 = input("Dime el nombre del archivo que quieres fusionar al proyecto:")

    def create_action(self):
        return Fusion(self.filename,self.image_name2)