from modulos import *
from functions import *
import licence

from otherswindows import *
from multilanguage import *

janela = Tk()
class MeuOrc( Validadores, Functions, Formulas, Multilanguage, OthersWindows):
    def __init__(self):
        self.multiGlacx(); self.cores(); self.images_base64()
        ###########################################################################
        ### Variaveis dos Widgets desenhados
        self.orcamentoLb         = PhotoImage(data=base64.b64decode(self.ORCAMENTOLB))
        self.add                 = PhotoImage(data=base64.b64decode(self.ADD))
        self.seulogo             = PhotoImage(data=base64.b64decode(self.SEULOGO))
        self.cadcliBt = PhotoImage(data=base64.b64decode(self.CADCLI_BT))
        self.cadautBt = PhotoImage(data=base64.b64decode(self.CADAUT_BT))
        self.cadprodBt = PhotoImage(data=base64.b64decode(self.CADPROD_BT))
        self.cadfornecBt = PhotoImage(data=base64.b64decode(self.CADFORNEC_BT))
        self.cadservBt = PhotoImage(data=base64.b64decode(self.CADSERV_BT))

        self.button_imprime2     = PhotoImage(data=base64.b64decode(self.BTIMPRIME2))
        self.logo_rf             = PhotoImage(data=base64.b64decode(self.LOGORF))

        self.norcLb              = PhotoImage(data=base64.b64decode(self.LBNORC))
        self.clientBt            = PhotoImage(data=base64.b64decode(self.BTCLIENT))
        self.tecnicoBt           = PhotoImage(data=base64.b64decode(self.BTTECNICO))
        self.lupaBt 			 = PhotoImage(data=base64.b64decode(self.BTLUPA))

        self.TelaOrc()
    def cores(self):
        self.fundo_do_frame = '#dfe3ee'; self.borda_frame = '#759fe6'; self.fundo_da_tela = '#4682b4'
        self.bg_button = '#7492c8'; self.fg_button = 'white'; self.bg_label = '#dfe3ee'
        self.fg_label = '#3b5998'; self.fg_entry = 'gray25'; self.bg_entry = '#edf3f8'
        self.bg_button_del = '#c66c73'
    def TelaOrc(self):
		#######################################################################################################
		### Montagem da janela
        self.janela = janela;
        self.janela.title(self.m_Orcamento + self.m_e + self.m_Ordem + self.m_Glac)
        self.janela.configure(background=self.fg_label);
        self.janela.geometry("1000x600")
        self.janela.resizable(TRUE, TRUE);
        self.janela.minsize(width=800, height=500)
        #self.janela.maxsize(width=100, height=800)
        ######################################################################################################
        ### Chammando a função dos Menus
        self.Menus()
        #######################################################################################################
        ### Nomeando validadores das entradas
        self.vcmd8=(self.janela.register(self.validate_entry8), "%P")
        self.vcmd6=(self.janela.register(self.validate_entry6), "%P")
        self.vcmd4=(self.janela.register(self.validate_entry4), "%P")
        self.vcmd2=(self.janela.register(self.validate_entry2), "%P")
        self.vcmd8float=(self.janela.register(self.validate_entry8float), "%P")
        self.vcmd9float=(self.janela.register(self.validate_entry9float), "%P")
        self.vcmd4float=(self.janela.register(self.validate_entry4float), "%P")
        ########################################################################################################
        ###     Primeiro Container da janela
        top=Frame(self.janela, bd=2, bg=self.fg_label,highlightbackground=self.borda_frame,highlightthickness=3)
        top.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.13)
		########################################################################################################
        ### Segundo Container da Janela
        top2=Frame(self.janela,bd=1,bg=self.fundo_da_tela,highlightbackground= self.borda_frame,highlightthickness=1)
        top2.place(relx=0.005, rely=0.14, relwidth=0.99, relheight=0.2)
        ########################################################################################################
		### Moldura dos dados do cliente
        self.FrameCliente = Frame(top2, bd=1, bg=self.fundo_do_frame, highlightbackground= self.borda_frame,
            highlightthickness=3);self.FrameCliente.place(relx=0.002, rely=0.002, relwidth=0.45, relheight=1)

        self.top2 = top2
        ###########################################################################################################
		### Lista das placas de veiculos do cliente
        FrameAut2 = Frame(top2, width=10, bg=self.fundo_do_frame, bd=1, highlightbackground= self.borda_frame,
            highlightthickness=3); FrameAut2.place(relx=0.46, rely=0.002, relwidth=0.1, relheight=1)
        ############################################################################################################
		### Moldura dos dados veiculo
        self.FrameAut = Frame(top2, bd=1, bg=self.fundo_do_frame, highlightbackground= self.borda_frame,
            highlightthickness=3); self.FrameAut.place(relx=0.57, rely=0.002, relwidth=0.42, relheight=1)
		############################################################################################################
        ### Terceiro Container da janela
        top3 = Frame(self.janela, bd=1, bg=self.fundo_do_frame, highlightbackground= self.borda_frame,
            highlightthickness=3); top3.place(relx=0.005, rely=0.35, relwidth=0.99, relheight=0.45)
        self.top3 = top3
        ############################################################################################################
		### Moldura dos botoes
        self.FrameBot = Frame(top, bg= self.fg_label);self.FrameBot.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        self.botoes_atalho()
        FrameAbas = Frame(top3, bg=self.fundo_do_frame);FrameAbas.place(relx=0, rely=0, relwidth=1, relheight=1)
        ##############################################################################################################
        ### Quarto Container da Janela
        top4 = Frame(self.janela, width=95, bd=2, bg=self.fundo_do_frame, highlightbackground= self.borda_frame,
            highlightthickness=3); top4.place(relx=0.005, rely=0.805, relwidth=0.99, relheight=0.09)
        FrameTec=Frame(top4, bg=self.fundo_do_frame);FrameTec.place(relx=0.005, rely=0.005, relwidth=1, relheight=1)
        #############################################################################################################
        ### Quinto Container da janela
        top5=Frame(self.janela,bd=2,bg=self.fundo_do_frame,highlightbackground=self.borda_frame,highlightthickness=3)
        top5.place(relx=0.005, rely=0.905, relwidth=0.99, relheight=0.09)
        ###########################################################################################################
        ###  Logotipo GlacX - Tela Superior
        self.logo = Label(top, image=self.logo_rf, bd=0, bg=self.fg_label, relief=SUNKEN)
        self.logo.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        self.textoLogo=Label(top,bg=self.fg_label,text=self.m_logorf,bd=0,fg= self.bg_label,font=('Comic','36','bold'))
        self.textoLogo.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.6)
        ##########################################################################################################
        ### Container dos dados do cliente
        self.contCliente()
        ###########################################################################################################
        ####  Lista de placas
        self.entradaCod_aut=Listbox(FrameAut2,width=11,height=9, bd=3,bg=self.fundo_do_frame,fg=self.fg_entry,                                      font=('Verdana', '8', 'bold'))
        self.entradaCod_aut.pack()
        ###########################################################################################################
        #### Container dos dados do veiculo
        self.contAut()
        ##########################################################################################################
        ###  A B A S
        self.abas = Notebook(FrameAbas); self.frame_aba1 = Frame(self.abas); self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas); self.frame_aba4 = Frame(self.abas); self.frame_aba5 = Frame(self.abas)
        self.frame_aba3.configure(background=self.fundo_do_frame)
        self.frame_aba1.configure(background=self.fundo_do_frame)
        self.frame_aba2.configure(background=self.fundo_do_frame)
        self.frame_aba4.configure(background=self.fundo_do_frame)
        self.frame_aba5.configure(background=self.fundo_do_frame)
        self.label1 = Label(self.frame_aba1);self.label1.pack(padx=850, pady=225)
        self.label2 = Label(self.frame_aba2);self.label2.pack(padx=850, pady=225)
        self.label3 = Label(self.frame_aba3);self.label3.pack(padx=850, pady=225)
        self.label4 = Label(self.frame_aba4);self.label4.pack(padx=850, pady=225)
        self.label5 = Label(self.frame_aba5);self.label5.pack(padx=850, pady=225)
        self.abas.add(self.frame_aba1, text=self.m_Aba3);self.abas.add(self.frame_aba2, text = self.m_Aba1)
        self.abas.add(self.frame_aba3, text = self.m_Aba2);self.abas.add(self.frame_aba4, text = self.m_Aba4)
        self.abas.add(self.frame_aba5, text = self.m_Aba5)
        self.abas.pack(side="bottom")
        ### ABAS
        self.aba1();self.aba2();self.aba3();self.aba4();self.aba5()
        ###########################################################################
        #### Tecnico de reparo
        self.tecnico = Label(FrameTec, bg = self.fundo_do_frame, fg=self.fg_label, text = self.m_Tecnico)
        self.tecnico.place(relx=0.005, rely=0.05, relwidth=0.15, relheight=0.3)
        self.entradaTecnico = Entry(FrameTec, bd=1, width=14,  fg=self.fg_entry,font=('Verdana', '9', 'bold'))
        self.entradaTecnico.place(relx=0.005, rely=0.45, relwidth=0.15, relheight=0.3)
        self.entradaTecnico.insert(END, '???')
        self.botaotec = Button(FrameTec, image=self.tecnicoBt, bd=0, command=self.busca_tecnico)
        self.botaotec.place(relx=0.15, rely=0.1, relwidth=0.04, relheight=0.77)
        ###################################################################################################
        ##### label e listbox do numero do orcamento
        self.descrNumOrc=Label(FrameTec,text=self.m_Numero,bg=self.fundo_do_frame, fg=self.fg_label,
                               font=('Verdana','12','bold'))
        self.descrNumOrc.place(relx=0.24, rely=0.05, relwidth=0.08, relheight=0.9)
        self.listaNumOrc=Entry(FrameTec,width=6,justify='center',bd=3,fg=self.fg_entry,font=('Verdana','12','bold'))
        self.listaNumOrc.place(relx=0.32, rely=0.28, relwidth=0.08, relheight=0.4)
        ##################################################################################################
        #### Botões Orçamento
        ###  Botao Gravar
        self.botaoAbreOrc=Button(FrameTec,text=self.m_Gravar,bd=2,bg=self.bg_button_del,fg=self.fg_button,
            font=('Verdana','12','bold'),command=self.abre_orc)
        self.botaoAbreOrc.place(relx=0.4,rely=0.24,relwidth=0.07, relheight=0.5)
        ###  Botao Buscar
        self.botaoCarregaOrc = Button(FrameTec, text= self.m_Buscar, bd=2, bg =self.bg_button, fg =self.fg_button,
                                      font=('Verdana', '12', 'bold'),command=self.busca_orc)
        self.botaoCarregaOrc.place(relx=0.48, rely=0.24, relwidth=0.07, relheight=0.5)
        ### Botao Alterar
        self.botaoAlteraOrc = Button(FrameTec, text= self.m_Alterar, bd=2, bg =self.bg_button, fg =self.fg_button,
                                     font=('Verdana', '12', 'bold'),command=self.altera_orc)
        self.botaoAlteraOrc.place(relx=0.56, rely=0.24, relwidth=0.07, relheight=0.5)
        def funcpag():
            if self.listaNumOrc.get() == "" :
                msg = "É necessário que um Orçamento ou Ordem de Serviço \n" \
                      "esteja devidamente carregada na tela!!!"
                msg += ""
                messagebox.showinfo("GLAC - Pagamentos", msg)
            else:
                self.pagaOrdem()
        ###########################################################################################################
        ##  Entrada Total
        self.entradatotal=Entry(FrameTec,width=10,justify='right',fg=self.fg_entry,bd=1,font=('Verdana','12','bold'))
        self.entradatotal.place(relx=0.86, rely=0.3, relwidth=0.12, relheight=0.5);self.entradatotal2=Entry(FrameTec)
        ############################################################################################################
        ## Botao Total
        self.descrtotal=Button(FrameTec,text=self.m_Total,bg=self.bg_button,fg=self.fg_button,
            font=('Verdana','14','bold'),command=self.totalbotao);
        self.descrtotal.place(relx=0.75, rely=0.25, relwidth=0.1, relheight=0.6)
        self.totalbotao()
        ############################################################################################################
        #### Caixa de Seleção de Orçamento ou Ordemm de Serviço
        self.entradaTipoorc=Frame(top5,bd=2,width=40,bg=self.fundo_do_frame);
        self.entradaTipoorc.columnconfigure(0, weight=1);self.entradaTipoorc.rowconfigure(0, weight=1)
        self.entradaTipoorc.place(relx=0.01,rely=0.01,relwidth=0.16,relheight=0.8);self.Tipvar = StringVar(top5)
        self.TipV = {self.m_Ordem, self.m_Orcamento};self.Tipvar.set(self.m_Orcamento)
        self.popupMenu = OptionMenu(self.entradaTipoorc, self.Tipvar, *self.TipV)
        self.labelTip = Label(top5, bd=2, bg='gray95', fg=self.fg_label, font=('Verdana', '8', 'bold'))
        self.popupMenu.grid(row=2, column=1)
        #############################################################################################################
        ###  Label Licença
        self.licenciamento=Label(top5,text=licence.Licenca,bd=0,bg=self.fundo_do_frame,fg=self.bg_button,
            font=('Verdana','12','bold'));self.licenciamento.place(relx=0.3,rely=0.05,relwidth=0.3, relheight=0.4)
        ############################################################################################################
        ## Botao Acesse nossa pagina
        self.licenciamentoBt=Button(top5,text=self.m_Acesse,bd=1,bg=self.bg_button,fg=self.fg_button,
            font=('Verdana', '10', 'bold'), command=self.PaginaRf)
        self.licenciamentoBt.place(relx=0.3, rely=0.6, relwidth=0.3, relheight=0.4)
        ###############################################################################################################
        ###  Botao Imprimir Orçamento
        self.botaoImprimirOrc = Button(top5, image=self.button_imprime2, bd=0, bg=self.fundo_do_frame,
            command=self.imprime_orc);self.botaoImprimirOrc.place(relx=0.74,rely=0.01,relwidth=0.08,relheight=0.95)
        ##############################################################################################################
        ## Botao Forma de Pagamento
        self.formapag=Button(top5,text=self.m_Forma,bg=self.bg_button,font=('Verdana','8','bold'),fg=self.fg_button,
            command=funcpag);
        self.formapag.place(relx=0.84,rely=0.03,relwidth=0.15,relheight=0.7)

        #self.calendario = Calendar(top5, text=self.m_Forma, bg=self.bg_button, font=('Verdana', '8', 'bold'));
        #self.calendario.place(relx=0.74, rely=0.03)

        janela.mainloop()
    def contCliente(self):
        ####                Container de cadastro do cliente
        # Label do codigo do cliente
        self.descrCod_cli=Label(self.FrameCliente,text=self.m_Codigo+self.m_Pontinhos,font=('Verdana', '8', 'bold'))
        self.descrCod_cli.configure(fg=self.fg_label,bg=self.fundo_do_frame)
        self.descrCod_cli.place(relx=0.01, rely=0.04, relheight= 0.17)
        # Entrada do Codigo do Cliente
        self.entradaCod_cli=Entry(self.FrameCliente)
        self.entradaCod_cli.configure(validate="key",validatecommand=self.vcmd6)
        self.entradaCod_cli.configure(bd=1, width=6, fg=self.fg_entry, bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.entradaCod_cli.place(relx=0.2, rely=0.04, relwidth = 0.13, relheight= 0.17)
        # Botão Carrega
        self.botaoAdd = Button(self.FrameCliente, text = self.m_Buscar, bd=2, bg=self.bg_button, fg=self.fg_button,
            font=('Verdana','9','bold'),command=self.busca_cliente)
        self.botaoAdd.place(relx=0.34, rely=0.01, relwidth = 0.17, relheight= 0.23)
        # Botão Limpa
        self.botaoLimp = Button(self.FrameCliente, text = self.m_Limpar, bd=2,  bg=self.bg_button, fg=self.fg_button,
            font=('Verdana', '9', 'bold'), command=self.limpa_cliente)
        self.botaoLimp.place(relx=0.52, rely=0.01, relwidth = 0.17, relheight= 0.23)
        ### Variavel do dia de hoje
        hj = date.today()
        # Label data
        self.descrData = Label(self.FrameCliente, text= self.m_Data)
        self.descrData.configure(fg=self.fg_label, bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrData.place(relx=0.7, rely=0.04, relwidth = 0.1, relheight= 0.17)
        # Entrada Dia
        self.entradaDataorc = Entry(self.FrameCliente, fg='darkred', bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.entradaDataorc.configure(width=2, validate="key", validatecommand=self.vcmd2)
        self.entradaDataorc.place(relx=0.8, rely=0.04, relwidth = 0.05, relheight= 0.17)
        self.entradaDataorc.insert(END, hj.day)
        # Entrada Mês
        self.entradaDataorc2 = Entry(self.FrameCliente, width=2, validate="key", font=('Verdana', '8', 'bold'))
        self.entradaDataorc2.configure(validatecommand=self.vcmd2, bg=self.bg_entry, justify='right', fg='darkred')
        self.entradaDataorc2.place(relx=0.85, rely=0.04, relwidth = 0.05, relheight= 0.17)
        self.entradaDataorc2.insert(END, hj.month)
        # Entrada Ano
        self.entradaDataorc3 = Entry(self.FrameCliente, font=('Verdana', '8', 'bold'), fg='darkred')
        self.entradaDataorc3.configure(width=4, validate="key", bg=self.bg_entry, validatecommand=self.vcmd4)
        self.entradaDataorc3.place(relx=0.9, rely=0.04, relwidth = 0.1, relheight= 0.17)
        self.entradaDataorc3.insert(END, hj.year)
        # Label Cliente
        self.descrNome = Label(self.FrameCliente, text= self.m_Cliente + self.m_Pontinhos, font=('Verdana', '8', 'bold'))
        self.descrNome.configure(justify="right", fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrNome.place(relx=0.01, rely=0.24, relheight= 0.15)
        # Entrada do nome do cliente
        self.listNome = Entry(self.FrameCliente, width=40, bd=1, fg=self.fg_entry)
        self.listNome.configure(bg=self.bg_entry, font=('Verdana', '8', 'italic', 'bold'))
        self.listNome.place(relx=0.2, rely=0.24, relwidth = 0.78, relheight= 0.15)
        # Label do Endereço
        self.descrEndereco=Label(self.FrameCliente,text=self.m_Endereco+self.m_Pontinhos,font=('Verdana','8','bold'))
        self.descrEndereco.configure( fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrEndereco.place(relx=0.01, rely=0.39, relheight= 0.15)
        # Entrada do Endereço
        self.listEndereco=Entry(self.FrameCliente,width=40,bd=1,fg=self.fg_entry,font=('Verdana','8','bold','italic'),
            bg = self.bg_entry);self.listEndereco.place(relx=0.2,rely=0.39,relwidth=0.78,relheight= 0.15)
        ############################################
        # Label Bairro
        self.descrBairro=Label(self.FrameCliente,text=self.m_Bairro+self.m_Pontinhos,font=('Verdana', '8', 'bold'))
        self.descrBairro.configure( fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrBairro.place(relx=0.01, rely=0.54,  relheight= 0.15)
        ############################################
        # Entrada Bairro
        self.listBairro=Entry(self.FrameCliente,width=14,bd=1,fg=self.fg_entry,font=('Verdana','8','bold','italic'),
            bg=self.bg_entry); self.listBairro.place(relx=0.2, rely=0.54, relwidth = 0.25, relheight= 0.15)
        ################################################
        # Label Municipio
        self.descrMunicipio = Label(self.FrameCliente, width=6, text= self.m_Cidade, fg=self.fg_label,
            bg=self.fundo_do_frame); self.descrMunicipio.configure(font=('Verdana', '8', 'bold'))
        self.descrMunicipio.place(relx=0.445, rely=0.54, relheight= 0.15)
        ################################################
        # Entrada Municipio
        self.listMunicipio=Entry(self.FrameCliente,width=14,bd=1,fg=self.fg_entry,bg=self.bg_entry,
            font=('Verdana','8','bold','italic'))
        self.listMunicipio.place(relx=0.57,rely=0.54,relwidth=0.27,relheight= 0.15)
        ###############################################
        # Label UF
        self.descrUf=Label(self.FrameCliente,text=self.m_Uf,fg=self.fg_label,font=('Verdana', '8', 'bold'),
            bg = self.fundo_do_frame); self.descrUf.place(relx=0.85, rely=0.54, relwidth = 0.05, relheight= 0.15)
        ###############################################
        # Entrada UF
        self.listUf=Entry(self.FrameCliente,width=3,bd=1,fg=self.fg_entry,font=('Verdana','8','bold', 'italic'),
            bg = self.bg_entry); self.listUf.place(relx=0.91, rely=0.54, relwidth = 0.07, relheight= 0.15)
        ##############################################
        # Label CPF CNPJ
        self.descrCpf=Label(self.FrameCliente,fg=self.fg_label,text= self.m_Cpf+self.m_barra+self.m_Cnpj+
            self.m_Pontinhos,bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrCpf.place(relx=0.01, rely=0.69, relheight= 0.15)
        #############################################
        # Entrada CPF CNPJ
        self.listCpf=Entry(self.FrameCliente,bd=1,fg=self.fg_entry,bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listCpf.place(relx=0.2, rely=0.69, relwidth = 0.3, relheight= 0.15)
        ##############################################
        # Label Fone
        self.descrFone = Label(self.FrameCliente, fg=self.fg_label, text= self.m_Fone, bg=self.fundo_do_frame,
            font=('Verdana','8','bold'));self.descrFone.place(relx=0.55,rely=0.69,relwidth=0.12,relheight=0.15)
        ############################################
        # Entrada Fone
        self.listFone=Entry(self.FrameCliente,width=15,bd=1,fg=self.fg_entry,bg=self.bg_entry,
            font=('Verdana', '8', 'bold'));self.listFone.place(relx=0.68, rely=0.69, relwidth = 0.3, relheight= 0.15)
        ###########################################
        # Label OBS
        self.descrObs=Label(self.FrameCliente,text=self.m_Observacao+self.m_Pontinhos,bg=self.fundo_do_frame,
            fg=self.fg_label,font=('Verdana', '8', 'bold'));self.descrObs.place(relx=0.01, rely=0.84, relheight= 0.15)
        ##########################################
        # Entrada OBS
        self.listObs=Entry(self.FrameCliente,width=40,bd=1,fg=self.fg_entry,bg=self.bg_entry,
            font=('Verdana', '8', 'bold'));self.listObs.place(relx=0.2, rely=0.84, relwidth = 0.78, relheight= 0.15)
    def contAut(self):
        ###  		AUTOMOVEIS
        ###  Listbox da Placa do Automovel
        FrameAut = self.FrameAut
        # Binding da listbox da Placa
        self.entradaCod_aut.bind('<Button-1>', self.carrega_automovel)
        # Placa
        self.descrCod_aut=Label(FrameAut,text=self.m_Placa+self.m_Pontinhos,width=9,fg=self.fg_label,
            bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrCod_aut.place(relx=0, rely=0.01, relwidth = 0.2, relheight= 0.17)
        self.placa = Entry(FrameAut, width=9, bd=1, fg=self.fg_entry, bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.placa.place(relx=0.15, rely=0.01, relwidth = 0.2, relheight= 0.17)
        ###  Label e Entrada Ano
        self.descrAno=Label(FrameAut,text=self.m_Ano,fg=self.fg_label,bg=self.fundo_do_frame,
            font=('Verdana','8','bold'));
        self.descrAno.place(relx=0.45, rely=0.01, relwidth = 0.1, relheight= 0.17)
        self.listAno = Entry(FrameAut, width=5, validate="key", validatecommand=self.vcmd4, bd=1, fg=self.fg_entry,
                             bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listAno.place(relx=0.55, rely=0.01, relwidth = 0.2, relheight= 0.17)
        ###  Label e Entrada Veiculo
        self.descrAut = Label(FrameAut, text= self.m_Veiculo + self.m_Pontinhos, width=9, fg=self.fg_label,
                              bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrAut.place(relx=0, rely=0.20, relwidth = 0.22, relheight= 0.17)
        self.listAut = Entry(FrameAut, width=22, bd=1, fg=self.fg_entry, bg=self.bg_entry,
            font=('Verdana', '8', 'bold'));self.listAut.place(relx=0.15, rely=0.20, relwidth = 0.6, relheight= 0.17)
        ###  Label e Entrada Marca
        self.descrMarca=Label(FrameAut,text=self.m_Marca+self.m_Pontinhos,width=9,fg=self.fg_label,
            bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrMarca.place(relx=0, rely=0.4, relwidth = 0.2, relheight= 0.17)
        self.listMarca = Entry(FrameAut, width=22, bd=1, fg=self.fg_entry, bg=self.bg_entry,
            font=('Verdana','8','bold'));
        self.listMarca.place(relx=0.15,rely=0.4,relwidth=0.6,relheight= 0.17)
        ###  Label e Entrada Combustivel
        self.descrCombustivel=Label(FrameAut,text=self.m_Combustivel + self.m_Pontinhos, width=9, fg=self.fg_label,
            bg=self.fundo_do_frame,font=('Verdana', '8', 'bold'))
        self.descrCombustivel.place(relx=0, rely=0.6, relwidth = 0.28, relheight= 0.17)
        self.listCombustivel = Entry(FrameAut, width=22, bd=1, fg=self.fg_entry, bg=self.bg_entry,
            font=('Verdana','8','bold'));
        self.listCombustivel.place(relx=0.25,rely=0.6,relwidth=0.5,relheight=0.17)
        #########################################################
        ###  Label e Entrada km
        self.descrObs = Label(FrameAut,text=self.m_Km+self.m_Pontinhos);
        self.descrObs.configure(fg=self.fg_label,bg=self.fundo_do_frame, font=('Comic', '10', 'bold'))
        self.descrObs.place(relx=0, rely=0.8, relwidth = 0.15, relheight= 0.17)
        self.entradaObs=Entry(FrameAut,validate="key",validatecommand=self.vcmd9float)
        self.entradaObs.configure(fg='darkred',bg='lightblue', font=('Verdana', '8', 'bold'))
        self.entradaObs.place(relx=0.15, rely=0.8, relwidth = 0.2, relheight= 0.17)
        ###########################################################################
        ###  Label e Entrada Cor
        self.descrCor=Label(FrameAut);
        self.descrCor.configure(text=self.m_Cor,fg=self.fg_label,bg=self.fundo_do_frame,font=('Verdana','8','bold'))
        self.descrCor.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.17)
        self.listCor=Entry(FrameAut,width=12,bd=1,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','8','bold'))
        self.listCor.place(relx=0.55, rely=0.8, relwidth = 0.2, relheight= 0.17)
        ##########################################################################

    def botoes_atalho(self):
        #### Botoes
        self.ClientBot=Button(self.FrameBot,image=self.cadcliBt,bd=0,bg=self.fg_label,command=self.cadcli)
        self.ClientBot.place(relx=0.03, rely=0, relwidth=0.12, relheight=0.8)
        self.ClientLbBt=Label(self.FrameBot,text=self.m_Clientes,bd=2,bg=self.fg_label, fg= self.bg_label)
        self.ClientLbBt.place(relx=0.03, rely=0.82, relwidth=0.12, relheight=0.18)
        self.FornecBot=Button(self.FrameBot,image=self.cadfornecBt,bd=0,bg=self.fg_label,command=self.cadforn)
        self.FornecBot.place(relx=0.18, rely=0, relwidth=0.12, relheight=0.8)
        self.FornecLbBt = Label(self.FrameBot, text=self.m_Fornecedor, bd=2, bg=self.fg_label, fg=self.bg_label)
        self.FornecLbBt.place(relx=0.18, rely=0.82, relwidth=0.12, relheight=0.18)
        self.ModelosBot=Button(self.FrameBot,image=self.cadautBt,bd=0,bg=self.fg_label,fg=self.fg_button,
            command=self.cadaut);self.ModelosBot.place(relx=0.33, rely=0, relwidth=0.12, relheight=0.8)
        self.ModelosLbBt = Label(self.FrameBot, text=self.m_Automoveis, bd=2, bg=self.fg_label, fg=self.bg_label)
        self.ModelosLbBt.place(relx=0.33, rely=0.82, relwidth=0.12, relheight=0.18)
        self.ProdutosBot=Button(self.FrameBot,image=self.cadprodBt,bd=0,bg=self.fg_label,fg=self.fg_button,
            command=self.cadprod);self.ProdutosBot.place(relx=0.48, rely=0, relwidth=0.12, relheight=0.8)
        self.ProdutosLbBt = Label(self.FrameBot, text=self.m_Produtos, bd=2, bg=self.fg_label, fg=self.bg_label)
        self.ProdutosLbBt.place(relx=0.48, rely=0.82, relwidth=0.12, relheight=0.18)
        self.ServBot=Button(self.FrameBot,image=self.cadservBt,bd=0,bg=self.fg_label,fg=self.fg_button,
            command=self.cadserv);self.ServBot.place(relx=0.63, rely=0, relwidth=0.12, relheight=0.8)
        self.ServLbBt = Label(self.FrameBot, text=self.m_Serviços, bd=2, bg=self.fg_label, fg=self.bg_label)
        self.ServLbBt.place(relx=0.63, rely=0.82, relwidth=0.12, relheight=0.18)
    def aba1(self):

        ##########################################################################
        ####  Descrição dos problemas apresentados pelo veiculo - Aba 1
        self.frameProb = Frame(self.frame_aba1, bg= self.fundo_do_frame, bd=4, relief=SUNKEN)
        self.frameProb.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
        self.DescrProb=Label(self.frame_aba1,bg=self.bg_button,text=self.m_Atend1,bd=0,fg=self.fg_button,
            font=('Verdana', '12', 'bold'));
        self.DescrProb.place(relx=0.04, rely=0.04, relwidth=0.91, relheight=0.12)
        self.area1=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area1.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.1)
        self.area2=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area2.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.1)
        self.DescrProb2=Label(self.frame_aba1,text=self.m_Atend2,bd=0,width=85,fg=self.fg_button,
            font=('Verdana','12','bold'), bg= self.bg_button)
        self.DescrProb2.place(relx=0.04, rely=0.49, relwidth=0.91, relheight=0.12)
        self.area3=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area3.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.1)
        self.area4=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area4.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.1)
        ###########################################################################
        ###  Label e Entrada Inicio
        self.descrInicio = Button(self.frame_aba1, font=('Verdana', '8', 'bold'), command = self.calendarioInicio);
        self.descrInicio.configure(text='Data inicial', fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrInicio.place(relx=0.05, rely=0.045, relwidth=0.09, relheight=0.06)
        self.listInicio = Entry(self.frame_aba1, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listInicio.place(relx=0.05, rely=0.1, relwidth=0.09, relheight=0.05)
        ##########################################################################
        ###########################################################################
        ###  Label e Entrada Fim
        self.descrFim = Button(self.frame_aba1, font=('Verdana', '8', 'bold'), command = self.calendarioFim);
        self.descrFim.configure(text='Data final', fg=self.fg_label, bg=self.fundo_do_frame)

        self.descrFim.place(relx=0.05, rely=0.495, relwidth=0.09, relheight=0.06)
        self.listFim = Entry(self.frame_aba1, bd=1, fg=self.fg_entry, bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listFim.place(relx=0.05, rely=0.55, relwidth=0.09, relheight=0.05)
    def aba2(self):
        ### Cabeçalho dos itens_orc 1 A 10 - Aba 2
        self.frameItens = Frame(self.frame_aba2, bd=4, bg=self.bg_button)
        self.frameItens.place(relx=0.005, rely=0.01, relwidth=0.98, relheight=0.98)
        self.frameSP = Frame(self.frame_aba2,  bg= self.fundo_do_frame, bd=4,relief=SUNKEN)
        self.frameSP.place(relx=0.01, rely=0.03, relwidth=0.96, relheight=0.96)
        #### Label codigo
        self.descrCodI=Label(self.frame_aba2,bg=self.bg_button,fg= self.fg_label,text= self.m_Codigo+self.m_barra
            +self.m_Item,font=('Verdana', '10', 'bold'))
        self.descrCodI.place(relx=0.016, rely=0.05, relwidth=0.12, relheight=0.09)
        ######      Label Servicos Peças
        self.descrCol2 = Label(self.frame_aba2, bg= self.fg_label,text = self.m_Serviços + self.m_barra +
            self.m_Produtos,justify = 'center', fg=self.bg_label, font=('Verdana', '10', 'bold'))
        self.descrCol2.place(relx=0.137, rely=0.05, relwidth=0.55, relheight=0.09)
        ##      Label Valor
        self.descrCol3 = Label(self.frame_aba2, text= self.m_ValorUnit, bg=self.bg_label, fg= self.fg_label,
            font=('Verdana','10','bold'));self.descrCol3.place(relx=0.69, rely=0.05, relwidth=0.11, relheight=0.09)
        ###  Quantidade
        self.descrQuant = Label(self.frame_aba2, text= self.m_Quant, bg=self.fg_label, fg=self.bg_label,
            font=('Verdana','10','bold'));self.descrQuant.place(relx=0.8, rely=0.05, relwidth=0.06, relheight=0.09)
        ###     Total Item
        self.descrTotalItem = Label(self.frame_aba2, text= self.m_Total + ' ' + self.m_Item, bg=self.bg_label,
            fg= self.fg_label, font=('Verdana', '10', 'bold'))
        self.descrTotalItem.place(relx=0.86, rely=0.05, relwidth=0.1, relheight=0.09)
        ###############################
        ### Widgets - Listar item 1 ###
        ### Codigo do Item
        self.codServ1 = Entry(self.frame_aba2, validate="key", width=6, bd=1, justify='center', fg=self.fg_entry,
            bg=self.bg_entry, validatecommand=self.vcmd6, font=('Verdana', '8', 'bold'))
        self.codServ1.place(relx=0.016, rely=0.14, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos1=Button(self.frame_aba2,bd=0,bg=self.bg_label,image=self.add,command=self.add_servico1)
        self.botaoAddServicos1.place(relx=0.078, rely=0.14, relwidth=0.04, relheight=0.08)
        self.botaoAddServicos1F=Label(self.frame_aba2,bd=0,bg=self.bg_label,text="1-",font=('Verdana', '8', 'bold'),
            fg = self.fg_label); self.botaoAddServicos1F.place(relx=0.12, rely=0.14, relwidth=0.02, relheight=0.08)
        ####  Descricao do item Col2
        self.listaCol2a = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
            font=('Verdana','8','bold'));self.listaCol2a.place(relx=0.14,rely=0.14,relwidth=0.53,relheight=0.08)
        #### Botao Busca Item
        self.botaoBuscaSP1=Button(self.frame_aba2,bd=0,bg=self.bg_label,image=self.lupaBt,command=self.busca_servico1)
        self.botaoBuscaSP1.place(relx=0.67, rely=0.14, relwidth=0.03, relheight=0.08)
        #### Coluna Quantidade
        self.listaCol3a = Entry(self.frame_aba2, width=5, validate="key", bg=self.bg_entry,
            validatecommand=self.vcmd4float, bd=1,justify='center', fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3a.place(relx=0.8, rely=0.14, relwidth=0.1, relheight=0.08);  self.listaCol3a.insert(END, 1)
        #### Coluna Valor
        self.listaCol4a=Entry(self.frame_aba2,validate="key",bg=self.bg_entry,bd=1,justify='right',fg=self.fg_entry,
            font=('Verdana', '8', 'bold'));self.listaCol4a.place(relx=0.7,rely=0.14,relwidth=0.1,relheight=0.08)
        self.listaCol4a.insert(END, 0)
        self.labelCol4a = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bg=self.bg_entry, bd=0,
            font=('Verdana', '6', 'bold'));self.labelCol4a.place(relx=0.71,rely=0.15,relwidth=0.02,relheight=0.06)
        ###### Coluna Total Unitario
        self.listaCol5a=Entry(self.frame_aba2,validate="key",bg=self.bg_entry,bd=1,justify='right',fg=self.fg_entry,
            font=('Verdana', '8', 'bold'));self.listaCol5a.place(relx=0.86, rely=0.14, relwidth=0.1, relheight=0.08)
        self.listaCol5a.insert(END, 0)
        ###############################
        ### Widgets - Listar item 2 ###
        ###############################
        ### Codigo do Item
        self.codServ2 = Entry(self.frame_aba2, validate="key", width=6, bd=1, bg=self.bg_entry, justify='center',
                              fg=self.fg_entry,  validatecommand=self.vcmd6, font=('Verdana', '8', 'bold'))
        self.codServ2.place(relx=0.016, rely=0.22, relwidth=0.06, relheight=0.08)

        self.botaoAddServicos2 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico2)
        self.botaoAddServicos2.place(relx=0.078, rely=0.22, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos2F = Label(self.frame_aba2, bg=self.bg_label, bd=0, text="2-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos2F.place(relx=0.12, rely=0.22, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3b = Entry(self.frame_aba2, width=5, bd=1, justify='center', bg=self.bg_entry, fg=self.fg_entry,
                                validate="key", font=('Verdana', '8', 'bold'))
        self.listaCol3b.place(relx=0.8, rely=0.22, relwidth=0.1, relheight=0.08)
        self.listaCol3b.insert(END, 1)
        #### Botao Busca Item
        self.botaoBuscaSP2 = Button(self.frame_aba2, bd=0, bg = self.bg_label, image=self.lupaBt, font=('Verdana', '10', 'bold'),
                                    command=self.busca_servico2)
        self.botaoBuscaSP2.place(relx=0.67, rely=0.22, relwidth=0.03, relheight=0.08)
        #### Coluna Valor
        self.listaCol4b = Entry(self.frame_aba2, width=10, bd=1, validate="key", bg=self.bg_entry,
                                justify='right', fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4b.place(relx=0.7, rely=0.22, relwidth=0.1, relheight=0.08)
        self.listaCol4b.insert(END, 0)

        self.labelCol4b = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bg=self.bg_entry, bd=0,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4b.place(relx=0.71, rely=0.23, relwidth=0.02, relheight=0.06)

        ####  Descricao do item Col2
        self.listaCol2b = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2b.place(relx=0.14, rely=0.22, relwidth=0.53, relheight=0.08)
        ###### Coluna Total Unitario
        self.listaCol5b = Entry(self.frame_aba2, width=10, bd=1, justify='right', bg=self.bg_entry, validate="key",
                                fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5b.place(relx=0.86, rely=0.22, relwidth=0.1, relheight=0.08)
        self.listaCol5b.insert(END, 0)

        ###############################
        ### Widgets - Listar item 3 ###
        ###############################
        ''' Codigo do Item '''
        self.codServ3 = Entry(self.frame_aba2, width=6, bd=1, justify='center', bg=self.bg_entry, fg=self.fg_entry,
                              validatecommand=self.vcmd6, validate="key", font=('Verdana', '8', 'bold'))
        self.codServ3.place(relx=0.016, rely=0.3, relwidth=0.06, relheight=0.08)

        self.botaoAddServicos3 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add,
                                        command=self.add_servico3)
        self.botaoAddServicos3.place(relx=0.078, rely=0.3, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos3F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="3-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos3F.place(relx=0.12, rely=0.3, relwidth=0.02, relheight=0.08)

        ''' Coluna Quantidade '''
        self.listaCol3c = Entry(self.frame_aba2, width=5, bd=1, justify='center', bg=self.bg_entry, fg=self.fg_entry,
                                validate="key", font=('Verdana', '8', 'bold'))
        self.listaCol3c.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.08)
        self.listaCol3c.insert(END, 1)
        ''' Botao Busca Item '''
        self.botaoBuscaSP3 = Button(self.frame_aba2, bg = self.bg_label, bd=0, image=self.lupaBt, font=('Verdana', '10', 'bold'),
                                    command=self.busca_servico3)
        self.botaoBuscaSP3.place(relx=0.67, rely=0.3, relwidth=0.03, relheight=0.08)
        ''' Coluna Valor '''
        self.listaCol4c = Entry(self.frame_aba2, width=10, bd=1, justify='right', bg=self.bg_entry, validate="key",
                                fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4c.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.08)
        self.listaCol4c.insert(END, 0)
        self.labelCol4c = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bg=self.bg_entry, bd=0,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4c.place(relx=0.71, rely=0.31, relwidth=0.02, relheight=0.06)

        '''  Descricao do item Col2 '''
        self.listaCol2c = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2c.place(relx=0.14, rely=0.3, relwidth=0.53, relheight=0.08)
        ''' Coluna Total Unitario'''
        self.listaCol5c = Entry(self.frame_aba2, width=10, validate="key", bg=self.bg_entry,
                                bd=1, justify='right', fg=self.fg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol5c.place(relx=0.86, rely=0.3, relwidth=0.1, relheight=0.08)
        self.listaCol5c.insert(END, 0)

        ###############################
        ### Widgets - Listar item 4 ###
        ###############################

        ### Codigo do Item
        self.codServ4 = Entry(self.frame_aba2, width=6, bd=1, justify='center', bg=self.bg_entry,
                              font=('Verdana', '8', 'bold'))
        self.codServ4.configure(fg=self.fg_entry, validatecommand=self.vcmd6, validate="key")
        self.codServ4.place(relx=0.016, rely=0.38, relwidth=0.06, relheight=0.08)

        self.botaoAddServicos4 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico4)
        self.botaoAddServicos4.place(relx=0.078, rely=0.38, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos4F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="4-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos4F.place(relx=0.12, rely=0.38, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3d = Entry(self.frame_aba2, width=5, bd=1, justify='center', bg=self.bg_entry, fg=self.fg_entry,
                                validate="key", font=('Verdana', '8', 'bold'))
        self.listaCol3d.place(relx=0.8, rely=0.38, relwidth=0.1, relheight=0.08)
        self.listaCol3d.insert(END, 1)

        #### Botao Busca Item
        self.botaoBuscaSP4 = Button(self.frame_aba2, bg = self.bg_label, bd=0, image=self.lupaBt,
                                    font=('Verdana', '10', 'bold'), command=self.busca_servico4)
        self.botaoBuscaSP4.place(relx=0.67, rely=0.38, relwidth=0.03, relheight=0.08)

        #### Coluna Valor
        self.listaCol4d = Entry(self.frame_aba2, width=10, bd=1, bg=self.bg_entry, justify='right', fg=self.fg_entry,
                                validate="key", font=('Verdana', '8', 'bold'))
        self.listaCol4d.place(relx=0.7, rely=0.38, relwidth=0.1, relheight=0.08)
        self.listaCol4d.insert(END, 0)
        self.labelCol4d = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bg=self.bg_entry, bd=0,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4d.place(relx=0.71, rely=0.39, relwidth=0.02, relheight=0.06)

        ####  Descricao do item Col2
        self.listaCol2d = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2d.place(relx=0.14, rely=0.38, relwidth=0.53, relheight=0.08)

        ###### Coluna Total Unitario
        self.listaCol5d = Entry(self.frame_aba2, width=10, bd=1, justify='right', bg=self.bg_entry, fg=self.fg_entry,
                                validate="key", font=('Verdana', '8', 'bold'))
        self.listaCol5d.place(relx=0.86, rely=0.38, relwidth=0.1, relheight=0.08)
        self.listaCol5d.insert(END, 0)

        ###############################
        ### Widgets - Listar item 5 ###
        ###############################

        ### Codigo do Item
        self.codServ5 = Entry(self.frame_aba2, width=6, bd=1, justify='center', fg=self.fg_entry,
                              validatecommand=self.vcmd6,
                              validate="key", bg=self.bg_entry,
                              font=('Verdana', '8', 'bold'))
        self.codServ5.place(relx=0.016, rely=0.46, relwidth=0.06, relheight=0.08)

        self.botaoAddServicos3 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico5)
        self.botaoAddServicos3.place(relx=0.078, rely=0.46, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos5F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="5-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos5F.place(relx=0.12, rely=0.46, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3e = Entry(self.frame_aba2, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3e.place(relx=0.8, rely=0.46, relwidth=0.1, relheight=0.08)
        self.listaCol3e.insert(END, 1)

        #### Botao Busca Item
        self.botaoBuscaSP5 = Button(self.frame_aba2, bg = self.bg_label, bd=0, image=self.lupaBt,
                                    font=('Verdana', '10', 'bold'),
                                    command=self.busca_servico5)
        self.botaoBuscaSP5.place(relx=0.67, rely=0.46, relwidth=0.03, relheight=0.08)

        #### Coluna Valor
        self.listaCol4e = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4e.place(relx=0.7, rely=0.46, relwidth=0.1, relheight=0.08)
        self.listaCol4e.insert(END, 0)

        self.labelCol4e = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bg=self.bg_entry, bd=0,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4e.place(relx=0.71, rely=0.47, relwidth=0.02, relheight=0.06)



        ###  Descricao do item Col2
        self.listaCol2e = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2e.place(relx=0.14, rely=0.46, relwidth=0.53, relheight=0.08)

        ###### Coluna Total Unitario
        self.listaCol5e = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5e.place(relx=0.86, rely=0.46, relwidth=0.1, relheight=0.08)
        self.listaCol5e.insert(END, 0)

        ###############################
        ### Widgets - Listar item 6 ###
        ###############################

        ### Codigo do Item
        self.codServ6 = Entry(self.frame_aba2, width=6, bd=1, justify='center', bg=self.bg_entry, fg=self.fg_entry,
                              validatecommand=self.vcmd6, validate="key", font=('Verdana', '8', 'bold'))
        self.codServ6.place(relx=0.016, rely=0.54, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos6 = Button(self.frame_aba2, bd=0, bg=self.bg_label, image=self.add, command=self.add_servico6)
        self.botaoAddServicos6.place(relx=0.078, rely=0.54, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos6F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="6-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos6F.place(relx=0.12, rely=0.54, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3f = Entry(self.frame_aba2, width=5, bd=1, justify='center', bg=self.bg_entry, fg=self.fg_entry,
                                validate="key", font=('Verdana', '8', 'bold'))
        self.listaCol3f.place(relx=0.8, rely=0.54, relwidth=0.1, relheight=0.08)
        self.listaCol3f.insert(END, 1)

        #### Botao Busca Item
        self.botaoBuscaSP6 = Button(self.frame_aba2, bg= self.bg_label, bd=0, image=self.lupaBt,
                                    font=('Verdana', '10', 'bold'),
                                    command=self.busca_servico6)
        self.botaoBuscaSP6.place(relx=0.67, rely=0.54, relwidth=0.03, relheight=0.08)

        #### Coluna Valor
        self.listaCol4f = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4f.place(relx=0.7, rely=0.54, relwidth=0.1, relheight=0.08)
        self.listaCol4f.insert(END, 0)
        self.labelCol4f = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bg=self.bg_entry, bd=0,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4f.place(relx=0.71, rely=0.55, relwidth=0.02, relheight=0.06)

        ####  Descricao do item Col2
        self.listaCol2f = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2f.place(relx=0.14, rely=0.54, relwidth=0.53, relheight=0.08)

        ###### Coluna Total Unitario
        self.listaCol5f = Entry(self.frame_aba2, width=10, bd=1, justify='right', validate="key",
                                fg=self.fg_entry, bg=self.bg_entry,font=('Verdana', '8', 'bold'))
        self.listaCol5f.place(relx=0.86, rely=0.54, relwidth=0.1, relheight=0.08)
        self.listaCol5f.insert(END, 0)

        ###############################
        ### Widgets - Listar item 7 ###
        ###############################

        ### Codigo do Item
        self.codServ7 = Entry(self.frame_aba2, width=6, bd=1, justify='center', fg=self.fg_entry,
                              validatecommand=self.vcmd6,
                              validate="key", bg=self.bg_entry,
                              font=('Verdana', '8', 'bold'))
        self.codServ7.place(relx=0.016, rely=0.62, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos7 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico7)
        self.botaoAddServicos7.place(relx=0.078, rely=0.62, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos7F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="7-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos7F.place(relx=0.12, rely=0.62, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3g = Entry(self.frame_aba2, width=5, bd=1, bg=self.bg_entry,justify='center', fg=self.fg_entry, validate="key",
                                font=('Verdana', '8', 'bold'))
        self.listaCol3g.place(relx=0.8, rely=0.62, relwidth=0.1, relheight=0.08)
        self.listaCol3g.insert(END, 1)

        #### Botao Busca Item
        self.botaoBuscaSP7 = Button(self.frame_aba2, bg= self.bg_label,bd=0, image=self.lupaBt,
                                    font=('Verdana', '10', 'bold'),
                                    command=self.busca_servico7)
        self.botaoBuscaSP7.place(relx=0.67, rely=0.62, relwidth=0.03, relheight=0.08)

        #### Coluna Valor
        self.listaCol4g = Entry(self.frame_aba2, width=10, bd=1, justify='right', bg=self.bg_entry,fg=self.fg_entry, validate="key",
                                font=('Verdana', '8', 'bold'))
        self.listaCol4g.place(relx=0.7, rely=0.62, relwidth=0.1, relheight=0.08)
        self.listaCol4g.insert(END, 0)
        self.labelCol4g = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4g.place(relx=0.71, rely=0.63, relwidth=0.02, relheight=0.06)

        ####  Descricao do item Col2
        self.listaCol2g = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2g.place(relx=0.14, rely=0.62, relwidth=0.53, relheight=0.08)

        ###### Coluna Total Unitario
        self.listaCol5g = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                font=('Verdana', '8', 'bold'),bg=self.bg_entry)
        self.listaCol5g.place(relx=0.86, rely=0.62, relwidth=0.1, relheight=0.08)
        self.listaCol5g.insert(END, 0)

        ###############################
        ### Widgets - Listar item 8 ###
        ###############################

        ### Codigo do Item
        self.codServ8 = Entry(self.frame_aba2, width=6, bd=1, justify='center', fg=self.fg_entry,
                              validatecommand=self.vcmd6,
                              validate="key", bg=self.bg_entry,
                              font=('Verdana', '8', 'bold'))
        self.codServ8.place(relx=0.016, rely=0.7, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos8 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico8)
        self.botaoAddServicos8.place(relx=0.078, rely=0.7, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos8F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="8-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos8F.place(relx=0.12, rely=0.7, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3h = Entry(self.frame_aba2, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3h.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.08)
        self.listaCol3h.insert(END, 1)

        #### Botao Busca Item
        self.botaoBuscaSP8 = Button(self.frame_aba2, bg=self.bg_label, bd=0, image=self.lupaBt,
                                    font=('Verdana', '10', 'bold'),
                                    command=self.busca_servico8)
        self.botaoBuscaSP8.place(relx=0.67, rely=0.7, relwidth=0.03, relheight=0.08)

        #### Coluna Valor
        self.listaCol4h = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4h.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.08)
        self.listaCol4h.insert(END, 0)
        self.labelCol4h = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4h.place(relx=0.71, rely=0.71, relwidth=0.02, relheight=0.06)

        ####  Descricao do item Col2
        self.listaCol2h = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2h.place(relx=0.14, rely=0.7, relwidth=0.53, relheight=0.08)

        ###### Coluna Total Unitario
        self.listaCol5h = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5h.place(relx=0.86, rely=0.7, relwidth=0.1, relheight=0.08)
        self.listaCol5h.insert(END, 0)

        ### Widgets - Listar item 9 ###

        ### Codigo do Item
        self.codServ9 = Entry(self.frame_aba2, width=6, bd=1, justify='center', fg=self.fg_entry,
                              validatecommand=self.vcmd6,
                              validate="key", bg=self.bg_entry,
                              font=('Verdana', '8', 'bold'))
        self.codServ9.place(relx=0.016, rely=0.78, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos9 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico9)
        self.botaoAddServicos9.place(relx=0.078, rely=0.78, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos9F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="9-",
                                        font=('Verdana', '8', 'bold'), fg = self.fg_label)
        self.botaoAddServicos9F.place(relx=0.12, rely=0.78, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3i = Entry(self.frame_aba2, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3i.place(relx=0.8, rely=0.78, relwidth=0.1, relheight=0.08)
        self.listaCol3i.insert(END, 1)

        #### Botao Busca Item
        self.botaoBuscaSP9 = Button(self.frame_aba2, bg=self.bg_label, bd=0, image=self.lupaBt,
                                    font=('Verdana', '10', 'bold'),
                                    command=self.busca_servico9)
        self.botaoBuscaSP9.place(relx=0.67, rely=0.78, relwidth=0.03, relheight=0.08)

        #### Coluna Valor
        self.listaCol4i = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4i.place(relx=0.7, rely=0.78, relwidth=0.1, relheight=0.08)
        self.listaCol4i.insert(END, 0)
        self.labelCol4i = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4i.place(relx=0.71, rely=0.79, relwidth=0.02, relheight=0.06)

        ####  Descricao do item Col2
        self.listaCol2i = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2i.place(relx=0.14, rely=0.78, relwidth=0.53, relheight=0.08)

        ###### Coluna Total Unitario
        self.listaCol5i = Entry(self.frame_aba2, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5i.place(relx=0.86, rely=0.78, relwidth=0.1, relheight=0.08)
        self.listaCol5i.insert(END, 0)

        ### Widgets - Listar item 10 ###

        ### Codigo do Item
        self.codServ10 = Entry(self.frame_aba2, width=6, bd=1, justify='center', validatecommand=self.vcmd6,
                               validate="key",
                               fg=self.fg_entry, bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.codServ10.place(relx=0.016, rely=0.86, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos10 = Button(self.frame_aba2, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico10)
        self.botaoAddServicos10.place(relx=0.078, rely=0.86, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos10F = Label(self.frame_aba2, bd=0, bg=self.bg_label, text="10-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos10F.place(relx=0.12, rely=0.86, relwidth=0.02, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3j = Entry(self.frame_aba2, width=5, bd=1, justify='center', validate="key",
                                bg=self.bg_entry, fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3j.place(relx=0.8, rely=0.86, relwidth=0.1, relheight=0.08)
        self.listaCol3j.insert(END, 1)

        #### Botao Busca Item
        self.botaoBuscaSP10 = Button(self.frame_aba2, bg=self.bg_label, bd=0, image=self.lupaBt,
                                     font=('Verdana', '10', 'bold'),
                                     command=self.busca_servico10)
        self.botaoBuscaSP10.place(relx=0.67, rely=0.86, relwidth=0.03, relheight=0.08)

        #### Coluna Valor
        self.listaCol4j = Entry(self.frame_aba2, width=10, bd=1, justify='right', validate="key",
                                bg=self.bg_entry, fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4j.place(relx=0.7, rely=0.86, relwidth=0.1, relheight=0.08)
        self.listaCol4j.insert(END, 0)
        ### Widgets - Listar item 10 ###

        self.labelCol4j = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4j.place(relx=0.71, rely=0.87, relwidth=0.02, relheight=0.06)

        ####  Descricao do item Col2
        self.listaCol2j = Entry(self.frame_aba2, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2j.place(relx=0.14, rely=0.86, relwidth=0.53, relheight=0.08)

        ###### Coluna Total Unitario
        self.listaCol5j = Entry(self.frame_aba2, width=10, bd=1, justify='right', validate="key",
                                bg=self.bg_entry, fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5j.place(relx=0.86, rely=0.86, relwidth=0.1, relheight=0.08)
        self.listaCol5j.insert(END, 0)
    def aba3(self):
        ### Cabeçalho dos itens_orc 11 A 20
        self.frameItens = Frame(self.frame_aba3, bd=4, bg=self.bg_button)
        self.frameItens.place(relx=0.005, rely=0.01, relwidth=0.98, relheight=0.98)
        self.frameSP = Frame(self.frame_aba3, bg=self.bg_label, bd=4, relief=SUNKEN)
        self.frameSP.place(relx=0.01, rely=0.03, relwidth=0.96, relheight=0.96)
        #### Label codigo
        self.descrCodI = Label(self.frame_aba3, bg=self.bg_button, fg= self.fg_label, text= self.m_Codigo +
                                self.m_barra +  self.m_Item,  font=('Verdana', '10', 'bold'))
        self.descrCodI.place(relx=0.016, rely=0.05, relwidth=0.12, relheight=0.09)
        ###### Label Servicos Peças
        self.descrCol2 = Label(self.frame_aba3, bg= self.fg_label, text= self.m_Serviços + self.m_barra +
                                self.m_Produtos, justify='center', fg= self.bg_label, font=('Verdana', '10', 'bold'))
        self.descrCol2.place(relx=0.137, rely=0.05, relwidth=0.55, relheight=0.09)
        ## Label Valor
        self.descrCol3 = Label(self.frame_aba3, text= self.m_ValorUnit, bg=self.bg_label, fg=self.fg_label,
                               font=('Verdana', '10', 'bold'))
        self.descrCol3.place(relx=0.69, rely=0.05, relwidth=0.11, relheight=0.09)
        self.descrQuant = Label(self.frame_aba3, text= self.m_Quant, bg=self.fg_label, fg=self.bg_label,
                                font=('Verdana', '10', 'bold'))
        self.descrQuant.place(relx=0.8, rely=0.05, relwidth=0.06, relheight=0.09)
        self.descrTotalItem = Label(self.frame_aba3, text= self.m_Total + '' + self.m_Item, bg=self.bg_label,
                                    fg= self.fg_label, font=('Verdana', '10', 'bold'))
        self.descrTotalItem.place(relx=0.86, rely=0.05, relwidth=0.1, relheight=0.09)
        ### Widgets - Listar item 11 ###
        ## entry cod
        self.codServ11 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6,
                               validate="key", bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ11.place(relx=0.016, rely=0.14, relwidth=0.06, relheight=0.08)
        ## Botao add
        self.botaoAddServicos11 = Button(self.frame_aba3, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico11)
        self.botaoAddServicos11.place(relx=0.078, rely=0.14, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos11F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="11-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos11F.place(relx=0.12, rely=0.14, relwidth=0.02, relheight=0.08)

        self.listaCol2k = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2k.place(relx=0.14, rely=0.14, relwidth=0.53, relheight=0.08)
        # botao busca item
        self.botaoBuscaSP11 = Button(self.frame_aba3, bd=0, bg=self.bg_label,image=self.lupaBt, font=('Verdana', '10', 'bold'),
                                     command=self.busca_servico11)
        self.botaoBuscaSP11.place(relx=0.67, rely=0.14, relwidth=0.03, relheight=0.08)

        self.listaCol3k = Entry(self.frame_aba3, width=5, bd=1, justify='center', validate="key", bg=self.bg_entry,
                                 fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3k.place(relx=0.8, rely=0.14, relwidth=0.1, relheight=0.08)
        self.listaCol3k.insert(END, 1)

        self.listaCol4k = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4k.place(relx=0.7, rely=0.14, relwidth=0.1, relheight=0.08)
        self.listaCol4k.insert(END, 0)
        ### Widgets - Listar item 11 ###
        self.labelCol4k = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4k.place(relx=0.71, rely=0.15, relwidth=0.02, relheight=0.06)

        self.listaCol5k = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5k.place(relx=0.86, rely=0.14, relwidth=0.1, relheight=0.08)
        self.listaCol5k.insert(END, 0)


        ### Widgets - Listar item 12 ###

        self.codServ12 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6, validate="key", bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ12.place(relx=0.016, rely=0.22, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos12 = Button(self.frame_aba3, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico12)
        self.botaoAddServicos12.place(relx=0.078, rely=0.22, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos12F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="12-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos12F.place(relx=0.12, rely=0.22, relwidth=0.02, relheight=0.08)

        self.listaCol3l = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol3l.place(relx=0.8, rely=0.22, relwidth=0.1, relheight=0.08)
        self.listaCol3l.insert(END, 1)

        self.botaoBuscaSP12 = Button(self.frame_aba3, bd=0, bg=self.bg_label,image=self.lupaBt,
                                     command=self.busca_servico12)
        self.botaoBuscaSP12.place(relx=0.67, rely=0.22, relwidth=0.03, relheight=0.08)

        self.listaCol4l = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol4l.place(relx=0.7, rely=0.22, relwidth=0.1, relheight=0.08)
        self.listaCol4l.insert(END, 0)

        ### Widgets - Listar item 12 ###
        self.labelCol4l = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4l.place(relx=0.71, rely=0.23, relwidth=0.02, relheight=0.06)


        self.listaCol2l = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2l.place(relx=0.14, rely=0.22, relwidth=0.53, relheight=0.08)
        self.listaCol5l = Entry(self.frame_aba3, width=10, bd=1, justify='right', validate="key", bg=self.bg_entry,
                                                                fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5l.place(relx=0.86, rely=0.22, relwidth=0.1, relheight=0.08)
        self.listaCol5l.insert(END, 0)


        ### Widgets - Listar item 13 ###

        self.codServ13 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6,
                               validate="key", bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ13.place(relx=0.016, rely=0.3, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos13 = Button(self.frame_aba3, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico13)
        self.botaoAddServicos13.place(relx=0.078, rely=0.3, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos13F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="13-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos13F.place(relx=0.12, rely=0.3, relwidth=0.02, relheight=0.08)

        self.listaCol3m = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,        font=('Verdana', '8', 'bold'))
        self.listaCol3m.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.08)
        self.listaCol3m.insert(END, 1)

        self.botaoBuscaSP13 = Button(self.frame_aba3, bd=0, bg=self.bg_label,image=self.lupaBt,
                                      command=self.busca_servico13)
        self.botaoBuscaSP13.place(relx=0.67, rely=0.3, relwidth=0.03, relheight=0.08)

        self.listaCol4m = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,               font=('Verdana', '8', 'bold'))
        self.listaCol4m.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.08)
        self.listaCol4m.insert(END, 0)

        ### Widgets - Listar item 13 ###
        self.labelCol4m = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4m.place(relx=0.71, rely=0.31, relwidth=0.02, relheight=0.06)

        self.listaCol2m = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2m.place(relx=0.14, rely=0.3, relwidth=0.53, relheight=0.08)
        self.listaCol5m = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol5m.place(relx=0.86, rely=0.3, relwidth=0.1, relheight=0.08)
        self.listaCol5m.insert(END, 0)

        ### Widgets - Listar item 14 ###

        self.codServ14 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6,
                               validate="key", bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ14.place(relx=0.016, rely=0.38, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos14 = Button(self.frame_aba3, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico14)
        self.botaoAddServicos14.place(relx=0.078, rely=0.38, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos14F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="14-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos14F.place(relx=0.12, rely=0.38, relwidth=0.02, relheight=0.08)

        self.listaCol3n = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol3n.place(relx=0.8, rely=0.38, relwidth=0.1, relheight=0.08)
        self.listaCol3n.insert(END, 1)

        self.botaoBuscaSP14 = Button(self.frame_aba3, bg=self.bg_label, bd=0, image=self.lupaBt,
                                      command=self.busca_servico14)
        self.botaoBuscaSP14.place(relx=0.67, rely=0.38, relwidth=0.03, relheight=0.08)

        self.listaCol4n = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol4n.place(relx=0.7, rely=0.38, relwidth=0.1, relheight=0.08)
        self.listaCol4n.insert(END, 0)

        ### Widgets - Listar item 14 ###
        self.labelCol4n = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4n.place(relx=0.71, rely=0.39, relwidth=0.02, relheight=0.06)


        self.listaCol2n = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2n.place(relx=0.14, rely=0.38, relwidth=0.53, relheight=0.08)
        self.listaCol5n = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol5n.place(relx=0.86, rely=0.38, relwidth=0.1, relheight=0.08)
        self.listaCol5n.insert(END, 0)


        ### Widgets - Listar item 15 ###

        self.codServ15 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6, bg=self.bg_entry,
                               validate="key",
                               font=('Verdana', '8', 'bold'))
        self.codServ15.place(relx=0.016, rely=0.46, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos15 = Button(self.frame_aba3, bg=self.bg_label,bd=0, image=self.add, command=self.add_servico15)
        self.botaoAddServicos15.place(relx=0.078, rely=0.46, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos15F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="15-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos15F.place(relx=0.12, rely=0.46, relwidth=0.02, relheight=0.08)

        self.listaCol3o = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol3o.place(relx=0.8, rely=0.46, relwidth=0.1, relheight=0.08)
        self.listaCol3o.insert(END, 1)

        self.botaoBuscaSP15 = Button(self.frame_aba3, bg=self.bg_label,bd=0, image=self.lupaBt,
                                      command=self.busca_servico15)
        self.botaoBuscaSP15.place(relx=0.67, rely=0.46, relwidth=0.03, relheight=0.08)

        self.listaCol4o = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4o.place(relx=0.7, rely=0.46, relwidth=0.1, relheight=0.08)
        self.listaCol4o.insert(END, 0)

        ### Widgets - Listar item 15 ###
        self.labelCol4o = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4o.place(relx=0.71, rely=0.47, relwidth=0.02, relheight=0.06)


        self.listaCol2o = Entry(self.frame_aba3, width=60, bd=1, bg=self.bg_entry, fg=self.fg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2o.place(relx=0.14, rely=0.46, relwidth=0.53, relheight=0.08)
        self.listaCol5o = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5o.place(relx=0.86, rely=0.46, relwidth=0.1, relheight=0.08)
        self.listaCol5o.insert(END, 0)


        ### Widgets - Listar item 16 ###

        self.codServ16 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6,
                               validate="key", bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ16.place(relx=0.016, rely=0.54, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos16 = Button(self.frame_aba3, bg=self.bg_label,bd=0, image=self.add, command=self.add_servico16)
        self.botaoAddServicos16.place(relx=0.078, rely=0.54, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos16F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="16-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos16F.place(relx=0.12, rely=0.54, relwidth=0.02, relheight=0.08)

        self.listaCol3p = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol3p.place(relx=0.8, rely=0.54, relwidth=0.1, relheight=0.08)
        self.listaCol3p.insert(END, 1)

        self.botaoBuscaSP16 = Button(self.frame_aba3, bg=self.bg_label, bd=0, image=self.lupaBt,
                                      command=self.busca_servico16)
        self.botaoBuscaSP16.place(relx=0.67, rely=0.54, relwidth=0.03, relheight=0.08)

        self.listaCol4p = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,     font=('Verdana', '8', 'bold'))
        self.listaCol4p.place(relx=0.7, rely=0.54, relwidth=0.1, relheight=0.08)
        self.listaCol4p.insert(END, 0)

        ### Widgets - Listar item 16 ###
        self.labelCol4p = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4p.place(relx=0.71, rely=0.55, relwidth=0.02, relheight=0.06)


        self.listaCol2p = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2p.place(relx=0.14, rely=0.54, relwidth=0.53, relheight=0.08)
        self.listaCol5p = Entry(self.frame_aba3, width=10, bd=1, justify='right', validate="key", bg=self.bg_entry,
                                        fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5p.place(relx=0.86, rely=0.54, relwidth=0.1, relheight=0.08)
        self.listaCol5p.insert(END, 0)


        ### Widgets - Listar item 17 ###

        self.codServ17 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6, bg=self.bg_entry,
                               validate="key",
                               font=('Verdana', '8', 'bold'))
        self.codServ17.place(relx=0.016, rely=0.62, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos17 = Button(self.frame_aba3, bg=self.bg_label,bd=0, image=self.add, command=self.add_servico17)
        self.botaoAddServicos17.place(relx=0.078, rely=0.62, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos17F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="17-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos17F.place(relx=0.12, rely=0.62, relwidth=0.02, relheight=0.08)

        self.listaCol3q = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol3q.place(relx=0.8, rely=0.62, relwidth=0.1, relheight=0.08)
        self.listaCol3q.insert(END, 1)

        self.botaoBuscaSP17 = Button(self.frame_aba3, bg=self.bg_label, bd=0, image=self.lupaBt,
                                      command=self.busca_servico17)
        self.botaoBuscaSP17.place(relx=0.67, rely=0.62, relwidth=0.03, relheight=0.08)

        self.listaCol4q = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol4q.place(relx=0.7, rely=0.62, relwidth=0.1, relheight=0.08)
        self.listaCol4q.insert(END, 0)

        ### Widgets - Listar item 17 ###
        self.labelCol4q = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4q.place(relx=0.71, rely=0.63, relwidth=0.02, relheight=0.06)

        self.listaCol2q = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2q.place(relx=0.14, rely=0.62, relwidth=0.53, relheight=0.08)
        self.listaCol5q = Entry(self.frame_aba3, width=10, bd=1, justify='right', bg=self.bg_entry, fg=self.fg_entry,
                                validate="key",
                                font=('Verdana', '8', 'bold'))
        self.listaCol5q.place(relx=0.86, rely=0.62, relwidth=0.1, relheight=0.08)
        self.listaCol5q.insert(END, 0)

        ### Widgets - Listar item 18 ###

        self.codServ18 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6, bg=self.bg_entry,
                               validate="key",
                               font=('Verdana', '8', 'bold'))
        self.codServ18.place(relx=0.016, rely=0.7, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos18 = Button(self.frame_aba3, bg=self.bg_label,bd=0, image=self.add, command=self.add_servico18)
        self.botaoAddServicos18.place(relx=0.078, rely=0.7, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos18F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="18-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos18F.place(relx=0.12, rely=0.7, relwidth=0.02, relheight=0.08)

        self.listaCol3r = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol3r.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.08)
        self.listaCol3r.insert(END, 1)

        self.botaoBuscaSP18 = Button(self.frame_aba3, bg=self.bg_label, bd=0, image=self.lupaBt,
                                      command=self.busca_servico18)
        self.botaoBuscaSP18.place(relx=0.67, rely=0.7, relwidth=0.03, relheight=0.08)

        self.listaCol4r = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol4r.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.08)
        self.listaCol4r.insert(END, 0)

        ### Widgets - Listar item 18 ###
        self.labelCol4r = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4r.place(relx=0.71, rely=0.71, relwidth=0.02, relheight=0.06)


        self.listaCol2r = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2r.place(relx=0.14, rely=0.7, relwidth=0.53, relheight=0.08)
        self.listaCol5r = Entry(self.frame_aba3, width=10, bg=self.bg_entry, bd=1, justify='right', fg=self.fg_entry,
                                validate="key",
                                font=('Verdana', '8', 'bold'))
        self.listaCol5r.place(relx=0.86, rely=0.7, relwidth=0.1, relheight=0.08)
        self.listaCol5r.insert(END, 0)


        ### Widgets - Listar item 19 ###

        self.codServ19 = Entry(self.frame_aba3, width=6, bd=1, justify='center', fg=self.fg_entry,
                               validatecommand=self.vcmd6,
                               validate="key", bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ19.place(relx=0.016, rely=0.78, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos19 = Button(self.frame_aba3, bg=self.bg_label,bd=0, image=self.add, command=self.add_servico19)
        self.botaoAddServicos19.place(relx=0.078, rely=0.78, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos19F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="19-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos19F.place(relx=0.12, rely=0.78, relwidth=0.02, relheight=0.08)

        self.listaCol3s = Entry(self.frame_aba3, width=5, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol3s.place(relx=0.8, rely=0.78, relwidth=0.1, relheight=0.08)
        self.listaCol3s.insert(END, 1)

        self.botaoBuscaSP19 = Button(self.frame_aba3, bg=self.bg_label,bd=0, image=self.lupaBt,
                                      command=self.busca_servico19)
        self.botaoBuscaSP19.place(relx=0.67, rely=0.78, relwidth=0.03, relheight=0.08)

        self.listaCol4s = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol4s.place(relx=0.7, rely=0.78, relwidth=0.1, relheight=0.08)
        self.listaCol4s.insert(END, 0)

        ### Widgets - Listar item 19 ###
        self.labelCol4s = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4s.place(relx=0.71, rely=0.79, relwidth=0.02, relheight=0.06)

        self.listaCol2s = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2s.place(relx=0.14, rely=0.78, relwidth=0.53, relheight=0.08)
        self.listaCol5s = Entry(self.frame_aba3, width=10, bd=1, justify='right', fg=self.fg_entry, validate="key",
                                bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol5s.place(relx=0.86, rely=0.78, relwidth=0.1, relheight=0.08)
        self.listaCol5s.insert(END, 0)


        ### Widgets - Listar item 20 ###

        self.codServ20 = Entry(self.frame_aba3, width=6, bd=1, justify='center', validatecommand=self.vcmd6,
                               validate="key",
                               fg=self.fg_entry, bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.codServ20.place(relx=0.016, rely=0.86, relwidth=0.06, relheight=0.08)
        self.botaoAddServicos20 = Button(self.frame_aba3, bg=self.bg_label, bd=0, image=self.add, command=self.add_servico20)
        self.botaoAddServicos20.place(relx=0.078, rely=0.86, relwidth=0.04, relheight=0.08)

        self.botaoAddServicos20F = Label(self.frame_aba3, bd=0, bg=self.bg_label, text="20-",
                                         font=('Verdana', '7', 'bold'), fg = self.fg_label)
        self.botaoAddServicos20F.place(relx=0.12, rely=0.86, relwidth=0.02, relheight=0.08)

        self.listaCol3t = Entry(self.frame_aba3, width=5, bd=1, justify='center', validate="key", bg=self.bg_entry,
                                        fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3t.place(relx=0.8, rely=0.86, relwidth=0.1, relheight=0.08)
        self.listaCol3t.insert(END, 1)

        self.botaoBuscaSP20 = Button(self.frame_aba3, bg=self.bg_label, bd=0, image=self.lupaBt,
                                      command=self.busca_servico20)
        self.botaoBuscaSP20.place(relx=0.67, rely=0.86, relwidth=0.03, relheight=0.08)

        self.listaCol4t = Entry(self.frame_aba3, width=10, bd=1, justify='right', validate="key", bg=self.bg_entry,
                                          fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol4t.place(relx=0.7, rely=0.86, relwidth=0.1, relheight=0.08)
        self.listaCol4t.insert(END, 0)

        ### Widgets - Listar item 20 ###

        self.labelCol4t = Label(self.frame_aba3, text=self.m_Reais, fg=self.fg_entry, bd=0, bg=self.bg_entry,
                                font=('Verdana', '6', 'bold'))
        self.labelCol4t.place(relx=0.71, rely=0.87, relwidth=0.02, relheight=0.06)

        self.listaCol2t = Entry(self.frame_aba3, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listaCol2t.place(relx=0.14, rely=0.86, relwidth=0.53, relheight=0.08)
        self.listaCol5t = Entry(self.frame_aba3, width=10, bd=1, justify='right', validate="key", bg=self.bg_entry,
                                      fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol5t.place(relx=0.86, rely=0.86, relwidth=0.1, relheight=0.08)
        self.listaCol5t.insert(END, 0)
    def aba4(self):
        #####################
        ###Frames da moldura
        self.frameProb = Frame(self.frame_aba4, width=790, height=228, bd=4, bg=self.bg_button)
        self.frameProb.place(relx=0.015, rely=0.03, relwidth=0.97, relheight=0.94)

        self.frameProb = Frame(self.frame_aba4, width=780, height=218, bd=4, bg=self.bg_label, relief=SUNKEN)
        self.frameProb.place(relx=0.017, rely=0.035, relwidth=0.965, relheight=0.935)
        ###########################
        ### Tanque de combustivel
        descrTanq = Label(self.frame_aba4, bd=2, width=22, text= self.m_Tanque, bg= self.bg_button,
                          fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrTanq.place(relx=0.05, rely=0.1, relwidth=0.18, relheight=0.1)
        self.are1 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry, bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are1.place(relx=0.23, rely=0.1, relwidth=0.18, relheight=0.1)
        ##################
        #### Odometro
        descrOdom = Label(self.frame_aba4, width=22, bd=2, text= self.m_Odometro, bg= self.bg_button,
                          fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrOdom.place(relx=0.05, rely=0.22, relwidth=0.18, relheight=0.1)
        self.are2 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are2.place(relx=0.23, rely=0.22, relwidth=0.18, relheight=0.1)
        ############################
        ###  Radio Kit Multimidia
        descrRad = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                         fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrRad.place(relx=0.05, rely=0.34, relwidth=0.18, relheight=0.1)
        self.are3 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are3.place(relx=0.23, rely=0.34, relwidth=0.18, relheight=0.1)
        ###################
        ####   Calotas
        descrCalot = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                           fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrCalot.place(relx=0.05, rely=0.46, relwidth=0.18, relheight=0.1)
        self.are4 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are4.place(relx=0.23, rely=0.46, relwidth=0.18, relheight=0.1)
        ###################
        ####  Triangulo
        descrtri = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                         fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrtri.place(relx=0.05, rely=0.58, relwidth=0.18, relheight=0.1)
        self.are5 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are5.place(relx=0.23, rely=0.58, relwidth=0.18, relheight=0.1)
        ################
        ###   Macaco
        descrMacaco = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                            fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrMacaco.place(relx=0.05, rely=0.7, relwidth=0.18, relheight=0.1)
        self.are6 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are6.place(relx=0.23, rely=0.7, relwidth=0.18, relheight=0.1)
        #################
        ####   Estepe
        descrEst = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs, bg= self.bg_button,
                         fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrEst.place(relx=0.05, rely=0.82, relwidth=0.18, relheight=0.1)
        self.are7 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are7.place(relx=0.23, rely=0.82, relwidth=0.18, relheight=0.1)
        #################
        ####   Are 8
        descrAre8 = Label(self.frame_aba4, bd=2, width=10, text= self.m_Obs, bg= self.bg_button,
                          fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrAre8.place(relx=0.55, rely=0.1, relwidth=0.18, relheight=0.1)
        self.are8 = Entry(self.frame_aba4, bd=1, width=25, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are8.place(relx=0.73, rely=0.1, relwidth=0.18, relheight=0.1)
        #################
        ####   Are 9
        descrAre9 = Label(self.frame_aba4, bd=2, width=10, text= self.m_Obs, bg= self.bg_button,
                          fg=self.fg_label, font=('Verdana', '8', 'bold'))
        descrAre9.place(relx=0.55, rely=0.22, relwidth=0.18, relheight=0.1)
        self.are9 = Entry(self.frame_aba4, bd=1, width=25, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are9.place(relx=0.73, rely=0.22, relwidth=0.18, relheight=0.1)

        # Gerar PDF

        vistlabel = Label(self.frame_aba4, bd=2, text= self.m_ImprimirVistoria, bg= self.bg_button,
                          fg=self.fg_label, font=('Verdana', '8', 'bold'))
        vistlabel.place(relx=0.64, rely=0.6, relwidth=0.2, relheight=0.2)
        ###  Botao botaoImprimirVist
        self.botaoImprimirVist = Button(self.frame_aba4, image=self.button_imprime2, compound=LEFT, bd=0,
                                        bg = self.bg_button, command=self.imprime_vist)
        self.botaoImprimirVist.place(relx=0.69, rely=0.43, relwidth=0.1, relheight=0.2)
    def aba5(self):
        #####################################################################
        ### Cabeçalho dos itens_orc 1 A 10 - Aba 5
        self.frameItensF = Frame(self.frame_aba5, bd=2, bg=self.bg_button)
        self.frameItensF.place(relx=0.015, rely=0.015, relwidth=0.97, relheight=0.96)

        self.frameItensF = Frame(self.frame_aba5, bd=2, bg= self.fundo_do_frame,relief=SUNKEN)
        self.frameItensF.place(relx=0.02, rely=0.02, relwidth=0.93, relheight=0.93)
        #### Label codigo
        self.descrCodIF=Label(self.frame_aba5,bg=self.bg_button,text=self.m_Codigo+self.m_barra+self.m_Item,
                                font=('Verdana', '9', 'bold'), fg = self.fg_label)
        self.descrCodIF.place(relx=0.026, rely=0.028, relwidth=0.11, relheight=0.09)
        ###### Label Servicos Peças
        self.descrCol2F = Label(self.frame_aba5, bg=self.fg_label,fg= self.bg_label, text = self.m_DescricaoFalha,
                                font=('Verdana', '12', 'bold'))
        self.descrCol2F.place(relx=0.138, rely=0.028, relwidth=0.45, relheight=0.09)
        self.descrCol2F = Label(self.frame_aba5, bg=self.bg_label, fg= self.fg_label, text= self.m_Observacoes,
                                font=('Verdana', '12', 'bold'))
        self.descrCol2F.place(relx=0.65, rely=0.028, relwidth=0.3, relheight=0.09)
        ###############################
        ### Widgets - Listar item 1 ###
        ### Codigo do Item
        self.codServ1F = Entry(self.frame_aba5, validate="key", width=6, bg=self.bg_entry, bd=1, justify='center',
                               fg=self.fg_entry , font=('Verdana', '8', 'bold'))
        self.codServ1F.place(relx=0.026, rely=0.12, relwidth=0.055, relheight=0.08)

        self.botaoAddServicos1F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico1F)
        self.botaoAddServicos1F.place(relx=0.08, rely=0.12, relwidth=0.055, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2aF = Entry(self.frame_aba5, width=60, bd=1, bg=self.bg_entry, fg=self.fg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2aF.place(relx=0.14, rely=0.12, relwidth=0.45, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP1F = Button(self.frame_aba5, bd=0, bg=self.bg_label,
                                     image=self.lupaBt, font=('Verdana', '10', 'bold'),command=self.busca_servico1F)
        self.botaoBuscaSP1F.place(relx=0.59, rely=0.12, relwidth=0.05, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3aF = Entry(self.frame_aba5, width=25, validate="key", bd=1, bg=self.bg_entry,
                                 justify='center', fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3aF.place(relx=0.64, rely=0.12, relwidth=0.3, relheight=0.08)

        ###############################
        ### Widgets - Listar item 2 ###
        ###############################
        ### Codigo do Item
        self.codServ2F = Entry(self.frame_aba5, validate="key", width=6, bd=1, justify='center', fg=self.fg_entry,
                               bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ2F.place(relx=0.026, rely=0.2, relwidth=0.055, relheight=0.08)
        self.botaoAddServicos2F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico2F)
        self.botaoAddServicos2F.place(relx=0.08, rely=0.2, relwidth=0.055, relheight=0.08)
        #### Coluna Quantidade
        self.listaCol3bF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3bF.place(relx=0.64, rely=0.2, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP2F = Button(self.frame_aba5, bd=0, bg=self.bg_label, image=self.lupaBt, command=self.busca_servico2F)
        self.botaoBuscaSP2F.place(relx=0.59, rely=0.2, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2bF = Entry(self.frame_aba5, width=60, bd=1, bg=self.bg_entry, fg=self.fg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2bF.place(relx=0.14, rely=0.2, relwidth=0.45, relheight=0.08)

        ###############################
        ### Widgets - Listar item 3 ###
        ###############################
        ''' Codigo do Item '''
        self.codServ3F = Entry(self.frame_aba5, width=6, bd=1, justify='center', validate="key", fg=self.fg_entry,
                               bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ3F.place(relx=0.026, rely=0.28, relwidth=0.055, relheight=0.08)
        self.botaoAddServicos3F = Button(self.frame_aba5, bg=self.bg_label,bd=0, image=self.add, command=self.add_servico3F)
        self.botaoAddServicos3F.place(relx=0.08, rely=0.28, relwidth=0.055, relheight=0.08)
        ''' Coluna Quantidade '''
        self.listaCol3cF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3cF.place(relx=0.64, rely=0.28, relwidth=0.3, relheight=0.08)

        ''' Botao Busca Item '''
        self.botaoBuscaSP3F = Button(self.frame_aba5, bg=self.bg_label, bd=0, image=self.lupaBt,
                                     command=self.busca_servico3F)
        self.botaoBuscaSP3F.place(relx=0.59, rely=0.28, relwidth=0.05, relheight=0.08)

        '''  Descricao do item Col2 '''
        self.listaCol2cF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2cF.place(relx=0.14, rely=0.28, relwidth=0.45, relheight=0.08)

        ###############################
        ### Widgets - Listar item 4 ###
        ###############################

        ### Codigo do Item
        self.codServ4F = Entry(self.frame_aba5, width=6, bd=1, bg=self.bg_entry, justify='center',
                               font=('Verdana', '8', 'bold'))
        self.codServ4F.configure(fg=self.fg_entry, validate="key")
        self.codServ4F.place(relx=0.026, rely=0.36, relwidth=0.055, relheight=0.08)

        self.botaoAddServicos4F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico4F)
        self.botaoAddServicos4F.place(relx=0.08, rely=0.36, relwidth=0.055, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3dF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3dF.place(relx=0.64, rely=0.36, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP4F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.lupaBt, command=self.busca_servico4F)
        self.botaoBuscaSP4F.place(relx=0.59, rely=0.36, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2dF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2dF.place(relx=0.14, rely=0.36, relwidth=0.45, relheight=0.08)

        ###############################
        ### Widgets - Listar item 5 ###
        ###############################

        ### Codigo do Item
        self.codServ5F = Entry(self.frame_aba5, width=6, bd=1, justify='center', fg=self.fg_entry, validate="key",
                               bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ5F.place(relx=0.026, rely=0.44, relwidth=0.055, relheight=0.08)
        self.botaoAddServicos3F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico5F)
        self.botaoAddServicos3F.place(relx=0.08, rely=0.44, relwidth=0.055, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3eF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3eF.place(relx=0.64, rely=0.44, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP5F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.lupaBt,
                                     command=self.busca_servico5F)
        self.botaoBuscaSP5F.place(relx=0.59, rely=0.44, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2eF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2eF.place(relx=0.14, rely=0.44, relwidth=0.45, relheight=0.08)

        ###############################
        ### Widgets - Listar item 6 ###
        ###############################

        ### Codigo do Item
        self.codServ6F = Entry(self.frame_aba5, width=6, bd=1, justify='center', fg=self.fg_entry, validate="key",
                               bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ6F.place(relx=0.026, rely=0.52, relwidth=0.055, relheight=0.08)
        self.botaoAddServicos6F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico6F)
        self.botaoAddServicos6F.place(relx=0.08, rely=0.52, relwidth=0.055, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3fF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3fF.place(relx=0.64, rely=0.52, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP6F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.lupaBt,
                                     command=self.busca_servico6F)
        self.botaoBuscaSP6F.place(relx=0.59, rely=0.52, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2fF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2fF.place(relx=0.14, rely=0.52, relwidth=0.45, relheight=0.08)

        ###############################
        ### Widgets - Listar item 7 ###
        ###############################

        ### Codigo do Item
        self.codServ7F = Entry(self.frame_aba5, width=6, bd=1, bg=self.bg_entry, justify='center', fg=self.fg_entry,
                               validate="key", font=('Verdana', '8', 'bold'))
        self.codServ7F.place(relx=0.026, rely=0.6, relwidth=0.055, relheight=0.08)
        self.botaoAddServicos7F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico7F)
        self.botaoAddServicos7F.place(relx=0.08, rely=0.6, relwidth=0.055, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3gF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3gF.place(relx=0.64, rely=0.6, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP7F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.lupaBt,
                                     command=self.busca_servico7F)
        self.botaoBuscaSP7F.place(relx=0.59, rely=0.6, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2gF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2gF.place(relx=0.14, rely=0.6, relwidth=0.45, relheight=0.08)

        ###############################
        ### Widgets - Listar item 8 ###
        ###############################

        ### Codigo do Item
        self.codServ8F = Entry(self.frame_aba5, width=6, bd=1, justify='center', fg=self.fg_entry, validate="key",
                               bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ8F.place(relx=0.026, rely=0.68, relwidth=0.055, relheight=0.08)
        self.botaoAddServicos8F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico8F)
        self.botaoAddServicos8F.place(relx=0.08, rely=0.68, relwidth=0.055, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3hF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3hF.place(relx=0.64, rely=0.68, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP8F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.lupaBt,
                                     command=self.busca_servico8F)
        self.botaoBuscaSP8F.place(relx=0.59, rely=0.68, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2hF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2hF.place(relx=0.14, rely=0.68, relwidth=0.45, relheight=0.08)

        ### Widgets - Listar item 9 ###

        ### Codigo do Item
        self.codServ9F = Entry(self.frame_aba5, width=6, bd=1, justify='center', fg=self.fg_entry, validate="key",
                               bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'))
        self.codServ9F.place(relx=0.026, rely=0.76, relwidth=0.055, relheight=0.08)
        self.botaoAddServicos9F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico9F)
        self.botaoAddServicos9F.place(relx=0.08, rely=0.76, relwidth=0.055, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3iF = Entry(self.frame_aba5, width=25, bd=1, justify='center', fg=self.fg_entry, validate="key",
                                 bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol3iF.place(relx=0.64, rely=0.76, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP9F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.lupaBt,
                                     command=self.busca_servico9F)
        self.botaoBuscaSP9F.place(relx=0.59, rely=0.76, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2iF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2iF.place(relx=0.14, rely=0.76, relwidth=0.45, relheight=0.08)

        ### Widgets - Listar item 10 ###

        ### Codigo do Item
        self.codServ10F = Entry(self.frame_aba5, width=6, bd=1, justify='center', bg=self.bg_entry,
                                validate="key", fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.codServ10F.place(relx=0.026, rely=0.84, relwidth=0.055, relheight=0.08)

        self.botaoAddF10 = Button(self.frame_aba5, bg=self.bg_label,bd=0, image=self.add, command=self.add_servico10F)
        self.botaoAddF10.place(relx=0.08, rely=0.84, relwidth=0.055, relheight=0.08)

        #### Coluna Quantidade
        self.listaCol3jF = Entry(self.frame_aba5, width=25, bd=1, justify='center', bg=self.bg_entry, validate="key",
                                 fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3jF.place(relx=0.64, rely=0.84, relwidth=0.3, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP10F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.lupaBt,
                                      command=self.busca_servico10F)
        self.botaoBuscaSP10F.place(relx=0.59, rely=0.84, relwidth=0.05, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2jF = Entry(self.frame_aba5, width=60, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2jF.place(relx=0.14, rely=0.84, relwidth=0.45, relheight=0.08)

    def Menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)
        filemenu4 = Menu(menubar)
        filemenu5 = Menu(menubar)

        def Quit(): self.janela.destroy()
        def Help():
            msg = self.m_Ajuda
            msg += ""
            messagebox.showinfo("GLAC ", msg)
        def Sobre():
            msg = "GlacX -        rafaelserafim.rfzorzi@gmail.com                \n "
            msg += "RfZorzi - https://www.facebook.com/rfzorzi/ - Brazil"
            messagebox.showinfo("GLAC ", msg)

        menubar.add_cascade(label= self.m_Cadastros, menu=filemenu)
        menubar.add_cascade(label= self.m_Consulta, menu=filemenu2)
        menubar.add_cascade(label= self.m_Relatorios, menu=filemenu3)
        menubar.add_cascade(label= self.m_Procedimentos, menu=filemenu4)
        menubar.add_cascade(label= self.m_Ajuda, menu=filemenu5)

        filemenu.add_command(label= self.m_Automoveis, command= self.cadaut)
        filemenu.add_command(label= self.m_Clientes, command= self.cadcli)
        filemenu.add_command(label= self.m_Fornecedores, command= self.cadforn)
        filemenu.add_command(label= self.m_Produtos, command= self.cadprod)
        filemenu.add_command(label= self.m_Marca + self.m_Produtos, command= self.cadmarcaprod)
        filemenu.add_command(label= self.m_Serviços, command= self.cadserv)
        filemenu.add_command(label= self.m_Tecnico, command= self.cadtec)
        filemenu.add_command(label= self.m_Estab, command= self.cademp)
        filemenu.add_command(label= self.m_Copia, command= self.backup)
        filemenu.add_command(label= self.m_Sair, command=Quit)

        filemenu2.add_command(label= self.m_Cons_Rec, command= self.cadfinan)
        filemenu2.add_command(label= self.m_Cons_Pag, command= self.consultapag)

        filemenu3.add_command(label= self.m_Orcamento, command=self.PrintOrc)
        filemenu3.add_command(label= self.m_ImprimirVistoria, command=self.PrintVist)

        filemenu4.add_command(label= self.m_Proced_Lanc, command= self.cadest)
        filemenu4.add_command(label= self.m_Proced_Atual, command= self.procedServ)

        filemenu5.add_command(label= self.m_Sobre, command=Sobre)

MeuOrc()