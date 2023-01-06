import os
direccion = "C:\\Users\\nicos\\Downloads"
class File:
    def __init__(self):
        self.path = os.listdir(direccion)
        self.ordenar_ficheros(self.path)
        '''for i in self.path:
            if os.path.isdir(os.path.join(direccion, i)):
                print(i)'''

    def ordenar_ficheros (self, lista):
        lista = self.path
        directorios = []
        for item in lista:
            if os.path.isdir(os.path.join(direccion,item)):
                dir_removido = lista.pop(str(item)) 
                directorios.append(dir_removido)
        print(f"\n{lista}\n")
        print(f"\n{directorios}\n")


if __name__ == "__main__":
    f = File()
