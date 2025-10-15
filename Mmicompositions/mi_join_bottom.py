from Mmicompositions.MenuMicompositions import MenuItemComp
from Compositions.join_bottom import Join_bottom

class MIJoin_bottom(MenuItemComp):
    @classmethod
    def get_description(cls) -> str:
        return 'Unir imagen abajo del proyecto'
    
    def ask_params(self) -> None:
        self.image_name2 = input("Dime el nombre del archivo que quieres fusionar al proyecto:")

    def create_action(self):
        return Join_bottom(self.filename,self.image_name2)