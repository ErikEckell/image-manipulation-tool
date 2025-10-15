from Mmicompositions.MenuMicompositions import MenuItemComp
from Compositions.join_right import Join_right

class MIJoin_right(MenuItemComp):
    @classmethod
    def get_description(cls) -> str:
        return 'Unir imagen a la derecha del proyecto'
    
    def ask_params(self) -> None:
        self.image_name2 = input("Dime el nombre del archivo que quieres fusionar al proyecto:")

    def create_action(self):
        return Join_right(self.filename,self.image_name2)