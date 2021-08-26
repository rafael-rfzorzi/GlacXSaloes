from funcs.modulos import *
from Janelas.estiloWidgets.gradienteFrame import *
from Janelas.estiloWidgets.autcomplety import *

class Molduras:
    def molduras(self):
        ### Moldura dos dados do cliente
        self.FrameCliente = Frame(self.top2, bg="#C6CCFF", relief="sunken")
        self.FrameCliente.place(relx=0.02, rely=0.02, relwidth=0.975, relheight=0.96)

        self.FrameAbas = GradientFrame(self.top3, borderwidth=1, relief="sunken");
        self.FrameAbas.place(relx=0, rely=0, relwidth=1, relheight=1)
        ######################
        self.FrameTec = GradientFrame(self.top4, borderwidth=1, relief="sunken");
        self.FrameTec.place(relx=0, rely=0, relwidth=1, relheight=1)
        ######################
