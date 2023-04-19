import tkinter as tk
from dnf_test import query_local_packages, query_available_packages

class Aplicacion(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mguel Pls")
        self.window.geometry("500x800")
        self.label = tk.Label(text="Filtrar paquetes instalados: ")
        self.label.pack()
        self.filtro = tk.Entry(width=25)
        self.filtro.pack()
        self.boton_locales = tk.Button(width=10, text="Instalados", command=self.locales)
        self.boton_locales.pack()
        self.boton_linea = tk.Button(width=10, text="Explorar", command=self.linea)
        self.boton_linea.pack()
        self.texto = tk.Text(width=50, height=50)
        
        #self.scrollbar = tk.Scrollbar(self.texto, orient=tk.VERTICAL)
        #self.scrollbar.set(0.2, 0.5)
        #self.scrollbar.place(x=100, y=40, height=200)
        self.texto.pack()
        self.window.mainloop()

    def locales(self):
        self.texto.delete(1.0,tk.END)
        self.packages = query_local_packages(str(self.filtro.get()))
        print(self.packages)
        if self.packages:
            for pkg in self.packages:
                self.texto.insert(tk.END,str(pkg))
                self.texto.insert(tk.END,f"\n")
        else:
            self.texto.insert(tk.END,f"El paquete no se encuentra instalado \n")

    def linea(self):
        self.texto.delete(1.0,tk.END)
        self.packages = query_available_packages(str(self.filtro.get()))
        if self.packages:
            for pkg in self.packages:
                self.texto.insert(tk.END,str(pkg))
                self.texto.insert(tk.END,f"\n")
        else:
            self.texto.insert(tk.END,f"No es posible encontrar el paquete \n")


if __name__ == "__main__":
    app1 = Aplicacion()