from Mitems.mitems import MenuItem
import Mmidraws
from Mmidraws.MenuMidraws import MenuItemDraw

class MIDraw(MenuItem):
    def __init__(self,filename):
        self.draw = []
        self.filename = filename

    def start(self) -> None:
        working = True
        while working:
            self._show()
            option = int(input())
            while ((option<1) or (option>len(self.draw)+1)):
                self._show()
                option = int(input())

            if option < len(self.draw)+1:
                self._execute(option-1)
                return (self.filename)
            else:
                return (self.filename)

    def _execute(self, option_idx):
        mi = self.draw[option_idx](self.filename)
        mi.ask_params()
        action = mi.create_action()
        self.filename = action.action()
  
    def load_draw(self):
        self.draw = [cls_obj for cls_name, cls_obj in vars(Mmidraws).items() 
                            if isinstance(cls_obj, type) and issubclass(cls_obj, MenuItemDraw) and cls_obj is not MenuItemDraw]

    def _show(self):
        print("Elije el filtro a utilizar:")
        for idx, mi in enumerate(self.draw):
            print(f'[{idx+1}] {mi.get_description()}')
        print(f'[{len(self.draw)+1}] Volver')
    @classmethod
    def get_description(cls):
        return "Dibujo"

    @classmethod
    def ask_params(cls):
        pass

    @classmethod
    def create_action(cls):
        pass