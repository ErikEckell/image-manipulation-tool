import Compositions.compositions
import Draw.draw
import Filters
import Filters.filters
import Compositions
import Draw
import Mitems
import Mitems.mitems
from PIL import Image
from Project.project import Project
import pickle
from Mitems.mcompositions import MICompositions
from Mitems.mfilters import MIFilters
from Mitems.mdraw import MIDraw

class menu():
    def __init__(self):
        self.menus = []
        self.projects = []
        self.mproject = None
        self.choice = -1
        
    def start(self) -> None:
        print("¡Bienvenido a nuestro editor de imagenes!")
        working = True
        while working:
            print("1. Crear o abrir proyecto") #crear o abrir
            print("2. Trabajar en un proyecto existente") #filtros, composiciones, draw, deshacer, mostrar historial, script
            print("3. Ver proyecto actual") #ver proyecto
            print("4. Salir")
            option = int(input())
            while (option != 1) and (option != 2) and (option != 3) and (option != 4):
                print("Valor invalido, escoga uno de los siguientes: ")
                print("1. Crear o abrir proyecto") #crear o abrir
                print("2. Trabajar en el proyecto actual") #filtros, composiciones, draw, deshacer, mostrar historial, script
                print("3. Ver proyecto actual") #ver proyecto
                print("4. Salir")
                option = int(input())
            
            if option == 4:
                print("¡Gracias por usar nuestro editor de imagenes!")
                working = False
            
            else:
                self._execute(option)
        
    def _execute(self, option_idx):
        if option_idx == 1:
            print("")
            print("1. Crear proyecto")
            print("2. Abrir proyecto")
            print("3. Guardar proyecto")
            print("4. Volver ")
            action = int(input())
            while (action != 1) and (action != 2) and (action != 3) and (action !=4):
                print("Valor invalido, escoga uno de los siguientes: ")
                print("1. Crear proyecto")
                print("2. Abrir proyecto")
                print("3. Guardar proyecto")
                print("4. Volver")
                action = int(input())
            
            if (action == 1):

                filename = (input("Dime el nombre del archivo a crear: "))
                self.projects.append(filename)
                self.mproject = Project(filename)
                self.choice = len(self.projects)-1
                self.mproject.show()
                
            if (action == 2):
                if (self.projects == []):
                    print("No hay proyectos creados")
                else:
                    idx = 1
                    print("Proyectos actuales: ")                
                    for x in self.projects:
                        print(idx,":",x)
                        idx += 1
                    self.choice = int(input())-1
                    self.mproject = Project(self.projects[self.choice])
                    self.mproject.show()
            
            if (action == 3):
                if (self.choice == -1):
                    return print("No hay ningun proyecto seleccionado")
                save = input("Dime el nombre para guardar la imagen: ")
                self.mproject.save_image(save)
                self.projects.append(save)

        if option_idx == 2:
            if (self.choice == -1):
                return print("No hay ningun proyecto seleccionado")
            
            print("1. Filtros")
            print("2. Composiciones")
            print("3. Dibujos")
            print("4. Mostrar historial")
            print("5. Deshacer")
            print("6. Guardar script")
            print("7. Aplicar script")
            print("8. Volver")
            action = int(input())
            while (action<1) or (action>8):
                print("Valor invalido, escoga uno de los siguientes: ")
                print("1. Filtros")
                print("2. Composiciones")
                print("3. Dibujos")
                print("4. Mostrar historial")
                print("5. Deshacer")
                print("6. Guardar script")
                print("7. Aplicar script")
                print("8. Volver")
                action = int(input())

            if (action == 1):
                mfilters = MIFilters(self.projects[self.choice])
                mfilters.load_filters()
                cambio = mfilters.start()
                self.projects[self.choice] = cambio
                self.mproject.add_changes(cambio) 
                self.mproject.change_filename(cambio)
                self.mproject.reset_image()

            if (action == 2):
                mcompositons = MICompositions(self.projects[self.choice])
                mcompositons.load_compositions()
                cambio = mcompositons.start()
                self.projects[self.choice] = cambio
                self.mproject.add_changes(cambio) 
                self.mproject.change_filename(cambio)
                self.mproject.reset_image()
            
            if (action == 3):
                mdraw = MIDraw(self.projects[self.choice])
                mdraw.load_draw()
                cambio = mdraw.start()
                self.projects[self.choice] = cambio
                self.mproject.add_changes(cambio) 
                self.mproject.change_filename(cambio)
                self.mproject.reset_image()
                
            if (action == 4):
                self.mproject.show_history()

            if (action == 5):
                self.mproject.delete_history()

        if option_idx == 3:
            if (self.choice == -1):
                print("No hay ningún proyecto seleccionado")
            else:
                self.mproject.show()

    def _add_project(self, object):
        self.projects.append(object)
