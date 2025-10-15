from Mmidraws.MenuMidraws import MenuItemDraw
from Draw.text import Text

class MIText(MenuItemDraw):

    @classmethod
    def get_description(cls) -> str:
        return 'Escribir texto'
    
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
        self.text = (input("Escribe el texto que deseas dibujar en la imagen: "))
        self.size = int(input("Dime el tamaño de las letras a utilizar: "))

    def create_action(self):
        return Text(self.filename, self.xy, self.text, self.r, self.g, self.b, self.size)