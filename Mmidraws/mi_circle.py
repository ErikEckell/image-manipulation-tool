from Mmidraws.MenuMidraws import MenuItemDraw
from Draw.circle import Circle

class MICircle(MenuItemDraw):

    @classmethod
    def get_description(cls) -> str:
        return 'Circulo'
    
    def ask_params(self) -> None:
        x = int(input("Dime la posición inicial del dibujo en el eje x: "))
        while x<0:
            print("El valor no puede ser menor a 0")
            x = int(input("Dime la posición inicial del dibujo en el eje x: "))

        y = int(input("Dime la posición inicial del dibujo en el eje y: "))
        while y<0:
            print("El valor no puede ser menor a 0")
            y = int(input("Dime la posición inicial del dibujo en el eje y: "))
            
        self.xy = (x,y)
        print("Considere que si coloca un valor mayor o menor a los indicados se considerara como maximo y minimo respectivamente")
        self.r = int(input("Considerando un color RGB, dime el R para el color: "))
        self.g = int(input("Considerando un color RGB, dime el G para el color: "))
        self.b = int(input("Considerando un color RGB, dime el B para el color: "))
        self.size = int(input("Dime el tamaño del circulo: "))
        self.width = 5

    def create_action(self):
        return Circle(self.filename, self.xy, self.r,self.g,self.b,self.size,self.width)