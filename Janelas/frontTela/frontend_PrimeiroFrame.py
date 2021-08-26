from funcs.modulos import *
from Janelas.estiloWidgets.autcomplety import *

class PrimeiroFrame:
    def primeiro_frame(self):
        #### Botoes
        self.cadcliBt = self.cadcliBt.subsample(2,2)
        self.ClientBot = Button(self.top,
                                bd=0,image=self.cadcliBt,
                                command=self.cadcli)
        self.ClientBot.place(relx=0.03, rely=0.2,
                             width= 50, height= 43)

        self.cadfornecBt = self.cadfornecBt.subsample(2,2)
        self.FornecBot = Button(self.top, bd=0,image=self.cadfornecBt, command=self.cadforn)
        self.FornecBot.place(relx=0.09, rely=0.2, width= 50, height= 43)

        self.cadprodBt = self.cadprodBt.subsample(2, 2)
        self.ProdutosBot = Button(self.top, bd=0,image=self.cadprodBt,command=self.cadprod);
        self.ProdutosBot.place(relx=0.21, rely=0.2, width= 50, height= 43)

        self.cadservBt = self.cadservBt.subsample(2, 2)
        self.ServBot = Button(self.top, bd=0,image=self.cadservBt,command=self.cadserv);
        self.ServBot.place(relx=0.27, rely=0.2, width= 50, height= 43)
