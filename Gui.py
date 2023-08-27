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


