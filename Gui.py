from tkinter import *

class Gui():
    """"Classe da interface Gráfica
    """
x_pad = 5
y_pad = 3
width_entry = 30

window = Tk()
window.wm_title("Pysql versão remaque")

#Definindo variaveis para receber os dados
txtNome = StringVar()
txtSobrenome = StringVar()
txtEmail = StringVar()
txtCPF = StringVar()
#
#Criando os objetos

lblnome = Label(window, text="Nome")
lblsobrenome = Label(window, text="Sobrenome")
lblemail = Label(window, text="Email")
lblcpf = Label(window, text="CPF")
entNome = Entry(window, textvariable=txtNome, width=width_entry)

entSobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
entCPF = Entry(window, textvariable=txtEmail, width=width_entry)

listClientes = Listbox(window, width=100)
scrollClientes = Scrollbar(window)
btnViewAll = Button(window, text="Ver todos")
btnBuscar = Button(window, text="Buscar")
btnInserir = Button(window, text="Inserir")
btnUpdate = Button(window, text="Atualizar Selecionados")
btnDel = Button(window, text="Deletar Selecionados")
btnClose = Button(window, text="Fechar")

#Associando aos Grids

lblnome.grid(row=0,column=0)
lblsobrenome.grid(row=1, column=2)
lblemail.grid(row=2, column=0)
lblcpf.grid(row=3,column=0)
entNome.grid(row=0, column=1,padx=50, pady=50) 
entSobrenome.grid(row=1,column=1)
entEmail.grid(row=2,column=1)
entCPF.grid(row=3,column=1)
listClientes.grid(row=0,column=2,rowspan=10)
scrollClientes.grid(row=0,column=6,rowspan=10) 
btnViewAll.grid(row=4,column=0, columnspan=2)
btnBuscar.grid(row=5,column=0,columnspan=2) 
btnInserir.grid(row=6,column=0, columnspan=2) 
btnUpdate.grid(row=7,column=0,columnspan=2)
btnDel.grid(row=8,column=0,columnspan=2)
btnClose.grid(row=9,column=0,columnspan=2)

#Unindo Scrollbar com ListBox
listClientes.configure(yscrollcommand=scrollClientes.set)
scrollClientes.configure(command=listClientes.yview)

#adicionando estilo

for child in window.winfo_children():
    widget_class = child.__class__.__name__
    if widget_class == "Button":
        child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)
    elif widget_class == "ListBox":
        child.grid_configure(padx=0, pady=0, sticky="NS")
    elif widget_class == "Scrollbar":
        child.grid_configure(padx=0, pady=0, sticky="NS")
    else:
        child.grid_configure(padx=x_pad , pady=y_pad, sticky="N")

def run(self):
    Gui.window.mainloop()

#nova classe com heranças

from tkinter import Tk, Label, Entry, Listbox, Scrollbar, Button, StringVar

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30
        self.wm_title("Pysql versão remaque")

        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        self.lblnome = Label(self, text="Nome")
        self.lblsobrenome = Label(self, text="Sobrenome")
        self.lblemail = Label(self, text="Email")
        self.lblcpf = Label(self, text="CPF")
        self.entNome = Entry(self, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self, textvariable=self.txtEmail, width=self.width_entry)
        self.listClientes = Listbox(self, width=100)
        self.scrollClientes = Scrollbar(self)
        self.btnViewAll = Button(self, text="Ver todos")
        self.btnBuscar = Button(self, text="Buscar")
        self.btnInserir = Button(self, text="Inserir")
        self.btnUpdate = Button(self, text="Atualizar Selecionados")
        self.btnDel = Button(self, text="Deletar Selecionados")
        self.btnClose = Button(self, text="Fechar")

        self.lblnome.grid(row=0, column=0)
        self.lblsobrenome.grid(row=1, column=2)
        self.lblemail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)
        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)
        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)
        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        for child in self.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky="WE", padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "ListBox":
                child.grid_configure(padx=0, pady=0, sticky="NS")
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky="NS")
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky="N")

    def run(self):
        self.mainloop()

# Exemplo de uso
if __name__ == "__main__":
    app = Gui()
    app.run()

