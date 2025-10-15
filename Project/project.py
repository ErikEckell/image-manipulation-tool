from PIL import Image

class Project():
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(self.filename).convert("RGB")
        self.changes = []

    def show(self):    #mostrar imagen
        self.image.show()

    def add_changes(self,change):
        self.changes.append(change)

    def change_filename(self,filename):
        self.filename = filename
    
    def reset_image(self):
        self.image = Image.open(self.filename).convert("RGB")

    def save_image(self,filename):
        self.image.save(filename)

    def show_history(self):
        ctr = 1
        print("Historial del proyecto: ")
        for x in self.changes:
            print(ctr,".",x)
            ctr +=1

    def delete_history(self):
        if self.changes == []:
            return print("No hay historial") 
        self.changes.pop()
        self.show_history()
        self.filename = self.changes[len(self.changes)-1]
        self.reset_image()
        self.show()