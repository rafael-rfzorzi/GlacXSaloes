from funcs.modulos import *
from Janelas.estiloWidgets.entryPlaceHolder import *
from Janelas.estiloWidgets.buttonStyle import *
from Janelas.estiloWidgets.labelStyle import *

class SegundoFrame:
    def segundo_frame(self):
        # Container de cadastro do cliente
        codigo_cliente = LabelGlac(self.FrameCliente)
        codigo_cliente.configure(text='Cod', font=('Verdana', 8, 'bold'))
        codigo_cliente.place(relx=0, rely=0.04, relwidth=0.13, relheight=0.17)
        # Entrada do Codigo do Cliente
        self.entradaCod_cli = Entry(self.FrameCliente,
                                    validate="key", validatecommand=self.vcmd6)
        self.entradaCod_cli.place(relx=0.1, rely=0.04, relwidth=0.13, relheight=0.17)

        # Botão Carrega
        self.botaoAdd = ButtonGlac(self.FrameCliente)
        self.botaoAdd.configure(text=self.m_Buscar, command=self.busca_cliente)
        self.botaoAdd.place(relx=0.34, rely=0.011, relwidth=0.17, relheight=0.21)

        # Botão Limpa
        self.botaoLimp = ButtonGlac(self.FrameCliente)
        self.botaoLimp.configure(text=self.m_Limpar, command=self.limpa_cliente)
        self.botaoLimp.place(relx=0.52, rely=0.011, relwidth=0.17, relheight=0.21)

        # Variavel do dia de hoje
        self.hj = date.today()
        # Label data
        self.descrData = LabelGlac(self.FrameCliente)
        self.descrData.configure(text=self.m_Data)
        self.descrData.place(relx=0.7, rely=0.04, relwidth=0.1, relheight=0.17)

        # Entrada Dia
        self.entradaDataorc = EntPlaceHold(self.FrameCliente, self.hj.day)
        self.entradaDataorc.configure(width=2, validate="key",
                                      validatecommand=self.vcmd2, fg='darkred', bg=self.bg_entry,
                                      font=('Verdana', '8', 'bold'))
        self.entradaDataorc.place(relx=0.8, rely=0.04, relwidth=0.05,
                                  relheight=0.17)
        # Entrada Mês
        self.entradaDataorc2 = Entry(self.FrameCliente, width=2,
                                     validate="key", font=('Verdana', '8', 'bold'))
        self.entradaDataorc2.configure(validatecommand=self.vcmd2,
                                       bg=self.bg_entry, justify='right', fg='darkred')
        self.entradaDataorc2.place(relx=0.85, rely=0.04,
                                   relwidth=0.05, relheight=0.17)
        self.entradaDataorc2.insert(END, self.hj.month)
        # Entrada Ano
        self.entradaDataorc3 = Entry(self.FrameCliente,
                                     font=('Verdana', '8', 'bold'), fg='darkred')
        self.entradaDataorc3.configure(width=4, validate="key",
                                       bg=self.bg_entry, validatecommand=self.vcmd4)
        self.entradaDataorc3.place(relx=0.9, rely=0.04,
                                   relwidth=0.08, relheight=0.17)
        self.entradaDataorc3.insert(END, self.hj.year)

        # Entrada do nome do cliente
        self.lbNome = LabelGlac(self.FrameCliente)
        self.lbNome.configure(text='Nome',
                              font=('Verdana', 8, 'bold'))
        self.lbNome.place(relx=0, rely=0.24,
                          relwidth=0.2, relheight=0.15)

        self.listNome = Entry(self.FrameCliente)
        self.listNome.place(relx=0.2, rely=0.24,
                            relwidth=0.8, relheight=0.15)

        # Entrada do Endereço
        self.lbEndereco = LabelGlac(self.FrameCliente)
        self.lbEndereco.configure(text='Logradouro',
                                  font=('Verdana', 8, 'bold'))
        self.lbEndereco.place(relx=0, rely=0.39, relwidth=0.2, relheight=0.15)

        self.listEndereco = Entry(self.FrameCliente)
        self.listEndereco.place(relx=0.2, rely=0.39, relwidth=0.8, relheight=0.15)

        # Entrada Bairro
        self.listBairro = Entry(self.FrameCliente)
        self.listBairro.place(relx=0.2, rely=0.54, relwidth=0.35, relheight=0.15)

        # Entrada Municipio
        self.listMunicipio = Entry(self.FrameCliente)
        self.listMunicipio.place(relx=0.6, rely=0.54, relwidth=0.3, relheight=0.15)

        # Entrada UF
        self.listUf = Entry(self.FrameCliente)
        self.listUf.place(relx=0.92, rely=0.54, relwidth=0.08, relheight=0.15)

        # Entrada CPF CNPJ
        self.lbCpfCnpj = LabelGlac(self.FrameCliente)
        self.lbCpfCnpj.configure(text='Cpf/Cnpj', font=('Verdana', 8, 'bold'))
        self.lbCpfCnpj.place(relx=0, rely=0.69, relwidth=0.15, relheight=0.15)

        self.listCpf = Entry(self.FrameCliente)
        self.listCpf.place(relx=0.15, rely=0.69, relwidth=0.35, relheight=0.15)

        # Entrada Fone
        self.lbFone = LabelGlac(self.FrameCliente)
        self.lbFone.configure(text='Fone', font=('Verdana', 8, 'bold'))
        self.lbFone.place(relx=0.5, rely=0.69, relwidth=0.1, relheight=0.15)

        self.listFone = Entry(self.FrameCliente)
        self.listFone.place(relx=0.6, rely=0.69, relwidth=0.35, relheight=0.15)

        # Entrada OBS
        self.lbObs = LabelGlac(self.FrameCliente)
        self.lbObs.configure(text='Observação', font=('Verdana', 8, 'bold'))
        self.lbObs.place(relx=0, rely=0.84, relwidth=0.15, relheight=0.15)

        self.listObs = Entry(self.FrameCliente)
        self.listObs.place(relx=0.15, rely=0.84, relwidth=0.8, relheight=0.15)

        # List de placas
        self.entradaCod_aut = Listbox(width=1, height=1)
        # Placa
        self.placa = Entry()
        self.listAno = Entry()
        self.listAut = Entry()
        self.listMarca = Entry()
        self.listCombustivel = Entry()
        self.entradaObs = Entry()
        self.listCor = Entry()
