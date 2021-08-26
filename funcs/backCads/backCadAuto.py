from Janelas.estiloWidgets.autcomplety import *

class CadAuto():
    def variaveisA(self):
        self.cod_aut = self.entradaCod_autA.get()
        self.automovel = self.entradaAutA.get()
        self.montad = self.entradaMarca2A.get()
    def add_automovelA(self):
        self.variaveisA()
        self.conecta_Glac()
        if self.montad == '':
            msg = "É necessário escolher a marca do "
            msg += " automovel a ser cadastrado."
            messagebox.showinfo("GLAC - Automovel", msg)
            self.desconecta_Glac()
        else:
            self.cursor.execute("""
                INSERT INTO automoveis ( automovel, montad)
                VALUES ( ?, ?)""", (self.automovel, self.montad))
            self.conn.commit()
            self.desconecta_Glac()
            self.limpa_automovelA()
            self.busca_automovelA()
            msg = self.m_msgAutAdd
            msg += ""
            messagebox.showinfo("GLAC - Automovel", msg)
    def mud_automovelA(self):
        self.variaveisA()
        self.conecta_Glac()

        self.cursor.execute("""
       		UPDATE automoveis SET automovel = ? WHERE cod_aut = ?""",
            (self.automovel, self.cod_aut))
        self.conn.commit()

        self.cursor.execute("""
       		UPDATE automoveis SET montad = ? WHERE cod_aut = ?""",
            (self.montad, self.cod_aut))
        self.conn.commit()
        self.desconecta_Glac()

        self.busca_automovelA()

        msg = self.m_msgAutAlt
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def del_automovelA(self):
        self.variaveisA()
        self.conecta_Glac()

        self.cursor.execute(""" DELETE FROM automoveis 
            WHERE cod_aut=?;""", (self.cod_aut,))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor
        self.cursor.execute("""
            SELECT automoveis.cod_aut, automoveis.automovel, montadora.marca 
            FROM automoveis, montadora
       		WHERE montadora.cod = automoveis.montad  
       		ORDER BY automovel ASC;
       		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.limpa_automovelA()
        msg = self.m_msgAutDel
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def carrega_automovelA(self):
        cod_aut = self.entradaCod_autA.get()
        self.conecta_Glac()

        nomeaut = self.cursor

        self.entradaAutA.delete('0', 'end')
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')

        nomeaut.execute(
            "SELECT automovel FROM automoveis, montadora "
            "WHERE montadora.cod = automoveis.montad "
            "AND cod_aut = '%s'" % cod_aut)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaAutA.insert(0, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT marca FROM automoveis, montadora "
            "WHERE montadora.cod = automoveis.montad "
            "AND cod_aut = '%s'" % cod_aut)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarcaA.insert(0, i)

        nomemarca2 = self.cursor
        nomemarca2.execute(
            "SELECT montad FROM automoveis, montadora "
            "WHERE montadora.cod = automoveis.montad "
            "AND cod_aut = '%s'" % cod_aut)
        consultamarca2 = self.cursor.fetchall()
        for i in consultamarca2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarca2A.insert(0, i)

        self.desconecta_Glac()
    def busca_automovelA(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.entradaAutA.insert(0, '%')
        autom = self.entradaAutA.get()

        lista = self.cursor.execute("""
            SELECT automoveis.cod_aut, automoveis.automovel, montadora.marca 
            FROM automoveis, montadora
       		WHERE montadora.cod = automoveis.montad  
       		ORDER BY automovel ASC; """ )
        for i in lista:
            self.listaServ.insert("", 0, values=i)
        self.limpa_automovelA()
        self.desconecta_Glac()
    def OnDoubleClickA(self, event):
        self.limpa_automovelA()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod_autA.insert(0, col1)

        self.carrega_automovelA()
    def OnVsbA(self, *args):
        self.listaServ.yview(*args)
    def add_autobindA(self, event):
        for n in self.listaTec1.selection():
            col1, col2 = self.listaTec1.item(n, 'values')
            self.entradaMarca2A.insert(0, col1)
            self.entradaMarcaA.insert(0, col2)
        self.listatec.destroy()
    def limpa_automovelA(self):
        self.entradaCod_autA.delete('0', 'end')
        self.entradaAutA.delete('0', 'end')
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')