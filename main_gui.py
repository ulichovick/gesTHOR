import tkinter as tk
from dnf_test import test_dnf_query

class Aplicacion(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mguel Pls")
        self.window.geometry("500x800")
        self.label = tk.Label(text="Filtrar paquetes instalados: ")
        self.label.pack()
        self.filtro = tk.Entry(width=25)
        self.filtro.pack()
        self.boton = tk.Button(width=10, text="Filtrar", command=self.resultado)
        self.boton.pack()
        self.texto = tk.Text(width=50, height=50)
        
        #self.scrollbar = tk.Scrollbar(self.texto, orient=tk.VERTICAL)
        #self.scrollbar.set(0.2, 0.5)
        #self.scrollbar.place(x=100, y=40, height=200)
        self.texto.pack()
        self.window.mainloop()

    def resultado(self):
        self.texto.delete(1.0,tk.END)
        self.packages = test_dnf_query(str(self.filtro.get()))
        print(self.packages)
        for pkg in self.packages:
            self.texto.insert(tk.END,str(pkg))
            self.texto.insert(tk.END,f"\n")


if __name__ == "__main__":
    app1 = Aplicacion()