#from distutils import command
from tkinter import *
#from tkinter import simpledialog

class Agenda():
    def __init__(self, nome, numero, email):
        self.nome = nome        
        self.numero = numero
        self.email = email

    def menu():
        AgendaMenu = Tk()
        AgendaMenu.title("Sua Agenda :)")

        AgendaMenu.geometry("500x400+500+100")
        AgendaMenu.resizable(False, False)
        AgendaMenu.iconbitmap("Icon_Agenda.ico")  
        AgendaMenu["bg"] = "#00997a"      

        buttonColors = "#00cca3"
        buttonsLargura = 20 

        MenuTitulo = Label( AgendaMenu,
                            text="Menu de opções",                  #Título
                            bg = "#006652",                         #cor de fundo
                            fg = "#00ffcc",                         #cor da letra
                            font = "ArialBlack 30 bold italic",     #Editando fonte 
                            bd = 7,                                 #Espessura da moldura
                            relief = "ridge"                        #tipo de moldura
                            )

        InserirB = Button(  AgendaMenu,
                            text="Inserir contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,                 #Largura do botão
                            command = agenda1.inserir) 

        RemoverB = Button(  AgendaMenu,
                            text="Remover contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = agenda1.remover)
                                    
        BuscarB = Button(   AgendaMenu,
                            text="Buscar contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = agenda1.buscar)

        EditarB = Button(   AgendaMenu,
                            text="Editar contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = agenda1.editar)

        FinalizarB = Button(AgendaMenu,
                            text="Finalizar Agenda",
                            bg = "#FA8072",
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura)
        MenuTitulo.pack()
        InserirB.pack()
        RemoverB.pack()
        BuscarB.pack()
        EditarB.pack()
        FinalizarB.pack()      

        AgendaMenu.mainloop()

    def inserir_aux(self):
        
        self.nome.get() 
        self.numero.get()
        self.email.get()  

        print("Dentro da função Nome:",self.nome)
        print("Dentro da função Numero:",self.numero)
        print("Dentro da função Email:",self.email)     

        agenda1 = open("Contatos.txt", "a")
        agenda1.write("{}-{}-{}\n".format(self.nome, self.numero, self.email))

    def inserir(self): #Insesir contato        
        InserirMenu = Tk()
        InserirMenu.title("Inserindo novo contato")
        InserirMenu.geometry("500x400+500+100")
        InserirMenu.resizable(False, False)

        Label(InserirMenu, text="Digite o nome: ").grid(row=0, sticky=W)
        Label(InserirMenu, text="Digite o número: ").grid(row=1, sticky=W)
        Label(InserirMenu, text="Digite o email: ").grid(row=2, sticky=W)
        
        self.nome = Entry(InserirMenu, width=25)
        self.nome.grid(row=0, column=1)                    
        print(self.nome)

        self.numero = Entry(InserirMenu, width=25)
        self.numero.grid(row=1, column=1)
        print(self.numero)

        self.email = Entry(InserirMenu, width=25)
        self.email.grid(row=2, column=1) 
        print(self.email)

        button_inserir = Button(  InserirMenu,
                            text="Adicionar",
                            command =lambda: Agenda.inserir_aux(self)
                            )
        button_inserir.grid(row=4, column=0)        

    def remover():
        pass

    def buscar():
        pass

    def editar():
        pass

#nome = ""
#numero = ""
#email = ""

agenda1 = Agenda()
Agenda.menu()  