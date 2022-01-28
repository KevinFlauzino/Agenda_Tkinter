from distutils import command
from tkinter import *
from tkinter import simpledialog

class Agenda():

    def Inserir(): #Insesir contato        
        InserirMenu = Tk()
        InserirMenu.title("Inserindo novo contato")
        InserirMenu.geometry("500x400+500+100")
        InserirMenu.resizable(False, False)

        Label(InserirMenu, text="Digite o nome: ").grid(row=0, sticky=W)
        Label(InserirMenu, text="Digite o número: ").grid(row=1, sticky=W)
        Label(InserirMenu, text="Digite o email: ").grid(row=2, sticky=W)

        def Inserir2():
            Nomex = Nome.get()              

            print("Nome: ",Nomex, "\nNumero: ",Numerox, "\nEmail: ", Emailx) 

            #contatos = open('Contatos.txt', 'a')       
            #contatos.write("{}-{}-{}\n".format(Nomex, Numerox, Emailx)) 
            #contatos.close()

        Nome = Entry(InserirMenu, width=25).grid(row=0, column=1)
        Numero = Entry(InserirMenu, width=25).grid(row=1, column=1)
        Email = Entry(InserirMenu, width=25).grid(row=2, column=1)



        ButtonOk = Button(  InserirMenu,
                            text="Adicionar",
                            command = Inserir2
                            ).grid(row=4, column=0)   
    
    def Remover():
        pass

    def Buscar():
        pass

    def Editar():
        pass


contatos = Agenda()

class Menu: #Criando menu para poder usar como loop
    def Iniciar_menu(self): 


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
                            command = Agenda.Inserir) 

        RemoverB = Button(  AgendaMenu,
                            text="Remover contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = Agenda.Remover)
                                    
        BuscarB = Button(   AgendaMenu,
                            text="Buscar contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = Agenda.Buscar)

        EditarB = Button(   AgendaMenu,
                            text="Editar contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = Agenda.Editar)

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
           
    
menu = Menu() #setando
escolhaX = 0 
menu.Iniciar_menu()