from Mmicompositions.MenuMicompositions import MenuItemComp
from Compositions.watermark import Watermark

class MIWatermark(MenuItemComp):
    @classmethod
    def get_description(cls) -> str:
        return 'Colocar marca de agua'
    
    def ask_params(self) -> None:
        self.image_name2 = input("Dime el nombre del archivo que quieres fusionar al proyecto:")

    def create_action(self):
        return Watermark(self.filename,self.image_name2)