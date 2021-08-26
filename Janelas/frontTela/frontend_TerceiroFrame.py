from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class TerceiroFrame:
    def terceiro_frame(self):
        ##########################################################################################################
        # A B A S
        self.abas = ttk.Notebook(self.FrameAbas)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)

        self.frame_aba1.configure(background=self.fundo_do_frame)
        self.frame_aba2.configure(background=self.fundo_do_frame)

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=850, pady=225)

        self.abas.add(self.frame_aba1, text=self.m_Aba3)
        self.abas.add(self.frame_aba2, text=self.m_Aba1)

        self.abas.pack(side="bottom")
