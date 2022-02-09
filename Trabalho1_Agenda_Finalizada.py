from tkinter import *
from tkinter import ttk

###################### Se não exixtir o arquivo .txt é necessário rodar "inserir o primeiro contato" 

class Agenda():
    ############################################################################################ Init (Começo)
    def __init__(self, nome = "", numero = int, email = "", busc = "", esc = int):        
        self.nome = nome        
        self.numero = numero
        self.email = email
        self.busc = busc
        self.esc = esc        
    ############################################################################################ Init (Final)



    ############################################################################################ Menu (começo)
    def menu():
        agenda_menu = Tk()
        agenda_menu.title("Sua Agenda :)")

        agenda_menu.geometry("500x400+500+100")
        agenda_menu.resizable(False, False)
        agenda_menu.iconbitmap("Icon_Agenda.ico")  
        agenda_menu["bg"] = "#00997a"      

        buttonColors = "#00cca3"
        buttonsLargura = 20 

        menu_titulo = Label( agenda_menu,
                            text="Menu de opções",                  #Título
                            bg = "#006652",                         #cor de fundo
                            fg = "#00ffcc",                         #cor da letra
                            font = "ArialBlack 30 bold italic",     #Editando fonte 
                            bd = 7,                                 #Espessura da moldura
                            relief = "ridge"                        #tipo de moldura
                            )

        inserir = Button(  agenda_menu,
                            text="Inserir contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,                 #Largura do botão
                            command = agenda1.inserir) 

        remover = Button(  agenda_menu,
                            text="Remover contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = agenda1.remover)
                                    
        buscar = Button(   agenda_menu,
                            text="Buscar contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = agenda1.buscar)

        editar = Button(   agenda_menu,
                            text="Editar contato",
                            bg = buttonColors,
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command = agenda1.editar)
       
        finalizar = Button(agenda_menu,
                            text="Finalizar Agenda",
                            bg = "#FA8072",
                            font = "ArialBlack 15 bold",
                            width = buttonsLargura,
                            command= lambda: agenda_menu.destroy())

        menu_titulo.pack(pady=(5,5))
        inserir.pack()
        remover.pack()
        buscar.pack()
        editar.pack()        
        finalizar.pack()            

        agenda_menu.mainloop()
    ############################################################################################ Menu (Final)



    ############################################################################################ Inserindo contato (Começo)
    def inserir_aux(self):
        #------------------------------------Adicionando o contato no .txt (começo)
        agenda1 = open("Contatos.txt", "a")
        agenda1.write("{}-{}-{}\n".format(self.nome.get(), self.numero.get(), self.email.get()))
        agenda1.close()
        #------------------------------------Adicionando o contato no .txt (fim)              

    def inserir(self): #Insesir contato    

        inserir_menu = Tk()
        inserir_menu.title("Inserindo novo contato")
        inserir_menu.geometry("500x400+500+100")
        inserir_menu.resizable(False, False)
        inserir_menu["bg"] = "#00997a"

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura =10
        labels_largura = 20
        tamanho_fonte ="15"
        largura_entry = 40
        ##################### Modificar

        text1 = Label(inserir_menu, text="Digite o nome: ",
                            bg = "#006652",                                         #cor de fundo
                            fg = "#00ffcc",                                         #cor da letra
                            font = "ArialBlack "+tamanho_fonte+" bold italic",      #Editando fonte
                            width = labels_largura, 
                            bd = 2,                                                 #Espessura da moldura
                            relief = "ridge"                                        #tipo de moldura
                        )

        text2 = Label(inserir_menu, text="Digite o número: ",
                            bg = "#006652",                                         #cor de fundo
                            fg = "#00ffcc",                                         #cor da letra
                            font = "ArialBlack "+tamanho_fonte+" bold italic",      #Editando fonte 
                            width = labels_largura,                                        
                            bd = 2,                                                 #Espessura da moldura
                            relief = "ridge"                                        #tipo de moldura       
                        )

        text3 = Label(inserir_menu, text="Digite o email: ",
                            bg = "#006652",                                          #cor de fundo
                            fg = "#00ffcc",                                          #cor da letra
                            font = "ArialBlack "+tamanho_fonte+" bold italic",       #Editando fonte
                            width = labels_largura,                         
                            bd = 2,                                                  #Espessura da moldura
                            relief = "ridge"                                         #tipo de moldura
                        )
        
        self.nome = Entry(inserir_menu,width = largura_entry)
        text1.pack()
        self.nome.pack()

        self.numero = Entry(inserir_menu, width = largura_entry)
        text2.pack(pady=(10,0))
        self.numero.pack()

        self.email = Entry(inserir_menu, width = largura_entry)
        text3.pack(pady=(10,0))
        self.email.pack(pady=(0,20)) 
        
        button_Voltar = Button( inserir_menu,
                                text="Voltar",
                                bg = "#FA8072",
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda: inserir_menu.destroy()
                                )

        add = Label(inserir_menu,   text="Contato adicionado com sucesso!",
                                    bg = "#006652",                                          #cor de fundo
                                    fg = "#00ffcc",                                          #cor da letra
                                    font = "ArialBlack 20 bold italic",                      #Editando fonte
                                    bd = 1,                                                  #Espessura da moldura
                                    relief = "ridge"                                         #tipo de moldura                                
                                ) 

        button_inserir = Button(inserir_menu,
                                text="Adicionar",
                                bg = buttonColors,
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda:[   Agenda.inserir_aux(self),
                                                    button_inserir.forget(),
                                                    add.pack()                                                                                                                                               
                                                ]
                                )

        button_inserir.pack()
        button_Voltar.pack()      
    ############################################################################################ Inserindo contato (Final)



    ############################################################################################ Removendo contato (Começo)
    ######################### Removendo contato quando se busca mais de 1, parte final (Começo)
    def remover_aux_buscando_2(self, esco, x1=[]):
        escolha = int(esco) - 1        
        buscado = x1[escolha]

        x1 = []
        x2 = [] 
        contatos = open('Contatos.txt', 'r')
        for linha in contatos:
            x1.append(linha) 
        
        for linha in range (0, len(x1)):
            if buscado not in x1[linha]:
                x2.append(x1[linha])
        contatos.close()

        contatos = open('Contatos.txt', 'w')
        for i in range (0, len(x2)):                    
            contatos.write(x2[i]) 

        contatos.close()
    ######################### Removendo contato quando se busca mais de 1, parte final (Final)

    ######################### Removendo contato quando só encontra 1 na busca (Começo)
    def remover_aux(self, busc):
        buscado = busc
        x1 = []
        x2 = [] 
        contatos = open('Contatos.txt', 'r')
        for linha in contatos:
            x1.append(linha) 
        
        for linha in range (0, len(x1)):
            if buscado not in x1[linha]:
                x2.append(x1[linha])
        contatos.close()

        contatos = open('Contatos.txt', 'w')
        for i in range (0, len(x2)):                    
            contatos.write(x2[i]) 

        contatos.close()
    ######################### Removendo contato quando só encontra 1 na busca (Final)

    ######################### Removendo contato tela de busca / tela 2 (Começo)
    def remover_aux_buscando(self, busc):
        buscado = busc

        remover_menu_2 = Tk()
        remover_menu_2.title("Contatos encontrados")
        remover_menu_2.geometry("500x400+500+100")
        remover_menu_2["bg"] = "#00997a"  

        contatos_encontrados = Tk()
        contatos_encontrados.title("Contatos encontrados")
        contatos_encontrados.geometry("400x400+1002+100")
        contatos_encontrados["bg"] = "#00997a"  
        
        
        ########### Barra de rolagem     
        frame= Frame(contatos_encontrados, background="#00997a")
        frame.pack(fill=BOTH, expand=1)

        canvas = Canvas(frame,background="#00997a")
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        barra_rolagem = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        barra_rolagem.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=barra_rolagem.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame_2 = Frame(canvas, background="#00997a")

        canvas.create_window((0,0), window=frame_2, anchor=W)
        ########### Barra de rolagem

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 10
        ##################### Modificar     

        text1 = Label(frame_2, text="Contatos encontrados:",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                        )
        text1.grid(row= 0, column=0,pady=10, padx=(2,0))  

        contatos = open('Contatos.txt', 'r') #buscando contato
        i = 1
        x1 = [] 

        for linha in contatos:
            linha = linha.rstrip()
            aux = linha.find(buscado)
                        
            if aux != -1:                
                x1.append(linha)                               
                Label(frame_2,     text="("+str(i)+")   "+linha,           #Mostrando contato que será removido com o numero correspondente
                                                bg = "#00997a",                         #cor de fundo
                                                font = "ArialBlack 11"
                    ).grid(row= i, column=0, sticky=W)             
                i +=1   

        text3 = Label(remover_menu_2,   text="Contato removido com sucesso!",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                                )
                        
        if i == 2:            
            text2 = Label(remover_menu_2,   text="Remover contato ao lado?",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                                )                              
            text2.pack(pady=(20,10))           

            button_voltar_menu = Button(remover_menu_2,
                                        text="Voltar",
                                        bg = "#FA8072",
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command =lambda:[  
                                                            text3.pack(pady=(20,0)),
                                                            remover_menu_2.destroy(),
                                                            contatos_encontrados.destroy()                                                   
                                                        ]
                                    )  

            button_remover = Button(remover_menu_2,
                                    text="Remover",
                                    bg = buttonColors,
                                    font = "ArialBlack 15 bold",
                                    width = buttonsLargura,
                                    command =lambda:[   Agenda.remover_aux(self, buscado),
                                                        button_remover.pack_forget(),
                                                        text3.pack(pady=(20,0))                                                             
                                                    ]
                                    )
            button_remover.pack()
            button_voltar_menu.pack()

        elif i > 2:
            text4 = Label(remover_menu_2,   text="Escolha o contato que será removido\ncom seu número correspondente",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                            )                              
            text4.pack(pady=(5,0))

            self.esc = Entry(remover_menu_2, width=5)

            button_voltar_menu = Button(remover_menu_2,
                                    text="Voltar",
                                    bg = "#FA8072",
                                    font = "ArialBlack 15 bold",
                                    width = buttonsLargura,
                                    command =lambda:[   remover_menu_2.destroy(),
                                                        contatos_encontrados.destroy()                                                     
                                                    ]
                                )

            button_remover = Button(remover_menu_2,
                                    text="Remover",
                                    bg = buttonColors,
                                    font = "ArialBlack 15 bold",
                                    width = buttonsLargura,
                                    command =lambda:[   Agenda.remover_aux_buscando_2(self, self.esc.get(), x1),
                                                        button_remover.pack_forget(),
                                                        text3.pack(pady=(20,0))                                                
                                                    ]
                                )

            
            self.esc.pack(pady=(15,0))
            button_remover.pack(pady=(5,0))
            button_voltar_menu.pack()

        else:
            remover_menu_2.destroy()
            contatos_encontrados.destroy()

            erro = Tk()
            erro.title("Contatos encontrados")
            erro.geometry("500x400+500+100")
            erro["bg"] = "#00997a"   
                    

            text_erro = Label(erro, text="Nenhum contato encontrado!",
                                bg = "#006652",                                          #cor de fundo
                                fg = "#00ffcc",                                          #cor da letra
                                font = "ArialBlack 20 bold italic",                      #Editando fonte
                                bd = 3,                                                  #Espessura da moldura
                                relief = "ridge"                                         #tipo de moldura                                
                            )                              
            button_voltar_menu = Button(erro,
                                    text="Voltar",
                                    bg = "#FA8072",
                                    font = "ArialBlack 15 bold",
                                    width = buttonsLargura,
                                    command =lambda: erro.destroy()
                                        )

            text_erro.pack()
            button_voltar_menu.pack(pady=(10,0))
            
    ######################### Removendo contato tela de busca / tela 2 (Final)

    ######################### Removendo contato Menu principal / tela 1 (Começo)
    def remover(self):        
        remover_menu = Tk()
        remover_menu.title("Removendo contato")
        remover_menu.geometry("500x400+500+100")
        remover_menu.resizable(False, False)
        remover_menu["bg"] = "#00997a"    

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura =10
        labels_largura = 30
        tamanho_fonte ="15"
        ##################### Modificar
        
        texto_remover = Label(remover_menu, text="Busque o contato que será removido:",
                                            bg = "#006652",                                         #cor de fundo
                                            fg = "#00ffcc",                                         #cor da letra
                                            font = "ArialBlack "+tamanho_fonte+" bold italic",      #Editando fonte
                                            width = labels_largura, 
                                            bd = 2,                                                 #Espessura da moldura
                                            relief = "ridge"                                        #tipo de moldura
                            )
                            
        self.busc = Entry(remover_menu, width=60)

        button_buscar = Button(remover_menu,
                                text="Buscar",
                                bg = buttonColors,
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda:[   Agenda.remover_aux_buscando(self, self.busc.get()),
                                                    remover_menu.destroy()
                                                ]
                                )

        button_voltar_menu = Button(remover_menu,
                                        text="Voltar",
                                        bg = "#FA8072",
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command =lambda: remover_menu.destroy() 
                                    )                         

                    
        texto_remover.pack(pady=(25,0)) 
        self.busc.pack(pady=(0,20)) 
        button_buscar.pack() 
        button_voltar_menu.pack()           
    ######################### Removendo contato Menu principal / tela 1 (Final)  
    ############################################################################################ Removendo contato (Final) 

    

    ############################################################################################ Buscando contato (Começo)
    ################################################## Mostrar contatos encontrados (Começo)
    def buscar_aux(self):
        buscar_menu_2 = Tk()
        buscar_menu_2.title("Contatos encontrados")
        buscar_menu_2.geometry("500x400+500+100")
        buscar_menu_2["bg"] = "#00997a"  

        ########### Barra de rolagem     
        frame= Frame(buscar_menu_2, background="#00997a")
        frame.pack(fill=BOTH, expand=1)

        canvas = Canvas(frame,background="#00997a")
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        barra_rolagem = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        barra_rolagem.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=barra_rolagem.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame_2 = Frame(canvas, background="#00997a")

        canvas.create_window((0,0), window=frame_2, anchor=W)
        ########### Barra de rolagem

        espaço_centralizar = 100            #Espaço que para centralizar dados na tela, será inserido nos "grid()"

        ##################### Modificar
        buttonsLargura = 10
        ##################### Modificar        

        text1 = Label(frame_2, text="Contatos encontrados:",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                        )
        text1.grid(row=0, column=0, pady=15, padx=(-30+espaço_centralizar,0))
        
        contatos = open('Contatos.txt', 'r') #buscando contato
        i = 1
        for linha in contatos:
            linha = linha.rstrip()
            aux = linha.find(self.busc.get())                        
            if aux != -1:    
                Label(frame_2,text="("+str(i)+")   "+linha,           
                                    bg = "#00997a",                       
                                    font = "ArialBlack 11"
                    ).grid(row = i, column= 0, sticky= W, padx=(0+espaço_centralizar,0))                  
                i +=1
                                     
        button_voltar = Button(frame_2,
                                text="Voltar",
                                bg = "#FA8072",
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda: buscar_menu_2.destroy()
                                )       
        button_voltar.grid(row = i+1, column= 0, sticky= W, pady=(15,0), padx=(25+espaço_centralizar,0))  
    ################################################## Mostrar contatos encontrados (Final)

    ################################################## Digitar para buscar / tela 1 (Começo)
    def buscar(self):
        buscar_menu = Tk()
        buscar_menu.title("Buscando contato")
        buscar_menu.geometry("500x400+500+100")
        buscar_menu.resizable(False, False)
        buscar_menu["bg"] = "#00997a" 

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 10
        ##################### Modificar 
        
        texto = Label(buscar_menu,  text="Buscar contato:",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            width= 16,
                                            relief = "ridge"                                         #tipo de moldura                                
                        )

        self.busc = Entry(buscar_menu, width=45)
        
        button_buscar = Button(buscar_menu,
                                text="Buscar",
                                bg = buttonColors,
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda:[   Agenda.buscar_aux(self), 
                                                    buscar_menu.destroy()                                                  
                                                ]
                                ) 

        button_voltar = Button(buscar_menu,
                                text="Voltar",
                                bg = "#FA8072",
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda: buscar_menu.destroy()
                                )      
              
        texto.pack(pady=(20,0)) 
        self.busc.pack() 
        button_buscar.pack(pady=(15,0)) 
        button_voltar.pack() 
    ################################################## Digitar para buscar / tela 1 (Final)           
    ############################################################################################ Buscando contato (Final)



    ############################################################################################ Editando contato (Começo)
    ################################################## NOME (Começo)
    ######################### Editando nome dentro do txt (Começo)
    def editar_nome_aux(self, nome, busc):
        buscado = busc
        novo_nome = nome        
        contatos = open('Contatos.txt', 'r')
        x1 = []    

        for linha in contatos:
            x1.append(linha) 
            
        for linha in range (0, len(x1)):
            if buscado in x1[linha]:
                pos = x1.index(x1[linha])
                aux1 = x1[pos] 

        aux2 = aux1.find("-")
        aux1 = aux1[aux2:]                
        aux1 = (novo_nome+aux1)

        contatos = open('Contatos.txt', 'w')
        for i in range (0, len(x1)):
            if buscado not in x1[i]:
                contatos.write(x1[i])
            
            else:
                contatos.write(aux1)
        contatos.close()     
    ######################### Editando nome dentro do txt (Final)

    ######################### Digitando o novo nome do contato (Começo)
    def editar_nome(self, busc):
        buscado = busc      
        
        editar_nome = Tk()
        editar_nome.title("Editando nome")
        editar_nome.geometry("500x400+500+100")
        editar_nome["bg"] = "#00997a"
        
        text = Label(editar_nome,   text="Digite o novo nome do contato:",
                                    bg = "#006652",                                          #cor de fundo
                                    fg = "#00ffcc",                                          #cor da letra
                                    font = "ArialBlack 20 bold italic",                      #Editando fonte
                                    bd = 3,                                                  #Espessura da moldura
                                    relief = "ridge"                                         #tipo de moldura                                
                        )        

        self.nome = Entry(editar_nome, width=30)


        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 15
        ##################### Modificar 

        text_sucess = Label(editar_nome,    text="Número editado com sucesso!",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                                )        

        button_voltar_menu = Button(editar_nome,
                                        text="Voltar",
                                        bg = "#FA8072",
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda: editar_nome.destroy()
                                    )


        button_editar_nome = Button(editar_nome,
                                        text="Editar nome",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda:[  Agenda.editar_nome_aux(self, self.nome.get(), buscado),
                                                            text_sucess.pack(),
                                                            button_editar_nome.forget()
                                                        ] 
                                    )

        text.pack(pady=(15,0))
        self.nome.pack(pady=(0,20))
        button_editar_nome.pack(pady=(10,0))
        button_voltar_menu.pack()
    ######################### Digitando o novo nome do contato (Final)
    ################################################## NOME (FInal)


    ################################################## NUMERO (Começo)
    ######################### Editando numero dentro do txt (Começo)
    def editar_numero_aux(self, numero, busc):
        buscado = busc
        novo_numero = numero

        contatos = open('Contatos.txt', 'r')
        x1 = []    

        for linha in contatos:
            x1.append(linha) 
            
        for linha in range (0, len(x1)):
            if buscado in x1[linha]:
                pos = x1.index(x1[linha])
                aux1 = x1[pos] 

        aux4 = aux1.find("-") 
        aux5 = aux1.rfind("-")             
        
        nomex = aux1[:aux4] + "-"
        emailx = aux1[aux5:]
        aux1 = (nomex + novo_numero + emailx)                              

        contatos = open('Contatos.txt', 'w')
        for i in range (0, len(x1)):
            if busc not in x1[i]:
                contatos.write(x1[i])
            
            else:
                contatos.write(aux1)
    ######################### Editando numero dentro do txt (Final)

    ######################### Digitando o novo numero do contato (Começo)
    def editar_numero(self, busc):
        buscado = busc      
        
        editar_numero = Tk()
        editar_numero.title("Editando número")
        editar_numero.geometry("500x400+500+100")
        editar_numero["bg"] = "#00997a"

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 15
        ##################### Modificar 
        
        text = Label(editar_numero, text="Digite o novo número do contato:",
                                    bg = "#006652",                                          #cor de fundo
                                    fg = "#00ffcc",                                          #cor da letra
                                    font = "ArialBlack 20 bold italic",                      #Editando fonte
                                    bd = 3,                                                  #Espessura da moldura
                                    relief = "ridge"                                         #tipo de moldura                                
                                )

        text.pack(pady=15)

        self.numero = Entry(editar_numero, width=30)

        text_sucess = Label(editar_numero,  text="Número editado com sucesso!",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                                )        

        button_voltar_menu = Button(editar_numero,
                                        text="Voltar",
                                        bg = "#FA8072",
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda: editar_numero.destroy()
                                    )

        button_editar_numero = Button(editar_numero,
                                        text="Editar numero",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda:[  Agenda.editar_numero_aux(self, self.numero.get(), buscado),                                                            
                                                            text_sucess.pack(),
                                                            button_editar_numero.forget()
                                                        ] 
                                    )
        self.numero.pack(pady=(0,20))
        button_editar_numero.pack()
        button_voltar_menu.pack()
    ######################### Digitando o numero nome do contato (Final)
    ################################################## NUMERO (FInal)

    ################################################## E-MAIL (Começo)
    ######################### Editando email dentro do txt (Começo)
    def editar_email_aux(self, email, busc):
        buscado = busc
        novo_email = email

        contatos = open('Contatos.txt', 'r')
        x1 = []    

        for linha in contatos:
            x1.append(linha) 
            
        for linha in range (0, len(x1)):
            if buscado in x1[linha]:
                pos = x1.index(x1[linha])
                aux1 = x1[pos] 

        aux4 = aux1.rfind("-")    
        aux1 = aux1[:aux4] + "-"               
        aux1 = (aux1+novo_email)              

        contatos = open('Contatos.txt', 'w')
        for i in range (0, len(x1)):
            if busc not in x1[i]:
                contatos.write(x1[i])
            
            else:
                contatos.write(aux1+"\n") 
    ######################### Editando email dentro do txt (Final)

    ######################### Digitando o novo email do contato (Começo)
    def editar_email(self, busc):
        buscado = busc      
        
        editar_email = Tk()
        editar_email.title("Editando E-mail")
        editar_email.geometry("500x400+500+100")
        editar_email["bg"] = "#00997a"

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 15
        ##################### Modificar 
    
        text = Label(editar_email, text="Digite o novo E-mail do contato:",
                            bg = "#006652",                                          #cor de fundo
                            fg = "#00ffcc",                                          #cor da letra
                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                            bd = 3,                                                  #Espessura da moldura
                            relief = "ridge"                                         #tipo de moldura                                
                )
        text.pack(pady=15)

        text_sucess = Label(editar_email,   text="E-mail editado com sucesso!",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                                )

        self.email = Entry(editar_email, width=30)

        button_voltar_menu = Button(editar_email,
                                        text="Voltar",
                                        bg = "#FA8072",
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda: editar_email.destroy()
                                    )

        button_editar_email = Button(editar_email,
                                        text="Editar E-mail",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda:[  Agenda.editar_email_aux(self, self.email.get(), buscado),
                                                            text_sucess.pack(),
                                                            button_editar_email.forget()
                                                        ] 
                                    )
        self.email.pack(pady=(0,20))
        button_editar_email.pack()
        button_voltar_menu.pack()
    ######################### Digitando o novo email do contato (Final)
    ################################################## E-MAIL (Final)

    ################################################## EDITANDO TUDO (Começo)
    ######################### Editando contato dentro do txt (Começo)
    def editar_tudo_aux(self, busc, nome, numero, email, x1=[]):
        aux = (nome+"-"+numero+"-"+email) 

        contatos = open('Contatos.txt', 'w')
        for i in range (0, len(x1)):
            if busc not in x1[i]:
                contatos.write(x1[i])
                contatos.write("\n")
            else:
                contatos.write(aux+"\n") 
    ######################### Editando contato dentro do txt (Final)

    ######################### Digitando o novo contato (Começo)
    def editar_tudo(self, busc, x1=[]):
        buscado = busc

        editar_tudo = Tk()
        editar_tudo.title("Editando todo o contato")
        editar_tudo.geometry("500x400+500+100")
        editar_tudo.resizable(False, False)
        editar_tudo["bg"] = "#00997a"

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura =10
        labels_largura = 20
        tamanho_fonte ="15"
        largura_entry = 40
        ##################### Modificar

        text1 = Label(editar_tudo, text="Digite o nome: ",
                            bg = "#006652",                                         #cor de fundo
                            fg = "#00ffcc",                                         #cor da letra
                            font = "ArialBlack "+tamanho_fonte+" bold italic",      #Editando fonte
                            width = labels_largura, 
                            bd = 2,                                                 #Espessura da moldura
                            relief = "ridge"                                        #tipo de moldura
                        )

        text2 = Label(editar_tudo, text="Digite o número: ",
                            bg = "#006652",                                         #cor de fundo
                            fg = "#00ffcc",                                         #cor da letra
                            font = "ArialBlack "+tamanho_fonte+" bold italic",      #Editando fonte 
                            width = labels_largura,                                        
                            bd = 2,                                                 #Espessura da moldura
                            relief = "ridge"                                        #tipo de moldura       
                        )

        text3 = Label(editar_tudo, text="Digite o email: ",
                            bg = "#006652",                                          #cor de fundo
                            fg = "#00ffcc",                                          #cor da letra
                            font = "ArialBlack "+tamanho_fonte+" bold italic",       #Editando fonte
                            width = labels_largura,                         
                            bd = 2,                                                  #Espessura da moldura
                            relief = "ridge"                                         #tipo de moldura
                        )
        
        self.nome = Entry(editar_tudo,width = largura_entry)
        text1.pack()
        self.nome.pack()

        self.numero = Entry(editar_tudo, width = largura_entry)
        text2.pack(pady=(10,0))
        self.numero.pack()

        self.email = Entry(editar_tudo, width = largura_entry)
        text3.pack(pady=(10,0))
        self.email.pack(pady=(0,20)) 
        
        button_Voltar = Button( editar_tudo,
                                text="Voltar",
                                bg = "#FA8072",
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda: editar_tudo.destroy()
                                )

        edit = Label(editar_tudo,    text="Contato editado com sucesso!",
                                    bg = "#006652",                                          #cor de fundo
                                    fg = "#00ffcc",                                          #cor da letra
                                    font = "ArialBlack 20 bold italic",                      #Editando fonte
                                    bd = 1,                                                  #Espessura da moldura
                                    relief = "ridge"                                         #tipo de moldura                                
                                ) 

        button_inserir = Button(editar_tudo,
                                text="Editar",
                                bg = buttonColors,
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda:[   Agenda.editar_tudo_aux(self, buscado, self.nome.get(), self.numero.get(), self.email.get(), x1),
                                                    button_inserir.forget(),
                                                    edit.pack()                                                                                                                                               
                                                ]
                                )
        button_inserir.pack(pady=(15,0))
        button_Voltar.pack()      
    ######################### Digitando o novo contato (Final)
    ################################################## EDITANDO TUDO (Final)

    ########################################################################### Menu's de edição do contato (começo)
    ######################### Separando o contato escolhido que será editado (Começo)    
    def editar_aux_escolha_2(self, esco, x1=[]):
        editar_menu_2 = Tk()
        editar_menu_2.title("Contatos encontrados")
        editar_menu_2.geometry("500x400+500+100")
        editar_menu_2["bg"] = "#00997a"  

        escolha = int(esco) - 1
        buscado = x1[escolha]

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 18
        ##################### Modificar 

        text_esc = Label(editar_menu_2, text="Escolha o que deseja\neditar no contato:",
                                        bg = "#006652",                                          #cor de fundo
                                        fg = "#00ffcc",                                          #cor da letra
                                        font = "ArialBlack 20 bold italic",                      #Editando fonte
                                        bd = 3,                                                  #Espessura da moldura
                                        relief = "ridge"                                         #tipo de moldura                                
                        ) 
        text_esc.pack(pady=15)

        button_editar_nome = Button(editar_menu_2,
                                    text="Editar nome",
                                    bg = buttonColors,
                                    font = "ArialBlack 15 bold",
                                    width = buttonsLargura,
                                    command = lambda:   [   Agenda.editar_nome(self, buscado),
                                                            editar_menu_2.destroy(),

                                                        ] 
                                    )

        button_editar_numero = Button(editar_menu_2,
                                        text="Editar número",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda:[  Agenda.editar_numero(self, buscado),
                                                            editar_menu_2.destroy()
                                                            ] 
                                    )

        button_editar_email = Button(editar_menu_2,
                                    text="Editar E-mail",
                                    bg = buttonColors,
                                    font = "ArialBlack 15 bold",
                                    width = buttonsLargura,
                                    command = lambda:[  Agenda.editar_email(self, buscado),
                                                            editar_menu_2.destroy()
                                                            ] 
                                    )

        button_editar_tudo = Button(editar_menu_2,
                                    text="Editar todo o contato",
                                    bg = buttonColors,
                                    font = "ArialBlack 15 bold",
                                    width = buttonsLargura,
                                    command = lambda:[  Agenda.editar_tudo(self, buscado, x1),
                                                            editar_menu_2.destroy()
                                                            ] 
                                    )

        button_Voltar = Button( editar_menu_2,
                                text="Voltar",
                                bg = "#FA8072",
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda: editar_menu_2.destroy()
                                )

        button_editar_nome.pack()
        button_editar_numero.pack()
        button_editar_email.pack()
        button_editar_tudo.pack() 
        button_Voltar.pack()       
    ######################### Separando o contato escolhido que será editado (Final)

    ################################################## Menu para 1 contato ou redireciona para o menu de mais contatos (começo)
    def editar_aux_escolha_1(self, busc):       #Aqui se faz a escolha do contato que será editado , se for apenas 1 contato encontrado ele já da as opções
        buscado = busc

        editar_menu_2 = Tk()
        editar_menu_2.title("Contatos encontrados")
        editar_menu_2.geometry("500x400+500+100")
        editar_menu_2["bg"] = "#00997a"  

        contatos_encontrados = Tk()
        contatos_encontrados.title("Contatos encontrados")
        contatos_encontrados.geometry("400x400+1002+100")
        contatos_encontrados["bg"] = "#00997a" 

        ########### Barra de rolagem     
        frame= Frame(contatos_encontrados, background="#00997a")
        frame.pack(fill=BOTH, expand=1)

        canvas = Canvas(frame,background="#00997a")
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        barra_rolagem = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        barra_rolagem.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=barra_rolagem.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame_2 = Frame(canvas, background="#00997a")

        canvas.create_window((0,0), window=frame_2, anchor=W)
        ########### Barra de rolagem 

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 18
        ##################### Modificar     

        text_encontrados = Label(frame_2, text="Contatos encontrados:",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                        )
        text_encontrados.grid(row=0, column=0)

        contatos = open('Contatos.txt', 'r') #buscando contato
        i = 1
        x1 = []
        for linha in contatos:
            linha = linha.rstrip()
            aux = linha.find(buscado)
                        
            if aux != -1:                
                x1.append(linha)                 
                Label(frame_2,     text="("+str(i)+")   "+linha,           #Mostrando contato que será removido com o numero correspondente
                                                bg = "#00997a",                         #cor de fundo
                                                font = "ArialBlack 11"
                    ).grid(row = i, column= 0, sticky= W)                  
                i +=1

        text3 = Label(editar_menu_2,   text="Contato editado com sucesso!",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                                )
                           
        if i == 2:            
            text_1 = Label(editar_menu_2,   text="Escolha o que deseja editar\nno contato ao lado ----->",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            relief = "ridge"                                         #tipo de moldura                                
                        ) 
            text_1.pack(pady=(15,0)) 

            button_editar_nome = Button(editar_menu_2,
                                        text="Editar nome",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda:   [   Agenda.editar_nome(self, buscado),
                                                                editar_menu_2.destroy(),
                                                                contatos_encontrados.destroy()
                                                            ] 
                                        )

            button_editar_numero = Button(editar_menu_2,
                                            text="Editar número",
                                            bg = buttonColors,
                                            font = "ArialBlack 15 bold",
                                            width = buttonsLargura,
                                            command = lambda:[  Agenda.editar_numero(self, buscado),
                                                                editar_menu_2.destroy(),
                                                                contatos_encontrados.destroy()
                                                             ] 
                                        )

            button_editar_email = Button(editar_menu_2,
                                        text="Editar E-mail",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda:[  Agenda.editar_email(self, buscado),
                                                                editar_menu_2.destroy(),
                                                                contatos_encontrados.destroy()
                                                             ] 
                                        )

            button_editar_tudo = Button(editar_menu_2,
                                        text="Editar todo o contato",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command = lambda:[  Agenda.editar_tudo(self, buscado, x1),
                                                                editar_menu_2.destroy(),
                                                                contatos_encontrados.destroy()
                                                             ] 
                                        )

            button_editar_nome.pack(pady=(10,0))
            button_editar_numero.pack()
            button_editar_email.pack()
            button_editar_tudo.pack()

        elif i > 2:  
                text_2 = Label(editar_menu_2,   text="Escolha o contato que será editado\ncom o número correspondente\nao lado ----->",
                                                bg = "#006652",                                          #cor de fundo
                                                fg = "#00ffcc",                                          #cor da letra
                                                font = "ArialBlack 20 bold italic",                      #Editando fonte
                                                bd = 3,                                                  #Espessura da moldura
                                                relief = "ridge"                                         #tipo de moldura                                
                        ) 

                self.esc = Entry(editar_menu_2, width=5)

                button_voltar_menu = Button(    editar_menu_2,
                                                text="Voltar",
                                                bg = "#FA8072",
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                                command =lambda:[   editar_menu_2.destroy(),
                                                                    contatos_encontrados.destroy()
                                                                ]
                                            )

                button_editar = Button(editar_menu_2,
                                        text="Editar",
                                        bg = buttonColors,
                                        font = "ArialBlack 15 bold",
                                        width = buttonsLargura,
                                        command =lambda:[   Agenda.editar_aux_escolha_2(self, self.esc.get(), x1),
                                                            button_editar.forget(),
                                                            text3.pack(),
                                                            editar_menu_2.destroy(),
                                                            contatos_encontrados.destroy()                                                  
                                                        ]
                                    )
                text_2.pack(pady=(15,10))    
                self.esc.pack()
                button_editar.pack(pady=(10,0))
                button_voltar_menu.pack()

        else:
            editar_menu_2.destroy()
            editar_menu_2 = Tk()
            editar_menu_2.title("Contatos encontrados")
            editar_menu_2.geometry("500x400+500+100")
                    

            Label(editar_menu_2, text="Nenhum contato encontrado.\n").pack()
            button_voltar_menu = Button (editar_menu_2,
                                        text="Voltar",
                                        command =lambda:editar_menu_2.destroy()
                                        )
            button_voltar_menu .pack()                                
    ################################################## Menu para 1 contato ou redireciona para o menu de mais contatos (Final)

    ######################### Primeira tela / chama o método que busca o contato (Começo)
    def editar(self):
        editando_menu = Tk()
        editando_menu.title("Editando contato")
        editando_menu.geometry("500x400+500+100")
        editando_menu.resizable(False, False)
        editando_menu["bg"] = "#00997a" 

        ##################### Modificar
        buttonColors = "#00cca3"
        buttonsLargura = 10
        ##################### Modificar 
        
        texto1 = Label(editando_menu,  text="Buscar contato:",
                                            bg = "#006652",                                          #cor de fundo
                                            fg = "#00ffcc",                                          #cor da letra
                                            font = "ArialBlack 20 bold italic",                      #Editando fonte
                                            bd = 3,                                                  #Espessura da moldura
                                            width= 16,
                                            relief = "ridge"                                         #tipo de moldura                                
                        )

        self.busc = Entry(editando_menu, width=45)
        
        button_buscar = Button(editando_menu,
                                text="Buscar",
                                bg = buttonColors,
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda:[   Agenda.editar_aux_escolha_1(self, self.busc.get()), 
                                                    editando_menu.destroy()                                                   
                                                ]
                                ) 

        button_voltar = Button(editando_menu,
                                text="Voltar",
                                bg = "#FA8072",
                                font = "ArialBlack 15 bold",
                                width = buttonsLargura,
                                command =lambda: editando_menu.destroy()
                                )      
              
        texto1.pack(pady=(20,0)) 
        self.busc.pack() 
        button_buscar.pack(pady=(15,0)) 
        button_voltar.pack() 
    ######################### Primeira tela / chama o método que busca o contato (Final) 
    ########################################################################### Menu's de edição do contato (Final)             
    ############################################################################################ Editando contato (Final) 
          
agenda1 = Agenda()
Agenda.menu()