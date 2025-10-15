from Mitems.mitems import MenuItem
import Mmicompositions

class MICompositions(MenuItem):
    def __init__(self,filename):
        self.compositions = []
        self.filename = filename

    def start(self) -> None:
        working = True
        while working:
            self._show()
            option = int(input())
            while ((option<1) or (option>len(self.compositions)+1)):
                self._show()
                option = int(input())

            if option < len(self.compositions)+1:
                self._execute(option-1)
                return (self.filename)
            else:
                return(self.filename)

    def _execute(self, option_idx):
        mi = self.compositions[option_idx](self.filename)
        mi.ask_params()
        action = mi.create_action()
        self.filename = action.action()
    
    def load_compositions(self):
        self.compositions = [cls_obj for cls_name, cls_obj in vars(Mmicompositions).items() 
                                if isinstance(cls_obj, type) and issubclass(cls_obj, Mmicompositions.MenuItemComp) and cls_obj is not Mmicompositions.MenuItemComp]

    def _show(self):
        print("Elije la composición a utilizar:")
        for idx, mi in enumerate(self.compositions):
            print(f'[{idx+1}] {mi.get_description()}')
        print(f'[{len(self.compositions)+1}] Volver')

    @classmethod
    def get_description(cls):
        return "Composiciones"

    @classmethod
    def ask_params(cls):
        pass

    @classmethod
    def create_action(cls):
        pass