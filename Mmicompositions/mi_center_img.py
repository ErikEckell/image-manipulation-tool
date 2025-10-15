from Mmicompositions.MenuMicompositions import MenuItemComp
from Compositions.center_img import Center

class MICenter(MenuItemComp):
    @classmethod
    def get_description(cls) -> str:
        return 'Centrar una imagen sobre el proyecto actual (se recomienda que la imagen sea mas chica que el proyecto)'
    
    def ask_params(self) -> None:
        self.image_name2 = input("Dime el nombre del archivo a centrar: ")

    def create_action(self):
        return Center(self.filename,self.image_name2)