import os
direccion = "C:\\Users\\nicos\\Downloads"
direccion_general = r"C:\Users\nicos\Desktop\Nico en C\HTML CSS\Aprendiendo HTML\Disposiciones"
class File:
    def __init__(self):
        print('\n')
        self.busca_ficheros(direccion)
        print('\n')
        self.buscar_directorios(direccion)
        print('\n')
        self.recorrido_recursivo(direccion_general)

    def busca_ficheros(self, direccion):
        print("He aqui la lista de ficheros y sus tama;os")
        with os.scandir(direccion) as ficheros:
            for fichero in ficheros:
                if fichero.is_file():
                    print(f'{fichero.name}: {os.stat(fichero).st_size} bytes')

    def buscar_directorios(self, direccion):
        print("He aqui la lista de directorios")
        with os.scandir(direccion) as directorios:
            for directorio in directorios:
                if directorio.is_dir():
                    print(f'{directorio.name}: {os.stat(directorio).st_size} bytes')

    def recorrido_recursivo(self, direccion_general):
        for nombre_directorio,dirs, ficheros in os.walk(direccion_general):
            print(nombre_directorio)
            for nombre_fichero in ficheros:
                print(nombre_fichero, dirs)

if __name__ == "__main__":
    f = File()
