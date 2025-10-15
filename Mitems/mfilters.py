from Mitems.mitems import MenuItem
import Mmifilters
from Mmifilters.MenuMifilters import MenuItemFilters

class MIFilters(MenuItem):
    def __init__(self,filename):
        self.filters = []
        self.filename = filename

    def start(self) -> None:
        working = True
        while working:
            self._show()
            option = int(input())
            while ((option<1) or (option>len(self.filters)+1)):
                self._show()
                option = int(input())

            if option < len(self.filters)+1:
                self._execute(option-1)
                return (self.filename)
            else:
                return (self.filename)

    def _execute(self, option_idx):
        mi = self.filters[option_idx](self.filename)
        mi.ask_params()
        action = mi.create_action()
        self.filename = action.action()
  
    def load_filters(self):
        self.filters = [cls_obj for cls_name, cls_obj in vars(Mmifilters).items() 
                            if isinstance(cls_obj, type) and issubclass(cls_obj, MenuItemFilters) and cls_obj is not MenuItemFilters]

    def _show(self):
        print("Elije el filtro a utilizar:")
        for idx, mi in enumerate(self.filters):
            print(f'[{idx+1}] {mi.get_description()}')
        print(f'[{len(self.filters)+1}] Volver')

    @classmethod
    def get_description(cls):
        return "Filtros"

    @classmethod
    def ask_params(cls):
        pass

    @classmethod
    def create_action(cls):
        pass