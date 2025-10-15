from Mmidraws.MenuMidraws import MenuItemDraw
from Draw.rectangle import Rectangle

class MIRectangle(MenuItemDraw):

    @classmethod
    def get_description(cls) -> str:
        return 'Rectangulo'
    
    def ask_params(self) -> None:
        x = int(input("Dime la posición inicial del dibujo en el eje x0: "))
        while x<0:
            print("El valor no puede ser menor a 0")
            x = int(input("Dime la posición inicial del dibujo en el eje x0: "))

        y = int(input("Dime la posición inicial del dibujo en el eje y0: "))
        while y<0:
            print("El valor no puede ser menor a 0")
            y = int(input("Dime la posición inicial del dibujo en el eje y0: "))
            
        self.xy = (x,y)
        print("Considere que si coloca un valor mayor o menor a los indicados se considerara como maximo y minimo respectivamente")
        self.r = int(input("Considerando un color RGB, dime el R para el color: "))
        self.g = int(input("Considerando un color RGB, dime el G para el color: "))
        self.b = int(input("Considerando un color RGB, dime el B para el color: "))
        
        x2 = int(input("Digame la posición final del dibujo en el eje x1 (debe ser mayor a x0): "))
        while x2<0 or x2<x:
            print("El valor ingresado es invalido")
            x2 = int(input("Digame la posición final del dibujo en el eje x1 (debe ser mayor a x0): "))

        y2 = int(input("Digame la posición final del dibujo en el eje y1 (debe ser mayor a y0): "))
        while y2<0 or y2<y:
            print("El valor ingresado es invalido")
            y2 = int(input("Digame la posición final del dibujo en el eje y1 (debe ser mayor a y0): "))

        self.xy2 = (x2,y2)
        self.width = 5

    def create_action(self):
        return Rectangle(self.filename, self.xy, self.xy2, self.r, self.g, self.b, self.width)