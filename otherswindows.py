from objects_glac import *


class OthersWindows(Objects_Glac):
    def cadcli(self):
        def abreJanela():
            self.janelaCli = Toplevel()
            self.janelaCli.title(self.m_Cadastro +
                                 ' ' + self.m_de +
                                 ' ' + self.m_Clientes)
            self.janelaCli.configure(background=self.fundo_do_frame)
            self.janelaCli.focus_force()
            self.janelaCli.geometry("800x600")
            self.janelaCli.resizable(TRUE, TRUE)
            self.janelaCli.minsize(width=780, height=450)
        def molduras():
            top2 = Canvas(self.janelaCli,
                          bd=0,
                          bg=self.fg_label,
                          highlightbackground=self.borda_frame,
                          highlightthickness=3)
            top2.place(relx=0,
                       rely=0,
                       relwidth=0.0165,
                       relheight=1)
            top3 = Canvas(self.janelaCli,
                          bd=0,
                          bg=self.fg_label,
                          highlightbackground=self.borda_frame,
                          highlightthickness=3)
            top3.place(relx=0,
                       rely=0,
                       relwidth=1,
                       relheight=0.1)
            top4 = Canvas(self.janelaCli,
                          bd=0,
                          bg=self.fg_label,
                          highlightbackground=self.borda_frame,
                          highlightthickness=3)
            top4.place(relx=0,
                       rely=0.98,
                       relwidth=1,
                       relheight=0.02)
            top5 = Canvas(self.janelaCli,
                          bd=0,
                          bg=self.fg_label,
                          highlightbackground=self.borda_frame,
                          highlightthickness=3)
            top5.place(relx=0.98,
                       rely=0.095,
                       relwidth=0.02,
                       relheight=0.905)
            top6 = Canvas(self.janelaCli,
                          bd=0,
                          bg=self.fg_label,
                          highlightbackground=self.borda_frame,
                          highlightthickness=3)
            top6.place(relx=0.016,
                       rely=0.5,
                       relwidth=0.967,
                       relheight=0.04)
            top7 = Canvas(self.janelaCli,
                          bd=0,
                          bg=self.fg_label,
                          highlightbackground=self.borda_frame,
                          highlightthickness=3)
            top7.place(relx=0.48,
                       rely=0.095,
                       relwidth=0.02,
                       relheight=0.41)

            top2l = Label(self.janelaCli,
                          bd=0,
                          bg=self.fg_label)
            top2l.place(relx=0.002,
                        rely=0.01,
                        relwidth=0.012,
                        relheight=0.98)
            top4l = Label(self.janelaCli,
                          bd=0,
                          bg=self.fg_label)
            top4l.place(relx=0.002,
                        rely=0.982,
                        relwidth=0.985,
                        relheight=0.016)
            top5l = Label(self.janelaCli,
                          bd=0,
                          bg=self.fg_label)
            top5l.place(relx=0.982,
                        rely=0.0945,
                        relwidth=0.017,
                        relheight=0.905)
            top6l = Label(self.janelaCli,
                          bd=0,
                          bg=self.fg_label)
            top6l.place(relx=0.014,
                        rely=0.503,
                        relwidth=0.985,
                        relheight=0.033)
            top7l = Label(self.janelaCli,
                          bd=0,
                          bg=self.fg_label)
            top7l.place(relx=0.482,
                        rely=0.094,
                        relwidth=0.017,
                        relheight=0.43)

        def tituloCadCli():
            labelTitulo = Label(self.janelaCli,
                                text=self.m_Clientes,
                                bg=self.fundo_do_frame,
                                fg='gray45',
                                font=('Verdana', '12', 'bold'))
            labelTitulo.place(relx=0.016,
                              rely=0.066,
                              relwidth=0.2,
                              relheight=0.03)

        def caixaClientes():
            #         MOLDURA CLIENTE
            # Label e entry Codigo
            self.codPeLabel.place(relx=0.02,
                                  rely=0.102,
                                  relwidth=0.06,
                                  relheight=0.02)
            self.codPeEntry.place(relx=0.02,
                                  rely=0.122,
                                  relwidth=0.05,
                                  relheight=0.026)
            # Label e entry Nome
            self.nomePeLabel.place(relx=0.02,
                                   rely=0.15,
                                   relwidth=0.06,
                                   relheight=0.02)
            self.nomePeEntry.place(relx=0.02,
                                   rely=0.17,
                                   relwidth=0.35,
                                   relheight=0.03)
            # Label e entry Nasc
            self.nascPeLabel.place(relx=0.39,
                                   rely=0.15,
                                   relwidth=0.05,
                                   relheight=0.02)
            self.nascDiaPeEntry.place(relx=0.39,
                                      rely=0.17,
                                      relwidth=0.02,
                                      relheight=0.03)
            self.nascMesPeEntry.place(relx=0.41,
                                      rely=0.17,
                                      relwidth=0.02,
                                      relheight=0.03)
            self.nascAnoPeEntry.place(relx=0.43,
                                      rely=0.17,
                                      relwidth=0.04,
                                      relheight=0.03)
            #    Endereço
            self.logradPeLabel.place(relx=0.02,
                                     rely=0.2,
                                     relwidth=0.08,
                                     relheight=0.02)
            self.logradPeEntry.place(relx=0.02,
                                     rely=0.22,
                                     relwidth=0.38,
                                     relheight=0.03)

            # numero
            self.numPeLabel.place(relx=0.41,
                                  rely=0.2,
                                  relwidth=0.07,
                                  relheight=0.02)
            self.numPeEntry.place(relx=0.41,
                                  rely=0.22,
                                  relwidth=0.06,
                                  relheight=0.03)
            # Complemento
            self.complemPeLabel.place(relx=0.02,
                                      rely=0.25,
                                      relwidth=0.12,
                                      relheight=0.02)
            self.complemPeEntry.place(relx=0.02,
                                      rely=0.27,
                                      relwidth=0.22,
                                      relheight=0.03)
            # Bairro
            self.bairroPeLabel.place(relx=0.25,
                                     rely=0.25,
                                     relwidth=0.06,
                                     relheight=0.02)
            self.bairroPeEntry.place(relx=0.25,
                                     rely=0.27,
                                     relwidth=0.22,
                                     relheight=0.03)
            # Cidade
            self.cidadePeLabel.place(relx=0.02,
                                     rely=0.3,
                                     relwidth=0.06,
                                     relheight=0.02)
            self.cidadePeEntry.place(relx=0.02,
                                     rely=0.32,
                                     relwidth=0.41,
                                     relheight=0.03)
            # UF
            self.ufPeLabel.place(relx=0.44,
                                 rely=0.3,
                                 relwidth=0.03,
                                 relheight=0.02)
            self.ufPeEntry.place(relx=0.44,
                                 rely=0.32,
                                 relwidth=0.03,
                                 relheight=0.03)
            # Fones
            self.fone1Pelabel.place(relx=0.02,
                                    rely=0.35,
                                    relwidth=0.06,
                                    relheight=0.02)
            self.fone1PeEntry.place(relx=0.02,
                                    rely=0.37,
                                    relwidth=0.03,
                                    relheight=0.03)
            self.fone1PeEntry2.place(relx=0.06,
                                     rely=0.37,
                                     relwidth=0.12,
                                     relheight=0.03)

            self.fone2Pelabel.place(relx=0.24, rely=0.35, relwidth=0.06, relheight=0.02)
            self.fone2PeEntry.place(relx=0.24, rely=0.37, relwidth=0.03, relheight=0.03)
            self.fone2PeEntry2.place(relx=0.28, rely=0.37, relwidth=0.12, relheight=0.03)
            ################################
            # Cep
            self.cepPeLabel.place(relx=0.02, rely=0.4, relwidth=0.06, relheight=0.02)
            self.cepPeBt.place(relx=0.02, rely=0.42, relwidth=0.04, relheight=0.03)
            self.cepPeEntry.place(relx=0.06, rely=0.42, relwidth=0.07, relheight=0.03)
            ###############################
            # cpf cnpj
            self.cnpjPeLabel.place(relx=0.14, rely=0.4, relwidth=0.05, relheight=0.02)
            self.cnpjPeEntry.place(relx=0.14, rely=0.42, relwidth=0.16, relheight=0.03)

            self.cpfPeLabel.place(relx=0.31, rely=0.4, relwidth=0.05, relheight=0.02)
            self.cpfPeEntry.place(relx=0.31, rely=0.42, relwidth=0.16, relheight=0.03)
            ################################
            # Obs
            self.obsPeLabel.place(relx=0.02, rely=0.45, relwidth=0.05, relheight=0.02)
            self.obsPeEntry.place(relx=0.02, rely=0.47, relwidth=0.22, relheight=0.028)
            ################################
            # E-mail
            self.emailPeLabel.place(relx=0.25, rely=0.45, relwidth=0.05, relheight=0.02)
            self.emailPeEntry.place(relx=0.25, rely=0.47, relwidth=0.22, relheight=0.028)

        def botoesCliente():
            ##############################################################################################
            ###             BOTOES CLIENTE
            ###  Botao Novo Cliente
            self.botaoAdd.configure(command=self.add_clienteC)
            self.botaoAdd.place(relx=0.24, rely=0.11, relwidth=0.07, relheight=0.04)
            ##############################################################################################
            ### Botao Altera dados do Cliente
            self.botaoMud.configure(command=self.mud_clienteC)
            self.botaoMud.place(relx=0.32, rely=0.11, relwidth=0.07, relheight=0.04)
            ##############################################################################################
            ### Botao deletar dados do Cliente
            self.botaoDel.configure(command=self.deletar_windowC)
            self.botaoDel.place(relx=0.4, rely=0.11, relwidth=0.07, relheight=0.04)
            ##############################################################################################
            ##  Botao limpa
            self.botaolimpa.configure(command=self.limpa_clienteC)
            self.botaolimpa.place(relx=0.075, rely=0.11, relwidth=0.06, relheight=0.04)
            ##############################################################################################
            ###  Botao busca Cabeça
            self.botaobusca.configure(command=self.busca_clienteC)
            self.botaobusca.place(relx=0.15, rely=0.11, width=35)

        def listaClientes():
            ##################################################################################
            ###             MOLDURA TREEVIEW CLIENTE
            self.barracliente = Scrollbar(self.janelaCli, orient='vertical', command=self.OnVsbC)

            self.listaServ = ttk.Treeview(self.janelaCli, height=6, yscrollcommand=self.barracliente.set,
                                          column=("col1", "col2", "col3", "col4"))

            self.listaServ.heading("#0", text="")
            self.listaServ.heading("#1", text=self.m_Codigo)
            self.listaServ.heading("#2", text=self.m_Nome)
            self.listaServ.heading("#3", text='DDD')
            self.listaServ.heading("#4", text=self.m_Fone)

            self.listaServ.column("#0", width=0)
            self.listaServ.column("#1", width=45)
            self.listaServ.column("#2", width=180)
            self.listaServ.column("#3", width=45)
            self.listaServ.column("#4", width=100)

            self.listaServ.place(relx=0.5, rely=0.13, relwidth=0.465, relheight=0.37)

            self.listaServ.configure(yscroll=self.barracliente.set)
            self.barracliente.place(relx=0.965, rely=0.1, relwidth=0.015, relheight=0.4)

            self.listaServ.bind("<Double-1>", self.OnDoubleClickC)
            self.lista1 = self.cursor.execute("""
                                                    SELECT  cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC;
                                                    """)
            for i in self.lista1:
                self.listaServ.insert("", END, values=i)

        def tituloListaClientes():
            labelTitulo = Label(self.janelaCli, text=self.m_lista + ' ' + self.m_de + ' ' + self.m_Clientes,
                                bg=self.fundo_do_frame, fg='gray45', font=('Verdana', '12', 'bold'))
            labelTitulo.place(relx=0.5, rely=0.066, relwidth=0.3, relheight=0.03)

        def caixaEquip():
            ###################################################################################
            ####             AUTOMOVEIS

            labelTitulo = Label(self.janelaCli, text=self.m_Automoveis,
                                bg=self.fundo_do_frame, fg='gray45', font=('Verdana', '12', 'bold'))
            labelTitulo.place(relx=0.016, rely=0.51, relwidth=0.2, relheight=0.028)

            ##### Placa
            self.serialEquipLabel.place(relx=0.02, rely=0.55, relwidth=0.1, relheight=0.04)
            self.serialEquipEntry.place(relx=0.02, rely=0.59, relwidth=0.1, relheight=0.04)

            ##### Veiculo
            self.descrVeiculo = Button(self.janelaCli, bd=2, text=self.m_Veiculo, bg='#37609b', fg='white',
                                       font=('Verdana', '8', 'bold'), command=self.busca_autoC)
            self.descrVeiculo.place(relx=0.13, rely=0.55, relwidth=0.1, relheight=0.04)

            self.nomeEquipEntry.place(relx=0.13, rely=0.59, relwidth=0.1, relheight=0.04)

            #### Fabricante
            self.marcaEquipLabel.place(relx=0.24, rely=0.55, relwidth=0.1, relheight=0.04)

            self.marcaEquipEntry.place(relx=0.24, rely=0.59, relwidth=0.1, relheight=0.04)

            #### Cor
            self.corEquipLabel.place(relx=0.35, rely=0.55, relwidth=0.1, relheight=0.04)

            self.corEquipEntry.place(relx=0.35, rely=0.58, relwidth=0.1, relheight=0.06)

            ### Combustivel
            self.combEquipLabel.place(relx=0.46, rely=0.55, relwidth=0.1, relheight=0.04)

            self.combEquipEntry.place(relx=0.46, rely=0.58, relwidth=0.1, relheight=0.06)

            #### Ano
            self.fabrAnoEquipLabel.place(relx=0.57, rely=0.55, relwidth=0.1, relheight=0.04)

            self.fabrAnoEquipEntry.place(relx=0.57, rely=0.59, relwidth=0.1, relheight=0.04)

        def botoesEquip():
            ################################################################################
            ####  Botoes automoveis
            self.botaoAdd2.configure(command=self.add_veiculoC)
            self.botaoAdd2.place(relx=0.68, rely=0.59, relwidth=0.07, relheight=0.04)

            self.botaoMud2.configure(command=self.mud_autoC)
            self.botaoMud2.place(relx=0.76, rely=0.59, relwidth=0.07, relheight=0.04)

            self.botaoDel2.configure(command=self.deletar_windowPlacaC)
            self.botaoDel2.place(relx=0.84, rely=0.59, relwidth=0.07, relheight=0.04)

        def listaEquip():
            ######################################################################################
            ### Widgets - Listar veiculos ###

            self.listaPlaca = ttk.Treeview(self.janelaCli, height=5,
                                           column=("col1", "col2", "col3", "col4", "col5", "col6"))
            self.listaPlaca.heading("#0", text="")
            self.listaPlaca.heading("#1", text=self.m_Placa)
            self.listaPlaca.heading("#2", text=self.m_Veiculo)
            self.listaPlaca.heading("#3", text=self.m_Montadora)
            self.listaPlaca.heading("#4", text=self.m_Cor)
            self.listaPlaca.heading("#5", text=self.m_Combustivel)
            self.listaPlaca.heading("#6", text=self.m_Ano)

            self.listaPlaca.column("#0", width=0)
            self.listaPlaca.column("#1", width=80)
            self.listaPlaca.column("#2", width=120)
            self.listaPlaca.column("#3", width=170)
            self.listaPlaca.column("#4", width=100)
            self.listaPlaca.column("#5", width=100)
            self.listaPlaca.column("#6", width=80)

            # Cria barra de rolagem
            self.barra = Scrollbar(self.janelaCli, orient='vertical', command=self.listaPlaca.yview)

            # Adiciona barra de rolagem
            self.listaPlaca.configure(yscroll=self.barra.set)
            self.barra.place(relx=0.855, rely=0.65, relwidth=0.02, relheight=0.3)

            self.listaPlaca.place(relx=0.05, rely=0.65, relwidth=0.81, relheight=0.3)
            #    Binding da listbox
            self.listaPlaca.bind('<Double-1>', self.bind_autoC)
            ############################################################################

        self.cores();
        self.multiGlacx();
        abreJanela();
        self.custommer_obj();
        self.conecta_Glac()
        molduras();
        tituloCadCli();
        caixaClientes();
        botoesCliente();
        listaClientes();
        tituloListaClientes();
        caixaEquip();
        botoesEquip();
        listaEquip();
        self.desconecta_Glac()

        self.janelaCli.mainloop()

    def cadaut(self):
        def abreJanela():
            self.janelaAut = Tk()
            self.janelaAut.title('Glac')
            self.janelaAut.configure(background=self.fundo_da_tela)
            self.janelaAut.geometry("800x235")
            self.janelaAut.resizable(FALSE, FALSE)

        def canvasAut():
            self.cliente_canvas2 = Canvas(self.janelaAut, width=790, height=200, cursor='X_cursor', bd=2,
                                          bg=self.fundo_da_tela, highlightbackground="gray75", highlightthickness=2)
            self.cliente_canvas2.place(x=0, y=28)
            self.cliente_canvas2 = Canvas(self.janelaAut, width=340, height=180, cursor='X_cursor', bd=2,
                                          bg=self.fundo_do_frame, highlightbackground="#45e0fc",
                                          highlightthickness=2)
            self.cliente_canvas2.place(x=8, y=38)

        def widgets():
            ####
            self.descrNomeServ.place(x=307, y=0, relheight=0.1)
            ###  Descrição e Entrada codigo
            self.descrCod_aut.place(x=10, y=52)
            self.entradaCod_autA.place(x=85, y=52)
            ###  Descrição e Entrada Automovel
            self.descrAut.place(x=10, y=90)
            self.entradaAutA.place(x=85, y=90)
            ###  Descrição e Entrada Marca
            self.entradaMarcaA.place(x=85, y=130)

        def botoes():
            ###  Botao busca automovel
            self.botaoBuscaAut.configure(command=self.busca_automovelA)
            self.botaoBuscaAut.place(x=290, y=89, width=55, height=23)
            ###  Botao Carrega automovel
            self.botaoCarregaAut.configure(command=self.carrega_automovelA)
            self.botaoCarregaAut.place(x=150, y=50, width=90)
            ###  Botao limpa automovel
            self.botaoLimpaAut.configure(command=self.limpa_automovelA)
            self.botaoLimpaAut.place(x=250, y=50, width=90)
            ###  Botao busca marca
            self.botaoMarcaAut.configure(command=self.busca_autoA)
            self.botaoMarcaAut.place(x=10, y=128, width=72, height=23)
            ###  Botao Novo Cliente
            self.botaoNovoAut.configure(command=self.add_automovelA)
            self.botaoNovoAut.place(x=30, y=180, width=80)
            ### Botao Altera dados do Cliente
            self.botaoAlterarAut.configure(command=self.mud_automovelA)
            self.botaoAlterarAut.place(x=130, y=180, width=80)
            ### Botao Deletar Cliente
            self.botaoApagarAut.configure(command=self.del_automovelA)
            self.botaoApagarAut.place(x=230, y=180, width=80)

        def listaAut():
            # Cria barra de rolagem
            self.barra = Scrollbar(self.janelaAut, orient='vertical', command=self.OnVsbA)

            ### Widgets - Listar veiculos ###
            self.listaServ = ttk.Treeview(self.janelaAut, height=8, column=("col1", "col2", "col3"))
            self.listaServ.heading("#0", text="")
            self.listaServ.heading("#1", text=self.m_Codigo)
            self.listaServ.heading("#2", text=self.m_Automovel)
            self.listaServ.heading("#3", text=self.m_Marca)

            self.listaServ.column("#0", width=0)
            self.listaServ.column("#1", width=45)
            self.listaServ.column("#2", width=170)
            self.listaServ.column("#3", width=170)

            # Adiciona barra de rolagem
            self.listaServ.configure(yscroll=self.barra.set)
            self.barra.place(x=755, y=40, width=30, height=185)

            self.conecta_Glac()

            lista = self.cursor.execute("""
                         SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
                         WHERE montadora.cod = automoveis.montad  ORDER BY automovel ASC;
                         """)
            for i in lista:
                self.listaServ.insert("", END, values=i)

            self.desconecta_Glac()

            self.listaServ.place(x=365, y=40)
            self.listaServ.bind("<Double-1>", self.OnDoubleClickA)

        self.cores();
        self.multiGlacx();
        abreJanela();
        canvasAut();
        self.model_car_obj();
        widgets();
        botoes();
        listaAut()
        self.janelaAut.mainloop()

    def cademp(self):
        self.multiGlacx()
        self.cores();

        def abre_janela():
            self.janela = Tk()
            self.janela.title('Glacx' + self.m_Empresa)
            self.janela.configure(background=self.fundo_da_tela)
            self.janela.geometry("410x250")
            self.janela.resizable(FALSE, FALSE)

        abre_janela()

        self.descrNomeServ = Label(self.janela, text=self.m_Estab, fg='gray75', bg=self.fundo_da_tela,
                                   font=('Times', '18', 'bold', 'italic'))
        self.descrNomeServ.place(x=75, y=1)

        self.cliente_canvas2 = Canvas(self.janela, width=380, height=190, cursor='X_cursor', bd=2,
                                      bg=self.fundo_do_frame)
        self.cliente_canvas2.place(x=8, y=38)

        self.entradaCod_emp = Entry(self.janela, width=6)

        ###  Descrição e Entrada Nome
        self.descrNome = Label(self.janela, text=self.m_Nome + self.m_Pontinhos, bg=self.fundo_do_frame,
                               fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrNome.place(x=10, y=53)
        self.entradaNome_emp = Entry(self.janela, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaNome_emp.place(x=85, y=53)

        ###  Descrição e Entrada Enedereco
        self.descrEndereco = Label(self.janela, text=self.m_Endereco + self.m_Pontinhos, bg=self.fundo_do_frame,
                                   fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrEndereco.place(x=10, y=83)
        self.entradaEndereco_emp = Entry(self.janela, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaEndereco_emp.place(x=85, y=83)

        ###  Descrição e Entrada Bairro
        self.descrBairro = Label(self.janela, text=self.m_Bairro + self.m_Pontinhos, bg=self.fundo_do_frame,
                                 fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrBairro.place(x=10, y=103)
        self.entradaBairro_emp = Entry(self.janela, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaBairro_emp.place(x=85, y=103)

        ###  Descrição e Entrada Municipio
        self.descrMunicipio = Label(self.janela, text=self.m_Cidade + self.m_Pontinhos, bg=self.fundo_do_frame,
                                    fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrMunicipio.place(x=10, y=123)
        self.entradaMunicipio_emp = Entry(self.janela, width=27, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaMunicipio_emp.place(x=85, y=123)

        ###  Descrição e Entrada UF
        self.descrUf = Label(self.janela, text=self.m_Uf, bg=self.fundo_do_frame, fg='darkblue',
                             font=('Verdana', '10', 'bold'))
        self.descrUf.place(x=320, y=123)
        self.entradaUf_emp = Entry(self.janela, width=2, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaUf_emp.place(x=350, y=123)

        ###  Descrição e Entrada Fone
        self.descrFone = Label(self.janela, text=self.m_Fone + self.m_Pontinhos, bg=self.fundo_do_frame,
                               fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrFone.place(x=10, y=143)
        self.entradaFone_emp = Entry(self.janela, width=14, fg='brown', validate="key",
                                     validatecommand=self.vcmd12, font=('Verdana', '9', 'bold'))
        self.entradaFone_emp.place(x=85, y=143)

        ###  Descrição e Entrada Cep
        self.descrCep = Label(self.janela, text=self.m_Cep, bg=self.fundo_do_frame, fg='darkblue',
                              font=('Verdana', '10', 'bold'))
        self.descrCep.place(x=220, y=143)
        self.entradaCep_emp = Entry(self.janela, width=12, validate="key",
                                    validatecommand=self.vcmd12, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaCep_emp.place(x=260, y=143)

        ###  Descrição e Entrada Cpf
        self.descrCpf = Label(self.janela, text=self.m_Cnpj + self.m_Pontinhos, bg=self.fundo_do_frame, fg='darkblue',
                              font=('Verdana', '8', 'bold'))
        self.descrCpf.place(x=10, y=163)
        self.entradaCpf_emp = Entry(self.janela, width=15, fg='brown', font=('Verdana', '9', 'bold'), validate="key",
                                    validatecommand=self.vcmd12)
        self.entradaCpf_emp.place(x=85, y=163)

        ###  Descrição e Entrada Rg
        self.descrRg = Label(self.janela, text=self.m_Cpf, bg=self.fundo_do_frame, fg='darkblue',
                             font=('Verdana', '10', 'bold'))
        self.descrRg.place(x=230, y=163)
        self.entradaRg_emp = Entry(self.janela, width=12, fg='brown', font=('Verdana', '9', 'bold'), validate="key",
                                   validatecommand=self.vcmd12)
        self.entradaRg_emp.place(x=260, y=163)

        ###  Descrição e Entrada Obs
        self.descrObs = Label(self.janela, text=self.m_Obs + self.m_Pontinhos, bg=self.fundo_do_frame, fg='darkblue',
                              font=('Verdana', '10', 'bold'))
        self.descrObs.place(x=10, y=193)
        self.entradaObs_emp = Entry(self.janela, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaObs_emp.place(x=85, y=193)

        ### Botao Altera dados do Cliente
        # self.botaoMudServ = Button(self.janela, text= multilingua.Alterar, command=self.mud_empresa, fg='darkblue', bd=3,
        #                   font=('Verdana', '12', 'bold'))
        # self.botaoMudServ.place(x=150, y=250, width=80)
        self.conecta_Glac()

        lista = self.cursor.execute("""
                SELECT cod_emp FROM empresa;
                """)
        for i in lista:
            self.entradaCod_emp.insert(END, i)

        self.desconecta_Glac()

        self.carrega_empresa()
        self.janela.mainloop()

    def cadtec(self):
        self.multiGlacx()
        self.cores()

        self.janela = Tk()
        self.janela.title(self.m_Tecnico)
        self.janela.configure(background=self.fundo_do_frame)
        self.janela.geometry("650x210")

        self.janela.resizable(FALSE, FALSE)
        self.tech_obj()

        self.servicos_canvas2 = Canvas(self.janela, width=650, height=42, bd=0, bg=self.fundo_da_tela,
                                       highlightbackground="#45e0fc", highlightthickness=1)
        self.servicos_canvas2.place(x=0, y=0)
        self.servicos_canvas2 = Canvas(self.janela, width=5, height=210, bd=0, bg=self.fundo_da_tela,
                                       highlightbackground="#45e0fc", highlightthickness=1)
        self.servicos_canvas2.place(x=0, y=0)

        self.descrServicos = Label(self.janela, text=self.m_Tecnico, fg='gray85', bg=self.fundo_da_tela,
                                   font=('Arial', '28', 'bold', 'italic'))
        self.descrServicos.place(x=250, y=1, height=40)

        self.descrCod = Label(self.janela, text=self.m_Codigo, fg='darkblue', bg=self.fundo_do_frame,
                              font=('Verdana', '10', 'bold'))
        self.descrCod.place(x=16, y=50)
        self.entradaCod = Entry(self.janela, width=6, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaCod.place(x=80, y=53)

        ###  Botao Carrega servico
        self.botaoCarregar.configure(command=self.carrega_servicoT)
        self.botaoCarregar.place(x=135, y=50, width=130)
        ###  Botao limpa servico
        self.botaolimpa.configure(command=self.limpa_servicoT)
        self.botaolimpa.place(x=270, y=50, width=70)

        self.descrServ = Label(self.janela, text=self.m_Tecnico, fg='darkblue', bg=self.fundo_do_frame,
                               font=('Verdana', '10', 'bold'))
        self.descrServ.place(x=15, y=80)
        self.entradaServ = Entry(self.janela, width=33, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaServ.place(x=80, y=83)

        ###  Botao busca SERVICO
        self.botaobusca.configure(command=self.busca_servicoT)
        self.botaobusca.place(x=290, y=80, width=50)

        self.botaoAdd.configure(command=self.add_servT)
        self.botaoAdd.place(x=30, y=140, width=80)

        self.botaoMud.configure(command=self.mud_servT)
        self.botaoMud.place(x=130, y=140, width=80)

        self.botaoDel.configure(command=self.del_servT)
        self.botaoDel.place(x=230, y=140, width=80)

        ### Widgets - Listar veiculos ###

        self.listaServ = ttk.Treeview(self.janela, height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Tecnico)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=35)
        self.listaServ.column("#2", width=230)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janela, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=610, y=50, width=30, height=147)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickT)

        self.conecta_Glac()

        lista = self.cursor.execute("""
                    SELECT cod, tecnico FROM tecnico  ORDER BY tecnico ASC;
                    """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=345, y=50)

        self.desconecta_Glac()

        self.janela.mainloop()

    def consultapag(self):
        self.multiGlacx()

        self.janela = Tk();
        self.janela.title("GlacX")
        self.janela.configure(background='lavender');
        self.janela.geometry("800x495")
        self.janela.resizable(FALSE, FALSE)

        ### Label principal
        self.labelformapag = Label(self.janela, text=self.m_Consulta + ' ' + self.m_Pagamento)
        self.labelformapag.configure(bg='lavender', fg='brown', font=('Comic', '16', 'bold', 'italic'))
        self.labelformapag.place(relx=0.35, rely=0)

        ###  Frame Moldura
        self.frame1 = Frame(self.janela)
        self.frame1.configure(background='lightgray')
        self.frame1.place(relx=0, rely=0.06, relwidth=1, relheight=1)
        self.frame2 = Frame(self.frame1, bd=4, bg='gray55')
        self.frame2.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
        self.frame3 = Frame(self.frame2, bd=4, bg='lightgray', relief=SUNKEN)
        self.frame3.place(relx=0.02, rely=0.02, relwidth=1, relheight=1)

        self.consulta1()

        self.consulta2()

        ### Widgets - Listar pagamentos ###
        ### Frame lista
        self.framelista = Frame(self.frame3, bg='darkblue')
        self.framelista.place(relx=0.022, rely=0.32, width=742, height=238)
        self.framelista = Frame(self.frame3, bg='lightblue')
        self.framelista.place(relx=0.026, rely=0.33, width=737, height=232)

        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.frame3, height=10,
                                     column=("col1", "col2", "col3", "col4",
                                             "col5", "col6", "col7", "col8", "col9"))

        self.listaPag.heading("#0", text="");
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text=self.m_Ordem);
        self.listaPag.column("#1", width=60)
        self.listaPag.heading("#2", text=self.m_Tipo);
        self.listaPag.column("#2", width=220)
        self.listaPag.heading("#3", text="");
        self.listaPag.column("#3", width=1)
        self.listaPag.heading("#4", text=self.m_Valor);
        self.listaPag.column("#4", width=120)
        self.listaPag.heading("#5", text=self.m_Dia);
        self.listaPag.column("#5", width=60)
        self.listaPag.heading("#6", text=self.m_Mes);
        self.listaPag.column("#6", width=60)
        self.listaPag.heading("#7", text=self.m_Ano);
        self.listaPag.column("#7", width=60)
        self.listaPag.heading("#8", text=self.m_Pago);
        self.listaPag.column("#8", width=110)
        self.listaPag.heading("#9", text="");
        self.listaPag.column("#9", width=1)
        self.listaPag.place(relx=0.03, rely=0.34)

        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame3, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.916, rely=0.34, width=38, height=227)

        self.listaPag.bind("<Double-1>")  # , self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        #### Frame do Valor a ser inserido
        self.frameValor = Frame(self.frame3, bg='darkblue')
        self.frameValor.place(x=590, y=392, width=110, height=52)
        self.frameValor = Frame(self.frame3, bg='lightblue')
        self.frameValor.place(x=593, y=394, width=105, height=50)

        ### Label do saldo a ser pago
        self.labelValor = Label(self.frame3, text=self.m_Valor + ' ' + self.m_Total)
        self.labelValor.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelValor.place(x=600, y=395)
        self.labelCifrao = Label(self.frame3, text=self.m_Reais)
        self.labelCifrao.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelCifrao.place(x=600, y=415)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(self.frame3, bd=1, fg='brown')
        self.entryValorDevido.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValorDevido.place(x=620, y=415)

        self.janela.mainloop()

    def consulta1(self):
        #### Frame do Valor a ser inserido
        self.frameValor = Frame(self.frame3, bg='darkblue')
        self.frameValor.place(relx=0.001, rely=0.018, width=550, height=52)
        self.frameValor = Frame(self.frame3, bg='lightblue')
        self.frameValor.place(relx=0.004, rely=0.02, width=547, height=50)

        #### Listbox do tipo de pagamento
        self.entrytipopag = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrytipopag.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrytipopag.columnconfigure(0, weight=1)
        self.entrytipopag.rowconfigure(0, weight=1)
        self.entrytipopag.place(relx=0.16, rely=0.022, width=120, height=45)
        self.listtipopag = StringVar(self.frame3)
        self.listtipopagV = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto, self.m_ChequePre,
                             self.m_ChequeVista, self.m_Crediario, self.m_Promissoria, self.m_Desconto, self.m_Avista}
        self.listtipopagV = sorted(self.listtipopagV)
        self.listtipopag.set(self.m_Dinheiro)
        self.popupMenu = OptionMenu(self.entrytipopag, self.listtipopag, *self.listtipopagV)
        Label(self.entrytipopag, bd=0, text=self.m_Tipo + ' ' + self.m_Pagamento, fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Entry data

        self.entrymes = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrymes.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrymes.columnconfigure(0, weight=1)
        self.entrymes.rowconfigure(0, weight=1)
        self.entrymes.place(relx=0.006, rely=0.022, width=55, height=45)
        self.mesvar = StringVar(self.frame3)
        self.mesesV = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                       '11', '12'}
        self.mesesV = sorted(self.mesesV)
        self.mesvar.set('01')
        self.popupMenu = OptionMenu(self.entrymes, self.mesvar, *self.mesesV)
        Label(self.entrymes, bd=0, text='Mês', fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        self.entryano = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entryano.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entryano.columnconfigure(0, weight=1)
        self.entryano.rowconfigure(0, weight=1)
        self.entryano.place(relx=0.08, rely=0.022, width=70, height=45)
        self.anovar = StringVar(self.frame3)
        self.anosV = {'2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                      '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV = sorted(self.anosV)
        self.anovar.set('2019')
        self.popupMenu = OptionMenu(self.entryano, self.anovar, *self.anosV)
        Label(self.entryano, bd=0, text='Ano', fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Pago?
        ### Pago?
        self.entrypago = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrypago.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrypago.columnconfigure(0, weight=1)
        self.entrypago.rowconfigure(0, weight=1)
        self.entrypago.place(x=260, y=11, width=65, height=45)
        self.entry7 = StringVar(self.frame3)
        self.entry7V = {self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set(self.m_Sim)

        self.popupMenu = OptionMenu(self.entrypago, self.entry7, *self.entry7V)
        Label(self.entrypago, text=self.m_Pago, bd=0, bg='lightblue', fg='darkblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Button Inserir Registro
        self.btinserir = Button(self.frame3, text=self.m_Consulta + ' ' + self.m_Competência + self.m_barra +
                                                  self.m_Tipo + self.m_barra + self.m_Pago, bg='#37609b', fg='white',
                                font=('Comic', '8', 'bold'), command=self.carregaConsulta)
        self.btinserir.place(relx=0.44, rely=0.06, width=205)

    def consulta2(self):
        #### Frame do Valor a ser inserido
        self.frameValor2 = Frame(self.frame3, bg='darkblue')
        self.frameValor2.place(relx=0.001, rely=0.128, width=550, height=52)
        self.frameValor2 = Frame(self.frame3, bg='lightblue')
        self.frameValor2.place(relx=0.004, rely=0.13, width=547, height=50)

        #### Listbox do tipo de pagamento
        self.entrytipopag2 = Label(self.frame3, text=self.m_Tipo + ' ' + self.m_Pagamento, fg='darkblue',
                                   bd=0, bg='lightblue', width=2)
        self.entrytipopag2.place(relx=0.16, rely=0.132, width=120)
        self.entrytipopag2 = Label(self.frame3, text='Todos', fg='darkblue',
                                   bd=0, bg='lightgray', width=2)
        self.entrytipopag2.place(relx=0.16, rely=0.17, width=120)

        #### Entry data

        self.entrymes2 = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrymes2.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrymes2.columnconfigure(0, weight=1)
        self.entrymes2.rowconfigure(0, weight=1)
        self.entrymes2.place(relx=0.006, rely=0.132, width=55, height=45)
        self.mesvar2 = StringVar(self.frame3)
        self.mesesV2 = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12'}
        self.mesesV2 = sorted(self.mesesV2)
        self.mesvar2.set('01')
        self.popupMenu2 = OptionMenu(self.entrymes2, self.mesvar2, *self.mesesV2)
        Label(self.entrymes2, bd=0, text='Mês', fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu2.grid(row=2, column=1)

        self.entryano2 = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entryano2.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entryano2.columnconfigure(0, weight=1)
        self.entryano2.rowconfigure(0, weight=1)
        self.entryano2.place(relx=0.08, rely=0.132, width=70, height=45)
        self.anovar2 = StringVar(self.frame3)
        self.anosV2 = {'2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                       '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV2 = sorted(self.anosV2)
        self.anovar2.set('2019')
        self.popupMenu2 = OptionMenu(self.entryano2, self.anovar2, *self.anosV2)
        Label(self.entryano2, bd=0, text=self.m_Ano, fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu2.grid(row=2, column=1)

        #### Pago?
        ### Pago?
        self.entrypago2 = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrypago2.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrypago2.columnconfigure(0, weight=1)
        self.entrypago2.rowconfigure(0, weight=1)
        self.entrypago2.place(x=260, y=61, width=65, height=45)
        self.entry72 = StringVar(self.frame3)
        self.entry7V2 = {self.m_Sim, self.m_Nao}
        self.entry7V2 = sorted(self.entry7V2)
        self.entry72.set(self.m_Sim)

        self.popupMenu2 = OptionMenu(self.entrypago2, self.entry72, *self.entry7V2)
        Label(self.entrypago2, text=self.m_Pago, bd=0, bg='lightblue', fg='darkblue').grid(row=1, column=1)
        self.popupMenu2.grid(row=2, column=1)

        #### Button Inserir Registro
        self.btinserir = Button(self.frame3, text=self.m_Consulta + ' ' + self.m_Competência + self.m_barra
                                                  + self.m_Pago, bg='#37609b', fg='white',
                                font=('Comic', '8', 'bold'), command=self.carregaConsulta2)
        self.btinserir.place(relx=0.44, rely=0.17, width=205)

    def cadest(self):
        self.multiGlacx()
        self.cores()
        self.janela = Tk()
        self.janela.title(self.m_Estoque)
        self.janela.configure(background=self.fundo_da_tela)
        self.janela.geometry("800x405")
        self.janela.resizable(FALSE, FALSE)

        self.conecta_Glac()

        self.descrNomeServ = Label(self.janela, text=self.m_ControleEstoque, bg=self.fundo_da_tela, fg='gray75',
                                   font=('Comic', '18', 'bold'))
        self.descrNomeServ.place(x=245, y=1)

        self.vcmd6 = (self.janela.register(self.validate_entry6), "%P")
        self.vcmd4 = (self.janela.register(self.validate_entry4), "%P")
        self.vcmd2 = (self.janela.register(self.validate_entry2), "%P")
        self.vcmd8float = (self.janela.register(self.validate_entry8float), "%P")

        ###  A B A S

        self.abas = Notebook(self.janela)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas)
        self.frame_aba4 = Frame(self.abas)

        self.frame_aba3.configure(background='lightgray')
        self.frame_aba1.configure(background='lightgray')
        self.frame_aba2.configure(background='lightgray')
        self.frame_aba4.configure(background='lightgray')

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=385, pady=160)
        self.label2 = Label(self.frame_aba2)
        self.label2.pack(padx=385, pady=160)
        self.label3 = Label(self.frame_aba3)
        self.label3.pack(padx=385, pady=160)
        self.label4 = Label(self.frame_aba4)
        self.label4.pack(padx=385, pady=160)

        self.abas.add(self.frame_aba1, text=self.m_Cadastro + ' ' + self.m_Produtos)
        self.abas.add(self.frame_aba2, text=self.m_MovimentaEst)

        self.abas.place(x=10, y=30)

        ####################################################################
        ####  Descrição dos problemas apresentados pelo veiculo - Aba 1
        ####################################################################
        self.frameProb = Frame(self.frame_aba1, width=755, height=260, bd=4, relief=SUNKEN)
        self.frameProb.place(x=10, y=10)

        self.descrCodprod = Label(self.frame_aba1, text=self.m_Codigo, font=('Verdana', '8', 'bold'))
        self.descrCodprod.place(x=14, y=15)
        self.entradaCodprod = Entry(self.frame_aba1, width=6, fg='brown', validate="key",
                                    validatecommand=self.vcmd6,
                                    font=('Verdana', '8', 'bold'))
        self.entradaCodprod.place(x=75, y=18)

        ###  Botao Carrega
        self.botaoAdd = Button(self.frame_aba1, text=self.m_Carregar + ' ' + self.m_Produtos, bd=3,
                               fg='darkblue', command=self.carrega_produtoE,
                               font=('Verdana', '7', 'bold'))
        self.botaoAdd.place(x=135, y=17, width=100)
        ###  Botao limpa
        self.botaolimpa = Button(self.frame_aba1, text=self.m_Limpar, bd=3, fg='darkblue',
                                 command=self.limpa_produtoE,
                                 font=('Verdana', '8', 'bold'))
        self.botaolimpa.place(x=275, y=17, width=60, height=22)

        self.descrProd = Label(self.frame_aba1, text=self.m_Produtos, font=('Verdana', '8', 'bold'))
        self.descrProd.place(x=14, y=43)
        self.entradaProd = Entry(self.frame_aba1, width=32, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaProd.place(x=75, y=43)

        ###  Botao busca automovel
        self.botaolimpa = Button(self.frame_aba1, text=self.m_Buscar, bd=3, fg='darkblue',
                                 command=self.busca_produtoE,
                                 font=('Verdana', '8', 'bold'))
        self.botaolimpa.place(x=275, y=40, width=60, height=24)

        self.descrIdMarcaprod = Button(self.frame_aba1, text=self.m_Marca, bg='gray75',
                                       font=('Verdana', '8', 'bold'),
                                       command=self.busca_marcaE)
        self.descrIdMarcaprod.place(x=14, y=65, width=63, height=23)
        self.entradaIdMarcaprod = Entry(self.frame_aba1, width=6)
        # entradaIdMarcaprod.place(x=75, y=63)
        self.entradaMarcaprod = Entry(self.frame_aba1, width=26, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaMarcaprod.place(x=76, y=68)

        self.descrIdFornec = Button(self.frame_aba1, text=self.m_Fornecedor, bg='gray75',
                                    font=('Verdana', '8', 'bold'),
                                    command=self.busca_fornecE)
        self.descrIdFornec.place(x=14, y=92, width=63, height=23)
        self.entradaIdFornec = Entry(self.frame_aba1, width=6)
        # entradaIdFornec.place(x=85, y=93)
        self.entradaFornec = Entry(self.frame_aba1, width=26, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaFornec.place(x=75, y=93)

        self.descrCusto = Label(self.frame_aba1, text=self.m_Custo_R, font=('Verdana', '8', 'bold'))
        self.descrCusto.place(x=14, y=122)
        self.entradaCusto = Entry(self.frame_aba1, width=8, fg='brown', font=('Verdana', '8', 'bold'),
                                  validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=75, y=123)

        self.descrValor = Label(self.frame_aba1, text=self.m_Valor_R, font=('Verdana', '8', 'bold'))
        self.descrValor.place(x=150, y=122)
        self.entradaValor = Entry(self.frame_aba1, width=8, fg='brown', font=('Verdana', '8', 'bold'),
                                  validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaValor.place(x=220, y=123)

        self.descrDescricao = Label(self.frame_aba1, text=self.m_Descricao, font=('Verdana', '9', 'bold'))
        self.descrDescricao.place(x=14, y=150)
        self.entradaDescricao = Entry(self.frame_aba1, width=36, fg='brown', font=('Verdana', '10', 'bold'))
        self.entradaDescricao.place(x=16, y=175)

        self.botaoAdd = Button(self.frame_aba1, text=self.m_Novo, command=self.add_produtoE, bd=3, fg='darkblue',
                               font=('Verdana', '10', 'bold'))
        self.botaoAdd.place(x=50, y=210, width=80)

        self.botaoMudServ = Button(self.frame_aba1, text=self.m_Alterar, command=self.mud_produtoE, bd=3, fg='darkblue',
                                   font=('Verdana', '10', 'bold'))
        self.botaoMudServ.place(x=150, y=210, width=80)

        self.botaoDel = Button(self.frame_aba1, text=self.m_Apagar, command=self.del_produtoE, bd=3, fg='brown',
                               font=('Verdana', '10', 'bold'))
        self.botaoDel.place(x=250, y=210, width=80)

        ### Widgets - Listar produtos ###

        self.listaServ = ttk.Treeview(self.frame_aba1, height=10,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Produtos)
        self.listaServ.heading("#3", text="")
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.heading("#5", text="")
        self.listaServ.heading("#6", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=39)
        self.listaServ.column("#2", width=180)
        self.listaServ.column("#3", width=25)
        self.listaServ.column("#4", width=65)
        self.listaServ.column("#5", width=25)
        self.listaServ.column("#6", width=65)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.frame_aba1, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=740, y=15, width=15, height=230)

        lista = self.cursor.execute("""
                            SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
                    	    WHERE sp = "P" ORDER BY servprod ASC ;
                            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=340, y=15)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickE)

        #####################################################################
        #### ABA 2
        #####################################################################
        ### Cabeçalho dos itens_orc 1 A 10 - Aba 2

        self.frameItens = Frame(self.frame_aba2, width=760, height=316, bd=4, bg='gray55')
        self.frameItens.place(x=10, y=8)

        self.frameItens = Frame(self.frame_aba2, width=750, height=307, bd=4, bg='lightgray', relief=SUNKEN)
        self.frameItens.place(x=15, y=15)
        ### Produto
        self.produto_aba2label = Label(self.frame_aba2, text=self.m_Produtos, fg='darkblue',
                                       font=('Verdana', '8', 'bold'), bg='lightgray')
        self.produto_aba2label.place(x=20, y=20)

        self.codproduto2 = Entry(self.frame_aba2)

        self.produto_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='30', font=('Verdana', '8', 'bold'))
        self.produto_aba2.place(x=130, y=20)

        #### Entrada
        self.quant_aba2label = Label(self.frame_aba2, text=self.m_Entrada, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.quant_aba2label.place(x=20, y=45)

        self.quant_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='10', font=('Verdana', '8', 'bold'),
                                validate="key",
                                validatecommand=self.vcmd8float)
        self.quant_aba2.place(x=130, y=45)
        self.quant_aba2.insert(END, 0)

        #### Saida
        self.saida_aba2label = Label(self.frame_aba2, text=self.m_Saida, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.saida_aba2label.place(x=20, y=70)

        self.saida_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='10', font=('Verdana', '8', 'bold'),
                                validate="key",
                                validatecommand=self.vcmd8float)
        self.saida_aba2.place(x=130, y=70)
        self.saida_aba2.insert(END, 0)

        #### Custo
        self.custo_aba2label = Label(self.frame_aba2, text=self.m_Custo_R, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.custo_aba2label.place(x=20, y=95)

        self.custo_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='10', font=('Verdana', '8', 'bold'),
                                validate="key",
                                validatecommand=self.vcmd8float)
        self.custo_aba2.place(x=130, y=95)
        #### Data
        self.data_aba2label = Label(self.frame_aba2, text=self.m_Data + self.m_Pontinhos + self.m_Pontinhos +
                                                          self.m_DataMasc, fg='darkblue',
                                    font=('Verdana', '8', 'bold'), bg='lightgray')
        self.data_aba2label.place(x=20, y=120)

        self.dia_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                              validate="key",
                              validatecommand=self.vcmd2)
        self.dia_aba2.place(x=130, y=120)

        self.mes_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                              validate="key",
                              validatecommand=self.vcmd2)
        self.mes_aba2.place(x=155, y=120)

        self.ano_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='4', font=('Verdana', '8', 'bold'),
                              validate="key",
                              validatecommand=self.vcmd4)
        self.ano_aba2.place(x=185, y=120)
        #### Lote
        self.lote_aba2label = Label(self.frame_aba2, text=self.m_Lote, fg='darkblue',
                                    font=('Verdana', '8', 'bold'), bg='lightgray')
        self.lote_aba2label.place(x=20, y=145)

        self.lote_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='20', font=('Verdana', '8', 'bold'))
        self.lote_aba2.place(x=130, y=145)
        self.lote_aba2.insert(END, 'xxx')
        #### Validade
        self.valid_aba2label = Label(self.frame_aba2, text=self.m_Validade, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.valid_aba2label.place(x=20, y=170)

        self.diaV_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                               validate="key", validatecommand=self.vcmd2)
        self.diaV_aba2.place(x=130, y=170)

        self.mesV_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                               validate="key", validatecommand=self.vcmd2)
        self.mesV_aba2.place(x=155, y=170)

        self.anoV_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='4', font=('Verdana', '8', 'bold')
                               , validate="key", validatecommand=self.vcmd4)
        self.anoV_aba2.place(x=185, y=170)

        self.darEntrada = Button(self.frame_aba2, text=self.m_InserirRegistro, command=self.add_movE)
        self.darEntrada.place(x=130, y=250)

        self.quantestlabel = Label(self.frame_aba2, text=self.m_Quant + ' ' + self.m_Estoque, fg='darkblue',
                                   font=('Verdana', '8', 'bold'), bg='lightgray')
        self.quantestlabel.place(x=430, y=300)

        self.quantest = Entry(self.frame_aba2, bd=0, fg='red', width='4', font=('Verdana', '9', 'bold'))
        self.quantest.place(x=630, y=300)

        ### Widgets - Listar produtos ###

        self.listaMov = ttk.Treeview(self.frame_aba2, height=10,
                                     column=(
                                         "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9",
                                         "col10",
                                         "col11"))
        self.listaMov.heading("#0", text="")
        self.listaMov.heading("#1", text=self.m_Lote)
        self.listaMov.heading("#2", text=self.m_Entrada)
        self.listaMov.heading("#3", text=self.m_Saida)
        self.listaMov.heading("#4", text=self.m_Custo_R)
        self.listaMov.heading("#5", text="")
        self.listaMov.heading("#6", text="")
        self.listaMov.heading("#7", text=self.m_Data)
        self.listaMov.heading("#8", text=self.m_Fornecedor)
        self.listaMov.heading("#9", text="")
        self.listaMov.heading("#10", text="")
        self.listaMov.heading("#11", text=self.m_Validade)

        self.listaMov.column("#0", width=0)
        self.listaMov.column("#1", width=50)
        self.listaMov.column("#2", width=50)
        self.listaMov.column("#3", width=50)
        self.listaMov.column("#4", width=50)
        self.listaMov.column("#5", width=15)
        self.listaMov.column("#6", width=15)
        self.listaMov.column("#7", width=35)
        self.listaMov.column("#8", width=80)
        self.listaMov.column("#9", width=15)
        self.listaMov.column("#10", width=15)
        self.listaMov.column("#11", width=70)

        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame_aba2, orient='vertical', command=self.listaMov.yview)
        # Adiciona barra de rolagem
        self.listaMov.configure(yscroll=self.barraMov.set)
        self.barraMov.place(x=750, y=50, width=15, height=230)

        # Cria barra de rolagem
        self.barraMov2 = Scrollbar(self.frame_aba2, orient='horizontal', command=self.listaMov.xview)
        # Adiciona barra de rolagem
        self.listaMov.configure(xscroll=self.barraMov2.set)
        self.barraMov2.place(x=310, y=277, width=420, height=20)

        self.listaMov.place(x=300, y=50)

        self.listaMov.bind("<Double-1>", self.OnDoubleClickE)

        self.desconecta_Glac()
        self.janela.mainloop()

    def cadserv(self):
        self.multiGlacx()
        self.cores()

        self.janela = Tk()
        self.janela.title(self.m_Serviços)
        self.janela.configure(background=self.fundo_da_tela)
        self.janela.geometry("1000x410")
        self.janela.resizable(FALSE, FALSE)

        top3 = Canvas(self.janela, bd=0, bg=self.fundo_do_frame, highlightbackground="gray70",
                      highlightthickness=2);
        top3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.96)

        self.servicos_canvas2 = Canvas(self.janela, width=835, height=2, cursor='X_cursor', bd=2, bg='gray55')
        self.servicos_canvas2.place(x=130, y=25)

        self.descrServicos = Label(self.janela, text=self.m_Serviços, fg='gray45', bg=self.fundo_do_frame,
                                   font=('Times', '18', 'bold'))
        self.descrServicos.place(x=15, y=15)

        self.descrCod = Label(self.janela, text=self.m_Codigo + self.m_Pontinhos, fg='darkblue',
                              bg=self.fundo_do_frame, font=('Verdana', '10', 'bold'))
        self.descrCod.place(x=16, y=50)
        self.entradaCod = Entry(self.janela, width=6, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaCod.place(x=80, y=53)

        ###  Botao Carrega servico
        self.botaoAdd = Button(self.janela, text=self.m_Carregar, bg='#37609b', fg='white',
                               font=('Verdana', '8', 'bold'), command=self.carrega_servicoS)
        self.botaoAdd.place(x=135, y=50, width=130)
        ###  Botao limpa servico
        self.botaolimpa = Button(self.janela, text=self.m_Limpar, bg='#37609b', fg='white',
                                 font=('Verdana', '8', 'bold'), command=self.limpa_servicoS)
        self.botaolimpa.place(x=270, y=50, width=70)

        self.descrServ = Label(self.janela, text=self.m_Serviços, fg='darkblue', bg=self.fundo_do_frame,
                               font=('Verdana', '10', 'bold'))
        self.descrServ.place(x=15, y=80)
        self.entradaServ = Entry(self.janela, width=45, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaServ.place(x=80, y=83)

        ###  Botao busca SERVICO
        self.botaolimpa = Button(self.janela, text=self.m_Buscar, bg='#37609b', fg='white',
                                 font=('Verdana', '8', 'bold'), command=self.busca_servicoS)
        self.botaolimpa.place(x=350, y=80, width=50)

        self.descrHor = Label(self.janela, text=self.m_Horas, fg='darkblue', bg=self.fundo_do_frame,
                              font=('Verdana', '10', 'bold'))
        self.descrHor.place(x=24, y=110)
        self.entradaHor = Entry(self.janela, width=5, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaHor.place(x=80, y=113)

        self.descrCustohora = Label(self.janela, text=self.m_Custo_R, fg='darkblue', bg=self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrCustohora.place(x=110, y=110)
        self.entradaCustohora = Entry(self.janela, width=6, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaCustohora.place(x=180, y=113)

        self.descrValorhora = Label(self.janela, text=self.m_Valor_R, fg='darkblue', bg=self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrValorhora.place(x=230, y=110)
        self.entradaValorhora = Entry(self.janela, width=6, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaValorhora.place(x=295, y=113)

        self.descrTipoServ = Label(self.janela, text=self.m_Tipo, fg='darkblue', bg=self.fundo_do_frame,
                                   font=('Verdana', '10', 'bold'))
        self.descrTipoServ.place(x=445, y=40)
        self.entradaTipoServ = Entry(self.janela, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaTipoServ.place(x=525, y=43)

        self.descrSistemaServ = Label(self.janela, text=self.m_Sistema, fg='darkblue', bg=self.fundo_do_frame,
                                      font=('Verdana', '10', 'bold'))
        self.descrSistemaServ.place(x=445, y=60)
        self.entradaSistemaServ = Entry(self.janela, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaSistemaServ.place(x=525, y=63)

        self.descrDescricao = Label(self.janela, text=self.m_Marca, fg='darkblue', bg=self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrDescricao.place(x=445, y=80)
        self.entradaDescricao = Entry(self.janela, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaDescricao.place(x=525, y=83)

        self.descrVeic = Button(self.janela, text=self.m_Veiculo, bg='#37609b', fg='white',
                                command=self.busca_serv_veicS,
                                font=('Verdana', '10', 'bold'))
        self.descrVeic.place(x=445, y=100)
        self.entradaVeic = Entry(self.janela, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaVeic.place(x=525, y=103)

        self.botaoAdd = Button(self.janela, text=self.m_Novo, command=self.add_servS, bg='#37609b', fg='white',
                               font=('Verdana', '10', 'bold'))
        self.botaoAdd.place(x=800, y=50, width=80)

        self.botaoMudServ = Button(self.janela, text=self.m_Alterar, command=self.mud_servS, bg='#37609b', fg='white',
                                   font=('Verdana', '10', 'bold'))
        self.botaoMudServ.place(x=800, y=80, width=80)

        self.botaoDel = Button(self.janela, text=self.m_Apagar, command=self.del_servS, fg='brown',
                               font=('Verdana', '10', 'bold'))
        self.botaoDel.place(x=800, y=110, width=80)

        ### Widgets - Listar veiculos ###

        self.listaServ = ttk.Treeview(self.janela, height=10,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Serviços)
        self.listaServ.heading("#3", text=self.m_Horas)
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.heading("#5", text=self.m_Valor)
        self.listaServ.heading("#6", text=self.m_Marca)
        self.listaServ.heading("#7", text=self.m_Veiculo)
        self.listaServ.heading("#8", text=self.m_Tipo)
        self.listaServ.heading("#9", text=self.m_Sistema)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=230)
        self.listaServ.column("#3", width=45)
        self.listaServ.column("#4", width=57)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=120)
        self.listaServ.column("#7", width=145)
        self.listaServ.column("#8", width=110)
        self.listaServ.column("#9", width=145)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janela, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=960, y=150, width=20, height=230)

        self.conecta_Glac()

        lista = self.cursor.execute("""
            SELECT cod_sp, servprod, hor, custo , valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "s" ORDER BY servprod ASC;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=15, y=150)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickS)

        self.desconecta_Glac()

        self.janela.mainloop()

    def cadprod(self):
        self.multiGlacx()
        self.cores()

        self.janela = Tk()
        self.janela.configure(background=self.fundo_do_frame)
        self.janela.title(self.m_Produtos)
        self.janela.geometry("882x250")
        self.janela.resizable(FALSE, FALSE)

        top3 = Canvas(self.janela, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                      highlightthickness=2);
        top3.place(relx=0, rely=0.96, relwidth=1, relheight=0.07)
        top4 = Canvas(self.janela, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                      highlightthickness=2);
        top4.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        self.vcmd6 = (self.janela.register(self.validate_entry6), "%P")
        self.vcmd8float = (self.janela.register(self.validate_entry8float), "%P")

        self.descrCodprod = Label(self.janela, text=self.m_Codigo + self.m_Pontinhos, fg='darkblue',
                                  bg=self.fundo_do_frame, font=('Verdana', '10'))
        self.descrCodprod.place(x=2, y=5)
        self.entradaCodprod = Entry(self.janela, width=6, fg='brown', validate="key", validatecommand=self.vcmd6,
                                    font=('Verdana', '8', 'bold'))
        self.entradaCodprod.place(x=75, y=8)

        ###  Botao Carrega
        self.botaoAdd = Button(self.janela, text=self.m_Carregar, bd=2, bg='#37609b', fg='white',
                               command=self.carrega_produtoP, font=('Verdana', '9', 'bold'))
        self.botaoAdd.place(x=135, y=2, width=130)
        ###  Botao limpa
        self.botaolimpa = Button(self.janela, text=self.m_Limpar, bd=2, bg='#37609b', fg='white',
                                 command=self.limpa_produtoP, font=('Verdana', '10', 'bold'))
        self.botaolimpa.place(x=275, y=2, width=70, height=28)

        self.descrProd = Label(self.janela, text=self.m_Produtos,
                               font=('Verdana', '9', 'bold'), fg='darkblue', bg=self.fundo_do_frame)
        self.descrProd.place(x=2, y=30)
        self.entradaProd = Entry(self.janela, width=32, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaProd.place(x=75, y=33)

        ###  Botao busca automovel
        self.botaolimpa = Button(self.janela, text=self.m_Buscar, bd=2, bg='#37609b', fg='white',
                                 command=self.busca_produtoP, font=('Verdana', '10', 'bold'))
        self.botaolimpa.place(x=275, y=30, width=70, height=28)

        self.descrIdMarcaprod = Button(self.janela, text=self.m_Marca, font=('Verdana', '10', 'bold'),
                                       bg='#37609b', fg='white', command=self.busca_marcaP)
        self.descrIdMarcaprod.place(x=2, y=62, width=85, height=23)
        self.entradaIdMarcaprod = Entry(self.janela, width=6)
        # entradaIdMarcaprod.place(x=75, y=63)
        self.entradaMarcaprod = Entry(self.janela, width=26, fg='brown', font=('Verdana', '10', 'bold'))
        self.entradaMarcaprod.place(x=86, y=63)

        self.descrIdFornec = Button(self.janela, text=self.m_Fornecedor, font=('Verdana', '10', 'bold'),
                                    bg='#37609b', fg='white', command=self.busca_fornecP)
        self.descrIdFornec.place(x=1, y=92, width=85, height=23)
        self.entradaIdFornec = Entry(self.janela, width=6)
        # entradaIdFornec.place(x=85, y=93)
        self.entradaFornec = Entry(self.janela, width=26, fg='brown', font=('Verdana', '10', 'bold'))
        self.entradaFornec.place(x=86, y=93)

        self.descrCusto = Label(self.janela, text=self.m_Custo_R, fg='darkblue', bg=self.fundo_do_frame,
                                font=('Verdana', '10'))
        self.descrCusto.place(x=2, y=122)
        self.entradaCusto = Entry(self.janela, width=8, fg='brown', font=('Verdana', '10', 'bold'), validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=75, y=123)

        self.descrValor = Label(self.janela, text=self.m_Valor_R, fg='darkblue', bg=self.fundo_do_frame,
                                font=('Verdana', '10'))
        self.descrValor.place(x=150, y=122)
        self.entradaValor = Entry(self.janela, width=8, fg='brown', font=('Verdana', '10', 'bold'), validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaValor.place(x=220, y=123)

        self.descrDescricao = Label(self.janela, text=self.m_Descricao, fg='darkblue', bg=self.fundo_do_frame,
                                    font=('Verdana', '9'))
        self.descrDescricao.place(x=2, y=150)
        self.entradaDescricao = Entry(self.janela, width=40, fg='brown', font=('Verdana', '10', 'bold'))
        self.entradaDescricao.place(x=75, y=153)

        self.botaoAdd = Button(self.janela, text=self.m_Novo, command=self.add_produtoP, bd=2,
                               bg='#37609b', fg='white', font=('Verdana', '10', 'bold'))
        self.botaoAdd.place(x=50, y=180, width=80)

        self.botaoMudServ = Button(self.janela, text=self.m_Alterar, command=self.mud_produtoP, bd=2,
                                   bg='#37609b', fg='white', font=('Verdana', '10', 'bold'))
        self.botaoMudServ.place(x=150, y=180, width=80)

        self.botaoDel = Button(self.janela, text=self.m_Apagar, command=self.del_produtoP, bd=2, fg='brown',
                               font=('Verdana', '10', 'bold'))
        self.botaoDel.place(x=250, y=180, width=80)

        ### Widgets - Listar produtos ###

        self.listaServ = ttk.Treeview(self.janela, height=10, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Produtos)
        self.listaServ.heading("#3", text="")
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.heading("#5", text="")
        self.listaServ.heading("#6", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=39)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=25)
        self.listaServ.column("#4", width=90)
        self.listaServ.column("#5", width=25)
        self.listaServ.column("#6", width=90)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janela, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=830, y=5, width=30, height=230)

        lista = self.cursor.execute("""
            SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
      	    WHERE sp = "P" ORDER BY servprod ASC ;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=360, y=5)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickP)

        self.desconecta_Glac()

        self.janela.mainloop()

    def cadmarcaprod(self):
        self.multiGlacx()
        self.cores()

        self.janelaM = Tk()
        self.janelaM.title(self.m_Marca + ' ' + self.m_Produtos)
        self.janelaM.configure(background=self.fundo_do_frame)
        self.janelaM.geometry("870x250")
        self.janelaM.resizable(FALSE, FALSE)

        self.descrTitulo = Label(self.janelaM, bg=self.fundo_da_tela)
        self.descrTitulo.place(x=1, y=1, width=868, height=55)

        self.descrServicos = Label(self.janelaM, text=self.m_Marca + ' ' + self.m_Produtos, fg='gray75',
                                   bg=self.fundo_da_tela, font=('Times', '22', 'bold'))
        self.descrServicos.place(x=15, y=10)

        self.servicos_canvas2 = Canvas(self.janelaM, width=600, height=2, cursor='X_cursor', bd=2, bg='gray75')
        self.servicos_canvas2.place(x=230, y=25)

        self.descrCod = Label(self.janelaM, text=self.m_Codigo, fg='darkblue', bg=self.fundo_do_frame,
                              font=('Verdana', '10', 'bold'))
        self.descrCod.place(x=18, y=70)
        self.entradaCod = Entry(self.janelaM, width=6, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaCod.place(x=80, y=73)

        ###  Botao Carrega marca
        self.botaoAdd = Button(self.janelaM, text=self.m_Carregar, bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.carrega_marca_prod)
        self.botaoAdd.place(x=135, y=70, width=130)
        ###  Botao limpa automovel
        self.botaolimpa = Button(self.janelaM, text=self.m_Limpar, bd=2, bg='#6d6789', fg='white',
                                 font=('Verdana', '9', 'bold'), command=self.limpa_marca_prod)
        self.botaolimpa.place(x=270, y=70, width=70)

        self.descrMarca = Label(self.janelaM, text=self.m_Marca, fg='darkblue', bg=self.fundo_do_frame,
                                font=('Verdana', '10', 'bold'))
        self.descrMarca.place(x=25, y=100)
        self.entradaMarca = Entry(self.janelaM, width=30, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaMarca.place(x=80, y=103)
        ###  Botao busca automovel
        self.botaobusca = Button(self.janelaM, text=self.m_Buscar, bd=2, bg='#6d6789', fg='white',
                                 font=('Verdana', '9', 'bold'), command=self.busca_marca_prod)
        self.botaobusca.place(x=270, y=100, width=70)

        self.descrDescricao = Label(self.janelaM, text=self.m_Descricao, fg='darkblue', bg=self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrDescricao.place(x=1, y=130)
        self.entradaDescricao = Entry(self.janelaM, width=40, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaDescricao.place(x=80, y=133)

        self.botaoAdd = Button(self.janelaM, text=self.m_Novo, bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.add_marca_prod)
        self.botaoAdd.place(x=50, y=210, width=85)

        self.botaoMud = Button(self.janelaM, text=self.m_Alterar, bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.mud_marca_prod)
        self.botaoMud.place(x=150, y=210, width=85)

        # botaoDel = Button(janelaM, text=" Apagar ", bd=4, fg='darkblue', command=del_marca_prod, font=('Verdana', '10', 'bold'))
        # botaoDel.place(x=250, y=210, width=85)

        ### Widgets - Listar produtos ###

        self.listaServ = ttk.Treeview(self.janelaM, height=7, column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Marca)
        self.listaServ.heading("#3", text=self.m_Descricao)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=35)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=250)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaM, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=845, y=70, width=30, height=180)

        lista = self.cursor.execute("""
            SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=360, y=70)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickMarc)

        self.desconecta_Glac()

        self.janelaM.mainloop()

    def cadforn(self):
        self.multiGlacx();
        self.cores()

        def abre_janela():
            self.janela = Tk()
            self.janela.title(self.m_Fornecedores)
            self.janela.configure(background=self.fundo_do_frame)
            self.janela.geometry("720x290")
            self.janela.resizable(FALSE, FALSE)

            top2 = Canvas(self.janela, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                          highlightthickness=2);
            top2.place(relx=0, rely=0, relwidth=1, relheight=0.04)
            top3 = Canvas(self.janela, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                          highlightthickness=2);
            top3.place(relx=0, rely=0.96, relwidth=1, relheight=0.04)
            top3 = Canvas(self.janela, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                          highlightthickness=2);
            top3.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)

        abre_janela()
        self.provider_obj()

        def widgets():
            #################################################################################################
            #####   Codigo
            self.descrCod_forn.place(x=5, y=20)
            self.entradaCod_forn.place(x=80, y=23)
            ####  Fornecedor
            self.descrFornecedor.place(x=1, y=50)
            self.entradaFornecedor.place(x=80, y=53)
            #### Fone
            self.descrFone.place(x=1, y=80)
            self.entradaFone.place(x=80, y=83)
            ####
            self.descrCnpj.place(x=160, y=80)
            self.entradaCnpj.place(x=200, y=83)
            ####
            self.entradaCep.place(x=80, y=113)
            ####
            self.descrEndereco.place(x=1, y=140)
            self.entradaEndereco.place(x=80, y=143)
            ####
            self.descrMunicipio.place(x=1, y=170)
            self.entradaMunicipio.place(x=80, y=173)
            ####
            self.descrDescricao.place(x=5, y=200)
            self.entradaDescricao.place(x=80, y=203)

        widgets()

        def botoes():
            ###  Botao Carrega fornecedor
            self.botaoCarregarForn.configure(command=self.carrega_fornecedor)
            self.botaoCarregarForn.place(x=120, y=20, width=140)
            ###  Botao limpa fornecedor
            self.botaoLimpaForn.configure(command=self.limpa_fornecedor)
            self.botaoLimpaForn.place(x=270, y=20, width=70)
            ###  Botao busca fornecedor
            self.botaoBuscaForn.configure(command=self.busca_fornecedor)
            self.botaoBuscaForn.place(x=270, y=50, width=70)
            #### Botao Cep
            self.botaoCepForn.configure(command=self.cepForn)
            self.botaoCepForn.place(x=30, y=108, width=50, height=25)
            #### botao novo fornecedor
            self.botaoNovoForn.configure(command=self.add_fornec)
            self.botaoNovoForn.place(x=50, y=240, width=90)
            #### botao alterar fornecedor
            self.botaoAlterarForn.configure(command=self.mud_fornec)
            self.botaoAlterarForn.place(x=150, y=240, width=90)
            ##### botao apagar fornacedor
            self.botaoApagarFornecedor.configure(command=self.del_fornec)
            self.botaoApagarFornecedor.place(x=250, y=240, width=90)

        botoes()
        ### Widgets - Listar veiculos ###
        self.listaServ = ttk.Treeview(self.janela, height=12, column=("col1", "col2", "col3", "col4"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Fornecedores)
        self.listaServ.heading("#3", text=self.m_Fone)
        self.listaServ.heading("#4", text=self.m_Cidade)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=120)
        self.listaServ.column("#3", width=70)
        self.listaServ.column("#4", width=90)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janela, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=678, y=12, width=30, height=268)
        self.listaServ.place(x=355, y=12)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickForn)

        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()
        lista = self.cursor.execute("""
            SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
            """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.janela.mainloop()

    def cadfinan(self):
        self.multiGlacx()
        self.cores()

        self.janela = Tk()
        self.janela.configure(background=self.fundo_da_tela)
        self.janela.title(self.m_Financeiro)
        self.janela.geometry("800x385")
        self.janela.resizable(FALSE, FALSE)

        self.vcmd6 = (self.janela.register(self.validate_entry6), "%P")
        self.vcmd4 = (self.janela.register(self.validate_entry4), "%P")
        self.vcmd2 = (self.janela.register(self.validate_entry2), "%P")
        self.vcmd8float = (self.janela.register(self.validate_entry8float), "%P")

        ###  A B A S

        self.abas = Notebook(self.janela)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)

        self.frame_aba1.configure(background='gray75')
        self.frame_aba2.configure(background='lightgray')

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=385, pady=160)
        self.label2 = Label(self.frame_aba2)
        self.label2.pack(padx=385, pady=160)

        self.abas.add(self.frame_aba1, text=self.m_Receitas)

        self.abas.place(x=10, y=5)

        ####################################################################
        ####  Descrição dos problemas apresentados pelo veiculo - Aba 1
        ####################################################################
        self.frameProb = Frame(self.frame_aba1, width=755, height=320, bd=4, relief=SUNKEN)
        self.frameProb.place(x=10, y=10)

        self.descrCodprod = Label(self.frame_aba1, text='Ano...........', font=('Verdana', '8', 'bold'))
        self.descrCodprod.place(x=14, y=15, width=90)
        self.entradaCodprod = Entry(self.frame_aba1, bd=3, width=4, fg='brown', validate="key",
                                    validatecommand=self.vcmd4, font=('Verdana', '8', 'bold'))
        self.entradaCodprod.place(x=75, y=18)

        self.descrProd = Label(self.frame_aba1, text='Mês...........', font=('Verdana', '8', 'bold'))
        self.descrProd.place(x=14, y=43, width=90)
        self.entradaProd = Entry(self.frame_aba1, width=2, fg='brown', validate="key", validatecommand=self.vcmd2,
                                 bd=3, font=('Verdana', '8', 'bold'))
        self.entradaProd.place(x=75, y=43)

        ###  Botao Carrega
        self.botaoAdd = Button(self.frame_aba1, text=self.m_Carregar, bd=1, command=self.carrega_produto,
                               bg='#6d6789', fg='white', font=('Verdana', '8', 'bold'))
        self.botaoAdd.place(x=25, y=73, width=110, height=25)
        ###  Botao limpa
        self.botaolimpa = Button(self.frame_aba1, text=self.m_Limpar, bd=1, command=self.limpa_produto,
                                 bg='#6d6789', fg='white', font=('Verdana', '8', 'bold'))
        self.botaolimpa.place(x=25, y=103, width=110, height=25)

        ### Widgets - Listar produtos ###
        self.frameProb2 = Frame(self.frame_aba1, bg='gray70', width=565, height=240, bd=4, relief=SUNKEN)
        self.frameProb2.place(x=190, y=13)

        self.listaServ = ttk.Treeview(self.frame_aba1, height=10,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Placa)
        self.listaServ.heading("#3", text=self.m_Dia)
        self.listaServ.heading("#4", text=self.m_Mes)
        self.listaServ.heading("#5", text=self.m_Ano)
        self.listaServ.heading("#6", text="")
        self.listaServ.heading("#7", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=150)
        self.listaServ.column("#3", width=55)
        self.listaServ.column("#4", width=55)
        self.listaServ.column("#5", width=75)
        self.listaServ.column("#6", width=20)
        self.listaServ.column("#7", width=100)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.frame_aba1, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=718, y=17, width=28, height=228)
        self.listaServ.place(x=200, y=18)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickFinan)

        ### Widgets - Listar produtos ###

        self.listaServ2 = ttk.Treeview(self.frame_aba1, height=1,
                                       column=("col1", "col2", "col3"))
        self.listaServ2.heading("#0", text="")
        self.listaServ2.heading("#1", text=self.m_Ano)
        self.listaServ2.heading("#2", text=self.m_Mes)
        self.listaServ2.heading("#3", text=self.m_Total)

        self.listaServ2.column("#0", width=0)
        self.listaServ2.column("#1", width=60)
        self.listaServ2.column("#2", width=60)
        self.listaServ2.column("#3", width=100)

        self.listaServ2.place(x=320, y=270)
        self.janela.mainloop()

    def busca_cliente(self):
        self.listacliente = Tk()
        self.listacliente.title("  GLAC  ")
        self.listacliente.configure(background=self.fundo_da_tela)
        self.listacliente.geometry("342x390")
        self.listacliente.resizable(FALSE, FALSE)

        frame1 = Frame(self.listacliente, bg=self.fundo_do_frame)
        frame1.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.97)

        self.LabelCliente = Label(self.listacliente, bd=0, fg='gray35', bg=self.fundo_do_frame,
                                  text=self.m_BuscaCliMsg1,
                                  font=('Verdana', '8', 'bold'))
        self.LabelCliente.place(relx=0.04, rely=0.01, relwidth=0.9, relheight=0.06)
        self.LabelCliente2 = Label(self.listacliente, bd=0, fg='gray35', bg=self.fundo_do_frame,
                                   text=self.m_BuscaCliMsg2,
                                   font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.04, rely=0.05, relwidth=0.9, relheight=0.05)

        self.LabelCliente2 = Label(self.listacliente, bd=0, fg='gray35', bg=self.fundo_do_frame, text=self.m_Pesquisa
                                                                                                      + self.m_Pontinhos,
                                   font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(x=10, y=46)

        self.EntryCliente2 = Entry(self.listacliente, bd=1, fg='brown', bg='gray90', font=('Verdana', '8'))
        self.EntryCliente2.place(x=80, y=45)

        self.ButtonCliente2 = Button(self.listacliente, bd=2, text=self.m_Buscar, bg='#178bca', fg='white',
                                     font=('Verdana', '8', 'bold'), command=self.buscaCli)
        self.ButtonCliente2.place(x=240, y=43)

        self.listaServ = ttk.Treeview(self.listacliente, height=12, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Nome)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=50)
        self.listaServ.column("#2", width=250)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listacliente, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=310, y=70, width=25, height=265)

        self.listaServ.place(x=7,
                             y=70)
        self.listaServ.bind("<Double-1>",
                            self.carrega_cliente2)

        self.ButtonClienteNovo = Button(self.listacliente,
                                        bd=2,
                                        bg='#178bca',
                                        fg='white', text="Novo",
                                        font=('Verdana', '8', 'bold'),
                                        command=self.cadcli)
        self.ButtonClienteNovo.place(x=10,
                                     y=350)

        self.LabelCliente2 = Label(self.listacliente,
                                   bd=0,
                                   fg='gray35',
                                   bg=self.fundo_do_frame,
                                   text=self.m_BuscaCliMsg3,
                                   font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.2,
                                 rely=0.88,
                                 relwidth=0.75,
                                 relheight=0.05)
        self.LabelCliente2 = Label(self.listacliente,
                                   bd=0,
                                   fg='gray35',
                                   bg=self.fundo_do_frame,
                                   text=self.m_BuscaCliMsg4,
                                   font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.2,
                                 rely=0.93,
                                 relwidth=0.75,
                                 relheight=0.05)

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        nome = self.listNome.get()
        nomecod = cursor

        lista = cursor.execute("""SELECT cod_cli, nome FROM clientes """)
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        conn.close()

    def busca_servico(self):
        # Listar Produtos e Serviços
        self.listaServP1 = Tk()
        self.listaServP1.title(self.m_PesquisaServProd)
        self.listaServP1.geometry("950x280")
        self.listaServP1.configure(background=self.fg_label)
        self.listaServP1.resizable(FALSE, FALSE)

        self.barra12 = Scrollbar(self.listaServP1,
                                 orient='vertical',
                                 command=self.OnVsb_S1)
        self.barra12.place(x=920,
                           y=41,
                           width=25,
                           height=226)

        self.listaServ1 = ttk.Treeview(self.listaServP1,
                                       height=10,
                                       yscrollcommand=self.barra12.set,
                                       column=("col1",
                                               "col2",
                                               "col3",
                                               "col4",
                                               "col5",
                                               "col6",
                                               "col7",
                                               "col8"))

        self.listaServ1.heading("#0",
                                text="")
        self.listaServ1.column("#0",
                               width=0)
        self.listaServ1.heading("#1",
                                text=self.m_Codigo)
        self.listaServ1.column("#1",
                               width=45)
        self.listaServ1.heading("#2", text=self.m_Serviços + self.m_barra + self.m_Produtos);
        self.listaServ1.column("#2", width=250)
        self.listaServ1.heading("#3", text=self.m_Tipo);
        self.listaServ1.column("#3", width=120)
        self.listaServ1.heading("#4", text=self.m_Quant);
        self.listaServ1.column("#4", width=50)
        self.listaServ1.heading("#5", text=self.m_Marca);
        self.listaServ1.column("#5", width=90)
        self.listaServ1.heading("#6", text=self.m_Automovel);
        self.listaServ1.column("#6", width=140)
        self.listaServ1.heading("#7", text=self.m_Sistema);
        self.listaServ1.column("#7", width=140)
        self.listaServ1.heading("#8", text=self.m_Valor);
        self.listaServ1.column("#8", width=70)

        self.listaServ1.place(x=15, y=40)
        self.listaServ1.configure(yscroll=self.barra12.set)
        self.listaServ1.delete(*self.listaServ1.get_children())

        self.descrCod_cli = Label(self.listaServP1,
                                  text=self.m_Pesquisa + self.m_Pontinhos,
                                  fg=self.fg_label,
                                  bg=self.bg_label,
                                  font=('Verdana', '8', 'bold'))\
        self.descrCod_cli.place(x=20,
                                y=7,
                                height=30)
        self.listaServicos1 = Entry(self.listaServP1,
                                    width=20,
                                    justify='right',
                                    bd=3,
                                    fg='brown',
                                    font=('Verdana', '12', 'bold'))
        self.listaServicos1.place(x=120,
                                  y=7,
                                  height=30)

        self.botaoBuscaServicos1 = Button(self.listaServP1,
                                          text=self.m_BuscaServProd,
                                          bd=2,
                                          bg='#178bca',
                                          fg='white',
                                          font=('Verdana', '9', 'bold'),
                                          command=self.busca_serv)
        self.botaoBuscaServicos1.place(x=350,
                                       y=7,
                                       width=200,
                                       height=30)

        self.botaoBuscaServicos2 = Button(self.listaServP1,
                                          text=self.m_BuscaVeiculos,
                                          bd=2,
                                          bg='#178bca',
                                          fg='white',
                                          font=('Verdana', '9', 'bold'),
                                          command=self.busca_serv_veic)
        self.botaoBuscaServicos2.place(x=570,
                                       y=7,
                                       width=120,
                                       height=30)
        servprod = self.listaServicos1.get()

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
            FROM servprod ORDER BY cod_sp ASC""")
        buscaservico12 = cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)
        conn.close()

    def busca_tecnico(self):
        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()
        ### Widgets - Listar tecnicos ###
        self.entradaTecnico.delete(0, END)
        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("360x160")
        self.listatec.resizable(TRUE, TRUE)

        self.listaServ = ttk.Treeview(self.listatec, height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Tecnico)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=280)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=325, y=5, width=30, height=145)

        self.listaServ.place(x=5, y=5)

        lista = cursor.execute("""
                SELECT cod, tecnico FROM tecnico ORDER BY cod ASC;
                """)
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        # Binding da listbox
        self.listaServ.bind('<Double-1>', self.add_tecnicobind)
        conn.close()

    def procedServ(self):
        ### Widgets - Listar Orçamentos ###
        self.listaOrc = Tk()
        self.listaOrc.title(" GLAC  ")
        self.listaOrc.configure(background='gray90', bd=6)
        self.listaOrc.geometry("260x100")
        self.listaOrc.resizable(FALSE, FALSE)

        self.MensLabel = Label(self.listaOrc, text=self.m_AtualizaMsg)
        self.MensLabel.place(x=10, y=10)

        self.listaNomeO = Entry(self.listaOrc, width=6, justify='right', bd=0, fg='#5c2f01',
                                font=('Verdana', '12', 'bold'))
        self.listaNomeO.place(x=10, y=60)

        self.botaoBuscaNome = Button(self.listaOrc, text=self.m_Atualizar, bd=1, bg='#178bca',
                                     fg='white', font=('verdana', '10', 'bold'), command=self.procedServF)
        self.botaoBuscaNome.place(x=100, y=60, width=80, height=25)

    def busca_orc(self):
        ### Widgets - Listar Orçamentos ###
        self.listaOrc = Tk();
        self.listaOrc.title(" GLAC  ");
        self.listaOrc.configure(background=self.fg_label, bd=6)
        self.listaOrc.geometry("640x360");
        self.listaOrc.resizable(FALSE, FALSE)

        self.cliente_canvas2 = Canvas(self.listaOrc, width=600, height=60, cursor='X_cursor', bg=self.fundo_do_frame,
                                      highlightbackground=self.borda_frame, highlightthickness=3);
        self.cliente_canvas2.place(x=10, y=1)

        self.listaNomeO = Entry(self.listaOrc, width=20, justify='right', bd=2, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '12', 'bold'));
        self.listaNomeO.place(x=140, y=7)

        self.botaoBuscaNome = Button(self.listaOrc, text=self.m_Buscar + " " + self.m_Nome, bd=1, bg=self.bg_button,
                                     fg='white', font=('verdana', '10', 'bold'), command=self.buscanomeorc)
        self.botaoBuscaNome.place(x=370, y=6, width=110, height=25)

        self.listaPlaca = Entry(self.listaOrc, width=20, justify='right', bd=2, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '12', 'bold'));
        self.listaPlaca.place(x=140, y=37)

        self.botaoBuscaPlaca = Button(self.listaOrc, text=self.m_Buscar + ' ' + self.m_Placa, bd=1, bg=self.bg_button,
                                      fg='white', font=('Verdana', '10', 'bold'), command=self.buscaplacaorc)
        self.botaoBuscaPlaca.place(x=370, y=36, width=110, height=25)

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        ### Widgets - Listar veiculos ###

        self.listaServ = ttk.Treeview(self.listaOrc, height=12,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Orcamento)
        self.listaServ.heading("#2", text=self.m_Nome)
        self.listaServ.heading("#3", text=self.m_Dia)
        self.listaServ.heading("#4", text=self.m_Mes)
        self.listaServ.heading("#5", text=self.m_Ano)
        self.listaServ.heading("#6", text=self.m_Placa)
        self.listaServ.heading("#7", text=self.m_Tipo)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=35)
        self.listaServ.column("#4", width=35)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=80)
        self.listaServ.column("#7", width=137)
        # Cria barra de rolagem
        self.barra = Scrollbar(self.listaOrc, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=595, y=70, width=30, height=270)

        self.listaServ.place(x=10, y=70)

        self.listaServ.bind("<Double-1>", self.carrega_orc)

        lista = cursor.execute("""
                SELECT id_orc1, clientes.nome, dia , mes , ano, placa_orc, tipoOrc FROM orcamento1, clientes WHERE cod_cli =
                cliente_orc ORDER BY id_orc1 DESC;
                """)
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        # self.listaO.delete(0, END)
        conn.close()

        def busca_orc_a(event):
            busca_orc()

    def pagaOrdem(self):
        conn = sqlite3.connect("glac.db");
        cursor = conn.cursor()
        numAt = self.listaNumOrc.get()

        self.janela = Tk();
        self.janela.title("GlacX");
        self.janela.configure(background=self.fundo_da_tela);
        self.janela.geometry("800x495");
        self.janela.resizable(FALSE, FALSE)
        ### Label principal
        self.labelformapag = Label(self.janela, text=self.m_Forma)
        self.labelformapag.configure(bg=self.fundo_da_tela, fg=self.bg_entry, font=('Comic', '18', 'bold', 'italic'))
        self.labelformapag.place(relx=0.35, rely=0)
        ###  Frame Moldura
        self.frame1 = Frame(self.janela);
        self.frame1.configure(background=self.fg_label)
        self.frame1.place(relx=0, rely=0.1, relwidth=1, relheight=1)
        self.frame2 = Frame(self.frame1, bd=4, bg=self.bg_button)
        self.frame2.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
        self.frame3 = Frame(self.frame2, bd=4, bg=self.fundo_do_frame, relief=SUNKEN)
        self.frame3.place(relx=0.02, rely=0.02, relwidth=1, relheight=1)
        ### Frame do Numero do Atendimento e Valor Total
        self.frameAt = Frame(self.frame3, bg=self.bg_button)
        self.frameAt.place(relx=0, rely=0, width=205, height=44)
        self.frameAt2 = Frame(self.frame3, bg=self.fundo_do_frame)
        self.frameAt2.place(relx=0.002, rely=0.002, width=202, height=42)
        ## Label do numero de atendimento
        self.labelNumAtend = Label(self.frame3, text=self.m_NumAtend)
        self.labelNumAtend.configure(fg=self.fg_label, font=('Verdana', '8', 'bold'), bg=self.fundo_do_frame)
        self.labelNumAtend.place(relx=0.006, rely=0.006)
        #### Entry do numero de atendimento
        self.entryNumAtend = Listbox(self.frame3, height=1)
        self.entryNumAtend.configure(bd=1, fg='brown', bg='lightgray', width='10', font=('Verdana', '8', 'bold'))
        self.entryNumAtend.place(relx=0.15, rely=0.006);
        self.entryNumAtend.insert(END, numAt)
        #### Label do valor total
        self.labelValorTotal = Label(self.frame3, fg=self.fg_label)
        self.labelValorTotal.configure(text=self.m_Valor + ' ' + self.m_Total,
                                       font=('Verdana', '8', 'bold'), bg=self.fundo_do_frame)
        self.labelValorTotal.place(relx=0.006, rely=0.05)
        #### Entry do valor total
        valorT = self.entradatotal.get()
        self.entryValorTotal = Entry(self.frame3, bd=1, fg='brown', bg='lightgray')
        self.entryValorTotal.configure(width='10', font=('Verdana', '8', 'bold'))
        self.entryValorTotal.place(relx=0.15, rely=0.05);
        self.entryValorTotal.insert(END, self.totalsimples)
        #### Frame do Valor a ser inserido
        self.frameValor = Frame(self.frame3, bg=self.bg_label)
        self.frameValor.place(relx=0.448, rely=0.018, width=100, height=36)
        self.frameValor = Frame(self.frame3, bg=self.bg_label)
        self.frameValor.place(relx=0.45, rely=0.02, width=97, height=34)
        ### Label do valor a ser inserido
        self.labelValor = Label(self.frame3, text=self.m_Valor)
        self.labelValor.configure(fg=self.fg_label, font=('Verdana', '8', 'bold'), bg=self.fg_button)
        self.labelValor.place(relx=0.45, rely=0.02, width=90)
        self.labelCifrao = Label(self.frame3, text=self.m_Reais)
        self.labelCifrao.configure(fg=self.fg_label, font=('Verdana', '8', 'bold'), bg=self.fg_button)
        self.labelCifrao.place(relx=0.45, rely=0.05)
        #### Entry do valor a ser inserido
        self.entryValor = Entry(self.frame3, bd=1, fg='brown')
        self.entryValor.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValor.place(relx=0.48, rely=0.055);
        self.entryValor.insert(END, '0.00')
        #### Frame do tipo de pagamento
        self.frametipopag = Frame(self.frame3, bg=self.bg_button)
        self.frametipopag.place(relx=0.586, rely=0, width=105, height=48)

        #### Listbox do tipo de pagamento
        self.entrytipopag = Frame(self.frame3, bd=0, bg=self.fg_button, width=2)
        self.entrytipopag.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrytipopag.columnconfigure(0, weight=1)
        self.entrytipopag.rowconfigure(0, weight=1)
        self.entrytipopag.place(relx=0.588, rely=0.003, width=100, height=45)
        self.listtipopag = StringVar(self.frame3)
        self.listtipopagV = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto,
                             self.m_ChequePre, self.m_ChequeVista, self.m_Crediario, self.m_Promissoria,
                             self.m_Desconto, self.m_Avista}
        self.listtipopagV = sorted(self.listtipopagV)
        self.listtipopag.set(self.m_Dinheiro)
        self.popupMenu = OptionMenu(self.entrytipopag, self.listtipopag, *self.listtipopagV)
        Label(self.entrytipopag, bd=0).grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)
        #### Label do tipo de pagamento
        self.labeltipopag = Label(self.frame3, text=self.m_Tipo + ' ' + self.m_Pagamento)
        self.labeltipopag.configure(fg=self.fg_label, font=('Verdana', '7', 'bold'), bg=self.fg_button)
        self.labeltipopag.place(relx=0.60, rely=0.003)
        #### Data frame
        self.framedata = Frame(self.frame3, bg=self.bg_button)
        self.framedata.place(relx=0.718, rely=0, width=98, height=48)
        self.framedata = Frame(self.frame3, bg=self.fg_button)
        self.framedata.place(relx=0.72, rely=0.003, width=95, height=45)
        #### Entry data
        self.entrydia = Frame(self.frame3, bd=0, bg=self.fg_label, width=2)
        self.entrydia.grid(column=0, row=0, sticky=(N, W, E, S));
        self.entrydia.columnconfigure(0, weight=1)
        self.entrydia.rowconfigure(0, weight=1);
        self.entrydia.place(relx=0.72, rely=0.003, width=30, height=45)
        self.diavar = StringVar(self.frame3)
        self.diasV = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                      '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                      '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
        self.diasV = sorted(self.diasV);
        self.diavar.set('01')
        self.popupMenu = OptionMenu(self.entrydia, self.diavar, *self.diasV)
        Label(self.entrydia, bd=0).grid(row=1, column=1);
        self.popupMenu.grid(row=2, column=1)

        self.entrymes = Frame(self.frame3, bd=0, bg='azure3', width=2)
        self.entrymes.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrymes.columnconfigure(0, weight=1)
        self.entrymes.rowconfigure(0, weight=1)
        self.entrymes.place(relx=0.75, rely=0.003, width=30, height=45)
        self.mesvar = StringVar(self.frame3)
        self.mesesV = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                       '11', '12'}
        self.mesesV = sorted(self.mesesV)
        self.mesvar.set('01')
        self.popupMenu = OptionMenu(self.entrymes, self.mesvar, *self.mesesV)
        Label(self.entrymes, bd=0).grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        self.entryano = Frame(self.frame3, bd=0, bg='azure3', width=2)
        self.entryano.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entryano.columnconfigure(0, weight=1)
        self.entryano.rowconfigure(0, weight=1)
        self.entryano.place(relx=0.78, rely=0.003, width=40, height=45)
        self.anovar = StringVar(self.frame3)
        self.anosV = {'2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                      '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV = sorted(self.anosV)
        self.anovar.set('2019')
        self.popupMenu = OptionMenu(self.entryano, self.anovar, *self.anosV)
        Label(self.entryano, bd=0).grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)
        #### Data label
        self.labeldata = Label(self.frame3, text=self.m_Data, fg=self.fg_label)
        self.labeldata.configure(bg=self.fg_button, font=('Verdana', '8', 'bold'))
        self.labeldata.place(relx=0.72, rely=0.002, width=95, height=18)
        #### Button Inserir Registro
        self.btinserir = Button(self.frame3, text=self.m_Inserir, command=self.add_pag)
        self.btinserir.place(relx=0.85, rely=0.04)
        ### Widgets - Listar pagamentos ###
        ### Frame lista
        self.framelista = Frame(self.frame3, bg=self.fg_label)
        self.framelista.place(relx=0.024, rely=0.113, width=745, height=318)
        self.framelista = Frame(self.frame3, bg=self.bg_label)
        self.framelista.place(relx=0.026, rely=0.115, width=742, height=315)
        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.frame3, height=14,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.listaPag.heading("#0", text="");
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text=self.m_Ordem);
        self.listaPag.column("#1", width=50)
        self.listaPag.heading("#2", text=self.m_Tipo);
        self.listaPag.column("#2", width=170)
        self.listaPag.heading("#3", text=self.m_Valor + ' ' + self.m_Pagamento);
        self.listaPag.column("#3", width=120)
        self.listaPag.heading("#4", text=self.m_ValorDeduzir);
        self.listaPag.column("#4", width=120)
        self.listaPag.heading("#5", text=self.m_Dia);
        self.listaPag.column("#5", width=50)
        self.listaPag.heading("#6", text=self.m_Mes);
        self.listaPag.column("#6", width=50)
        self.listaPag.heading("#7", text=self.m_Mes);
        self.listaPag.column("#7", width=50)
        self.listaPag.heading("#8", text=self.m_Pago);
        self.listaPag.column("#8", width=100)
        self.listaPag.heading("#9", text="");
        self.listaPag.column("#9", width=1)
        self.listaPag.place(relx=0.03, rely=0.12)
        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame3, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.917, rely=0.12, width=38, height=310)

        self.listaPag.bind("<Double-1>", self.OnDoubleClickpag);
        self.listaPag.configure(yscroll=self.barraMov.set)
        ### Label do saldo a ser pago
        self.labelValor = Label(self.frame3, text=self.m_ValorDevido)
        self.labelValor.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelValor.place(x=600, y=375)
        self.labelCifrao = Label(self.frame3, text="R$")
        self.labelCifrao.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelCifrao.place(x=600, y=395)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(self.frame3, bd=1, fg='brown')
        self.entryValorDevido.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValorDevido.place(x=620, y=395)

        ### Label do saldo ja pago
        self.labelValor = Label(self.frame3, text=self.m_ValorInformado)
        self.labelValor.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelValor.place(x=460, y=375)
        self.labelCifrao = Label(self.frame3, text=self.m_Reais)
        self.labelCifrao.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelCifrao.place(x=460, y=395)

        #### Entry do saldo ja pago
        self.entryValorInform = Entry(self.frame3, bd=1, fg='brown')
        self.entryValorInform.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValorInform.place(x=480, y=395)

        lista = cursor.execute("""
                           SELECT  ordem, tipopag, valorpagar, valordeduzir, dia, mes, ano, pago, id
                            FROM formapag WHERE ordem = '%s'   ORDER BY id ASC;
                           """ % numAt)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = cursor.execute("""
                                   SELECT SUM(valordeduzir) FROM formapag WHERE ordem = '%s'   ORDER BY id ASC;
                                   """ % numAt)
        for i in informe:
            self.entryValorInform.insert(END, i)

        rest1 = self.entryValorTotal.get()
        rest1 = float(rest1)
        rest2 = self.entryValorInform.get()
        rest2 = float(rest2)
        restante = rest1 - rest2
        # restante = self.entryValorDevido.get()
        self.entryValorDevido.insert(END, restante)

        conn.close()
        self.janela.mainloop()

    def busca_falha(self):
        ### Widgets - Listar Produtos e Serviços ###
        self.conecta_Glac()
        self.listaServP1F = Tk();
        self.listaServP1F.title(self.m_Pesquisa)
        self.listaServP1F.geometry("890x280");
        self.listaServP1F.resizable(FALSE, FALSE)
        self.listaServP1F.configure(background=self.bg_label)

        self.barra12F = Scrollbar(self.listaServP1F, orient='vertical', command=self.OnVsb_S1F)
        self.barra12F.place(x=850, y=47, width=25, height=230)

        self.listaServ1F = ttk.Treeview(self.listaServP1F, height=10, yscrollcommand=self.barra12F.set,
                                        column=("col1", "col2", "col3"))
        self.listaServ1F.heading("#0", text="")
        self.listaServ1F.heading("#1", text=self.m_Codigo)
        self.listaServ1F.heading("#2", text=self.m_Falhas)
        self.listaServ1F.heading("#3", text=self.m_Obs)

        self.listaServ1F.column("#0", width=0)
        self.listaServ1F.column("#1", width=80)
        self.listaServ1F.column("#2", width=395)
        self.listaServ1F.column("#3", width=350)
        self.listaServ1F.place(x=15, y=40)
        self.listaServ1F.configure(yscroll=self.barra12F.set)
        self.listaServ1F.delete(*self.listaServ1F.get_children())
        self.descrCod_cliF = Label(self.listaServP1F, text=self.m_Pesquisa, fg=self.fg_label, bg=self.bg_label,
                                   font=('Verdana', '8', 'bold'))
        self.descrCod_cliF.place(x=35, y=7)
        self.listaServicos1F = Entry(self.listaServP1F, width=20, justify='right', bd=3, fg='brown',
                                     font=('Verdana', '12', 'bold'))
        self.listaServicos1F.place(x=120, y=7)

        self.botaoBuscaServicos1F = Button(self.listaServP1F, text=self.m_Buscar, bd=3, bg=self.bg_button,
                                           fg='white', font=('Verdana', '7', 'bold'), command=self.busca_servF)
        self.botaoBuscaServicos1F.place(x=350, y=7, width=110)
        servprodF = self.listaServicos1F.get()
        self.cursor.execute(
            """SELECT cod_falha, falha, falha2 FROM codfalha ORDER BY cod_falha ASC""")
        buscaservico12F = self.cursor.fetchall()
        for i in buscaservico12F:
            self.listaServ1F.insert("", END, values=i)
        self.desconecta_Glac()

    def calendarioInicio(self):
        self.multiGlacx()
        self.cores()

        self.calendario1 = Calendar(self.top3, fg='gray75', bg=self.fundo_da_tela, font=('Times', '9', 'bold'))
        self.calendario1.place(x=140, y=30)

        self.calDataInicio = Button(self.top3, text='Inserir', command=self.print_calInicio,
                                    fg='gray35', font=('Times', '10', 'bold'))

        self.calDataInicio.place(x=140, y=215, height=25, width=150)

    def print_calInicio(self):
        dataInicio = self.calendario1.get_date()
        self.calendario1.destroy()
        self.listInicio.delete(0, END)
        self.listInicio.insert(END, dataInicio)
        self.calDataInicio.destroy()

    def calendarioFim(self):
        self.multiGlacx()
        self.cores()
        self.calendario2 = Calendar(self.top3,
                                    text=self.m_Estab,
                                    fg='gray75',
                                    bg=self.fundo_da_tela,
                                    font=('Times', '9', 'bold'))
        self.calendario2.place(x=300, y=50)

        self.calDataFim = Button(self.top3, text='Inserir', command=self.print_calFim,
                                 fg='gray35', font=('Times', '10', 'bold'))
        self.calDataFim.place(x=300, y=235, height=25)

    def print_calFim(self):
        dataFim = self.calendario2.get_date()
        self.listFim.delete(0, END)
        self.listFim.insert(END, dataFim)
        self.calendario2.destroy()
        self.calDataFim.destroy()
