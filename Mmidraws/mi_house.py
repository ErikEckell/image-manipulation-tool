from Mmidraws.MenuMidraws import MenuItemDraw
from Draw.house import House

class MIHouse(MenuItemDraw):

    @classmethod
    def get_description(cls) -> str:
        return 'Casa'
    
    def ask_params(self) -> None:
        self.x = int(input("Dime la posición inicial del dibujo en el eje x: "))
        while self.x<0:
            print("El valor no puede ser menor a 0")
            self.x = int(input("Dime la posición inicial del dibujo en el eje x: "))

        self.y = int(input("Dime la posición inicial del dibujo en el eje y: "))
        while self.y<0:
            print("El valor no puede ser menor a 0")
            self.y = int(input("Dime la posición inicial del dibujo en el eje y: "))
            
        self.r = int(input("Considerando un color RGB, dime el R para el color: "))
        self.g = int(input("Considerando un color RGB, dime el G para el color: "))
        self.b = int(input("Considerando un color RGB, dime el B para el color: "))
        
        self.size = int(input("Dime el tamaño de la casa (45-60): "))
        while self.size<45 or self.size>60:
            print("Tamaño invalido")
            self.size = int(input("Dime el tamaño de la casa (45-60): "))

    def create_action(self):
        return House(self.filename, self.x, self.y, self.r,self.g,self.b,self.size)