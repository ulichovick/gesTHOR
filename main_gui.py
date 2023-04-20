import tkinter as tk
from tkinter import ttk
from dnf_test import query_local_packages, query_available_packages

class Aplicacion(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GesTHOR")
        self.window.geometry("500x630")
        self.cuaderno = ttk.Notebook(self.window, width=495, height=600)
        self.c = {}

        self.pestana_instalados = ttk.Frame(self.cuaderno, relief="solid")
        self.cuaderno.add(self.pestana_instalados, text="Instalados")
        self.busqueda = ttk.Frame(self.pestana_instalados, relief="solid", width=495, height=200)
        self.busqueda.grid(column=0,row=0)
        self.label = ttk.Label(self.busqueda, text="Buscar paquetes instalados ", font=("Liberation Serif",20))
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.filtro = ttk.Entry(self.busqueda, width=25)
        self.filtro.place(relx=0.5, rely=0.3, anchor="center")

        self.boton_locales = ttk.Button(self.busqueda, width=10, text="Buscar", command=self.locales)
        self.boton_locales.place(relx=0.5, rely=0.5, anchor="center")

        
        self.resultados = ttk.Frame(self.pestana_instalados, relief="solid", width=495, height=400)
        self.resultados.grid(column=0,row=1)
        self.label_resultados = ttk.Label(self.resultados, text="Resultados: ", font=("Liberation Serif",20))
        self.label_resultados.place(relx=0.5, rely=0.1, anchor="center")

        self.pestana_disponibles = ttk.Frame(self.cuaderno, relief="solid")
        self.cuaderno.add(self.pestana_disponibles, text="Explorar")
        self.busqueda = ttk.Frame(self.pestana_disponibles, relief="solid", width=495, height=200)
        self.busqueda.grid(column=0,row=0)
        self.label = ttk.Label(self.busqueda, text="Buscar paquetes disponibles ", font=("Liberation Serif",20))
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.filtro_linea = ttk.Entry(self.busqueda, width=25)
        self.filtro_linea.place(relx=0.5, rely=0.3, anchor="center")

        self.boton_locales = ttk.Button(self.busqueda, width=10, text="Buscar", command=self.linea)
        self.boton_locales.place(relx=0.5, rely=0.5, anchor="center")
        
        self.resultados_linea = ttk.Frame(self.pestana_disponibles, relief="solid", width=495, height=400)
        self.resultados_linea.grid(column=0,row=1)
        self.label_resultados_linea = ttk.Label(self.resultados_linea, text="Resultados: ", font=("Liberation Serif",20))
        self.label_resultados_linea.place(relx=0.5, rely=0.1, anchor="center")

        self.cuaderno.grid(column=0, row=0)
        self.window.mainloop()

    def locales(self):
        self.i = 1
        self.j = 0.2
        if self.c:
            self.resultados.destroy()    
            self.resultados = ttk.Frame(self.pestana_instalados, relief="solid", width=495, height=400)
            self.resultados.grid(column=0,row=1)
            self.label_resultados = ttk.Label(self.resultados, text="Resultados: ", font=("Liberation Serif",20))
            self.label_resultados.place(relx=0.5, rely=0.1, anchor="center")
        self.packages = query_local_packages(str(self.filtro.get()))
        print(self.packages)
        if self.packages:
            for pkg in self.packages:
                self.c[self.i] = ttk.Checkbutton(self.resultados, text = str(pkg), variable=str(pkg))
                self.c[self.i].place(relx=0.5, rely=self.j, anchor="e")
                self.i = self.i + 1
                self.j = self.j + 0.1

        else:
            self.texto.insert(tk.END,f"El paquete no se encuentra instalado \n")

    def linea(self):
        self.k = 1
        self.l = 0.2
        if self.c:
            self.resultados_linea.destroy()
            self.resultados_linea = ttk.Frame(self.pestana_disponibles, relief="solid", width=495, height=400)
            self.resultados_linea.grid(column=0,row=1)
            self.label_resultados_linea = ttk.Label(self.resultados_linea, text="Resultados: ", font=("Liberation Serif",20))
            self.label_resultados_linea.place(relx=0.5, rely=0.1, anchor="center")
        self.packages = query_available_packages(str(self.filtro_linea.get()))
        if self.packages:
            for pkg in self.packages:
                self.c[self.k] = ttk.Checkbutton(self.resultados_linea, text = str(pkg), variable=str(pkg))
                self.c[self.k].place(relx=0.5, rely=self.l, anchor="e")
                self.k = self.k + 1
                self.l = self.l + 0.1
        else:
            self.texto.insert(tk.END,f"No es posible encontrar el paquete \n")


if __name__ == "__main__":
    app1 = Aplicacion()