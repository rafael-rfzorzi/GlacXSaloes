from modulos import *
from multilanguage import *
import licence
import re

class Formulas:
    def totalbotao(self):
        def moedaTotal1(total1=0, moeda='R$'):
            return f'{moeda}{total1:>8.2f}'.replace('.', ',')
        def moedaTotal2(total2=0, moeda='R$'):
            return f'{moeda}{total2:>8.2f}'.replace('.', ',')
        def moedaTotal3(total3=0, moeda='R$'):
            return f'{moeda}{total3:>8.2f}'.replace('.', ',')
        def moedaTotal4(total4=0, moeda='R$'):
            return f'{moeda}{total4:>8.2f}'.replace('.', ',')
        def moedaTotal5(total5=0, moeda='R$'):
            return f'{moeda}{total5:>8.2f}'.replace('.', ',')
        def moedaTotal6(total6=0, moeda='R$'):
            return f'{moeda}{total6:>8.2f}'.replace('.', ',')
        def moedaTotal7(total7=0, moeda='R$'):
            return f'{moeda}{total7:>8.2f}'.replace('.', ',')
        def moedaTotal8(total8=0, moeda='R$'):
            return f'{moeda}{total8:>8.2f}'.replace('.', ',')
        def moedaTotal9(total9=0, moeda='R$'):
            return f'{moeda}{total9:>8.2f}'.replace('.', ',')
        def moedaTotal10(total10=0, moeda='R$'):
            return f'{moeda}{total10:>8.2f}'.replace('.', ',')
        def moedaTotal11(total11=0, moeda='R$'):
            return f'{moeda}{total11:>8.2f}'.replace('.', ',')
        def moedaTotal12(total12=0, moeda='R$'):
            return f'{moeda}{total12:>8.2f}'.replace('.', ',')
        def moedaTotal13(total13=0, moeda='R$'):
            return f'{moeda}{total13:>8.2f}'.replace('.', ',')
        def moedaTotal14(total14=0, moeda='R$'):
            return f'{moeda}{total14:>8.2f}'.replace('.', ',')
        def moedaTotal15(total15=0, moeda='R$'):
            return f'{moeda}{total15:>8.2f}'.replace('.', ',')
        def moedaTotal16(total16=0, moeda='R$'):
            return f'{moeda}{total16:>8.2f}'.replace('.', ',')
        def moedaTotal17(total17=0, moeda='R$'):
            return f'{moeda}{total17:>8.2f}'.replace('.', ',')
        def moedaTotal18(total18=0, moeda='R$'):
            return f'{moeda}{total18:>8.2f}'.replace('.', ',')
        def moedaTotal19(total19=0, moeda='R$'):
            return f'{moeda}{total19:>8.2f}'.replace('.', ',')
        def moedaTotal20(total20=0, moeda='R$'):
            return f'{moeda}{total20:>8.2f}'.replace('.', ',')

        quant1 = self.listaCol3a.get()
        quant1 = float(quant1)
        valor1 = self.listaCol4a.get()
        valor1 = float(valor1)
        total1 = quant1 * valor1
        total1 = float(total1)
        self.listaCol5a.delete(0, END)
        self.listaCol5a.insert(END, moedaTotal1(total1))

        quant2 = self.listaCol3b.get()
        quant2 = float(quant2)
        valor2 = self.listaCol4b.get()
        valor2 = float(valor2)
        total2 = quant2 * valor2
        total2 = float(total2)
        self.listaCol5b.delete(0, END)
        self.listaCol5b.insert(END, moedaTotal2(total2))

        quant3 = self.listaCol3c.get()
        quant3 = float(quant3)
        valor3 = self.listaCol4c.get()
        valor3 = float(valor3)
        total3 = quant3 * valor3
        total3 = float(total3)
        self.listaCol5c.delete(0, END)
        self.listaCol5c.insert(END, moedaTotal3(total3))

        quant4 = self.listaCol3d.get()
        quant4 = float(quant4)
        valor4 = self.listaCol4d.get()
        valor4 = float(valor4)
        total4 = quant4 * valor4
        total4 = float(total4)
        self.listaCol5d.delete(0, END)
        self.listaCol5d.insert(END, moedaTotal4(total4))

        quant5 = self.listaCol3e.get()
        quant5 = float(quant5)
        valor5 = self.listaCol4e.get()
        valor5 = float(valor5)
        total5 = quant5 * valor5
        total5 = float(total5)
        self.listaCol5e.delete(0, END)
        self.listaCol5e.insert(END, moedaTotal5(total5))

        quant6 = self.listaCol3f.get()
        quant6 = float(quant6)
        valor6 = self.listaCol4f.get()
        valor6 = float(valor6)
        total6 = quant6 * valor6
        total6 = float(total6)
        self.listaCol5f.delete(0, END)
        self.listaCol5f.insert(END, moedaTotal6(total6))

        quant7 = self.listaCol3g.get()
        quant7 = float(quant7)
        valor7 = self.listaCol4g.get()
        valor7 = float(valor7)
        total7 = quant7 * valor7
        total7 = float(total7)
        self.listaCol5g.delete(0, END)
        self.listaCol5g.insert(END, moedaTotal7(total7))

        quant8 = self.listaCol3h.get()
        quant8 = float(quant8)
        valor8 = self.listaCol4h.get()
        valor8 = float(valor8)
        total8 = quant8 * valor8
        total8 = float(total8)
        self.listaCol5h.delete(0, END)
        self.listaCol5h.insert(END, moedaTotal8(total8))

        quant9 = self.listaCol3i.get()
        quant9 = float(quant9)
        valor9 = self.listaCol4i.get()
        valor9 = float(valor9)
        total9 = quant9 * valor9
        total9 = float(total9)
        self.listaCol5i.delete(0, END)
        self.listaCol5i.insert(END, moedaTotal9(total9))

        quant10 = self.listaCol3j.get()
        quant10 = float(quant10)
        valor10 = self.listaCol4j.get()
        valor10 = float(valor10)
        total10 = quant10 * valor10
        total10 = float(total10)
        self.listaCol5j.delete(0, END)
        self.listaCol5j.insert(END, moedaTotal10(total10))

        quant11 = self.listaCol3k.get()
        quant11 = float(quant11)
        valor11 = self.listaCol4k.get()
        valor11 = float(valor11)
        total11 = quant11 * valor11
        total11 = float(total11)
        self.listaCol5k.delete(0, END)
        self.listaCol5k.insert(END, moedaTotal11(total11))

        quant12 = self.listaCol3l.get()
        quant12 = float(quant12)
        valor12 = self.listaCol4l.get()
        valor12 = float(valor12)
        total12 = quant12 * valor12
        total12 = float(total12)
        self.listaCol5l.delete(0, END)
        self.listaCol5l.insert(END, moedaTotal12(total12))

        quant13 = self.listaCol3m.get()
        quant13 = float(quant13)
        valor13 = self.listaCol4m.get()
        valor13 = float(valor13)
        total13 = quant13 * valor13
        total13 = float(total13)
        self.listaCol5m.delete(0, END)
        self.listaCol5m.insert(END, moedaTotal13(total13))

        quant14 = self.listaCol3n.get()
        quant14 = float(quant14)
        valor14 = self.listaCol4n.get()
        valor14 = float(valor14)
        total14 = quant14 * valor14
        total14 = float(total14)
        self.listaCol5n.delete(0, END)
        self.listaCol5n.insert(END, moedaTotal14(total14))

        quant15 = self.listaCol3o.get()
        quant15 = float(quant15)
        valor15 = self.listaCol4o.get()
        valor15 = float(valor15)
        total15 = quant15 * valor15
        total15 = float(total15)
        self.listaCol5o.delete(0, END)
        self.listaCol5o.insert(END, moedaTotal15(total15))

        quant16 = self.listaCol3p.get()
        quant16 = float(quant16)
        valor16 = self.listaCol4p.get()
        valor16 = float(valor16)
        total16 = quant16 * valor16
        total16 = float(total16)
        self.listaCol5p.delete(0, END)
        self.listaCol5p.insert(END, moedaTotal16(total16))

        quant17 = self.listaCol3q.get()
        quant17 = float(quant17)
        valor17 = self.listaCol4q.get()
        valor17 = float(valor17)
        total17 = quant17 * valor17
        total17 = float(total17)
        self.listaCol5q.delete(0, END)
        self.listaCol5q.insert(END, moedaTotal17(total17))

        quant18 = self.listaCol3r.get()
        quant18 = float(quant18)
        valor18 = self.listaCol4r.get()
        valor18 = float(valor18)
        total18 = quant18 * valor18
        total18 = float(total18)
        self.listaCol5r.delete(0, END)
        self.listaCol5r.insert(END, moedaTotal18(total18))

        quant19 = self.listaCol3s.get()
        quant19 = float(quant19)
        valor19 = self.listaCol4s.get()
        valor19 = float(valor19)
        total19 = quant19 * valor19
        total19 = float(total19)
        self.listaCol5s.delete(0, END)
        self.listaCol5s.insert(END, moedaTotal19(total19))

        quant20 = self.listaCol3t.get()
        quant20 = float(quant20)
        valor20 = self.listaCol4t.get()
        valor20 = float(valor20)
        total20 = quant20 * valor20
        total20 = float(total20)
        self.listaCol5t.delete(0, END)
        self.listaCol5t.insert(END, moedaTotal20(total20))

        self.entradatotal.delete(0, END)
        self.totalsimples = float(total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9
                                  + total10 + total11 + total12 + total13 + total14 + total15 + total16 + total17
                                  + total18 + total19 + total20)
        self.entradatotal.insert(END, self.moedaTotalizador(total1 + total2 + total3 + total4 + total5 + total6
                                                            + total7 + total8 + total9 + total10 + total11 + total12 +
                                                            total13 + total14 + total15 + total16 + total17 + total18 +
                                                            total19 + total20))
    def moedaTotalizador(self, totalizador=0, moeda='R$'):
        return f'{moeda}{totalizador:>8.2f}'.replace('.',',')
    def moedaTotal1(self, total1=0, moeda='R$'):
        return f'{moeda}{self.total1:>8.2f}'.replace('.',',')
    def moedaTotal2(self, total2=0, moeda='R$'):
        return f'{moeda}{self.total2:>8.2f}'.replace('.',',')
    def moedaTotal3(self, total3=0, moeda='R$'):
        return f'{moeda}{self.total3:>8.2f}'.replace('.',',')
    def moedaTotal4(self, total4=0, moeda='R$'):
        return f'{moeda}{self.total4:>8.2f}'.replace('.',',')
    def moedaTotal5(self, total5=0, moeda='R$'):
        return f'{moeda}{self.total5:>8.2f}'.replace('.',',')
    def moedaTotal6(self, total6=0, moeda='R$'):
        return f'{moeda}{self.total6:>8.2f}'.replace('.',',')
    def moedaTotal7(self, total7=0, moeda='R$'):
        return f'{moeda}{self.total7:>8.2f}'.replace('.',',')
    def moedaTotal8(self, total8=0, moeda='R$'):
        return f'{moeda}{self.total8:>8.2f}'.replace('.',',')
    def moedaTotal9(self, total9=0, moeda='R$'):
        return f'{moeda}{self.total9:>8.2f}'.replace('.',',')
    def moedaTotal10(self, total10=0, moeda='R$'):
        return f'{moeda}{self.total10:>8.2f}'.replace('.',',')
    def busca_servico1(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico1bind)
    def add_servico1(self):
        self.listaCol2a.delete(0, END)
        self.listaCol4a.delete(0, END)
        self.entradatotal.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ1.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2a.insert(END, i)

        self.listaCol3a.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3a.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT  valor  FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4a.insert(END, i)

        quant1 = self.listaCol3a.get()
        quant1 = float(quant1)
        valor1 = self.listaCol4a.get()
        valor1 = float(valor1)
        self.total1 = quant1 * valor1
        self.total1 = float(self.total1)

        self.listaCol5a.delete(0, END)
        self.listaCol5a.insert(END, self.moedaTotal1(self.total1))

        self.totalbotao()
        self.desconecta_Glac()
    def add_servico1bind(self, event):
        self.codServ1.delete(0, END)
        self.listaCol2a.delete(0, END)
        self.listaCol4a.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ1.insert(END, col1)

        self.add_servico1()
        self.listaServP1.destroy()
    def busca_servico2(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico2bind)
    def add_servico2(self):

        self.listaCol2b.delete(0, END)
        self.listaCol4b.delete(0, END)
        self.entradatotal.delete(0, END)

        cod_sp = self.codServ2.get()

        self.conecta_Glac()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2b.insert(END, i)

        self.listaCol3b.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3b.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4b.insert(END, i)

        quant2 = self.listaCol3b.get()
        quant2 = float(quant2)
        valor2 = self.listaCol4b.get()
        valor2 = float(valor2)
        self.total2 = quant2 * valor2
        self.total2 = float(self.total2)

        self.listaCol5b.delete(0, END)
        self.listaCol5b.insert(END, self.moedaTotal2(self.total2))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico2bind(self, event):
        self.codServ2.delete(0, END)
        self.listaCol2b.delete(0, END)
        self.listaCol4b.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ2.insert(END, col1)

        self.add_servico2()
        self.listaServP1.destroy()
    def busca_servico3(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico3bind)
    def add_servico3(self):

        self.listaCol2c.delete(0, END)
        self.listaCol4c.delete(0, END)
        self.entradatotal.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ3.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2c.insert(END, i)

        self.listaCol3c.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3c.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4c.insert(END, i)

        quant3 = self.listaCol3c.get()
        quant3 = float(quant3)
        valor3 = self.listaCol4c.get()
        valor3 = float(valor3)
        self.total3 = quant3 * valor3
        self.total3 = float(self.total3)

        self.listaCol5c.delete(0, END)
        self.listaCol5c.insert(END, self.moedaTotal3(self.total3))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico3bind(self, event):
        self.codServ3.delete(0, END)
        self.listaCol2c.delete(0, END)
        self.listaCol4c.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ3.insert(END, col1)

        self.add_servico3()
        self.listaServP1.destroy()
    def busca_servico4(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico4bind)
    def add_servico4(self):

        self.listaCol2d.delete(0, END)
        self.listaCol4d.delete(0, END)
        self.entradatotal.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ4.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2d.insert(END, i)

        self.listaCol3d.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3d.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4d.insert(END, i)

        quant4 = self.listaCol3d.get()
        quant4 = float(quant4)
        valor4 = self.listaCol4d.get()
        valor4 = float(valor4)
        self.total4 = quant4 * valor4
        self.total4 = float(self.total4)

        self.listaCol5d.delete(0, END)
        self.listaCol5d.insert(END, self.moedaTotal4(self.total4))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico4bind(self, event):
        self.codServ4.delete(0, END)
        self.listaCol2d.delete(0, END)
        self.listaCol4d.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ4.insert(END, col1)

        self.add_servico4()
        self.listaServP1.destroy()
    def busca_servico5(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico5bind)
    def add_servico5(self):

        self.listaCol2e.delete(0, END)
        self.listaCol4e.delete(0, END)
        self.entradatotal.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ5.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2e.insert(END, i)

        self.listaCol3e.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3e.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4e.insert(END, i)

        quant5 = self.listaCol3e.get()
        quant5 = float(quant5)
        valor5 = self.listaCol4e.get()
        valor5 = float(valor5)
        self.total5 = quant5 * valor5
        self.total5 = float(self.total5)

        self.listaCol5e.delete(0, END)
        self.listaCol5e.insert(END, self.moedaTotal5(self.total5))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico5bind(self, event):
        self.codServ5.delete(0, END)
        self.listaCol2e.delete(0, END)
        self.listaCol4e.delete(0, END)
        self.entradatotal.delete(0, END)


        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ5.insert(END, col1)

        self.add_servico5()
        self.listaServP1.destroy()
    def busca_servico6(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico6bind)
    def add_servico6(self):

        self.listaCol2f.delete(0, END)
        self.listaCol4f.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ6.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2f.insert(END, i)

        self.listaCol3f.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3f.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4f.insert(END, i)

        quant6 = self.listaCol3f.get()
        quant6 = float(quant6)
        valor6 = self.listaCol4f.get()
        valor6 = float(valor6)
        self.total6 = quant6 * valor6
        self.total6 = float(self.total6)

        self.listaCol5f.delete(0, END)
        self.listaCol5f.insert(END, self.moedaTotal6(self.total6))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico6bind(self, event):
        self.codServ6.delete(0, END)
        self.listaCol2f.delete(0, END)
        self.listaCol4f.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ6.insert(END, col1)

        self.add_servico6()
        self.listaServP1.destroy()
    def busca_servico7(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico7bind)
    def add_servico7(self):

        self.listaCol2g.delete(0, END)
        self.listaCol4g.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()


        cod_sp = self.codServ7.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2g.insert(END, i)

        self.listaCol3g.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3g.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4g.insert(END, i)

        quant7 = self.listaCol3g.get()
        quant7 = float(quant7)
        valor7 = self.listaCol4g.get()
        valor7 = float(valor7)
        self.total7 = quant7 * valor7
        self.total7 = float(self.total7)

        self.listaCol5g.delete(0, END)
        self.listaCol5g.insert(END, self.moedaTotal7(self.total7))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico7bind(self, event):
        self.codServ7.delete(0, END)
        self.listaCol2g.delete(0, END)
        self.listaCol4g.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ7.insert(END, col1)

        self.add_servico7()
        self.listaServP1.destroy()
    def busca_servico8(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico8bind)
    def add_servico8(self):

        self.listaCol2h.delete(0, END)
        self.listaCol4h.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ8.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2h.insert(END, i)

        self.listaCol3h.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3h.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4h.insert(END, i)

        quant8 = self.listaCol3h.get()
        quant8 = float(quant8)
        valor8 = self.listaCol4h.get()
        valor8 = float(valor8)
        self.total8 = quant8 * valor8
        self.total8 = float(self.total8)

        self.listaCol5h.delete(0, END)
        self.listaCol5h.insert(END, self.moedaTotal8(self.total8))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico8bind(self, event):
        self.codServ8.delete(0, END)
        self.listaCol2h.delete(0, END)
        self.listaCol4h.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ8.insert(END, col1)

        self.add_servico8()

        self.listaServP1.destroy()
    def busca_servico9(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico9bind)
    def add_servico9(self):

        self.listaCol2i.delete(0, END)
        self.listaCol4i.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ9.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2i.insert(END, i)

        self.listaCol3i.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3i.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4i.insert(END, i)

        quant9 = self.listaCol3i.get()
        quant9 = float(quant9)
        valor9 = self.listaCol4i.get()
        valor9 = float(valor9)
        self.total9 = quant9 * valor9
        self.total9 = float(self.total9)

        self.listaCol5i.delete(0, END)
        self.listaCol5i.insert(END, self.moedaTotal9(self.total9))
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico9bind(self, event):
        self.codServ9.delete(0, END)
        self.listaCol2i.delete(0, END)
        self.listaCol4i.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ9.insert(END, col1)

        self.add_servico9()
        self.listaServP1.destroy()
    def busca_servico10(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico10bind)
    def add_servico10(self):

        self.listaCol2j.delete(0, END)
        self.listaCol4j.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ10.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2j.insert(END, i)

        self.listaCol3j.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3j.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4j.insert(END, i)

        quant10 = self.listaCol3j.get()
        quant10 = float(quant10)
        valor10 = self.listaCol4j.get()
        valor10 = float(valor10)
        self.total10 = quant10 * valor10
        self.total10 = float(self.total10)

        self.listaCol5j.delete(0, END)
        self.listaCol5j.insert(END, self.moedaTotal10(self.total10))

        self.desconecta_Glac()
        self.totalbotao()
    def add_servico10bind(self, event):
        self.codServ10.delete(0, END)
        self.listaCol2j.delete(0, END)
        self.listaCol4j.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ10.insert(END, col1)



        self.add_servico10()
        self.listaServP1.destroy()
    def busca_servico11(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico11bind)
    def add_servico11(self):

        self.listaCol2k.delete(0, END)
        self.listaCol4k.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ11.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2k.insert(END, i)

        self.listaCol3k.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3k.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT  ROUND(valor,2)  FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4k.insert(END, i)

        quant11 = self.listaCol3k.get()
        quant11 = float(quant11)
        valor11 = self.listaCol4k.get()
        valor11 = float(valor11)
        self.total11 = quant11 * valor11
        self.total11 = float(self.total11)

        self.listaCol5k.delete(0, END)
        self.listaCol5k.insert(END, self.total11)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico11bind(self, event):
        self.codServ11.delete(0, END)
        self.listaCol2k.delete(0, END)
        self.listaCol4k.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ11.insert(END, col1)

        self.add_servico11()
        self.listaServP1.destroy()
    def busca_servico12(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico12bind)
    def add_servico12(self):

        self.listaCol2l.delete(0, END)
        self.listaCol4l.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ12.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico12 = self.cursor.fetchall()
        for i in addservico12:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2l.insert(END, i)

        self.listaCol3l.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3l.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4l.insert(END, i)

        quant12 = self.listaCol3l.get()
        quant12 = float(quant12)
        valor12 = self.listaCol4l.get()
        valor12 = float(valor12)
        self.total12 = quant12 * valor12
        self.total12 = float(self.total12)

        self.listaCol5l.delete(0, END)
        self.listaCol5l.insert(END, self.total12)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico12bind(self, event):
        self.codServ12.delete(0, END)
        self.listaCol2l.delete(0, END)
        self.listaCol4l.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ12.insert(END, col1)

        self.add_servico12()
        self.listaServP1.destroy()
    def busca_servico13(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico13bind)
    def add_servico13(self):

        self.listaCol2m.delete(0, END)
        self.listaCol4m.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ13.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2m.insert(END, i)

        self.listaCol3m.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3m.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4m.insert(END, i)

        quant13 = self.listaCol3m.get()
        quant13 = float(quant13)
        valor13 = self.listaCol4m.get()
        valor13 = float(valor13)
        self.total13 = quant13 * valor13
        self.total13 = float(self.total13)

        self.listaCol5m.delete(0, END)
        self.listaCol5m.insert(END, self.total13)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico13bind(self, event):
        self.codServ13.delete(0, END)
        self.listaCol2m.delete(0, END)
        self.listaCol4m.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ13.insert(END, col1)

        self.add_servico13()
        self.listaServP1.destroy()
    def busca_servico14(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico14bind)
    def add_servico14(self):

        self.listaCol2n.delete(0, END)
        self.listaCol4n.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ14.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2n.insert(END, i)

        self.listaCol3n.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3n.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4n.insert(END, i)

        quant14 = self.listaCol3n.get()
        quant14 = float(quant14)
        valor14 = self.listaCol4n.get()
        valor14 = float(valor14)
        self.total14 = quant14 * valor14
        self.total14 = float(self.total14)

        self.listaCol5n.delete(0, END)
        self.listaCol5n.insert(END, self.total14)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico14bind(self, event):
        self.codServ14.delete(0, END)
        self.listaCol2n.delete(0, END)
        self.listaCol4n.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ14.insert(END, col1)

        self.add_servico14()
        self.listaServP1.destroy()
    def busca_servico15(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico15bind)
    def add_servico15(self):

        self.listaCol2o.delete(0, END)
        self.listaCol4o.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ15.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2o.insert(END, i)

        self.listaCol3o.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3o.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4o.insert(END, i)

        quant15 = self.listaCol3o.get()
        quant15 = float(quant15)
        valor15 = self.listaCol4o.get()
        valor15 = float(valor15)
        self.total15 = quant15 * valor15
        self.total15 = float(self.total15)

        self.listaCol5o.delete(0, END)
        self.listaCol5o.insert(END, self.total15)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico15bind(self, event):
        self.codServ15.delete(0, END)
        self.listaCol2o.delete(0, END)
        self.listaCol4o.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ15.insert(END, col1)

        self.add_servico15()
        self.listaServP1.destroy()
    def busca_servico16(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico16bind)
    def add_servico16(self):

        self.listaCol2p.delete(0, END)
        self.listaCol4p.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ16.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2p.insert(END, i)

        self.listaCol3p.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3p.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4p.insert(END, i)

        quant16 = self.listaCol3p.get()
        quant16 = float(quant16)
        valor16 = self.listaCol4p.get()
        valor16 = float(valor16)
        self.total16 = quant16 * valor16
        self.total16 = float(self.total16)

        self.listaCol5p.delete(0, END)
        self.listaCol5p.insert(END, self.total16)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico16bind(self, event):
        self.codServ16.delete(0, END)
        self.listaCol2p.delete(0, END)
        self.listaCol4p.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ16.insert(END, col1)

        self.add_servico16()
        self.listaServP1.destroy()
    def busca_servico17(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico17bind)
    def add_servico17(self):

        self.listaCol2q.delete(0, END)
        self.listaCol4q.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ17.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2q.insert(END, i)

        self.listaCol3q.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3q.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4q.insert(END, i)

        quant17 = self.listaCol3q.get()
        quant17 = float(quant17)
        valor17 = self.listaCol4q.get()
        valor17 = float(valor17)
        self.total17 = quant17 * valor17
        self.total17 = float(self.total17)

        self.listaCol5q.delete(0, END)
        self.listaCol5q.insert(END, self.total17)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico17bind(self, event):
        self.codServ17.delete(0, END)
        self.listaCol2q.delete(0, END)
        self.listaCol4q.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ17.insert(END, col1)

        self.add_servico17()
        self.listaServP1.destroy()
    def busca_servico18(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico18bind)
    def add_servico18(self):

        self.listaCol2r.delete(0, END)
        self.listaCol4r.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ18.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2r.insert(END, i)

        self.listaCol3r.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3r.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4r.insert(END, i)

        quant18 = self.listaCol3r.get()
        quant18 = float(quant18)
        valor18 = self.listaCol4r.get()
        valor18 = float(valor18)
        self.total18 = quant18 * valor18
        self.total18 = float(self.total18)

        self.listaCol5r.delete(0, END)
        self.listaCol5r.insert(END, self.total18)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico18bind(self, event):
        self.codServ18.delete(0, END)
        self.listaCol2r.delete(0, END)
        self.listaCol4r.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ18.insert(END, col1)

        self.add_servico18()
        self.listaServP1.destroy()
    def busca_servico19(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico19bind)
    def add_servico19(self):

        self.listaCol2s.delete(0, END)
        self.listaCol4s.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ19.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2s.insert(END, i)

        self.listaCol3s.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3s.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4s.insert(END, i)

        quant19 = self.listaCol3s.get()
        quant19 = float(quant19)
        valor19 = self.listaCol4s.get()
        valor19 = float(valor19)
        self.total19 = quant19 * valor19
        self.total19 = float(self.total19)

        self.listaCol5s.delete(0, END)
        self.listaCol5s.insert(END, self.total19)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico19bind(self, event):
        self.codServ19.delete(0, END)
        self.listaCol2s.delete(0, END)
        self.listaCol4s.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ19.insert(END, col1)

        self.add_servico19()
        self.listaServP1.destroy()
    def busca_servico20(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico20bind)
    def add_servico20(self):

        self.listaCol2t.delete(0, END)
        self.listaCol4t.delete(0, END)
        self.entradatotal.delete(0, END)
        self.conecta_Glac()

        cod_sp = self.codServ20.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT servprod, "-",  tiposerv FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2t.insert(END, i)

        self.listaCol3t.delete(0, END)
        self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3t.insert(END, i)

        addserv4 = self.cursor
        addserv4.execute("""SELECT ROUND(valor,2) FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
        addservico4 = self.cursor.fetchall()
        for i in addservico4:
            self.listaCol4t.insert(END, i)

        quant20 = self.listaCol3t.get()
        quant20 = float(quant20)
        valor20 = self.listaCol4t.get()
        valor20 = float(valor20)
        self.total20 = quant20 * valor20
        self.total20 = float(self.total20)

        self.listaCol5t.delete(0, END)
        self.listaCol5t.insert(END, self.total20)
        self.totalbotao()

        self.desconecta_Glac()
    def add_servico20bind(self, event):
        self.codServ20.delete(0, END)
        self.listaCol2t.delete(0, END)
        self.listaCol4t.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ20.insert(END, col1)

        self.add_servico20()
        self.listaServP1.destroy()

    def busca_servico1F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico1bindF)
    def add_servico1F(self):
        self.listaCol2aF.delete(0, END)
        self.listaCol3aF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ1F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2aF.insert(END, i)

        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3aF.insert(END, i)

        self.desconecta_Glac()
    def add_servico1bindF(self, event):
        self.codServ1F.delete   (0, END)
        self.listaCol2aF.delete (0, END)
        self.listaCol3aF.delete (0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ1F.insert(END, col1)
            self.listaCol2aF.insert(END, col2)
            self.listaCol3aF.insert(END, col3)
            self.listaServP1F.destroy()
    def busca_servico2F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico2bindF)
    def add_servico2F(self):

        self.listaCol2bF.delete(0, END)
        self.listaCol3bF.delete(0, END)

        cod_sp = self.codServ2F.get()

        self.conecta_Glac()

        addserv2F = self.cursor
        addserv2F.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2F = self.cursor.fetchall()
        for i in addservico2F:
            self.listaCol2bF.insert(END, i)

        self.listaCol3bF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3F = self.cursor.fetchall()
        for i in addservico3F:
            self.listaCol3bF.insert(END, i)


        self.desconecta_Glac()
    def add_servico2bindF(self, event):
        self.codServ2F.delete(0, END)
        self.listaCol2bF.delete(0, END)
        self.listaCol3bF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ2F.insert(END, col1)
            self.add_servico2F()
            self.listaServP1F.destroy()
    def busca_servico3F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico3bindF)
    def add_servico3F(self):

        self.listaCol2cF.delete(0, END)
        self.listaCol3cF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ3F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2cF.insert(END, i)

        self.listaCol3cF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3cF.insert(END, i)

        self.desconecta_Glac()
    def add_servico3bindF(self, event):
        self.codServ3F.delete(0, END)
        self.listaCol2cF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ3F.insert(END, col1)
            self.add_servico3F()
            self.listaServP1F.destroy()
    def busca_servico4F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico4bindF)
    def add_servico4F(self):

        self.listaCol2dF.delete(0, END)
        self.listaCol3dF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ4F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2dF.insert(END, i)

        self.listaCol3dF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3dF.insert(END, i)

        self.desconecta_Glac()
    def add_servico4bindF(self, event):
        self.codServ4F.delete(0, END)
        self.listaCol2dF.delete(0, END)
        self.listaCol3dF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ4F.insert(END, col1)
            self.add_servico4F()
            self.listaServP1F.destroy()
    def busca_servico5F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico5bindF)
    def add_servico5F(self):

        self.listaCol2eF.delete(0, END)
        self.listaCol3eF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ5F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2eF.insert(END, i)

        self.listaCol3eF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3eF.insert(END, i)

        self.desconecta_Glac()
    def add_servico5bindF(self, event):
        self.codServ5F.delete(0, END)
        self.listaCol2eF.delete(0, END)
        self.listaCol3eF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ5F.insert(END, col1)
            self.add_servico5F()
            self.listaServP1F.destroy()
    def busca_servico6F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico6bindF)
    def add_servico6F(self):

        self.listaCol2fF.delete(0, END)
        self.listaCol3fF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ6F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2fF.insert(END, i)

        self.listaCol3fF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3fF.insert(END, i)


        self.desconecta_Glac()
    def add_servico6bindF(self, event):
        self.codServ6F.delete(0, END)
        self.listaCol2fF.delete(0, END)
        self.listaCol3fF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ6F.insert(END, col1)
            self.add_servico6F()
            self.listaServP1F.destroy()
    def busca_servico7F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico7bindF)
    def add_servico7F(self):

        self.listaCol2gF.delete(0, END)
        self.listaCol3gF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ7F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2gF.insert(END, i)

        self.listaCol3gF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3gF.insert(END, i)


        self.desconecta_Glac()
    def add_servico7bindF(self, event):
        self.codServ7F.delete(0, END)
        self.listaCol2gF.delete(0, END)
        self.listaCol3gF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ7F.insert(END, col1)
            self.add_servico7F()
            self.listaServP1F.destroy()
    def busca_servico8F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico8bindF)
    def add_servico8F(self):

        self.listaCol2hF.delete(0, END)
        self.listaCol3hF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ8F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2hF.insert(END, i)

        self.listaCol3hF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3hF.insert(END, i)


        self.desconecta_Glac()
    def add_servico8bindF(self, event):
        self.codServ8F.delete(0, END)
        self.listaCol2hF.delete(0, END)
        self.listaCol3hF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ8F.insert(END, col1)
            self.add_servico8F()
            self.listaServP1F.destroy()
    def busca_servico9F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico9bindF)
    def add_servico9F(self):

        self.listaCol2iF.delete(0, END)
        self.listaCol3iF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ9F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2iF.insert(END, i)

        self.listaCol3iF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3iF.insert(END, i)

        self.desconecta_Glac()
    def add_servico9bindF(self, event):
        self.codServ9F.delete(0, END)
        self.listaCol2iF.delete(0, END)
        self.listaCol3iF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ9F.insert(END, col1)
            self.add_servico9F()
            self.listaServP1F.destroy()
    def busca_servico10F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico10bindF)
    def add_servico10F(self):

        self.listaCol2jF.delete(0, END)
        self.listaCol3jF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ10F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2jF.insert(END, i)

        self.listaCol3jF.delete(0, END)
        self.cursor.execute("""SELECT falha2 FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico3 = self.cursor.fetchall()
        for i in addservico3:
            self.listaCol3jF.insert(END, i)

        self.desconecta_Glac()
    def add_servico10bindF(self, event):
        self.codServ10F.delete(0, END)
        self.listaCol2jF.delete(0, END)
        self.listaCol3jF.delete(0, END)

        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ10F.insert(END, col1)
            self.add_servico10F()
            self.listaServP1F.destroy()
class Validadores:
    def validate_entry1(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 10
    def validate_entry2(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100
    def validate_entry4(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 10000
    def validate_entry8(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100000000
    def validate_entry12(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100000000000000
    def validate_entry8float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 9
    def validate_entry6(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 1000000
    def validate_entry4float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 5
    def validate_entry9float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 10

class Functions():
    def images_base64(self):
        ########################
        #### Logo da Empresa Seu Logo Aqui
        self.CADFORNEC_BT = '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'
        self.CADAUT_BT = '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'
        self.CADPROD_BT = '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'
        self.CADSERV_BT = 'iVBORw0KGgoAAAANSUhEUgAAAEEAAAA/CAYAAAC/36X0AAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOxAAADsQBlSsOGwAAA11JREFUeF7tmDGOUzEQhgPKcXIAClpqToAEDcW20K/ood2CBiROsDUX4AC5Qe6xkH/XI82bzIw9z+On5eV90tM6Ly/2zOexneyL17f3f3dXzsvy96rZJJzZJJxx94T7z29K6//n7dffpXWJWglIfk0CgJfPhYS1Jc+xcru6PUETMZGw5irw2E6HM5uEM5MjMrIcPr5/V1pTvv/8VVrPF3lczpJgCZBkC8kSnyKBIwM7HA6Pf4/H4+PfDBGe9Dn9SwndewKC4IEgeVwko7VqLOjz6I/6zCZtY5QzkimCoOoiMqoMpJ4OXlC9IrgAWX29DD8iT6dTaeWQmTwxVAJm7+HhobxaDlRdpPKGV0IPWiK15OYsu2ctgZCngpUo3acl0yrElIAOtMtDvo/g9/t9eRWD+rKORTlWLTYP98tST8c8eLmz1/AEyGNSQp+h57TxQl+WRuzENWoVgPvae3QfyXsCNKp7guyIBtMCseDPetVVE8DhcdDztSqxCP120BJoCZhjzVJNQCTBWgWk/YDyZhR4cnhCCLhVQGt510j7AYWA5MXxZi5SPdkCNFK/J0gZLSK8KlhCAEiVQERFAPncUgLAEAkgIoJk0HNLCgDDJEg8EUCKWJLJ6XD34VVp5fHl001pPaGtfUIKuP12V1q53Pz4U1pPDK8EJMKTQaLWbPOlsSSLLQeJV/ZLixguAcuBloSc6ZoI/tmRDJXAE7Bmt6UiRosYJsESwJOmvQL3LBlLiEg/HbzZ1wTI5OZUDNF6msjToVlCZCa0RDQBHE8e0SIC1GSEJURnao4AolWEfE+T443T9T3BCgzgvR4BgL+vJQYsAXL8SOWGJGBA75LwezUBRIsIbUxqaxNRI/V0kIERrQIIKYL65G08Qxehjd1CWAIfXAaRiddvbUyqhtYl4UqQnYxK2IKPxytAgns9sTVVQm2QngBamLPOI7gSeg33opWzVeL8fnRvSN0YAc3a3E3KYmQ1pEuQZFSSFIpZl1cPKb8dKAhZBRkCeIK1apCyrPHT/7PEg0QQuEbtJdQ/XRz5OjJ+lwStDLOT9/qzhERjGP6P1mys9R9JfPZP6TWRviesgYkEaWiNaDleVMI1iJCoy2GtIqy8zD1hTSKQi5fP5HS4VrbT4cwmYbfb/QMeykqz2oYGmgAAAABJRU5ErkJggg=='
        self.CADCLI_BT = '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'
        self.LOGORF = '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'

        self.SEULOGO = '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'
        ################################

        self.BTIMPRIME2 = 'iVBORw0KGgoAAAANSUhEUgAAAEUAAAAsCAYAAAAzdnW7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAJSSURBVGhD7Zm7SwNBEMb3El//iqXWki6WahlEULBJoYL4xCYoKPGBgja2ioqlsdTOXu1sFBtREU1SWPlIzttz7txbZmNyt5e7S/YHQ4ZLsbNfZr/ZI1pPJqcThYMYfCoYKnbK6kQvZI3F3PYZZDioKKczjSkGT986Lo5DFFYMXW8eq+nfOIfsF9tTVsebozswctNJyH5RRougREFQoiAoURDs6ZM1jLazXSeapplfeJk+A+ktyPzlZHcSMu+wEyjSneKX+NI7hS1U5i/JI3udhukUv1CiIChREJQoCH9GO5YknR3GAwkjOYqwRutJlP9GYr2mD4+bdaVMH7/uCDKgtXmpr2ZRsAVX0gkzgsJan6/BrTCejDZoMTBk1FSzp1jqYwsv7F5AVl9oLezaVm30WbX+4sloK4kSNtyKYh8fLaaR+5ciuXl4JbdPeXL3XEAjajwW3tF98MGiLm8IShQE21PoH19txQL5+CqR1rhYq+nFPfMzTEZLEdWzszxKPj6/4YmYqcNLyFSnoDhEKZfxidNs+NIpFwcLZoSBkosfGhWlZNxRRFEtiaEVyIIH2wcfLMpTEBzTpyWfJ1+lMokZFzkRc0v7kImpx9GpthM3F0fMPf3H7NEVZD6KEpbj41kU7e3NnECVRInDuxGGdYcJolM2MsOQOaF7qVWUhvcUN9cMZbQI9vGhrA12Szk+QSA6PhR+5GIIj4/1BRVGFFEE2wcbrCAUR6ewZFNdkDmp9LIYVkRGO398DZkToSg89GhFFdoNIgEwqhalmVDThyOb6iI/07GWSu7pmdsAAAAASUVORK5CYII='

        self.BTLOGORF = ''

        self.LBNORC = 'iVBORw0KGgoAAAANSUhEUgAAADwAAAAuCAYAAAB04nriAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAF5SURBVGhD7Zq9boJgFIZfewVcAyVp4tiBO0AHJ4burG6uvYKubq7sHZwYKnfA4EhiQrkG7qA9wAcV6AAh/TnH8yTH7wcTffg+XjG6APBB9acURWF6P8+CXmyWsGVZv/qG53Jn2ptBhaWjwtJRYemosHRUWDoqLB0V/rfEu+qr6OqQ1+P8gBWNLWuHuJ6hp5Tj6/o61sBuhZPjG4xyjxhRaLotIaKeMb8tnVzwbrod8gxp2bovOBcFitegmk6z7ulheA0PV20KLEMrnGHMUpiMB2E0FnbCruvSY4qsfyHbDpZlmzzjsUzopzrBlo5dtQ38Vtj3ESDBMbqYiQYPmzqnrgiw8UzXwHBLO3igRU7CkLS7eHtK5zKh29rTaejCUPgea7/c1j3aG5FutTcqBpahZa99fKM8CpbCZIzBIttbnDrbua7TlntoVdhwqkieDlNhCqhhJI+CrTAZ04fOdPTXQ+mosHRUWDoqLB0Vlo4KS0eFpXNjfy4FPgF1Zm9BmKrCzwAAAABJRU5ErkJggg=='

        self.BTCLIENT = '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'

        self.BTTECNICO = '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'

        self.BTLUPA = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAFPSURBVEhLvZUhTwNBEEb3TtTVonHFkwaNQyCKQSGxJSkYEjS6gf6Opoha0qS2IVgIpkldZSUIyCwze3NzM3t7R8IT7ew2fd/O7nWbfWx23y7CcLzCqspRd+kuLm9wpGMGxMSSWFAloIlYMhn1sSooBVjyg/0MqzJv62rzMiQEaHJNPB4eY+XcaLKoDfEBUm6tmOQgBvhYBlFI7l8ZqXKA19b38iaHyoUcCuch5C11cHfWwSodK5QIASCfvn7hKB1+6ABfJHQRAlLkUkbwLqSncsgaXGzVFrUBXHJ4euXfYY7m684gO7l+9g/w9v3JT3Be5o9YFfIU9noDrCIdtJVLQgBP/Yuce+DXXOqAfwg0lT/cnmNVkGtXLNBmW+5nn1hF7iLooo1cdk9Er2vtyZJoYr4roQNtq6xVEXVy4H//MjlNgjQxYQYQsaCY+BfnfgDiMKCq6QYtEwAAAABJRU5ErkJggg=='

        self.ADD = 'iVBORw0KGgoAAAANSUhEUgAAACYAAAAQCAYAAAB6Hg0eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAJJSURBVEhLxZZfSFNRHMe/x9S2bKz1TxqLqD2ZYH+0f+JDb0GFhEGCEWRB9GCBT9FD9NxLvRREDzkIgyxEQUfT6ilWLWemra3NNkdr4ixbs7a13e107h+0tXP78+DuB778zu+c7zl877lwuSQej9O+0Qjsr6OIxlPQkmqjDofqzGhp2Ahy+9EEveX9Arp7OyoMVYpFG7LfkiAvXuFs7WqQo1cdNNLUiPq1Ohw3CoqltFAKEFa7E+Vwz6awyfkcpOlyP0XrYVxZn0GNTjaWGsqSEULg/QFcmKkE7g2gTFkDCy0Z1OVA50o9DtyYLFobPqdH55B6/zfxWAjGHMpAhaAfb1l56Xsv90vMQjBSRqTrVNPUw17g1Gns8gQwxfqlZvHGGFlBUJXfm0dzx3k04z7sfgFCLofA9f1YY1iB1i4gz+lFz7+IR0Ew8W3yNQy7rRbWzVtg3eqCf1KeD75z4UTPPO6eFDcX98Xn8MWjIFgskeRr3IMJdKHNZECbDbjTNyDNxzNAKqlei85R0ce5eUQ+J5QUMgXB8iw+T+HH/RhTPBK+AMLimjimIYR8YuX0/6lfKQiWy1OuQoER1F1ywh2cZupGy6gfITZvsTbgQXsHHGyvePDvPe+sP0kQcux55ICLH9jqDGhsVposNcsrlkk1bTThYox9YHsGQY5dG6Lhxr2oX6fHvu/TkkErnlVtgPtTGpanThDbkzf0pmcOdM8OZMrl5FpRmRVAXGM4U2OC9NvTO/IBg+NRzHxNKxZtMK/S4+A2M47stOAnOz0vNHr8npEAAAAASUVORK5CYII='

        self.ORCAMENTOLB = 'iVBORw0KGgoAAAANSUhEUgAAAHMAAAAZCAYAAAACLBHaAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAQbSURBVGhD7Zp/aFNXFMe/kQpOrHWsFSakselWKBgonWVMaG2roqbIZJhpnUqZTEH3VyMIs7ao+Uexf8mEVaxi/bHh/qh/NFNqTW1hQYqh0MF+aBOSFv2j+6PtBP1Dmp1732nyniZNfMkTn7wPpO/cc8+9ee+ce8+96bu26enpeG9oEpH7N2FhThy1O/DVWjts3XfH4tHhX3Hb7cW3K15wtYVZ6J75AFv6zqJsvQe2jo6O+O2mI/iseAm+KXrJJhbvMvG5OGw2m5SvzRbg4dRzbPF3KsFctfsw1nxUiJlHT6WBhXkoqvgYf/z7H55c/xGLWIc4Xy3MSyKYiFvhNDuJYNoWKTnYwrwkZ6aF6dEZzEGc+8IJd+KzA70TXPXeEUXvASdaf4lyeZ4sfDBxCa2ZbPKIvmAG+/EbiwohDP3+6sO+QwSP6XdksAtdY9WoW+dgBZONDyYf4y8WFUKYmGTRAHJIs804EQzDH+zGVta8j4wM3QC2f4/tdlZoWNgHT2N/01+tTSRm3KAv4KvEvrKQpQwULZaXErK3YymWkbykcCni/p1oOlWJ8+NuBMp34dHxB+hpieAkycl/Fu6j+k7UIoyrns9xOsTqah/6bh5E6aAXrv2QNmgrwaEbir3jspv7Fm0HtH1q2v6Jo/f8cFwQbWtI9iLcSgEhur7eiQ9FuTHV/aQg+hN+6AU8F7eRb1g3TxofqH1od62RV8VmG86MT8lyPpnlq8CADdAVHCr3w3m8BqN9/YgN+slxwqlTGLvnQxXVBwbJLNqPOyHhSNaHbmEoMWhFHyUIkKPn5WOPK5Nt1X1eJBtN2xGcbqS2n4jvGkE4sgHtwkba+7EnkuZ+UhAL3MIoDZSWela8KfWdON8s7t+Nq29hFTIgmMpIr+OSBsdB9FDw2oVzpKyeEcLxLMo+yG6jkBXH93xXIWsyo9i3N3BRNwO4fGoEVU2bUMoaPdT6piigYoAZH1ADgqlQ2uLHmEh9XH4dkSpL4BKfxjaMsjZ7lBno2n+Fy3mGZ//mBicr9PO2AmpYMDMinaVKs6zOHk6Vov04pc9XNpu5MnyXBkmzN6d+Y7TOu8q9GCa51vczPDQA7wTCSqUB5BBMZS1zaTY3mVBm48k0a5QuaJOyN99rEvXZRXsmz8YNrEhHCh/I+1GesXR1JSm0Np+uzn2mp0NfMOvdNMrULJCOpC2nRPlA+9Ag1kyp5wd90zSr7lO0rf4SdQvNoIQ9BR0VcmOUaDt/Pyqy2vhk44My8V1qauAsY9EAkq/AiguxfPoZqw1AjNjGf3Ag3c8AC13MrliW4hXYnJFvTSi9yllAM7FtgHUW+SaZZvnNtTHQbz25UaGPL9M6ZKGXRDCtF2DmxzoDZHKuzajOAFmn88yN5nSedW7W/CjnZu34HzHHwHvwVqgGAAAAAElFTkSuQmCC'
    def conecta_Glac(self):
        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()
    def desconecta_Glac(self):
        self.conn.close()
    def montaTabelas(self):
        ### Cria tabela servprod
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS servprod (
                cod_sp INTEGER PRIMARY KEY,
                servprod CHAR(40) NOT NULL,
    			tiposerv CHAR(20),
    			sistemaserv CHAR(20),
    			id_marcaprod INTEGER,
    			id_fornec INTEGER,
                hor INTEGER(2,2),
                custo MONEY NOT NULL,
                valor MONEY NOT NULL,
    			sp CHAR(2) NOT NULL,
                descricao VARCHAR(200) NOT NULL

            );
        """)
        ### Automoveis
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS automoveis (
                cod_aut INTEGER PRIMARY KEY,
                automovel CHAR(40) NOT NULL,
                ano INTEGER NOT NULL,
    			marca CHAR NOT NULL


            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores (
                cod_forn INTEGER PRIMARY KEY,
                fornecedor CHAR(20) NOT NULL,
    			fone SMALLINT NOT NULL,
    			cnpj SMALLINT NOT NULL,
                cep SMALLINT NOT NULL,
    			endereco CHAR(20) NOT NULL,
                municipio CHAR(15) NOT NULL,
                descricao VARCHAR(200) NOT NULL

            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS marcaprod (
                cod_marca INTEGER PRIMARY KEY,
                marca CHAR(20) NOT NULL,
    			descricao VARCHAR(200) NOT NULL

            );
        """)
        ###
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS orcamento1 (
    			id_orc1 INTEGER PRIMARY KEY,
    			cliente_orc NUMERIC(8) NOT NULL,
    			placa_orc VARCHAR(12) NOT NULL,
    			descp1 VARCHAR(120) NOT NULL,
    			descp2 VARCHAR(120) NOT NULL,
    			descp3 VARCHAR(120) NOT NULL,
    			dia NUMERIC(4) NOT NULL,
    			mes NUMERIC(4) NOT NULL,
    			ano NUMERIC(4) NOT NULL,
    			totalizador NUMERIC(8) NOT NULL
    			);
    	""")
        ###
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS orcamento2 (
    			cod_orc2 INTEGER PRIMARY KEY,
    			id_orc2 NUMERIC(10) NOT NULL,
    			cod_item NUMERIC(8) NOT NULL,
    			desc_item VARCHAR(120) NOT NULL,
    			valor NUMERIC(8) NOT NULL,
    			quant NUMERIC(8) NOT NULL,
    			total NUMERIC(8) NOT NULL
    			);
    	""")
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS empresa (
                cod_emp INTEGER PRIMARY KEY,
                nome_emp CHAR(40) NOT NULL,
                endereco_emp CHAR(40) NOT NULL,
                bairro_emp CHAR(20) NOT NULL,
                municipio_emp CHAR(20) NOT NULL,
                uf_emp CHAR(2) NOT NULL,
                fone_emp CHAR(12) NOT NULL,
                cep_emp CHAR(12) NOT NULL,
                cpf_emp CHAR(12) NOT NULL,
                rg_emp CHAR(10) NOT NULL,
                obs_emp CHAR(200) NOT NULL
            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS frota (
                id INTEGER PRIMARY KEY,
    			veiculo CHAR NOT NULL,
    			anoveic CHAR NOT NULL,
                placa CHAR NOT NULL,
    			renavan CHAR NOT NULL,
    			cliente CHAR NOT NULL,
    			combust CHAR NOT NULL,
    			motor CHAR NOT NULL,
    			cor CHAR NOT NULL


            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_orc (
                cod_item INTEGER PRIMARY KEY,
                quant INTEGER,
    			valor INTEGER,
                item INTEGER

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod_cli INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
    			nascdia NUMERIC(2) NOT NULL,
    			nascmes NUMERIC(2) NOT NULL,
    			endereco CHAR(40) NOT NULL,
    			complemento CHAR(40) NOT NULL,
    			bairro CHAR(20) NOT NULL,
                municipio CHAR(20) NOT NULL,
    			cep NUMERIC(12) NOT NULL,
                uf CHAR(2) NOT NULL,
    			numcasa CHAR(20) NOT NULL,
                fone1ddd NUMERIC(2) NOT NULL,
    			fone1 NUMERIC(10) NOT NULL,
    			fone2ddd NUMERIC(2) NOT NULL,
    			fone2 NUMERIC(10) NOT NULL,
                cpf NUMERIC(12) NOT NULL,
                rg NUMERIC(10) NOT NULL,
    			email CHAR(40) NOT NULL,
                obs CHAR(200) NOT NULL,
    			nascano NUMERIC(4) NOT NULL

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS codfalha (
                cod_falha CHAR(40) NOT NULL,
                falha CHAR(40) NOT NULL,
    			falha2 CHAR(20),
    			falha3 CHAR(20),
    			falha4 CHAR(20),
    			falha5 NUMERIC(20)

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orcfalha (
                id_orcfalha NUMERIC(10),
                cod_orcfalha VARCHAR(40),
                orcfalha CHAR(40),
    			orcfalha2 CHAR(200),
    			orcfalha3 CHAR(200),
    			orcfalha4 CHAR(200),
    			orcfalha5 NUMERIC(10)

            );
        """)
        ####
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS formapag (
    	    	id INTEGER PRIMARY KEY,
    			ordem CHAR NOT NULL,
    			tipopag CHAR NOT NULL,
    	        valorpagar CHAR NOT NULL,
    			valordeduzir CHAR NOT NULL,
    			dia CHAR NOT NULL,
    			mes CHAR NOT NULL,
    			ano CHAR NOT NULL,
    			pago CHAR NOT NULL,
    			fpag10 CHAR NULL,
    			fpag11 CHAR NULL

    	        );
    	    """)
        ####
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS meiopag (
    	    	id INTEGER PRIMARY KEY,
    			meiopag CHAR NOT NULL,
    			meiopag2 CHAR NOT NULL,
    	        meiopag3 CHAR NOT NULL,
    			meiopag4 CHAR NOT NULL

    	        );
    	    """)
        self.conn.commit()

    def carrega_cliente(self):

        self.listNome.delete(0, END)
        self.listEndereco.delete(0, END)
        self.listBairro.delete(0, END)
        self.listMunicipio.delete(0, END)
        self.listCpf.delete(0, END)
        self.listFone.delete(0, END)
        self.listUf.delete(0, END)
        self.listObs.delete(0, END)
        self.entradaCod_aut.delete(0, END)
        self.listAut.delete(0, END)
        self.listAno.delete(0, END)
        self.listMarca.delete(0, END)
        self.listCombustivel.delete(0, END)
        self.listCor.delete(0, END)
        self.placa.delete(0, END)

        self.conecta_Glac()


        cod_cli = self.entradaCod_cli.get()
        nomecur = self.cursor

        nomecur.execute("SELECT UPPER(nome) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            i = str(i); i = i.replace('(',''); i = i.replace(')',''); i = i.replace("'",""); i = i.replace(',','')
            self.listNome.insert(END, i)
            print(i)

        nomeend = self.cursor
        nomeend.execute("""SELECT UPPER(endereco), "Nº", numcasa
            FROM clientes WHERE cod_cli = '%s' """ % cod_cli)
        consultaend = self.cursor.fetchall()
        for i in consultaend:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listEndereco.insert(END, i)
            print(i)

        nomebairro = self.cursor
        nomebairro.execute("SELECT UPPER(bairro) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultabairro = self.cursor.fetchall()
        for i in consultabairro:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listBairro.insert(END, i)
            print(i)

        nomemunicipio = self.cursor
        nomemunicipio.execute("SELECT UPPER(municipio) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultamunicipio = self.cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMunicipio.insert(END, i)
            print(i)

        nomecpf = self.cursor
        nomecpf.execute("SELECT cpf FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacpf = self.cursor.fetchall()
        for i in consultacpf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCpf.insert(END, i)
            print(i)

        nomefone = self.cursor
        nomefone.execute("SELECT fone1ddd, fone1 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone = self.cursor.fetchall()
        for i in consultafone:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listFone.insert(END, i)
            print(i)

        nomeuf = self.cursor
        nomeuf.execute("SELECT UPPER(uf) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultauf = self.cursor.fetchall()
        for i in consultauf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listUf.insert(END, i)
            print(i)

        nomeobs = self.cursor
        nomeobs.execute("SELECT obs FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaobs = self.cursor.fetchall()
        for i in consultaobs:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listObs.insert(END, i)
            print(i)

        pla = self.cursor
        pla.execute("SELECT placa FROM frota, clientes WHERE idcliente = cod_cli and cod_cli = '%s'" % cod_cli)
        consultapla = self.cursor.fetchall()
        for i in consultapla:
            self.entradaCod_aut.insert(END, i)

        self.desconecta_Glac()

        def carrega_cliente_a(event):
            self.carrega_cliente()
    def limpa_cliente(self):
        self.entradaCod_cli.delete(0, END)
        self.listNome.delete(0, END)
        self.listEndereco.delete(0, END)
        self.listBairro.delete(0, END)
        self.listMunicipio.delete(0, END)
        self.listCpf.delete(0, END)
        self.listFone.delete(0, END)
        self.listUf.delete(0, END)
        self.listObs.delete(0, END)
        self.entradaCod_aut.delete(0, END)
        self.listAut.delete(0, END)
        self.listAno.delete(0, END)
        self.listMarca.delete(0, END)
        self.listCombustivel.delete(0, END)
        self.listCor.delete(0, END)
        self.placa.delete(0, END)
        self.entradaObs.delete(0, END)
        self.area1.delete(0, END)
        self.area2.delete(0, END)
        self.area3.delete(0, END)
        self.area4.delete(0, END)
        self.entradatotal.delete(0, END)
        self.listInicio.delete(0, END)
        self.listFim.delete(0, END)

        self.codServ1.delete(0, END)
        self.codServ2.delete(0, END)
        self.codServ3.delete(0, END)
        self.codServ4.delete(0, END)
        self.codServ5.delete(0, END)
        self.codServ6.delete(0, END)
        self.codServ7.delete(0, END)
        self.codServ8.delete(0, END)
        self.codServ9.delete(0, END)
        self.codServ10.delete(0, END)
        self.codServ11.delete(0, END)
        self.codServ12.delete(0, END)
        self.codServ13.delete(0, END)
        self.codServ14.delete(0, END)
        self.codServ15.delete(0, END)
        self.codServ16.delete(0, END)
        self.codServ17.delete(0, END)
        self.codServ18.delete(0, END)
        self.codServ19.delete(0, END)
        self.codServ20.delete(0, END)

        self.listaCol2a.delete(0, END)
        self.listaCol3a.delete(0, END)
        self.listaCol3a.insert(END, 1)
        self.listaCol4a.delete(0, END)
        self.listaCol4a.insert(END, 0)
        self.listaCol5a.delete(0, END)
        self.listaCol5a.insert(END, 0)

        self.listaCol2b.delete(0, END)
        self.listaCol3b.delete(0, END)
        self.listaCol3b.insert(END, 1)
        self.listaCol4b.delete(0, END)
        self.listaCol4b.insert(END, 0)
        self.listaCol5b.delete(0, END)
        self.listaCol5b.insert(END, 0)

        self.listaCol2c.delete(0, END)
        self.listaCol3c.delete(0, END)
        self.listaCol3c.insert(END, 1)
        self.listaCol4c.delete(0, END)
        self.listaCol4c.insert(END, 0)
        self.listaCol5c.delete(0, END)
        self.listaCol5c.insert(END, 0)

        self.listaCol2d.delete(0, END)
        self.listaCol3d.delete(0, END)
        self.listaCol3d.insert(END, 1)
        self.listaCol4d.delete(0, END)
        self.listaCol4d.insert(END, 0)
        self.listaCol5d.delete(0, END)
        self.listaCol5d.insert(END, 0)

        self.listaCol2e.delete(0, END)
        self.listaCol3e.delete(0, END)
        self.listaCol3e.insert(END, 1)
        self.listaCol4e.delete(0, END)
        self.listaCol4e.insert(END, 0)
        self.listaCol5e.delete(0, END)
        self.listaCol5e.insert(END, 0)

        self.listaCol2f.delete(0, END)
        self.listaCol3f.delete(0, END)
        self.listaCol3f.insert(END, 1)
        self.listaCol4f.delete(0, END)
        self.listaCol4f.insert(END, 0)
        self.listaCol5f.delete(0, END)
        self.listaCol5f.insert(END, 0)

        self.listaCol2g.delete(0, END)
        self.listaCol3g.delete(0, END)
        self.listaCol3g.insert(END, 1)
        self.listaCol4g.delete(0, END)
        self.listaCol4g.insert(END, 0)
        self.listaCol5g.delete(0, END)
        self.listaCol5g.insert(END, 0)

        self.listaCol2h.delete(0, END)
        self.listaCol3h.delete(0, END)
        self.listaCol3h.insert(END, 1)
        self.listaCol4h.delete(0, END)
        self.listaCol4h.insert(END, 0)
        self.listaCol5h.delete(0, END)
        self.listaCol5h.insert(END, 0)

        self.listaCol2i.delete(0, END)
        self.listaCol3i.delete(0, END)
        self.listaCol3i.insert(END, 1)
        self.listaCol4i.delete(0, END)
        self.listaCol4i.insert(END, 0)
        self.listaCol5i.delete(0, END)
        self.listaCol5i.insert(END, 0)

        self.listaCol2j.delete(0, END)
        self.listaCol3j.delete(0, END)
        self.listaCol3j.insert(END, 1)
        self.listaCol4j.delete(0, END)
        self.listaCol4j.insert(END, 0)
        self.listaCol5j.delete(0, END)
        self.listaCol5j.insert(END, 0)

        self.listaCol2k.delete(0, END)
        self.listaCol3k.delete(0, END)
        self.listaCol3k.insert(END, 1)
        self.listaCol4k.delete(0, END)
        self.listaCol4k.insert(END, 0)
        self.listaCol5k.delete(0, END)
        self.listaCol5k.insert(END, 0)

        self.listaCol2l.delete(0, END)
        self.listaCol3l.delete(0, END)
        self.listaCol3l.insert(END, 1)
        self.listaCol4l.delete(0, END)
        self.listaCol4l.insert(END, 0)
        self.listaCol5l.delete(0, END)
        self.listaCol5l.insert(END, 0)

        self.listaCol2m.delete(0, END)
        self.listaCol3m.delete(0, END)
        self.listaCol3m.insert(END, 1)
        self.listaCol4m.delete(0, END)
        self.listaCol4m.insert(END, 0)
        self.listaCol5m.delete(0, END)
        self.listaCol5m.insert(END, 0)

        self.listaCol2n.delete(0, END)
        self.listaCol3n.delete(0, END)
        self.listaCol3n.insert(END, 1)
        self.listaCol4n.delete(0, END)
        self.listaCol4n.insert(END, 0)
        self.listaCol5n.delete(0, END)
        self.listaCol5n.insert(END, 0)

        self.listaCol2o.delete(0, END)
        self.listaCol3o.delete(0, END)
        self.listaCol3o.insert(END, 1)
        self.listaCol4o.delete(0, END)
        self.listaCol4o.insert(END, 0)
        self.listaCol5o.delete(0, END)
        self.listaCol5o.insert(END, 0)

        self.listaCol2p.delete(0, END)
        self.listaCol3p.delete(0, END)
        self.listaCol3p.insert(END, 1)
        self.listaCol4p.delete(0, END)
        self.listaCol4p.insert(END, 0)
        self.listaCol5p.delete(0, END)
        self.listaCol5p.insert(END, 0)

        self.listaCol2q.delete(0, END)
        self.listaCol3q.delete(0, END)
        self.listaCol3q.insert(END, 1)
        self.listaCol4q.delete(0, END)
        self.listaCol4q.insert(END, 0)
        self.listaCol5q.delete(0, END)
        self.listaCol5q.insert(END, 0)

        self.listaCol2r.delete(0, END)
        self.listaCol3r.delete(0, END)
        self.listaCol3r.insert(END, 1)
        self.listaCol4r.delete(0, END)
        self.listaCol4r.insert(END, 0)
        self.listaCol5r.delete(0, END)
        self.listaCol5r.insert(END, 0)

        self.listaCol2s.delete(0, END)
        self.listaCol3s.delete(0, END)
        self.listaCol3s.insert(END, 1)
        self.listaCol4s.delete(0, END)
        self.listaCol4s.insert(END, 0)
        self.listaCol5s.delete(0, END)
        self.listaCol5s.insert(END, 0)

        self.listaCol2t.delete(0, END)
        self.listaCol3t.delete(0, END)
        self.listaCol3t.insert(END, 1)
        self.listaCol4t.delete(0, END)
        self.listaCol4t.insert(END, 0)
        self.listaCol5t.delete(0, END)
        self.listaCol5t.insert(END, 0)

        self.listaNumOrc.delete(0, END)
        self.are1.delete(0, END)
        self.are2.delete(0, END)
        self.are3.delete(0, END)
        self.are4.delete(0, END)
        self.are5.delete(0, END)
        self.are6.delete(0, END)
        self.are7.delete(0, END)
        self.are8.delete(0, END)
        self.are9.delete(0, END)

        self.codServ1F.delete(0, END)
        self.codServ2F.delete(0, END)
        self.codServ3F.delete(0, END)
        self.codServ4F.delete(0, END)
        self.codServ5F.delete(0, END)
        self.codServ6F.delete(0, END)
        self.codServ7F.delete(0, END)
        self.codServ8F.delete(0, END)
        self.codServ9F.delete(0, END)
        self.codServ10F.delete(0, END)

        self.listaCol2aF.delete(0, END)
        self.listaCol3aF.delete(0, END)

        self.listaCol2bF.delete(0, END)
        self.listaCol3bF.delete(0, END)

        self.listaCol2cF.delete(0, END)
        self.listaCol3cF.delete(0, END)

        self.listaCol2dF.delete(0, END)
        self.listaCol3dF.delete(0, END)

        self.listaCol2eF.delete(0, END)
        self.listaCol3eF.delete(0, END)

        self.listaCol2fF.delete(0, END)
        self.listaCol3fF.delete(0, END)

        self.listaCol2gF.delete(0, END)
        self.listaCol3gF.delete(0, END)

        self.listaCol2hF.delete(0, END)
        self.listaCol3hF.delete(0, END)

        self.listaCol2iF.delete(0, END)
        self.listaCol3iF.delete(0, END)

        self.listaCol2jF.delete(0, END)
        self.listaCol3jF.delete(0, END)
    def carrega_automovel(self, event):
        self.listAut.delete(0, END)
        self.listAno.delete(0, END)
        self.listMarca.delete(0, END)
        self.listCombustivel.delete(0, END)
        self.listCor.delete(0, END)
        self.listObs.delete(0, END)
        self.placa.delete(0, END)

        self.conecta_Glac()

        pos = int(self.entradaCod_aut.curselection()[0])
        placa = self.entradaCod_aut.get(pos)

        nomeplac = self.cursor

        nomeplac.execute("SELECT placa FROM frota WHERE placa = '%s'" % placa)
        consultaplac = self.cursor.fetchall()
        for i in consultaplac:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.placa.insert(END, i)

        nomeaut = self.cursor

        nomeaut.execute(
            "SELECT UPPER(veiculo) FROM frota WHERE placa = '%s'" % placa)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAut.insert(END, i)

        nomeano = self.cursor
        nomeano.execute("SELECT ano FROM frota WHERE placa = '%s'" % placa)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAno.insert(END, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT UPPER(montadora) FROM frota WHERE placa = '%s'" % placa)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMarca.insert(END, i)

        nomecomb = self.cursor
        nomecomb.execute("SELECT UPPER(combust) FROM frota WHERE placa = '%s'" % placa)
        consultacomb = self.cursor.fetchall()
        for i in consultacomb:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCombustivel.insert(END, i)

        nomecor = self.cursor
        nomecor.execute("SELECT UPPER(cor) FROM frota WHERE placa = '%s'" % placa)
        consultacor = self.cursor.fetchall()
        for i in consultacor:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCor.insert(END, i)

        self.desconecta_Glac()

        def carrega_automovel_a(event):
            carrega_automovel()
    def abre_orc(self):

        self.listaNumOrc.delete(0, END)
        id_orc1 = self.listaNumOrc.get()
        numeroorcamento = self.listaNumOrc.get()
        cliente_orc = self.entradaCod_cli.get()
        placa_orc = self.placa.get()
        dia = self.entradaDataorc.get()
        mes = self.entradaDataorc2.get()
        ano = self.entradaDataorc3.get()
        descp1 = self.area1.get()
        descp2 = self.area2.get()
        descp3 = self.area3.get()
        descp4 = self.area4.get()
        totalizador = self.entradatotal.get()
        km = self.entradaObs.get()
        tecnico = self.entradaTecnico.get()
        tipoOrc = self.Tipvar.get()
        comp1 = self.listInicio.get()
        comp2 = self.listFim.get()

        self.conecta_Glac()

        self.cursor.execute("""
    			INSERT INTO orcamento1 ( cliente_orc, placa_orc, descp1, descp2, descp3, descp4, dia, mes, ano, tecnico, totalizador, tipoOrc, km, comp1, comp2)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cliente_orc, placa_orc, descp1, descp2, descp3, descp4, dia, mes, ano, tecnico, totalizador,
                        tipoOrc, km, comp1, comp2))
        self.conn.commit()

        numeroorc = self.cursor

        numeroorc.execute("""SELECT MAX(id_orc1) FROM orcamento1""")
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaNumOrc.insert(END, i)

        # variaveis orcamento2
        id_orc2 = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        cod_item2 = self.codServ2.get()
        cod_item3 = self.codServ3.get()
        cod_item4 = self.codServ4.get()
        cod_item5 = self.codServ5.get()
        cod_item6 = self.codServ6.get()
        cod_item7 = self.codServ7.get()
        cod_item8 = self.codServ8.get()
        cod_item9 = self.codServ9.get()
        cod_item10 = self.codServ10.get()
        cod_item11 = self.codServ11.get()
        cod_item12 = self.codServ12.get()
        cod_item13 = self.codServ13.get()
        cod_item14 = self.codServ14.get()
        cod_item15 = self.codServ15.get()
        cod_item16 = self.codServ16.get()
        cod_item17 = self.codServ17.get()
        cod_item18 = self.codServ18.get()
        cod_item19 = self.codServ19.get()
        cod_item20 = self.codServ20.get()

        desc_item1 = self.listaCol2a.get()
        desc_item2 = self.listaCol2b.get()
        desc_item3 = self.listaCol2c.get()
        desc_item4 = self.listaCol2d.get()
        desc_item5 = self.listaCol2e.get()
        desc_item6 = self.listaCol2f.get()
        desc_item7 = self.listaCol2g.get()
        desc_item8 = self.listaCol2h.get()
        desc_item9 = self.listaCol2i.get()
        desc_item10 = self.listaCol2j.get()
        desc_item11 = self.listaCol2k.get()
        desc_item12 = self.listaCol2l.get()
        desc_item13 = self.listaCol2m.get()
        desc_item14 = self.listaCol2n.get()
        desc_item15 = self.listaCol2o.get()
        desc_item16 = self.listaCol2p.get()
        desc_item17 = self.listaCol2q.get()
        desc_item18 = self.listaCol2r.get()
        desc_item19 = self.listaCol2s.get()
        desc_item20 = self.listaCol2t.get()
        ###
        valor1 = self.listaCol4a.get()
        valor2 = self.listaCol4b.get()
        valor3 = self.listaCol4c.get()
        valor4 = self.listaCol4d.get()
        valor5 = self.listaCol4e.get()
        valor6 = self.listaCol4f.get()
        valor7 = self.listaCol4g.get()
        valor8 = self.listaCol4h.get()
        valor9 = self.listaCol4i.get()
        valor10 = self.listaCol4j.get()
        valor11 = self.listaCol4k.get()
        valor12 = self.listaCol4l.get()
        valor13 = self.listaCol4m.get()
        valor14 = self.listaCol4n.get()
        valor15 = self.listaCol4o.get()
        valor16 = self.listaCol4p.get()
        valor17 = self.listaCol4q.get()
        valor18 = self.listaCol4r.get()
        valor19 = self.listaCol4s.get()
        valor20 = self.listaCol4t.get()

        quant1 = self.listaCol3a.get()
        quant2 = self.listaCol3b.get()
        quant3 = self.listaCol3c.get()
        quant4 = self.listaCol3d.get()
        quant5 = self.listaCol3e.get()
        quant6 = self.listaCol3f.get()
        quant7 = self.listaCol3g.get()
        quant8 = self.listaCol3h.get()
        quant9 = self.listaCol3i.get()
        quant10 = self.listaCol3j.get()
        quant11 = self.listaCol3k.get()
        quant12 = self.listaCol3l.get()
        quant13 = self.listaCol3m.get()
        quant14 = self.listaCol3n.get()
        quant15 = self.listaCol3o.get()
        quant16 = self.listaCol3p.get()
        quant17 = self.listaCol3q.get()
        quant18 = self.listaCol3r.get()
        quant19 = self.listaCol3s.get()
        quant20 = self.listaCol3t.get()

        total1 = self.listaCol5a.get()
        self.total2 = self.listaCol5b.get()
        self.total3 = self.listaCol5c.get()
        self.total4 = self.listaCol5d.get()
        self.total5 = self.listaCol5e.get()
        self.total6 = self.listaCol5f.get()
        self.total7 = self.listaCol5g.get()
        self.total8 = self.listaCol5h.get()
        self.total9 = self.listaCol5i.get()
        self.total10 = self.listaCol5j.get()
        self.total11 = self.listaCol5k.get()
        self.total12 = self.listaCol5l.get()
        self.total13 = self.listaCol5m.get()
        self.total14 = self.listaCol5n.get()
        self.total15 = self.listaCol5o.get()
        self.total16 = self.listaCol5p.get()
        self.total17 = self.listaCol5q.get()
        self.total18 = self.listaCol5r.get()
        self.total19 = self.listaCol5s.get()
        self.total20 = self.listaCol5t.get()

        ordem1 = int(1)
        ordem2 = int(2)
        ordem3 = int(3)
        ordem4 = int(4)
        ordem5 = int(5)
        ordem6 = int(6)
        ordem7 = int(7)
        ordem8 = int(8)
        ordem9 = int(9)
        ordem10 = int(10)
        ordem11 = int(11)
        ordem12 = int(12)
        ordem13 = int(13)
        ordem14 = int(14)
        ordem15 = int(15)
        ordem16 = int(16)
        ordem17 = int(17)
        ordem18 = int(18)
        ordem19 = int(19)
        ordem20 = int(20)

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item1, desc_item1, valor1, quant1, total1, ordem1))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item2, desc_item2, valor2, quant2, self.total2, ordem2))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item3, desc_item3, valor3, quant3, self.total3, ordem3))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item4, desc_item4, valor4, quant4, self.total4, ordem4))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item5, desc_item5, valor5, quant5, self.total5, ordem5))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item6, desc_item6, valor6, quant6, self.total6, ordem6))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item7, desc_item7, valor7, quant7, self.total7, ordem7))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item8, desc_item8, valor8, quant8, self.total8, ordem8))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item9, desc_item9, valor9, quant9, self.total9, ordem9))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item10, desc_item10, valor10, quant10, self.total10, ordem10))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item11, desc_item11, valor11, quant11, self.total11, ordem11))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item12, desc_item12, valor12, quant12, self.total12, ordem12))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item13, desc_item13, valor13, quant13, self.total13, ordem13))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item14, desc_item14, valor14, quant14, self.total14, ordem14))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item15, desc_item15, valor15, quant15, self.total15, ordem15))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item16, desc_item16, valor16, quant16, self.total16, ordem16))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item17, desc_item17, valor17, quant17, self.total17, ordem17))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item18, desc_item18, valor18, quant18, self.total18, ordem18))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item19, desc_item19, valor19, quant19, self.total19, ordem19))
        self.conn.commit()

        self.cursor.execute("""
    			INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, total, ordem_item)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item20, desc_item20, valor20, quant20, self.total20, ordem20))
        self.conn.commit()

        ################
        # Vistoria variaveis
        codVist = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("""
    			INSERT INTO vistoria ( cod, vist1, vist2, vist3, vist4, vist5, vist6, vist7, vist8, vist9)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (codVist, tanque, radio, odometro, calota, triangulo, macaco, estepe, obs1, obs2))
        self.conn.commit()

        ########################
        ### OrcFalha
        # variaveis orcfalha

        # id_orc2 = self.listaNumOrc.get()
        cod_item1F = self.codServ1F.get()
        cod_item2F = self.codServ2F.get()
        cod_item3F = self.codServ3F.get()
        cod_item4F = self.codServ4F.get()
        cod_item5F = self.codServ5F.get()
        cod_item6F = self.codServ6F.get()
        cod_item7F = self.codServ7F.get()
        cod_item8F = self.codServ8F.get()
        cod_item9F = self.codServ9F.get()
        cod_item10F = self.codServ10F.get()

        desc_item1F = self.listaCol2aF.get()
        desc_item2F = self.listaCol2bF.get()
        desc_item3F = self.listaCol2cF.get()
        desc_item4F = self.listaCol2dF.get()
        desc_item5F = self.listaCol2eF.get()
        desc_item6F = self.listaCol2fF.get()
        desc_item7F = self.listaCol2gF.get()
        desc_item8F = self.listaCol2hF.get()
        desc_item9F = self.listaCol2iF.get()
        desc_item10F = self.listaCol2jF.get()

        ###

        quant1F = self.listaCol3aF.get()
        quant2F = self.listaCol3bF.get()
        quant3F = self.listaCol3cF.get()
        quant4F = self.listaCol3dF.get()
        quant5F = self.listaCol3eF.get()
        quant6F = self.listaCol3fF.get()
        quant7F = self.listaCol3gF.get()
        quant8F = self.listaCol3hF.get()
        quant9F = self.listaCol3iF.get()
        quant10F = self.listaCol3jF.get()

        self.cursor.execute("""
            			INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
            			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item1F, desc_item1F, quant1F, ordem1))
        self.conn.commit()

        self.cursor.execute("""
                    			INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                    			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item2F, desc_item2F, quant2F, ordem2))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                    			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item3F, desc_item3F, quant3F, ordem3))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                           			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item4F, desc_item4F, quant4F, ordem4))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                           			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item5F, desc_item5F, quant5F, ordem5))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                           			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item6F, desc_item6F, quant6F, ordem6))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                           			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item7F, desc_item7F, quant7F, ordem7))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                           			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item8F, desc_item8F, quant8F, ordem8))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                           			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item9F, desc_item9F, quant9F, ordem9))
        self.conn.commit()

        self.cursor.execute("""	INSERT INTO orcfalha ( id_orcfalha, cod_orcfalha, orcfalha, orcfalha2, orcfalha5)
                           			VALUES ( ?, ?, ?, ?, ?)""",
                       (id_orc2, cod_item10F, desc_item10F, quant10F, ordem10))
        self.conn.commit()

        self.desconecta_Glac()

        self.totalbotao()

        msg = "Orçamento gravado com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC - Orçamento", msg)
    def altera_orc(self):
        id_orc1 = self.listaNumOrc.get()
        cliente_orc = self.entradaCod_cli.get()
        placa_orc = self.placa.get()
        dia = self.entradaDataorc.get()
        mes = self.entradaDataorc2.get()
        ano = self.entradaDataorc3.get()
        descp1 = self.area1.get()
        descp2 = self.area2.get()
        descp3 = self.area3.get()
        descp4 = self.area4.get()
        totalizador = self.entradatotal.get()
        km = self.entradaObs.get()
        tecnico = self.entradaTecnico.get()
        tipoOrc = self.Tipvar.get()
        comp1 = self.listInicio.get()
        comp2 = self.listFim.get()

        self.conecta_Glac()

        self.cursor.execute("""
    			UPDATE orcamento1 SET id_orc1 = ?, cliente_orc = ?, placa_orc = ?, dia = ?,
    			mes = ?, ano = ?, descp1 = ?, descp2 = ?, descp3 = ?, descp4 = ?, totalizador = ?, km = ?,
    			tecnico = ?, tipoOrc = ? , comp1 = ?, comp2 = ? WHERE id_orc1 = ?""",
                       (id_orc1, cliente_orc, placa_orc, dia, mes, ano, descp1, descp2, descp3,
                        descp4, totalizador, km, tecnico, tipoOrc, comp1, comp2, id_orc1))
        self.conn.commit()

        # variaveis orcamento2
        id_orc2 = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        cod_item2 = self.codServ2.get()
        cod_item3 = self.codServ3.get()
        cod_item4 = self.codServ4.get()
        cod_item5 = self.codServ5.get()
        cod_item6 = self.codServ6.get()
        cod_item7 = self.codServ7.get()
        cod_item8 = self.codServ8.get()
        cod_item9 = self.codServ9.get()
        cod_item10 = self.codServ10.get()
        cod_item11 = self.codServ11.get()
        cod_item12 = self.codServ12.get()
        cod_item13 = self.codServ13.get()
        cod_item14 = self.codServ14.get()
        cod_item15 = self.codServ15.get()
        cod_item16 = self.codServ16.get()
        cod_item17 = self.codServ17.get()
        cod_item18 = self.codServ18.get()
        cod_item19 = self.codServ19.get()
        cod_item20 = self.codServ20.get()

        desc_item1 = self.listaCol2a.get()
        desc_item2 = self.listaCol2b.get()
        desc_item3 = self.listaCol2c.get()
        desc_item4 = self.listaCol2d.get()
        desc_item5 = self.listaCol2e.get()
        desc_item6 = self.listaCol2f.get()
        desc_item7 = self.listaCol2g.get()
        desc_item8 = self.listaCol2h.get()
        desc_item9 = self.listaCol2i.get()
        desc_item10 = self.listaCol2j.get()
        desc_item11 = self.listaCol2k.get()
        desc_item12 = self.listaCol2l.get()
        desc_item13 = self.listaCol2m.get()
        desc_item14 = self.listaCol2n.get()
        desc_item15 = self.listaCol2o.get()
        desc_item16 = self.listaCol2p.get()
        desc_item17 = self.listaCol2q.get()
        desc_item18 = self.listaCol2r.get()
        desc_item19 = self.listaCol2s.get()
        desc_item20 = self.listaCol2t.get()
        ###
        valor1 = self.listaCol4a.get()
        valor2 = self.listaCol4b.get()
        valor3 = self.listaCol4c.get()
        valor4 = self.listaCol4d.get()
        valor5 = self.listaCol4e.get()
        valor6 = self.listaCol4f.get()
        valor7 = self.listaCol4g.get()
        valor8 = self.listaCol4h.get()
        valor9 = self.listaCol4i.get()
        valor10 = self.listaCol4j.get()
        valor11 = self.listaCol4k.get()
        valor12 = self.listaCol4l.get()
        valor13 = self.listaCol4m.get()
        valor14 = self.listaCol4n.get()
        valor15 = self.listaCol4o.get()
        valor16 = self.listaCol4p.get()
        valor17 = self.listaCol4q.get()
        valor18 = self.listaCol4r.get()
        valor19 = self.listaCol4s.get()
        valor20 = self.listaCol4t.get()

        quant1 = self.listaCol3a.get()
        quant2 = self.listaCol3b.get()
        quant3 = self.listaCol3c.get()
        quant4 = self.listaCol3d.get()
        quant5 = self.listaCol3e.get()
        quant6 = self.listaCol3f.get()
        quant7 = self.listaCol3g.get()
        quant8 = self.listaCol3h.get()
        quant9 = self.listaCol3i.get()
        quant10 = self.listaCol3j.get()
        quant11 = self.listaCol3k.get()
        quant12 = self.listaCol3l.get()
        quant13 = self.listaCol3m.get()
        quant14 = self.listaCol3n.get()
        quant15 = self.listaCol3o.get()
        quant16 = self.listaCol3p.get()
        quant17 = self.listaCol3q.get()
        quant18 = self.listaCol3r.get()
        quant19 = self.listaCol3s.get()
        quant20 = self.listaCol3t.get()

        total1 = self.listaCol5a.get()
        self.total2 = self.listaCol5b.get()
        self.total3 = self.listaCol5c.get()
        self.total4 = self.listaCol5d.get()
        self.total5 = self.listaCol5e.get()
        self.total6 = self.listaCol5f.get()
        self.total7 = self.listaCol5g.get()
        self.total8 = self.listaCol5h.get()
        self.total9 = self.listaCol5i.get()
        self.total10 = self.listaCol5j.get()
        self.total11 = self.listaCol5k.get()
        self.total12 = self.listaCol5l.get()
        self.total13 = self.listaCol5m.get()
        self.total14 = self.listaCol5n.get()
        self.total15 = self.listaCol5o.get()
        self.total16 = self.listaCol5p.get()
        self.total17 = self.listaCol5q.get()
        self.total18 = self.listaCol5r.get()
        self.total19 = self.listaCol5s.get()
        self.total20 = self.listaCol5t.get()

        ordem1 = int(1)
        ordem2 = int(2)
        ordem3 = int(3)
        ordem4 = int(4)
        ordem5 = int(5)
        ordem6 = int(6)
        ordem7 = int(7)
        ordem8 = int(8)
        ordem9 = int(9)
        ordem10 = int(10)
        ordem11 = int(11)
        ordem12 = int(12)
        ordem13 = int(13)
        ordem14 = int(14)
        ordem15 = int(15)
        ordem16 = int(16)
        ordem17 = int(17)
        ordem18 = int(18)
        ordem19 = int(19)
        ordem20 = int(20)

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 1""",
                       (cod_item1, desc_item1, valor1, quant1, total1, ordem1, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 2""",
                       (cod_item2, desc_item2, valor2, quant2, self.total2, ordem2, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 3""",
                       (cod_item3, desc_item3, valor3, quant3, self.total3, ordem3, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 4""",
                       (cod_item4, desc_item4, valor4, quant4, self.total4, ordem4, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 5""",
                       (cod_item5, desc_item5, valor5, quant5, self.total5, ordem5, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 6""",
                       (cod_item6, desc_item6, valor6, quant6, self.total6, ordem6, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 7""",
                       (cod_item7, desc_item7, valor7, quant7, self.total7, ordem7, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 8""",
                       (cod_item8, desc_item8, valor8, quant8, self.total8, ordem8, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 9""",
                       (cod_item9, desc_item9, valor9, quant9, self.total9, ordem9, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 10""",
                       (cod_item10, desc_item10, valor10, quant10, self.total10, ordem10, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 11""",
                       (cod_item11, desc_item11, valor11, quant11, self.total11, ordem11, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 12""",
                       (cod_item12, desc_item12, valor12, quant12, self.total12, ordem12, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 13""",
                       (cod_item13, desc_item13, valor13, quant13, self.total13, ordem13, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 14""",
                       (cod_item14, desc_item14, valor14, quant14, self.total14, ordem14, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 15""",
                       (cod_item15, desc_item15, valor15, quant15, self.total15, ordem15, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 16""",
                       (cod_item16, desc_item16, valor16, quant16, self.total16, ordem16, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 17""",
                       (cod_item17, desc_item17, valor17, quant17, self.total17, ordem17, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 18""",
                       (cod_item18, desc_item18, valor18, quant18, self.total18, ordem18, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 19""",
                       (cod_item19, desc_item19, valor19, quant19, self.total19, ordem19, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
    			UPDATE orcamento2 SET cod_item = ?, desc_item = ?, valor = ?, quant = ?, total = ?,
    			ordem_item = ? WHERE id_orc2 = ? AND ordem_item = 20""",
                       (cod_item20, desc_item20, valor20, quant20, self.total20, ordem20, id_orc2))
        self.conn.commit()

        ################
        # Vistoria variaveis
        cod = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("""
    			UPDATE vistoria SET vist1 = ?, vist2 = ?, vist3 = ?, vist4 = ?, vist5 = ?,
    			vist6 = ? , vist7 = ?, vist8 = ?, vist9 = ? WHERE cod = ? """,
                       (tanque, radio, odometro, calota, triangulo, macaco, estepe, obs1, obs2, cod))
        self.conn.commit()

        ###########################
        ### Falhas
        cod_item1F = self.codServ1F.get()
        cod_item2F = self.codServ2F.get()
        cod_item3F = self.codServ3F.get()
        cod_item4F = self.codServ4F.get()
        cod_item5F = self.codServ5F.get()
        cod_item6F = self.codServ6F.get()
        cod_item7F = self.codServ7F.get()
        cod_item8F = self.codServ8F.get()
        cod_item9F = self.codServ9F.get()
        cod_item10F = self.codServ10F.get()

        desc_item1F = self.listaCol2aF.get()
        desc_item2F = self.listaCol2bF.get()
        desc_item3F = self.listaCol2cF.get()
        desc_item4F = self.listaCol2dF.get()
        desc_item5F = self.listaCol2eF.get()
        desc_item6F = self.listaCol2fF.get()
        desc_item7F = self.listaCol2gF.get()
        desc_item8F = self.listaCol2hF.get()
        desc_item9F = self.listaCol2iF.get()
        desc_item10F = self.listaCol2jF.get()

        ###


        quant1F = self.listaCol3aF.get()
        quant2F = self.listaCol3bF.get()
        quant3F = self.listaCol3cF.get()
        quant4F = self.listaCol3dF.get()
        quant5F = self.listaCol3eF.get()
        quant6F = self.listaCol3fF.get()
        quant7F = self.listaCol3gF.get()
        quant8F = self.listaCol3hF.get()
        quant9F = self.listaCol3iF.get()
        quant10F = self.listaCol3jF.get()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 1""",
                       (cod_item1F, desc_item1F, quant1F, ordem1, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 2""",
                       (cod_item2F, desc_item2F, quant2F, ordem2, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 3""",
                       (cod_item3F, desc_item3F, quant3F, ordem3, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 4""",
                       (cod_item4F, desc_item4F, quant4F, ordem4, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 5""",
                       (cod_item5F, desc_item5F, quant5F, ordem5, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 6""",
                       (cod_item6F, desc_item6F, quant6F, ordem6, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 7""",
                       (cod_item7F, desc_item7F, quant7F, ordem7, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 8""",
                       (cod_item8F, desc_item8F, quant8F, ordem8, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 9""",
                       (cod_item9F, desc_item9F, quant9F, ordem9, id_orc2))
        self.conn.commit()

        self.cursor.execute("""
            			UPDATE orcfalha SET cod_orcfalha = ?, orcfalha = ?, orcfalha2 = ?, orcfalha5 = ?
            			WHERE id_orcfalha = ? AND orcfalha5 = 10""",
                       (cod_item10F, desc_item10F, quant10F, ordem10, id_orc2))
        self.conn.commit()

        self.desconecta_Glac()

        msg = "Alterações realizadas com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC - Orçamento", msg)
    def buscanomeorc(self):
        self.listaNomeO.insert(END, '%')
        self.listaServ.delete((*self.listaServ.get_children()))

        nomeO = self.listaNomeO.get()

        self.conecta_Glac()

        nom = self.cursor

        nom.execute(
            """SELECT id_orc1, nome ,dia , mes , ano, placa_orc, orcamento1.tipoOrc FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND nome LIKE '%s' ORDER BY id_orc1 DESC""" % nomeO)
        buscanomeO = self.cursor.fetchall()
        for row in buscanomeO:
            self.listaServ.insert("", END, values=row)

        self.listaNomeO.delete(0, END)

        self.desconecta_Glac()
    def buscaplacaorc(self):
        self.listaPlaca.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())

        placaO = self.listaPlaca.get()
        self.conecta_Glac()

        plac = self.cursor

        plac.execute(
            """SELECT id_orc1, nome, dia , mes , ano, placa_orc, orcamento1.tipoOrc FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND placa_orc LIKE '%s'""" % placaO)
        buscaplac = self.cursor.fetchall()
        for row in buscaplac:
            self.listaServ.insert("", END, values=row)

        self.listaPlaca.delete(0, END)

        self.desconecta_Glac()
    def carrega_orc(self, event):
        self.limpa_cliente()
        self.entradaDataorc.delete(0, END)
        self.entradaDataorc2.delete(0, END)
        self.entradaDataorc3.delete(0, END)
        self.entradatotal.delete(0, END)
        self.listaNumOrc.delete(0, END)
        self.entradaTecnico.delete(0, END)

        self.listaServ.selection()

        self.conecta_Glac()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaServ.item(n, 'values')
            self.listaNumOrc.insert(END, col1)

        id_orc = self.listaNumOrc.get()

        nomecur = self.cursor

        nomecur.execute("SELECT cliente_orc FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            self.entradaCod_cli.insert(END, i)

        self.desconecta_Glac()
        self.carrega_cliente()
        self.conecta_Glac()

        self.entradaCod_aut.delete(0, END)

        nomeplaca = self.cursor

        nomeplaca.execute("SELECT placa_orc FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultaplaca = self.cursor.fetchall()
        for i in consultaplaca:
            self.placa.insert(END, i)

        nomedescp1 = self.cursor

        nomedescp1.execute("SELECT descp1 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap1 = self.cursor.fetchall()
        for i in consultap1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area1.insert(END, i)

        nomedescp2 = self.cursor

        nomedescp2.execute("SELECT descp2 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap2 = self.cursor.fetchall()
        for i in consultap2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area2.insert(END, i)

        nomedescp3 = self.cursor

        nomedescp3.execute("SELECT descp3 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap3 = self.cursor.fetchall()
        for i in consultap3:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area3.insert(END, i)

        nomedescp4 = self.cursor

        nomedescp4.execute("SELECT descp4 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap4 = self.cursor.fetchall()
        for i in consultap4:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area4.insert(END, i)

        self.entradaDataorc.delete(0, END)
        nomedia = self.cursor

        nomedia.execute("SELECT dia FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultadia = self.cursor.fetchall()
        for i in consultadia:
            self.entradaDataorc.insert(END, i)

        self.entradaDataorc2.delete(0, END)
        nomemes = self.cursor

        nomemes.execute("SELECT mes FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultames = self.cursor.fetchall()
        for i in consultames:
            self.entradaDataorc2.insert(END, i)

        self.entradaDataorc3.delete(0, END)
        nomeano = self.cursor

        nomeano.execute("SELECT ano FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            self.entradaDataorc3.insert(END, i)

        nometotal = self.cursor

        nometotal.execute("SELECT totalizador FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultatotal = self.cursor.fetchall()
        for i in consultatotal:
            self.entradatotal.insert(END, i)

        nomekm = self.cursor

        nomekm.execute("SELECT km FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultakm = self.cursor.fetchall()
        for i in consultakm:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaObs.insert(END, i)

        self.cursor.execute("SELECT comp1 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultacomp1 = self.cursor.fetchall()
        for i in consultacomp1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listInicio.insert(END, i)

        self.cursor.execute("SELECT comp2 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultacomp2 = self.cursor.fetchall()
        for i in consultacomp2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listFim.insert(END, i)
        ##################################################

        placa = self.placa.get()

        nomeaut = self.cursor

        nomeaut.execute(
            "SELECT UPPER(veiculo) FROM frota WHERE placa = '%s'" % placa)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAut.insert(END, i)

        nomeano = self.cursor
        nomeano.execute("SELECT ano FROM frota WHERE placa = '%s'" % placa)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAno.insert(END, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT UPPER(montadora) FROM frota WHERE placa = '%s'" % placa)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMarca.insert(END, i)

        nomecomb = self.cursor
        nomecomb.execute("SELECT UPPER(combust) FROM frota WHERE placa = '%s'" % placa)
        consultacomb = self.cursor.fetchall()
        for i in consultacomb:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCombustivel.insert(END, i)

        nomecor = self.cursor
        nomecor.execute("SELECT UPPER(cor) FROM frota WHERE placa = '%s'" % placa)
        consultacor = self.cursor.fetchall()
        for i in consultacor:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCor.insert(END, i)

        ################################################

        ### lista1
        self.codServ1.delete(0, END)
        self.listaCol2a.delete(0, END)
        self.listaCol3a.delete(0, END)
        self.listaCol4a.delete(0, END)
        self.listaCol5a.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv1 = self.cursor

        nomecodserv1.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 1" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.codServ1.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 1" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2a.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 1" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            self.listaCol3a.insert(END, i)

        nomevaloritem1 = self.cursor

        nomevaloritem1.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 1" % id_orc)
        consultavaloritem1 = self.cursor.fetchall()
        for i in consultavaloritem1:
            self.listaCol4a.insert(END, i)

        nometotalitem1 = self.cursor

        nometotalitem1.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 1" % id_orc)
        consultatotalitem1 = self.cursor.fetchall()
        for i in consultatotalitem1:
            self.listaCol5a.insert(END, i)

        ### lista2
        self.codServ2.delete(0, END)
        self.listaCol2b.delete(0, END)
        self.listaCol3b.delete(0, END)
        self.listaCol4b.delete(0, END)
        self.listaCol5b.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv2 = self.cursor

        nomecodserv2.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 2" % id_orc)
        consultacodserv2 = self.cursor.fetchall()
        for i in consultacodserv2:
            self.codServ2.insert(END, i)

        nomedescitem2 = self.cursor

        nomedescitem2.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 2" % id_orc)
        consultadescitem2 = self.cursor.fetchall()
        for i in consultadescitem2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2b.insert(END, i)

        nomequantitem2 = self.cursor

        nomequantitem2.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 2" % id_orc)
        consultaquantitem2 = self.cursor.fetchall()
        for i in consultaquantitem2:
            self.listaCol3b.insert(END, i)

        nomevaloritem2 = self.cursor

        nomevaloritem2.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 2" % id_orc)
        consultavaloritem2 = self.cursor.fetchall()
        for i in consultavaloritem2:
            self.listaCol4b.insert(END, i)

        nometotalitem2 = self.cursor

        nometotalitem2.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 2" % id_orc)
        consultatotalitem2 = self.cursor.fetchall()
        for i in consultatotalitem2:
            self.listaCol5b.insert(END, i)

        ### lista3
        self.codServ3.delete(0, END)
        self.listaCol2c.delete(0, END)
        self.listaCol3c.delete(0, END)
        self.listaCol4c.delete(0, END)
        self.listaCol5c.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv3 = self.cursor

        nomecodserv3.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 3" % id_orc)
        consultacodserv3 = self.cursor.fetchall()
        for i in consultacodserv3:
            self.codServ3.insert(END, i)

        nomedescitem3 = self.cursor

        nomedescitem3.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 3" % id_orc)
        consultadescitem3 = self.cursor.fetchall()
        for i in consultadescitem3:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2c.insert(END, i)

        nomequantitem3 = self.cursor

        nomequantitem3.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 3" % id_orc)
        consultaquantitem3 = self.cursor.fetchall()
        for i in consultaquantitem3:
            self.listaCol3c.insert(END, i)

        nomevaloritem3 = self.cursor

        nomevaloritem3.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 3" % id_orc)
        consultavaloritem3 = self.cursor.fetchall()
        for i in consultavaloritem3:
            self.listaCol4c.insert(END, i)

        nometotalitem3 = self.cursor

        nometotalitem3.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 3" % id_orc)
        consultatotalitem3 = self.cursor.fetchall()
        for i in consultatotalitem3:
            self.listaCol5c.insert(END, i)

        ############################################################################
        ### 					lista 4 									########
        ############################################################################
        self.codServ4.delete(0, END)
        self.listaCol2d.delete(0, END)
        self.listaCol3d.delete(0, END)
        self.listaCol4d.delete(0, END)
        self.listaCol5d.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv4 = self.cursor

        nomecodserv4.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 4" % id_orc)
        consultacodserv4 = self.cursor.fetchall()
        for i in consultacodserv4:
            self.codServ4.insert(END, i)

        nomedescitem4 = self.cursor

        nomedescitem4.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 4" % id_orc)
        consultadescitem4 = self.cursor.fetchall()
        for i in consultadescitem4:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2d.insert(END, i)

        nomequantitem4 = self.cursor

        nomequantitem4.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 4" % id_orc)
        consultaquantitem4 = self.cursor.fetchall()
        for i in consultaquantitem4:
            self.listaCol3d.insert(END, i)

        nomevaloritem4 = self.cursor

        nomevaloritem4.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' "
                               "and ordem_item = 4" % id_orc)
        consultavaloritem4 = self.cursor.fetchall()
        for i in consultavaloritem4:
            self.listaCol4d.insert(END, i)

        nometotalitem4 = self.cursor

        nometotalitem4.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 4" % id_orc)
        consultatotalitem4 = self.cursor.fetchall()
        for i in consultatotalitem4:
            self.listaCol5d.insert(END, i)

        ############################################################################
        ### 					lista 5										########
        ############################################################################
        self.codServ5.delete(0, END)
        self.listaCol2e.delete(0, END)
        self.listaCol3e.delete(0, END)
        self.listaCol4e.delete(0, END)
        self.listaCol5e.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv5 = self.cursor

        nomecodserv5.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 5" % id_orc)
        consultacodserv5 = self.cursor.fetchall()
        for i in consultacodserv5:
            self.codServ5.insert(END, i)

        nomedescitem5 = self.cursor

        nomedescitem5.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 5" % id_orc)
        consultadescitem5 = self.cursor.fetchall()
        for i in consultadescitem5:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2e.insert(END, i)

        nomequantitem5 = self.cursor

        nomequantitem5.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 5" % id_orc)
        consultaquantitem5 = self.cursor.fetchall()
        for i in consultaquantitem5:
            self.listaCol3e.insert(END, i)

        nomevaloritem5 = self.cursor

        nomevaloritem5.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' "
                               "and ordem_item = 5" % id_orc)
        consultavaloritem5 = self.cursor.fetchall()
        for i in consultavaloritem5:
            self.listaCol4e.insert(END, i)

        nometotalitem5 = self.cursor

        nometotalitem5.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 5" % id_orc)
        consultatotalitem5 = self.cursor.fetchall()
        for i in consultatotalitem5:
            self.listaCol5e.insert(END, i)

        ############################################################################
        ### 					lista 6										########
        ############################################################################
        self.codServ6.delete(0, END)
        self.listaCol2f.delete(0, END)
        self.listaCol3f.delete(0, END)
        self.listaCol4f.delete(0, END)
        self.listaCol5f.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv6 = self.cursor

        nomecodserv6.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 6" % id_orc)
        consultacodserv6 = self.cursor.fetchall()
        for i in consultacodserv6:
            self.codServ6.insert(END, i)

        nomedescitem6 = self.cursor

        nomedescitem6.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 6" % id_orc)
        consultadescitem6 = self.cursor.fetchall()
        for i in consultadescitem6:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2f.insert(END, i)

        nomequantitem6 = self.cursor

        nomequantitem6.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 5" % id_orc)
        consultaquantitem6 = self.cursor.fetchall()
        for i in consultaquantitem6:
            self.listaCol3f.insert(END, i)

        nomevaloritem6 = self.cursor

        nomevaloritem6.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' "
                               "and ordem_item = 6" % id_orc)
        consultavaloritem6 = self.cursor.fetchall()
        for i in consultavaloritem6:
            self.listaCol4f.insert(END, i)

        nometotalitem6 = self.cursor

        nometotalitem6.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 6" % id_orc)
        consultatotalitem6 = self.cursor.fetchall()
        for i in consultatotalitem6:
            self.listaCol5f.insert(END, i)

        ############################################################################
        ### 					lista 7										########
        ############################################################################
        self.codServ7.delete(0, END)
        self.listaCol2g.delete(0, END)
        self.listaCol3g.delete(0, END)
        self.listaCol4g.delete(0, END)
        self.listaCol5g.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv7 = self.cursor

        nomecodserv7.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 7" % id_orc)
        consultacodserv7 = self.cursor.fetchall()
        for i in consultacodserv7:
            self.codServ7.insert(END, i)

        nomedescitem7 = self.cursor

        nomedescitem7.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 7" % id_orc)
        consultadescitem7 = self.cursor.fetchall()
        for i in consultadescitem7:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2g.insert(END, i)

        nomequantitem7 = self.cursor

        nomequantitem7.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 7" % id_orc)
        consultaquantitem7 = self.cursor.fetchall()
        for i in consultaquantitem7:
            self.listaCol3g.insert(END, i)

        nomevaloritem7 = self.cursor

        nomevaloritem7.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' "
                               "and ordem_item = 7" % id_orc)
        consultavaloritem7 = self.cursor.fetchall()
        for i in consultavaloritem7:
            self.listaCol4g.insert(END, i)

        nometotalitem7 = self.cursor

        nometotalitem7.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 7" % id_orc)
        consultatotalitem7 = self.cursor.fetchall()
        for i in consultatotalitem7:
            self.listaCol5g.insert(END, i)

        ############################################################################
        ### 					lista 8										########
        ############################################################################
        self.codServ8.delete(0, END)
        self.listaCol2h.delete(0, END)
        self.listaCol3h.delete(0, END)
        self.listaCol4h.delete(0, END)
        self.listaCol5h.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv8 = self.cursor

        nomecodserv8.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 8" % id_orc)
        consultacodserv8 = self.cursor.fetchall()
        for i in consultacodserv8:
            self.codServ8.insert(END, i)

        nomedescitem8 = self.cursor

        nomedescitem8.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 8" % id_orc)
        consultadescitem8 = self.cursor.fetchall()
        for i in consultadescitem8:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2h.insert(END, i)

        nomequantitem8 = self.cursor

        nomequantitem8.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 8" % id_orc)
        consultaquantitem8 = self.cursor.fetchall()
        for i in consultaquantitem8:
            self.listaCol3h.insert(END, i)

        nomevaloritem8 = self.cursor

        nomevaloritem8.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' "
                               "and ordem_item = 8" % id_orc)
        consultavaloritem8 = self.cursor.fetchall()
        for i in consultavaloritem8:
            self.listaCol4h.insert(END, i)

        nometotalitem8 = self.cursor

        nometotalitem8.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 8" % id_orc)
        consultatotalitem8 = self.cursor.fetchall()
        for i in consultatotalitem8:
            self.listaCol5h.insert(END, i)

        ############################################################################
        ### 					lista 9										########
        ############################################################################
        self.codServ9.delete(0, END)
        self.listaCol2i.delete(0, END)
        self.listaCol3i.delete(0, END)
        self.listaCol4i.delete(0, END)
        self.listaCol5i.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv9 = self.cursor

        nomecodserv9.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 9" % id_orc)
        consultacodserv9 = self.cursor.fetchall()
        for i in consultacodserv9:
            self.codServ9.insert(END, i)

        nomedescitem9 = self.cursor

        nomedescitem9.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 9" % id_orc)
        consultadescitem9 = self.cursor.fetchall()
        for i in consultadescitem9:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2i.insert(END, i)

        nomequantitem9 = self.cursor

        nomequantitem9.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 9" % id_orc)
        consultaquantitem9 = self.cursor.fetchall()
        for i in consultaquantitem9:
            self.listaCol3i.insert(END, i)

        nomevaloritem9 = self.cursor

        nomevaloritem9.execute("SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' "
                               "and ordem_item = 9" % id_orc)
        consultavaloritem9 = self.cursor.fetchall()
        for i in consultavaloritem9:
            self.listaCol4i.insert(END, i)

        nometotalitem9 = self.cursor

        nometotalitem9.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 9" % id_orc)
        consultatotalitem9 = self.cursor.fetchall()
        for i in consultatotalitem9:
            self.listaCol5i.insert(END, i)

        ############################################################################
        ### 					lista 10										########
        ############################################################################
        self.codServ10.delete(0, END)
        self.listaCol2j.delete(0, END)
        self.listaCol3j.delete(0, END)
        self.listaCol4j.delete(0, END)
        self.listaCol5j.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv10 = self.cursor

        nomecodserv10.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 10" % id_orc)
        consultacodserv10 = self.cursor.fetchall()
        for i in consultacodserv10:
            self.codServ10.insert(END, i)

        nomedescitem10 = self.cursor

        nomedescitem10.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 10" % id_orc)
        consultadescitem10 = self.cursor.fetchall()
        for i in consultadescitem10:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2j.insert(END, i)

        nomequantitem10 = self.cursor

        nomequantitem10.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 10" % id_orc)
        consultaquantitem10 = self.cursor.fetchall()
        for i in consultaquantitem10:
            self.listaCol3j.insert(END, i)

        nomevaloritem10 = self.cursor

        nomevaloritem10.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 10" % id_orc)
        consultavaloritem10 = self.cursor.fetchall()
        for i in consultavaloritem10:
            self.listaCol4j.insert(END, i)

        nometotalitem10 = self.cursor

        nometotalitem10.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 10" % id_orc)
        consultatotalitem10 = self.cursor.fetchall()
        for i in consultatotalitem10:
            self.listaCol5j.insert(END, i)

        ############################################################################
        ### 					lista 11									########
        ############################################################################
        self.codServ11.delete(0, END)
        self.listaCol2k.delete(0, END)
        self.listaCol3k.delete(0, END)
        self.listaCol4k.delete(0, END)
        self.listaCol5k.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv11 = self.cursor

        nomecodserv11.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 11" % id_orc)
        consultacodserv11 = self.cursor.fetchall()
        for i in consultacodserv11:
            self.codServ11.insert(END, i)

        nomedescitem11 = self.cursor

        nomedescitem11.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 11" % id_orc)
        consultadescitem11 = self.cursor.fetchall()
        for i in consultadescitem11:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2k.insert(END, i)

        nomequantitem11 = self.cursor

        nomequantitem11.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 11" % id_orc)
        consultaquantitem11 = self.cursor.fetchall()
        for i in consultaquantitem11:
            self.listaCol3k.insert(END, i)

        nomevaloritem11 = self.cursor

        nomevaloritem11.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 11" % id_orc)
        consultavaloritem11 = self.cursor.fetchall()
        for i in consultavaloritem11:
            self.listaCol4k.insert(END, i)

        nometotalitem11 = self.cursor

        nometotalitem11.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 11" % id_orc)
        consultatotalitem11 = self.cursor.fetchall()
        for i in consultatotalitem11:
            self.listaCol5k.insert(END, i)

        ############################################################################
        ### 					lista 12									########
        ############################################################################
        self.codServ12.delete(0, END)
        self.listaCol2l.delete(0, END)
        self.listaCol3l.delete(0, END)
        self.listaCol4l.delete(0, END)
        self.listaCol5l.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv12 = self.cursor

        nomecodserv12.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 12" % id_orc)
        consultacodserv12 = self.cursor.fetchall()
        for i in consultacodserv12:
            self.codServ12.insert(END, i)

        nomedescitem12 = self.cursor

        nomedescitem12.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 12" % id_orc)
        consultadescitem12 = self.cursor.fetchall()
        for i in consultadescitem12:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2l.insert(END, i)

        nomequantitem12 = self.cursor

        nomequantitem12.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 12" % id_orc)
        consultaquantitem12 = self.cursor.fetchall()
        for i in consultaquantitem12:
            self.listaCol3l.insert(END, i)

        nomevaloritem12 = self.cursor

        nomevaloritem12.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 12" % id_orc)
        consultavaloritem12 = self.cursor.fetchall()
        for i in consultavaloritem12:
            self.listaCol4l.insert(END, i)

        nometotalitem12 = self.cursor

        nometotalitem12.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 12" % id_orc)
        consultatotalitem12 = self.cursor.fetchall()
        for i in consultatotalitem12:
            self.listaCol5l.insert(END, i)

        ############################################################################
        ### 					lista 13									########
        ############################################################################
        self.codServ13.delete(0, END)
        self.listaCol2m.delete(0, END)
        self.listaCol3m.delete(0, END)
        self.listaCol4m.delete(0, END)
        self.listaCol5m.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv13 = self.cursor

        nomecodserv13.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 13" % id_orc)
        consultacodserv13 = self.cursor.fetchall()
        for i in consultacodserv13:
            self.codServ13.insert(END, i)

        nomedescitem13 = self.cursor

        nomedescitem13.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 13" % id_orc)
        consultadescitem13 = self.cursor.fetchall()
        for i in consultadescitem13:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2m.insert(END, i)

        nomequantitem13 = self.cursor

        nomequantitem13.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 13" % id_orc)
        consultaquantitem13 = self.cursor.fetchall()
        for i in consultaquantitem13:
            self.listaCol3m.insert(END, i)

        nomevaloritem13 = self.cursor

        nomevaloritem13.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 13" % id_orc)
        consultavaloritem13 = self.cursor.fetchall()
        for i in consultavaloritem13:
            self.listaCol4m.insert(END, i)

        nometotalitem13 = self.cursor

        nometotalitem13.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 13" % id_orc)
        consultatotalitem13 = self.cursor.fetchall()
        for i in consultatotalitem13:
            self.listaCol5m.insert(END, i)

        ############################################################################
        ### 					lista 14									########
        ############################################################################
        self.codServ14.delete(0, END)
        self.listaCol2n.delete(0, END)
        self.listaCol3n.delete(0, END)
        self.listaCol4n.delete(0, END)
        self.listaCol5n.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv14 = self.cursor

        nomecodserv14.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 14" % id_orc)
        consultacodserv14 = self.cursor.fetchall()
        for i in consultacodserv14:
            self.codServ14.insert(END, i)

        nomedescitem14 = self.cursor

        nomedescitem14.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 14" % id_orc)
        consultadescitem14 = self.cursor.fetchall()
        for i in consultadescitem14:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2n.insert(END, i)

        nomequantitem14 = self.cursor

        nomequantitem14.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 14" % id_orc)
        consultaquantitem14 = self.cursor.fetchall()
        for i in consultaquantitem14:
            self.listaCol3n.insert(END, i)

        nomevaloritem14 = self.cursor

        nomevaloritem14.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 14" % id_orc)
        consultavaloritem14 = self.cursor.fetchall()
        for i in consultavaloritem14:
            self.listaCol4n.insert(END, i)

        nometotalitem14 = self.cursor

        nometotalitem14.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 14" % id_orc)
        consultatotalitem14 = self.cursor.fetchall()
        for i in consultatotalitem14:
            self.listaCol5n.insert(END, i)

        ############################################################################
        ### 					lista 15									########
        ############################################################################
        self.codServ15.delete(0, END)
        self.listaCol2o.delete(0, END)
        self.listaCol3o.delete(0, END)
        self.listaCol4o.delete(0, END)
        self.listaCol5o.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv15 = self.cursor

        nomecodserv15.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 15" % id_orc)
        consultacodserv15 = self.cursor.fetchall()
        for i in consultacodserv15:
            self.codServ15.insert(END, i)

        nomedescitem15 = self.cursor

        nomedescitem15.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 15" % id_orc)
        consultadescitem15 = self.cursor.fetchall()
        for i in consultadescitem15:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2o.insert(END, i)

        nomequantitem15 = self.cursor

        nomequantitem15.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 15" % id_orc)
        consultaquantitem15 = self.cursor.fetchall()
        for i in consultaquantitem15:
            self.listaCol3o.insert(END, i)

        nomevaloritem15 = self.cursor

        nomevaloritem15.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 15" % id_orc)
        consultavaloritem15 = self.cursor.fetchall()
        for i in consultavaloritem15:
            self.listaCol4o.insert(END, i)

        nometotalitem15 = self.cursor

        nometotalitem15.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 15" % id_orc)
        consultatotalitem15 = self.cursor.fetchall()
        for i in consultatotalitem15:
            self.listaCol5o.insert(END, i)

        ############################################################################
        ### 					lista 16									########
        ############################################################################
        self.codServ16.delete(0, END)
        self.listaCol2p.delete(0, END)
        self.listaCol3p.delete(0, END)
        self.listaCol4p.delete(0, END)
        self.listaCol5p.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv16 = self.cursor

        nomecodserv16.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 16" % id_orc)
        consultacodserv16 = self.cursor.fetchall()
        for i in consultacodserv16:
            self.codServ16.insert(END, i)

        nomedescitem16 = self.cursor

        nomedescitem16.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 16" % id_orc)
        consultadescitem16 = self.cursor.fetchall()
        for i in consultadescitem16:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2p.insert(END, i)

        nomequantitem16 = self.cursor

        nomequantitem16.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 16" % id_orc)
        consultaquantitem16 = self.cursor.fetchall()
        for i in consultaquantitem16:
            self.listaCol3p.insert(END, i)

        nomevaloritem16 = self.cursor

        nomevaloritem16.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 16" % id_orc)
        consultavaloritem16 = self.cursor.fetchall()
        for i in consultavaloritem16:
            self.listaCol4p.insert(END, i)

        nometotalitem16 = self.cursor

        nometotalitem16.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 16" % id_orc)
        consultatotalitem16 = self.cursor.fetchall()
        for i in consultatotalitem16:
            self.listaCol5p.insert(END, i)

        ############################################################################
        ### 					lista 17									########
        ############################################################################
        self.codServ17.delete(0, END)
        self.listaCol2q.delete(0, END)
        self.listaCol3q.delete(0, END)
        self.listaCol4q.delete(0, END)
        self.listaCol5q.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv17 = self.cursor

        nomecodserv17.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 17" % id_orc)
        consultacodserv17 = self.cursor.fetchall()
        for i in consultacodserv17:
            self.codServ17.insert(END, i)

        nomedescitem17 = self.cursor

        nomedescitem17.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 17" % id_orc)
        consultadescitem17 = self.cursor.fetchall()
        for i in consultadescitem17:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2q.insert(END, i)

        nomequantitem17 = self.cursor

        nomequantitem17.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 17" % id_orc)
        consultaquantitem17 = self.cursor.fetchall()
        for i in consultaquantitem17:
            self.listaCol3q.insert(END, i)

        nomevaloritem17 = self.cursor

        nomevaloritem17.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 17" % id_orc)
        consultavaloritem17 = self.cursor.fetchall()
        for i in consultavaloritem17:
            self.listaCol4q.insert(END, i)

        nometotalitem17 = self.cursor

        nometotalitem17.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 17" % id_orc)
        consultatotalitem17 = self.cursor.fetchall()
        for i in consultatotalitem17:
            self.listaCol5q.insert(END, i)

        ############################################################################
        ### 					lista 18									########
        ############################################################################
        self.codServ18.delete(0, END)
        self.listaCol2r.delete(0, END)
        self.listaCol3r.delete(0, END)
        self.listaCol4r.delete(0, END)
        self.listaCol5r.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv18 = self.cursor

        nomecodserv18.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 18" % id_orc)
        consultacodserv18 = self.cursor.fetchall()
        for i in consultacodserv18:
            self.codServ18.insert(END, i)

        nomedescitem18 = self.cursor

        nomedescitem18.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 18" % id_orc)
        consultadescitem18 = self.cursor.fetchall()
        for i in consultadescitem18:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2r.insert(END, i)

        nomequantitem18 = self.cursor

        nomequantitem18.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 18" % id_orc)
        consultaquantitem18 = self.cursor.fetchall()
        for i in consultaquantitem18:
            self.listaCol3r.insert(END, i)

        nomevaloritem18 = self.cursor

        nomevaloritem18.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 18" % id_orc)
        consultavaloritem18 = self.cursor.fetchall()
        for i in consultavaloritem18:
            self.listaCol4r.insert(END, i)

        nometotalitem18 = self.cursor

        nometotalitem18.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 18" % id_orc)
        consultatotalitem18 = self.cursor.fetchall()
        for i in consultatotalitem18:
            self.listaCol5r.insert(END, i)

        ############################################################################
        ### 					lista 19									########
        ############################################################################
        self.codServ19.delete(0, END)
        self.listaCol2s.delete(0, END)
        self.listaCol3s.delete(0, END)
        self.listaCol4s.delete(0, END)
        self.listaCol5s.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv19 = self.cursor

        nomecodserv19.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 19" % id_orc)
        consultacodserv19 = self.cursor.fetchall()
        for i in consultacodserv19:
            self.codServ19.insert(END, i)

        nomedescitem19 = self.cursor

        nomedescitem19.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 19" % id_orc)
        consultadescitem19 = self.cursor.fetchall()
        for i in consultadescitem19:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2s.insert(END, i)

        nomequantitem19 = self.cursor

        nomequantitem19.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 19" % id_orc)
        consultaquantitem19 = self.cursor.fetchall()
        for i in consultaquantitem19:
            self.listaCol3s.insert(END, i)

        nomevaloritem19 = self.cursor

        nomevaloritem19.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 19" % id_orc)
        consultavaloritem19 = self.cursor.fetchall()
        for i in consultavaloritem19:
            self.listaCol4s.insert(END, i)

        nometotalitem19 = self.cursor

        nometotalitem19.execute("SELECT total FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 19" % id_orc)
        consultatotalitem19 = self.cursor.fetchall()
        for i in consultatotalitem19:
            self.listaCol5s.insert(END, i)

        ############################################################################
        ### 					lista 20									########
        ############################################################################
        self.codServ20.delete(0, END)
        self.listaCol2t.delete(0, END)
        self.listaCol3t.delete(0, END)
        self.listaCol4t.delete(0, END)
        self.listaCol5t.delete(0, END)
        self.entradatotal.delete(0, END)

        nomecodserv20 = self.cursor

        nomecodserv20.execute("SELECT cod_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 20" % id_orc)
        consultacodserv20 = self.cursor.fetchall()
        for i in consultacodserv20:
            self.codServ20.insert(END, i)

        nomedescitem20 = self.cursor

        nomedescitem20.execute("SELECT desc_item FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 20" % id_orc)
        consultadescitem20 = self.cursor.fetchall()
        for i in consultadescitem20:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listaCol2t.insert(END, i)

        nomequantitem20 = self.cursor

        nomequantitem20.execute("SELECT quant FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 20" % id_orc)
        consultaquantitem20 = self.cursor.fetchall()
        for i in consultaquantitem20:
            self.listaCol3t.insert(END, i)

        nomevaloritem20 = self.cursor

        nomevaloritem20.execute(
            "SELECT ROUND(valor,2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 20" % id_orc)
        consultavaloritem20 = self.cursor.fetchall()
        for i in consultavaloritem20:
            self.listaCol4t.insert(END, i)

        nometotalitem20 = self.cursor

        nometotalitem20.execute(
            "SELECT ROUND(total, 2) FROM orcamento2 WHERE id_orc2 = '%s' and ordem_item = 20" % id_orc)
        consultatotalitem20 = self.cursor.fetchall()
        for i in consultatotalitem20:
            self.listaCol5t.insert(END, i)

        ##################################

        totaliza = self.cursor

        totaliza.execute("SELECT ROUND(totalizador, 2) FROM orcamento1 WHERE id_orc1 = '%s' " % id_orc)
        totalizad = self.cursor.fetchall()
        for i in totalizad:
            self.entradatotal.insert(END, i)

        ##################################

        tec = self.cursor

        tec.execute("SELECT tecnico FROM orcamento1 WHERE id_orc1 = '%s' " % id_orc)
        tecd = self.cursor.fetchall()
        for i in tecd:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaTecnico.insert(END, i)

        orcos = self.cursor
        orcos.execute("Select tipoOrc From orcamento1 Where id_orc1 = '%s' " % id_orc)
        orcos1 = self.cursor.fetchall()
        for i in orcos1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.Tipvar.set(i)

        ################
        # Vistoria variaveis
        codVist = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("SELECT vist1 FROM vistoria WHERE cod = '%s' " % codVist)
        codVisto = self.cursor.fetchall()
        for i in codVisto:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are1.insert(END, i)

        self.cursor.execute("SELECT vist2 FROM vistoria WHERE cod = '%s' " % codVist)
        codR = self.cursor.fetchall()
        for i in codR:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are3.insert(END, i)

        self.cursor.execute("SELECT vist3 FROM vistoria WHERE cod = '%s' " % codVist)
        codO = self.cursor.fetchall()
        for i in codO:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are2.insert(END, i)

        self.cursor.execute("SELECT vist4 FROM vistoria WHERE cod = '%s' " % codVist)
        codCalota = self.cursor.fetchall()
        for i in codCalota:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are4.insert(END, i)

        self.cursor.execute("SELECT vist5 FROM vistoria WHERE cod = '%s' " % codVist)
        codTri = self.cursor.fetchall()
        for i in codTri:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are5.insert(END, i)

        self.cursor.execute("SELECT vist6 FROM vistoria WHERE cod = '%s' " % codVist)
        cod6 = self.cursor.fetchall()
        for i in cod6:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are6.insert(END, i)

        self.cursor.execute("SELECT vist7 FROM vistoria WHERE cod = '%s' " % codVist)
        cod7 = self.cursor.fetchall()
        for i in cod7:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are7.insert(END, i)

        self.cursor.execute("SELECT vist8 FROM vistoria WHERE cod = '%s' " % codVist)
        cod8 = self.cursor.fetchall()
        for i in cod8:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are8.insert(END, i)

        self.cursor.execute("SELECT vist9 FROM vistoria WHERE cod = '%s' " % codVist)
        cod9 = self.cursor.fetchall()
        for i in cod9:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are9.insert(END, i)

        # self.add_servico1()
        ########################################
        #########   carrega falhas
        ################################################

        ### lista1
        self.codServ1F.delete(0, END)
        self.listaCol2aF.delete(0, END)
        self.listaCol3aF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 1" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ1F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 1" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2aF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 1" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3aF.insert(END, i)

        #############################################################
        ### lista2
        self.codServ2F.delete(0, END)
        self.listaCol2bF.delete(0, END)
        self.listaCol3bF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 2" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ2F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 2" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2bF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 2" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3bF.insert(END, i)

        ##############################################################
        ### lista3
        self.codServ3F.delete(0, END)
        self.listaCol2cF.delete(0, END)
        self.listaCol3cF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 3" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ3F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 3" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2cF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 3" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3cF.insert(END, i)

        ############################################################################
        ### 					lista 4 									########
        ############################################################################
        self.codServ4F.delete(0, END)
        self.listaCol2dF.delete(0, END)
        self.listaCol3dF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 4" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ4F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 4" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2dF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 4" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3dF.insert(END, i)

        ############################################################################
        ### 					lista 5										########
        ############################################################################
        self.codServ5F.delete(0, END)
        self.listaCol2eF.delete(0, END)
        self.listaCol3eF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 5" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ5F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 5" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2eF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 5" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3eF.insert(END, i)

        ############################################################################
        ### 					lista 6										########
        ############################################################################
        self.codServ6F.delete(0, END)
        self.listaCol2fF.delete(0, END)
        self.listaCol3fF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 6" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ6F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 6" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2fF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 6" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3fF.insert(END, i)

        ############################################################################
        ### 					lista 7										########
        ############################################################################
        self.codServ7F.delete(0, END)
        self.listaCol2gF.delete(0, END)
        self.listaCol3gF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 7" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ7F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 7" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2gF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 7" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3gF.insert(END, i)

        ############################################################################
        ### 					lista 8										########
        ############################################################################
        self.codServ8F.delete(0, END)
        self.listaCol2hF.delete(0, END)
        self.listaCol3hF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 8" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ8F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 8" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2hF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 8" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3hF.insert(END, i)

        ############################################################################
        ### 					lista 9										########
        ############################################################################
        self.codServ9F.delete(0, END)
        self.listaCol2iF.delete(0, END)
        self.listaCol3iF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 9" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ9F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 9" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2iF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 9" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3iF.insert(END, i)

        ############################################################################
        ### 					lista 10										########
        ############################################################################
        self.codServ10F.delete(0, END)
        self.listaCol2jF.delete(0, END)
        self.listaCol3jF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 10" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ10F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 10" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2jF.insert(END, i)

        nomequantitem1 = self.cursor

        nomequantitem1.execute("SELECT orcfalha2 FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 10" % id_orc)
        consultaquantitem1 = self.cursor.fetchall()
        for i in consultaquantitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol3jF.insert(END, i)

        self.listaOrc.destroy()
        self.desconecta_Glac()

        self.totalbotao()

        def carrega_orc_a(event):
            carrega_orc()
    def add_tecnicobind(self, event):
        self.codServ1.delete(0, END)

        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaTecnico.insert(END, col2)

        # self.add_servico1()
        self.listatec.destroy()

    def backup(self):
        try:
            shutil.copyfile("c:\glacx\glac.db", "c:\glacbkp\copiaGlacX.db")
            msg = "Backup salvo em c:\glacbkp\ \n" \
                 "Copie e salve em local seguro. ;) "
            msg += ""
            messagebox.showinfo("GLACX", msg)
        except:
            msg = "Copia não realizada, crie a pasta c:\glacbkp \n" \
                  "antes de realizar o backup"
            messagebox.showinfo("GLACX", msg)
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5 = listaServ.item(n, 'values')
            self.entradan.insert(END, col1)

        self.carrega_orc()
    def busca_serv(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        self.conecta_Glac()

        servprod = self.listaServicos1.get()

        servico12 = self.cursor

        servico12.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
    	FROM servprod WHERE servprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)

        self.listaServicos1.delete(0, END)

        self.desconecta_Glac()
    def busca_serv_veic(self):

        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        servprod = self.listaServicos1.get()

        self.conecta_Glac()

        servico12 = self.cursor

        servico12.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
    	FROM servprod WHERE id_marcaprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)

        self.listaServicos1.delete(0, END)

        self.desconecta_Glac()
    def OnTec(self, *args):
        self.listaServ.yview(*args)
    def OnVsb(self, *args):
        self.listaServ.yview(*args)
    def OnVsb_S1(self, *args):
        self.listaServ1.yview(*args)
    def OnVsb_Orc(self, *args):
        self.listaServ.yview(*args)
    def buscaCli(self):
        self.conecta_Glac()
        self.EntryCliente2.insert(END, '%')
        nome = self.EntryCliente2.get()
        nomecod = self.cursor
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_cli, nome FROM clientes WHERE nome LIKE '%s' """ % nome)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        self.EntryCliente2.delete(0, END)
        self.desconecta_Glac()
    def procedServF(self):
        valorServ = self.listaNomeO.get()
        Serv = 's'

        self.conecta_Glac()

        self.cursor.execute("""
                 		UPDATE servprod SET valor = ? WHERE sp = ?""", (valorServ, Serv))
        self.conn.commit()

        self.desconecta_Glac()
        msg = "Valor atualizado com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC", msg)
        self.listaOrc.destroy()
    def add_pag(self):
        ordem = self.listaNumOrc.get()
        tipopag = self.listtipopag.get()
        valortotal = self.entryValorTotal.get()
        valordeduzir = self.entryValor.get()
        dia = self.diavar.get()
        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = "Não"

        self.conecta_Glac()

        self.cursor.execute("""
       		INSERT INTO formapag ( ordem, tipopag, valorpagar, valordeduzir, dia, mes , ano, pago)
       		VALUES ( ?, ?, ?, ?, ?, ?, ? , ?)""",
                       (ordem, tipopag, valortotal, valordeduzir, dia, mes, ano, pago))
        self.conn.commit()

        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
               SELECT  ordem, tipopag, valorpagar, valordeduzir, dia, mes, ano, pago
                FROM formapag WHERE ordem = '%s'  ORDER BY id ASC;
               """ % ordem)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = self.cursor.execute("""
                                           SELECT SUM(valordeduzir) FROM formapag WHERE ordem = '%s'   ORDER BY id ASC;
                                           """ % ordem)
        for i in informe:
            self.entryValorInform.delete(0, END)
            self.entryValorInform.insert(END, i)

        self.entryValor.delete(0, END)

        self.desconecta_Glac()
        self.janela.destroy()
        #msg = "Pagamento incluido com sucesso"
        #msg += ""
        #messagebox.showinfo("GLAC - Pagamentos", msg)
        self.pagaOrdem()
    def OnDoubleClickpag(self, event):
        self.listaPag.selection()

        self.janPag2 = Tk();
        self.janPag2.title("GlacX")
        self.janPag2.configure(background='lavender');
        self.janPag2.geometry("480x85")
        self.janPag2.resizable(FALSE, FALSE)

        ## Entry NUm Atend
        self.label1 = Label(self.janPag2, text = self.m_NumAtend)
        self.label1.place(x=10, y=30)
        self.entry1 = Listbox(self.janPag2, width=8, height = 1)
        self.entry1.place(x=10, y=50)

        #### Listbox do tipo de pagamento
        self.entrytipopag = Frame(self.janPag2, bd=0, bg='lavender', width=2)
        self.entrytipopag.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrytipopag.columnconfigure(0, weight=1)
        self.entrytipopag.rowconfigure(0, weight=1)
        self.entrytipopag.place(x=70, y=30, width=120, height=40)
        self.entry2 = StringVar(self.janPag2)
        self.entry2V = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto, self.m_ChequePre,
                        self.m_ChequeVista, self.m_Crediario, self.m_Promissoria, self.m_Desconto, self.m_Avista}
        self.entry2V = sorted(self.entry2V)

        self.popupMenu = OptionMenu(self.entrytipopag, self.entry2, *self.entry2V)
        Label(self.entrytipopag, text= self.m_Tipo + ' ' + self.m_Pagamento,bd=0, bg = 'lavender').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Valor da parcela
        self.label1 = Label(self.janPag2, text= self.m_Valor_R)
        self.label1.place(x=210, y=30)
        self.entry3 = Entry(self.janPag2, width = 10)
        self.entry3.place(x=200, y=50)

        ### dia
        self.label1 = Label(self.janPag2, text= self.m_Data + ' ' + self.m_Pagamento)
        self.label1.place(x=285, y=30)
        self.entry4 = Entry(self.janPag2, width = 2)
        self.entry4.place(x=280, y=50)
        self.entry5 = Entry(self.janPag2, width = 2)
        self.entry5.place(x=300, y=50)
        self.entry6 = Entry(self.janPag2, width = 4)
        self.entry6.place(x=320, y=50)

        ### Pago?
        self.label1 = Label(self.janPag2, text= self.m_Pago)
        self.label1.place(x=360, y=30)
        self.entry7 = Entry(self.janPag2, width=6)
        self.entry7.place(x=360, y=50)
        self.entrypago = Frame(self.janPag2, bd=0, bg='lavender', width=2)
        self.entrypago.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrypago.columnconfigure(0, weight=1)
        self.entrypago.rowconfigure(0, weight=1)
        self.entrypago.place(x=360, y=30, width=55, height=40)
        self.entry7 = StringVar(self.janPag2)
        self.entry7V = {self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)

        self.popupMenu = OptionMenu(self.entrypago, self.entry7, *self.entry7V)
        Label(self.entrypago, text= self.m_Pago, bd=0, bg='lavender').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        ### Alterar registro
        self.button1 = Button(self.janPag2, text = self.m_Alterar, command = self.mud_pag)
        self.button1.place(x=430, y=47)

        self.entry9 = Entry(self.janPag2)

        for n in self.listaPag.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaPag.item(n, 'values')
            self.entry1.insert(END, col1)
            self.entry2.set(col2)
            self.entry3.insert(END, col4)
            self.entry4.insert(END, col5)
            self.entry5.insert(END, col6)
            self.entry6.insert(END, col7)
            self.entry7.set(col8)
            self.entry9.insert(END, col9)

        self.janPag2.mainloop()
    def mud_pag(self):
        self.conecta_Glac()

        tipopag = self.entry2.get()
        valor = self.entry3.get()
        diaA = self.entry4.get()
        mesA = self.entry5.get()
        anoA = self.entry6.get()
        pago = self.entry7.get()
        idA = self.entry9.get()

        self.cursor.execute(""" UPDATE formapag SET tipopag = ?, valordeduzir = ?, dia = ?,
            mes = ?, ano = ?, pago = ? WHERE id = ? """,
                       (tipopag, valor, diaA, mesA, anoA, pago, idA))
        self.conn.commit()

        self.desconecta_Glac()
        self.janPag2.destroy()
        self.janela.destroy()
        self.pagaOrdem()

    def carrega_cliente2(self, event):
        self.limpa_cliente()
        #### Variaveis da função
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod_cli.insert(END, col1)

        self.carrega_cliente()
        self.listacliente.destroy()

        def carrega_cliente2_a(event):
            self.carrega_cliente2()
    def OnVsb_S1F(self, *args):
        self.listaServ1F.yview(*args)
    def busca_servF(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1F.delete(*self.listaServ1F.get_children())
        self.listaServicos1F.insert(END, '%')

        self.conecta_Glac()

        servprodF = self.listaServicos1F.get()

        servico12F = self.cursor

        servico12F.execute("""SELECT cod_falha, falha, falha2 FROM codfalha WHERE falha LIKE '%s' """ % servprodF)
        buscaservico12F = self.cursor.fetchall()
        for i in buscaservico12F:
            self.listaServ1F.insert("", END, values=i)

        self.listaServicos1F.delete(0, END)
        self.desconecta_Glac()

    def VarRel(self):
        ### VARIAVEIS DO RELATORIO
        self.dia_R = self.entradaDataorc.get(); self.mes_R = self.entradaDataorc2.get()
        self.ano_R = self.entradaDataorc3.get();self.cliente_R = self.listNome.get()
        self.endereco_R = self.listEndereco.get();self.bairro_R = self.listBairro.get()
        self.municipio_R = self.listMunicipio.get();self.cpf_R = self.listCpf.get()
        self.fone_R = self.listFone.get(); self.uf_R = self.listUf.get()
        self.obs_R = self.listObs.get(); self.aut_R = self.listAut.get()
        self.anoAut_R = self.listAno.get();self.marca_R = self.listMarca.get()
        self.combustivel_R = self.listCombustivel.get();self.cor_R = self.listCor.get()
        self.placa_R = self.placa.get(); self.numorc_R = self.listaNumOrc.get()
        self.area1_R = self.area1.get(); self.area2_R = self.area2.get()
        self.area3_R = self.area3.get(); self.area4_R = self.area4.get()
        self.km_R = self.entradaObs.get();

        self.lista1_R = self.listaCol2a.get(); self.lista2_R = self.listaCol2b.get()
        self.lista3_R = self.listaCol2c.get(); self.lista4_R = self.listaCol2d.get()
        self.lista5_R = self.listaCol2e.get(); self.lista6_R = self.listaCol2f.get()
        self.lista7_R = self.listaCol2g.get(); self.lista8_R = self.listaCol2h.get()
        self.lista9_R = self.listaCol2i.get(); self.lista10_R = self.listaCol2j.get()
        self.lista11_R = self.listaCol2k.get(); self.lista12_R = self.listaCol2l.get()
        self.lista13_R = self.listaCol2m.get(); self.lista14_R = self.listaCol2n.get()
        self.lista15_R = self.listaCol2o.get(); self.lista16_R = self.listaCol2p.get()
        self.lista17_R = self.listaCol2q.get(); self.lista18_R = self.listaCol2r.get()
        self.lista19_R = self.listaCol2s.get(); self.lista20_R = self.listaCol2t.get()

        self.colquant1_R = self.listaCol3a.get(); self.colquant2_R = self.listaCol3b.get()
        self.colquant3_R = self.listaCol3c.get(); self.colquant4_R = self.listaCol3d.get()
        self.colquant5_R = self.listaCol3e.get(); self.colquant6_R = self.listaCol3f.get()
        self.colquant7_R = self.listaCol3g.get(); self.colquant8_R = self.listaCol3h.get()
        self.colquant9_R = self.listaCol3i.get(); self.colquant10_R = self.listaCol3j.get()
        self.colquant11_R = self.listaCol3k.get(); self.colquant12_R = self.listaCol3l.get();
        self.colquant13_R = self.listaCol3m.get(); self.colquant14_R = self.listaCol3n.get();
        self.colquant15_R = self.listaCol3o.get(); self.colquant16_R = self.listaCol3p.get();
        self.colquant17_R = self.listaCol3q.get(); self.colquant18_R = self.listaCol3r.get();
        self.colquant19_R = self.listaCol3s.get(); self.colquant20_R = self.listaCol3t.get();

        self.colunit1_R = self.listaCol4a.get(); self.colunit2_R = self.listaCol4b.get()
        self.colunit3_R = self.listaCol4c.get(); self.colunit4_R = self.listaCol4d.get()
        self.colunit5_R = self.listaCol4e.get(); self.colunit6_R = self.listaCol4f.get()
        self.colunit7_R = self.listaCol4g.get(); self.colunit8_R = self.listaCol4h.get()
        self.colunit9_R = self.listaCol4i.get(); self.colunit10_R = self.listaCol4j.get()
        self.colunit11_R = self.listaCol4k.get(); self.colunit12_R = self.listaCol4l.get()
        self.colunit13_R = self.listaCol4m.get(); self.colunit14_R = self.listaCol4n.get()
        self.colunit15_R = self.listaCol4o.get(); self.colunit16_R = self.listaCol4p.get()
        self.colunit17_R = self.listaCol4q.get(); self.colunit18_R = self.listaCol4r.get()
        self.colunit19_R = self.listaCol4s.get(); self.colunit20_R = self.listaCol4t.get()

        self.coltotal1_R = self.listaCol5a.get();  self.coltotal2_R = self.listaCol5b.get()
        self.coltotal3_R = self.listaCol5c.get(); self.coltotal4_R = self.listaCol5d.get()
        self.coltotal5_R = self.listaCol5e.get(); self.coltotal6_R = self.listaCol5f.get()
        self.coltotal7_R = self.listaCol5g.get(); self.coltotal8_R = self.listaCol5h.get()
        self.coltotal9_R = self.listaCol5i.get(); self.coltotal10_R = self.listaCol5j.get()
        self.coltotal11_R = self.listaCol5k.get(); self.coltotal12_R = self.listaCol5l.get()
        self.coltotal13_R = self.listaCol5m.get();self.coltotal14_R = self.listaCol5n.get()
        self.coltotal15_R = self.listaCol5o.get(); self.coltotal16_R = self.listaCol5p.get()
        self.coltotal17_R = self.listaCol5q.get(); self.coltotal18_R = self.listaCol5r.get()
        self.coltotal19_R = self.listaCol5s.get();  self.coltotal20_R = self.listaCol5t.get()

        self.entradatotal2_R = self.entradatotal.get(); self.tecnico_R = self.entradaTecnico.get()
        self.tiporc_R = self.Tipvar.get()
        self.comp1 = self.listInicio.get()
        self.comp2 = self.listFim.get()
    def PrintOrc(self):
        webbrowser.open("file:///c:/glacx/Orcamento.pdf")
    def imprime_orc(self):
        self.VarRel()
        # Gerar Relatorio de orçamento
        self.c = canvas.Canvas("c:\glacx\Orcamento.pdf");  self.c.setFont("Helvetica-Bold", 24)
        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, self.m_SeuLogo)
        self.c.setFont("Helvetica-Bold", 14)
        #### MOLDURA E TITULOS DO RELATORIO
        if self.tiporc_R == 'Orçamento':
            self.c.drawString(250, 755, 'Orçamento' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == "('Orçamento ',)":
            self.c.drawString(250, 755, 'Orçamento' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == self.m_Orcamento:
            self.c.drawString(250, 755, 'Orçamento' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == "('Ordem de Serviço ',)":
            self.c.drawString(250, 755, 'Ordem de Serviço' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == "Ordem de Serviço ":
            self.c.drawString(250, 755, 'Ordem de Serviço' + " Nº  " + self.numorc_R)
        elif self.tiporc_R == self.m_Ordem:
            self.c.drawString(250, 755, 'Ordem de Serviço' + " Nº  " + self.numorc_R)
        else:
            self.c.drawString(250, 755, self.tiporc_R + " Nº  " + self.numorc_R)
        self.c.drawString(15, 770, 'Entrada:  ' + self.comp1)
        self.c.drawString(15, 750, 'Saida  :  ' + self.comp2)
        self.c.drawString(15, 720, self.m_DadosDoCliente)
        self.c.rect(10, 732, 200, 3, fill=True, stroke=False); self.c.rect(211, 722, 375, 3, fill=True, stroke=False)
        self.c.rect(10, 482, 3, 250, fill=True, stroke=False); self.c.drawString(205, 722, " \ ")
        self.c.drawString(15, 640, self.m_DadosDoVeiculo)
        self.c.rect(10, 652, 200, 3, fill=True, stroke=False); self.c.rect(211, 642, 375, 3, fill=True, stroke=False)
        self.c.rect(585, 482, 5, 240, fill=True, stroke=False); self.c.drawString(205, 642, " \ ")
        #self.c.drawString(15, 580, self.m_Descricao_dos_Problemas)
        self.c.rect(10, 592, 350, 3, fill=True, stroke=False);self.c.rect(361, 582, 225, 3, fill=True, stroke=False)
        self.c.drawString(355, 582, " \ ")
        # self.c.drawString(15, 580, self.m_Descricao_dos_Problemas)
        self.c.rect(10, 542, 350, 3, fill=True, stroke=False); self.c.rect(361, 532, 225, 3, fill=True, stroke=False)
        self.c.drawString(355, 532, " \ ")
        self.c.drawString(15, 480, self.m_ProdutosEServicos)
        self.c.rect(10, 492, 165, 3, fill=True, stroke=False);self.c.rect(175, 482, 415, 5, fill=True, stroke=False)
        self.c.drawString(440, 130, self.m_Total); self.c.drawString(515, 130, self.entradatotal2_R)
        self.c.setFont("Helvetica", 12)
        ##### FORMATAÇÃO DOS CAMPOS DO RELATORIO
        self.c.drawString(15, 700, self.m_Nome + ": ________________________________  ")
        self.c.drawString(285, 700, self.m_Fone + ": ______________  ")
        self.c.drawString(415, 700, self.m_Cpf + '/' + self.m_Cnpj + ": _______________  ")
        self.c.drawString(15, 680, self.m_Endereco + ": ________________________________________")
        self.c.drawString(350, 680, self.m_Bairro + ": _____________________________")
        self.c.drawString(15, 660, self.m_Cidade + ": ______________________________________")
        self.c.drawString(335, 660, self.m_Uf + ": ____")
        self.c.drawString(15, 620, self.m_Placa + ": __________")
        self.c.drawString(120, 620, self.m_Veiculo + ": ______________________________")
        self.c.drawString(420, 620, self.m_Cor + ": __________________")
        self.c.drawString(90, 600, self.m_Combustivel + ": _______________________________")
        self.c.drawString(420, 600, self.m_Km + ": __________")
        self.c.drawString(14, 472,
                          "______________________________________________________________________________________")
        self.c.drawString(25, 460, self.m_Item); self.c.drawString(150, 460, self.m_Descricao)
        self.c.drawString(345, 460, self.m_Quant);  self.c.drawString(415, 460, self.m_ValorUnit)
        self.c.drawString(515, 460, self.m_Total);
        self.c.drawString(12, 460,
                          "______________________________________________________________________________________")
        self.c.drawString(15, 445, "___01____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 430, "___02____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 415,
                          "___03____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 400,
                          "___04____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 385,
                          "___05____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 370,
                          "___06____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 355,
                          "___07____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 340,
                          "___08____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 325,
                          "___09____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 310,
                          "___10____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 295,
                          "___11____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 280,
                          "___12____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 265,
                          "___13____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 250,
                          "___14____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 235,
                          "___15____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 220,
                          "___16____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 205,
                          "___17____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 190,
                          "___18____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 175,
                          "___19____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(15, 160,
                          "___20____________________________________________________"+ "__" +
                          "____________" + "__" + "____________")
        self.c.drawString(13, 445,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 430,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 415,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 400,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 385,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 370,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 355,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 340,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 325,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 310,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 295,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 280,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 265,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 250,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 235,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 220,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 205,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 190,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 175,
                          "___________________________________________________________________________________")
        self.c.drawString(13, 160,
                          "___________________________________________________________________________________")

        ## MOLDURAS DO RELATORIO
        self.c.rect(10, 155, 2, 330, fill=True, stroke=False), self.c.rect(58, 155, 2, 314, fill=True, stroke=False)
        self.c.rect(326, 155, 2, 314, fill=True, stroke=False), self.c.rect(390, 155, 2, 314, fill=True, stroke=False)
        self.c.rect(485, 155, 2, 314, fill=True, stroke=False), self.c.rect(585, 155, 4, 330, fill=True, stroke=False)
        self.c.rect(13, 155, 570, 2, fill=True, stroke=False)

        self.c.setFont("Helvetica", 10)

        ####  TEXTO DE DESCRICAO DOS PROBLEMAS
        self.c.drawString(50, 565, self.area1_R)
        self.c.drawString(50, 550, self.area2_R)
        self.c.drawString(50, 515, self.area3_R)
        self.c.drawString(50, 500, self.area4_R)

        self.c.setFont("Helvetica-Bold",10)
        self.c.drawString(15, 585, self.m_Atend1print)
        self.c.drawString(15, 535, self.m_Atend2print)

        #### DADOS DO CLIENTE
        self.c.rect(15, 745, 570, 2, fill=True, stroke=False)
        self.c.drawString(65, 700,  self.cliente_R)
        self.c.drawString(325, 700,  self.fone_R  )
        self.c.drawString(485, 700,  self.cpf_R  )
        self.c.drawString(80, 680,  self.endereco_R  )
        self.c.drawString(410, 680,  self.bairro_R  )
        self.c.drawString(85, 660,  self.municipio_R  )
        self.c.drawString(375, 660, self.uf_R)
        #### DADOS DO AUTOMOVEL
        self.c.drawString(60, 620,  self.placa_R  )
        self.c.drawString(165, 620,  self.aut_R  )
        self.c.drawString(320, 620, self.marca_R)
        self.c.drawString(470, 620, self.cor_R)
        self.c.drawString(180, 600, self.combustivel_R)
        self.c.drawString(450, 600, self.km_R)

        self.c.setFont("Helvetica", 10)

        #### DESCRIÇÃO DOS ITENS DO ORÇAMENTO

        ### Item 1
        def moedaValor1(colunit1_R=0):
            return f'{self.colunit1_R:>8.2f}'.replace('.', ',')
        if self.lista1_R == '{}':
            self.c.drawString(60, 445, ''); self.c.drawString(350, 445, '')
            self.c.drawString(420, 445, ''); self.c.drawString(530, 445, '')
        elif self.lista1_R == '':
            self.c.drawString(60, 445, ''); self.c.drawString(350, 445, '')
            self.c.drawString(420, 445, ''); self.c.drawString(530, 445, '')
        else:
            self.colunit1_R = float(self.colunit1_R)
            self.c.drawString(350, 445, self.colquant1_R);
            self.c.drawString(60, 445,  self.lista1_R  )
            self.c.drawString(420, 445, 'R$  ' + moedaValor1(self.colunit1_R));
            self.c.drawString(530, 445, self.coltotal1_R )
        ### Item 2
        def moedaValor2(colunit2_R=0):
            return f'{self.colunit2_R:>8.2f}'.replace('.', ',')
        self.colunit2_R = float(self.colunit2_R)
        if self.lista2_R == '{}':
            self.c.drawString(60, 430, ''); self.c.drawString(350, 430, '')
            self.c.drawString(440, 430, ''); self.c.drawString(530, 430, '')
        elif self.lista2_R == '':
            self.c.drawString(60, 430, ''); self.c.drawString(350, 430, '')
            self.c.drawString(440, 430, ''); self.c.drawString(530, 430, '')
        else:
            self.c.drawString(60, 430,  self.lista2_R  );
            self.c.drawString(350, 430, self.colquant2_R)
            self.c.drawString(420, 430, 'R$  ' + moedaValor2(self.colunit2_R));
            self.c.drawString(530, 430, self.coltotal2_R)
        ### Item 3
        def moedaValor3(colunit3_R=0):
            return f'{self.colunit3_R:>8.2f}'.replace('.', ',')
        self.colunit3_R = float(self.colunit3_R)
        if self.lista3_R == '{}':
            self.c.drawString(60, 415, ''); self.c.drawString(350, 415, '');
            self.c.drawString(440, 415, '');self.c.drawString(530, 415, '');
        elif self.lista3_R == '':
            self.c.drawString(60, 415, '');      self.c.drawString(350, 415, '');
            self.c.drawString(440, 415, '');    self.c.drawString(530, 415, '');
        else:
            self.c.drawString(60, 415,  self.lista3_R  );
            self.c.drawString(350, 415, self.colquant3_R);
            self.c.drawString(420, 415, 'R$  ' + moedaValor3(self.colunit3_R));
            self.c.drawString(530, 415, self.coltotal3_R);
        ### Item 4
        def moedaValor4(colunit4_R=0):
            return f'{self.colunit4_R:>8.2f}'.replace('.', ',')
        self.colunit4_R = float(self.colunit4_R)
        if self.lista4_R == '{}':
            self.c.drawString(60, 400, '');   self.c.drawString(350, 400, '')
            self.c.drawString(440, 400, ''); self.c.drawString(530, 400, '')
        elif self.lista4_R == '':
            self.c.drawString(60, 400, '');  self.c.drawString(350, 400, '')
            self.c.drawString(440, 400, ''); self.c.drawString(530, 400, '')
        else:
            self.c.drawString(60, 400,  self.lista4_R  );
            self.c.drawString(350, 400, self.colquant4_R)
            self.c.drawString(420, 400, 'R$  ' + moedaValor4(self.colunit4_R));
            self.c.drawString(530, 400, self.coltotal4_R)
        ### Item 5
        def moedaValor5(colunit5_R=0):
            return f'{self.colunit5_R:>8.2f}'.replace('.', ',')
        self.colunit5_R = float(self.colunit5_R)
        if self.lista5_R == '{}':
            self.c.drawString(60, 385, '');    self.c.drawString(350, 385, '');
            self.c.drawString(440, 385, '');  self.c.drawString(530, 385, '');
        elif self.lista5_R == '':
            self.c.drawString(60, 385, '');    self.c.drawString(350, 385, '');
            self.c.drawString(440, 385, ''); self.c.drawString(530, 385, '');
        else:
            self.c.drawString(60, 385,  self.lista5_R  );
            self.c.drawString(350, 385, self.colquant5_R);
            self.c.drawString(420, 385, 'R$  ' + moedaValor5(self.colunit5_R));
            self.c.drawString(530, 385, self.coltotal5_R);
        ### Item 6
        def moedaValor6(colunit6_R=0):
            return f'{self.colunit6_R:>8.2f}'.replace('.', ',')
        self.colunit6_R = float(self.colunit6_R)
        if self.lista6_R == '{}':
            self.c.drawString(60, 370, '');   self.c.drawString(350, 370, '')
            self.c.drawString(440, 370, '');   self.c.drawString(530, 370, '')
        elif self.lista6_R == '':
            self.c.drawString(60, 370, '');   self.c.drawString(350, 370, '')
            self.c.drawString(440, 370, ''); self.c.drawString(530, 370, '')
        else:
            self.c.drawString(60, 370,  self.lista6_R  );
            self.c.drawString(350, 370, self.colquant6_R)
            self.c.drawString(420, 370, 'R$  ' + moedaValor6(self.colunit6_R));
            self.c.drawString(530, 370, self.coltotal6_R)
        ### Item 7
        def moedaValor7(colunit7_R=0):
            return f'{self.colunit7_R:>8.2f}'.replace('.', ',')
        self.colunit7_R = float(self.colunit7_R)
        if self.lista7_R == '{}':
            self.c.drawString(60, 355, '');  self.c.drawString(350, 355, '');
            self.c.drawString(440, 355, ''); self.c.drawString(530, 355, '');
        elif self.lista7_R == '':
            self.c.drawString(60, 355, '');  self.c.drawString(350, 355, '');
            self.c.drawString(440, 355, '');  self.c.drawString(530, 355, '');
        else:
            self.c.drawString(60, 355,  self.lista7_R  );
            self.c.drawString(350, 355, self.colquant7_R);
            self.c.drawString(420, 355, 'R$  ' + moedaValor7(self.colunit7_R));
            self.c.drawString(530, 355, self.coltotal7_R);
        ### Item 8
        def moedaValor8(colunit8_R=0):
            return f'{self.colunit8_R:>8.2f}'.replace('.', ',')
        self.colunit8_R = float(self.colunit8_R)
        if self.lista8_R == '{}':
            self.c.drawString(60, 340, '');   self.c.drawString(350, 340, '')
            self.c.drawString(440, 340, '');  self.c.drawString(530, 340, '')
        elif self.lista8_R == '':
            self.c.drawString(60, 340, '');  self.c.drawString(350, 340, '')
            self.c.drawString(440, 340, ''); self.c.drawString(530, 340, '')
        else:
            self.c.drawString(60, 340,  self.lista8_R  );
            self.c.drawString(350, 340, self.colquant8_R)
            self.c.drawString(420, 340, 'R$  ' + moedaValor8(self.colunit8_R));
            self.c.drawString(530, 340, self.coltotal8_R)
        ### Item 9
        def moedaValor9(colunit9_R=0):
            return f'{self.colunit9_R:>8.2f}'.replace('.', ',')
        self.colunit9_R = float(self.colunit9_R)
        if self.lista9_R == '{}':
            self.c.drawString(60, 325, ''); self.c.drawString(350, 325, '');
            self.c.drawString(440, 325, ''); self.c.drawString(530, 325, '');
        elif self.lista9_R == '':
            self.c.drawString(60, 325, '');  self.c.drawString(350, 325, '');
            self.c.drawString(440, 325, ''); self.c.drawString(530, 325, '');
        else:
            self.c.drawString(60, 325,  self.lista9_R  );
            self.c.drawString(350, 325, self.colquant9_R);
            self.c.drawString(420, 325, 'R$  ' + moedaValor9(self.colunit9_R));
            self.c.drawString(530, 325, self.coltotal9_R);
        ### Item 10
        def moedaValor10(colunit10_R=0):
            return f'{self.colunit10_R:>8.2f}'.replace('.', ',')
        self.colunit10_R = float(self.colunit10_R)
        if self.lista10_R == '{}':
            self.c.drawString(60, 310, ''); self.c.drawString(350, 310, '')
            self.c.drawString(440, 310, ''); self.c.drawString(530, 310, '')
        elif self.lista10_R == '':
            self.c.drawString(60, 310, '');  self.c.drawString(350, 310, '')
            self.c.drawString(440, 310, ''); self.c.drawString(530, 310, '')
        else:
            self.c.drawString(60, 310,  self.lista10_R  );
            self.c.drawString(350, 310, self.colquant10_R)
            self.c.drawString(420, 310, 'R$  ' + moedaValor10(self.colunit10_R));
            self.c.drawString(530, 310, self.coltotal10_R)
        ### Item 11
        def moedaValor11(colunit11_R=0):
            return f'{self.colunit11_R:>8.2f}'.replace('.', ',')
        self.colunit11_R = float(self.colunit11_R)
        if self.lista11_R == '{}':
            self.c.drawString(60, 295, ''); self.c.drawString(350, 295, '');
            self.c.drawString(440, 295, ''); self.c.drawString(530, 295, '');
        elif self.lista11_R == '':
            self.c.drawString(60, 295, ''); self.c.drawString(350, 295, '');
            self.c.drawString(440, 295, ''); self.c.drawString(530, 295, '');
        else:
            self.c.drawString(60, 295,  self.lista11_R  );
            self.c.drawString(350, 295, self.colquant11_R);
            self.c.drawString(420, 295, 'R$  ' + moedaValor11(self.colunit11_R));
            self.c.drawString(530, 295, self.coltotal11_R);
        ### Item 12
        def moedaValor12(colunit12_R=0):
            return f'{self.colunit12_R:>8.2f}'.replace('.', ',')
        self.colunit12_R = float(self.colunit12_R)
        if self.lista12_R == '{}':
            self.c.drawString(60, 280, '');  self.c.drawString(350, 280,'')
            self.c.drawString(440, 280, '');  self.c.drawString(530, 280, '')
        elif self.lista12_R == '':
            self.c.drawString(60, 280, '');  self.c.drawString(350, 280, '')
            self.c.drawString(440, 280, '');  self.c.drawString(530, 280, '')
        else:
            self.c.drawString(60, 280,  self.lista12_R  );
            self.c.drawString(350, 280, self.colquant12_R)
            self.c.drawString(420, 280, 'R$  ' + moedaValor12(self.colunit12_R));
            self.c.drawString(530, 280, self.coltotal12_R)
        #### Item 13
        def moedaValor13(colunit13_R=0):
            return f'{self.colunit13_R:>8.2f}'.replace('.', ',')
        self.colunit13_R = float(self.colunit13_R)
        if self.lista13_R == '{}':
            self.c.drawString(60, 265, '');   self.c.drawString(350, 265, '');
            self.c.drawString(440, 265, ''); self.c.drawString(530, 265, '');
        elif self.lista13_R == '':
            self.c.drawString(60, 265, '');  self.c.drawString(350, 265, '');
            self.c.drawString(440, 265, '');  self.c.drawString(530, 265, '');
        else:
            self.c.drawString(60, 265,  self.lista13_R  );
            self.c.drawString(350, 265, self.colquant13_R);
            self.c.drawString(420, 265, 'R$  ' + moedaValor13(self.colunit13_R));
            self.c.drawString(530, 265, self.coltotal13_R);

        ### Item 14
        def moedaValor14(colunit14_R=0):
            return f'{self.colunit14_R:>8.2f}'.replace('.', ',')
        self.colunit14_R = float(self.colunit14_R)
        if self.lista14_R == '{}':
            self.c.drawString(60, 250, ''); self.c.drawString(350, 250, '')
            self.c.drawString(440, 250, '');self.c.drawString(530, 250, '')
        elif self.lista14_R == '':
            self.c.drawString(60, 250, ''); self.c.drawString(350, 250, '')
            self.c.drawString(440, 250, ''); self.c.drawString(530, 250, '')
        else:
            self.c.drawString(60, 250,  self.lista14_R  );
            self.c.drawString(350, 250, self.colquant14_R)
            self.c.drawString(420, 250, 'R$  ' + moedaValor14(self.colunit14_R));
            self.c.drawString(530, 250, self.coltotal14_R)
        ### Item 15
        def moedaValor15(colunit15_R=0):
            return f'{self.colunit15_R:>8.2f}'.replace('.', ',')
        self.colunit15_R = float(self.colunit15_R)
        if self.lista15_R == '{}':
            self.c.drawString(60, 235, ''); self.c.drawString(350, 235, '');
            self.c.drawString(440, 235, '');self.c.drawString(530, 235, '');
        elif self.lista15_R == '':
            self.c.drawString(60, 235, ''); self.c.drawString(350, 235, '');
            self.c.drawString(440, 235, '');self.c.drawString(530, 235, '');
        else:
            self.c.drawString(60, 235,  self.lista15_R  );
            self.c.drawString(350, 235, self.colquant15_R);
            self.c.drawString(420, 235, 'R$  ' + moedaValor15(self.colunit15_R));
            self.c.drawString(530, 235, self.coltotal15_R);
        ### Item 16
        def moedaValor16(colunit16_R=0):
            return f'{self.colunit16_R:>8.2f}'.replace('.', ',')
        self.colunit16_R = float(self.colunit16_R)
        if self.lista16_R == '{}':
            self.c.drawString(60, 220, ''); self.c.drawString(350, 220, '')
            self.c.drawString(440, 220, ''); self.c.drawString(530, 220, '')
        elif self.lista16_R == '':
            self.c.drawString(60, 220, ''); self.c.drawString(350, 220, '')
            self.c.drawString(440, 220, ''); self.c.drawString(530, 220, '')
        else:
            self.c.drawString(60, 220,  self.lista16_R  );
            self.c.drawString(350, 220, self.colquant16_R)
            self.c.drawString(420, 220, 'R$  ' + moedaValor16(self.colunit16_R));
            self.c.drawString(530, 220, self.coltotal16_R)
        ### Item 17
        def moedaValor17(colunit17_R=0):
            return f'{self.colunit17_R:>8.2f}'.replace('.', ',')
        self.colunit17_R = float(self.colunit17_R)
        if self.lista17_R == '{}':
            self.c.drawString(60, 205, ''); self.c.drawString(350, 205, '');
            self.c.drawString(440, 205, '');self.c.drawString(530, 205, '');
        elif self.lista17_R == '':
            self.c.drawString(60, 205, ''); self.c.drawString(350, 205, '');
            self.c.drawString(440, 205, '');self.c.drawString(530, 205, '');
        else:
            self.c.drawString(60, 205,  self.lista17_R  );
            self.c.drawString(350, 205, self.colquant17_R);
            self.c.drawString(420, 205, 'R$  ' + moedaValor17(self.colunit17_R));
            self.c.drawString(530, 205, self.coltotal17_R);
        ### Item 18
        def moedaValor18(colunit18_R=0):
            return f'{self.colunit18_R:>8.2f}'.replace('.', ',')
        self.colunit18_R = float(self.colunit18_R)
        if self.lista18_R == '{}':
            self.c.drawString(60, 190, ''); self.c.drawString(350, 190, '')
            self.c.drawString(440, 190, '');self.c.drawString(530, 190, '')
        elif self.lista18_R == '':
            self.c.drawString(60, 190, ''); self.c.drawString(350, 190, '')
            self.c.drawString(440, 190, '');self.c.drawString(530, 190, '')
        else:
            self.c.drawString(60, 190,  self.lista18_R  );
            self.c.drawString(350, 190, self.colquant18_R)
            self.c.drawString(420, 190, 'R$  ' + moedaValor18(self.colunit18_R));
            self.c.drawString(530, 190, self.coltotal18_R)
        ### Item 19
        def moedaValor19(colunit19_R=0):
            return f'{self.colunit19_R:>8.2f}'.replace('.', ',')
        self.colunit19_R = float(self.colunit19_R)
        if self.lista19_R == '{}':
            self.c.drawString(60, 175, ''); self.c.drawString(350, 175, '');
            self.c.drawString(440, 175, '');self.c.drawString(530, 175, '');
        elif self.lista19_R == '':
            self.c.drawString(60, 175, ''); self.c.drawString(350, 175, '');
            self.c.drawString(440, 175, '');self.c.drawString(530, 175, '');
        else:
            self.c.drawString(60, 175,  self.lista19_R  );
            self.c.drawString(350, 175, self.colquant19_R);
            self.c.drawString(420, 175, 'R$  ' + moedaValor19(self.colunit19_R));
            self.c.drawString(530, 175, self.coltotal19_R);
        ### Item 20
        def moedaValor20(colunit20_R=0):
            return f'{self.colunit20_R:>8.2f}'.replace('.', ',')
        self.colunit20_R = float(self.colunit20_R)
        if self.lista20_R == '{}':
            self.c.drawString(60, 160, ''); self.c.drawString(350, 160, '')
            self.c.drawString(440, 160, '');self.c.drawString(530, 160, '')
        elif self.lista20_R == '':
            self.c.drawString(60, 160, ''); self.c.drawString(350, 160, '')
            self.c.drawString(440, 160, '');self.c.drawString(530, 160, '')
        else:
            self.c.drawString(60, 160,  self.lista20_R  );
            self.c.drawString(350, 160, self.colquant20_R)
            self.c.drawString(420, 160, 'R$  ' + moedaValor20(self.colunit20_R));
            self.c.drawString(530, 160, self.coltotal20_R)

        self.c.setFont("Helvetica", 12)
        #### VARIAVEIS DO RODAPE DO RELATORIO - DADOS DA EMPRESA
        self.c.rect(15, 100, 570, 5, fill=True, stroke=False)
        self.c.drawString(30, 80, licence.NomeEmpresa); self.c.drawString(30, 60, licence.NomeRuaEmp)
        self.c.drawString(300, 60, licence.NomeBairroEmp); self.c.drawString(430, 60, licence.MunicipioEmp)
        self.c.drawString(30, 40, licence.TelefoneEmp);
        self.c.drawString(30, 20, self.m_Tecnico + self.tecnico_R);  self.c.setFont("Helvetica", 8)
        self.c.drawString(280, 5, "GlacX - Oficinas - RfZorzi Sistemas - https://www.facebook.com/rfzorzi/")
        self.c.showPage();  self.c.save();  self.PrintOrc()
    def PrintVist(self):
        webbrowser.open("file:///c:/glacx/Vistoria.pdf")
    def imprime_vist(self):
        self.VarRel()
        self.tecnico_R = self.entradaTecnico.get();self.tiporc_R = self.Tipvar.get()
        self.c = canvas.Canvas("c:\glacx\Vistoria.pdf")
        #### MOLDURA E TITULOS DO RELATORIO
        self.c.setFont("Helvetica-Bold", 24)
        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, 'Seu Logo')
        self.c.setFont("Helvetica-Bold", 16);
        self.c.drawString(200, 755, self.m_VistoriadoVeiculo + "Nº  " + self.numorc_R)
        self.c.setFont("Helvetica", 16)
        self.c.drawString(15, 750, self.m_Data + ': ' + self.dia_R + "/" + self.mes_R + "/" + self.ano_R)
        self.c.drawString(15, 720, self.m_DadosDoCliente)
        self.c.rect(10, 732, 200, 3, fill=True, stroke=False);self.c.rect(211, 722, 375, 3, fill=True, stroke=False)
        self.c.rect(10, 482, 3, 250, fill=True, stroke=False);self.c.drawString(205, 722, " \ ")
        self.c.drawString(15, 640, self.m_DadosDoVeiculo)
        self.c.rect(10, 652, 200, 3, fill=True, stroke=False);self.c.rect(211, 642, 375, 3, fill=True, stroke=False)
        self.c.rect(585, 482, 5, 240, fill=True, stroke=False);self.c.drawString(205, 642, " \ ")
        self.c.drawString(15, 580, self.m_ItensVistoriados)
        self.c.rect(10, 592, 195, 3, fill=True, stroke=False);self.c.rect(205, 582, 385, 5, fill=True, stroke=False)
        # Vistoria variaveis
        self.codVist_R = self.listaNumOrc.get(); self.tanque_R = self.are1.get(); self.odometro_R = self.are2.get()
        self.radio_R = self.are3.get(); self.calota_R = self.are4.get(); self.triangulo_R = self.are5.get()
        self.macaco_R = self.are6.get(); self.estepe_R = self.are7.get(); self.obs1_R = self.are8.get()
        self.obs2_R = self.are9.get()
        self.c.setFont("Helvetica-Bold", 14)
        ### Tanque
        self.c.drawString(35, 540, self.m_Tanque + self.m_ExtensLabel + self.m_DoisPontos +  self.tanque_R)
        #### Odometro
        self.c.drawString(35, 500, self.m_Odometro + self.m_ExtensLabel + self.m_DoisPontos +  self.odometro_R  )
        ### Obs 1
        self.c.drawString(35, 460, 'Obs 1' + self.m_ExtensLabel + self.m_DoisPontos +  self.radio_R  )
        ### Obs 2
        self.c.drawString(35, 420, 'Obs 2' + self.m_ExtensLabel + self.m_DoisPontos +  self.calota_R  )
        ### Obs 3
        self.c.drawString(35, 380, 'Obs 3' + self.m_ExtensLabel + self.m_DoisPontos +  self.triangulo_R  )
        ### Obs 4
        self.c.drawString(35, 340, 'Obs 4' + self.m_ExtensLabel + self.m_DoisPontos +  self.macaco_R  )
        ### Obs 5
        self.c.drawString(35, 300, 'Obs 5' + self.m_ExtensLabel + self.m_DoisPontos +  self.estepe_R  )
        ### Obs 6
        self.c.drawString(35, 260, 'Obs 6' + self.m_ExtensLabel + self.m_DoisPontos +  self.obs1_R  )
        ## Obs 7
        self.c.drawString(35, 220, 'Obs 7' + self.m_ExtensLabel + self.m_DoisPontos +  self.obs2_R  )
        self.c.setFont("Helvetica-Bold", 12); self.c.drawString(35, 180, self.m_ConfirmaVistoria)
        ##### FORMATAÇÃO DOS CAMPOS DO RELATORIO
        self.c.drawString(15, 700, self.m_Nome + ": ________________________________  ")
        self.c.drawString(285, 700, self.m_Fone + ": ______________  ")
        self.c.drawString(415, 700, self.m_Cpf + '/' +self.m_Cnpj + ": _______________  ")
        self.c.drawString(15, 680, self.m_Endereco + ": ________________________________________")
        self.c.drawString(350, 680, self.m_Bairro + ": _____________________________")
        self.c.drawString(15, 660, self.m_Cidade + ": ______________________________________")
        self.c.drawString(335, 660, self.m_Uf + ": ____")
        self.c.drawString(15, 620, self.m_Placa + ": __________")
        self.c.drawString(120, 620, self.m_Veiculo + ": ______________________________")
        self.c.drawString(420, 620, self.m_Cor + self.m_DoisPontos + "______________")
        self.c.drawString(90, 600, self.m_Combustivel + ": _______________________________")

        ## MOLDURAS DO RELATORIO
        self.c.rect(10, 155, 2, 330, fill=True, stroke=False); self.c.rect(13, 155, 570, 2, fill=True, stroke=False)
        self.c.rect(585, 155, 4, 330, fill=True, stroke=False); self.c.setFont("Helvetica", 10)
        #### DADOS DO CLIENTE
        self.c.rect(15, 745, 570, 2, fill=True, stroke=False)
        self.c.drawString(65, 700,  self.cliente_R);  self.c.drawString(325, 700,  self.fone_R  )
        self.c.drawString(485, 700, self.cpf_R); self.c.drawString(80, 680,  self.endereco_R  )
        self.c.drawString(410, 680,  self.bairro_R); self.c.drawString(85, 660,  self.municipio_R)
        self.c.drawString(375, 660, self.uf_R);
        #### DADOS DO AUTOMOVEL
        self.c.drawString(60, 620, self.placa_R);  self.c.drawString(180, 620,  self.aut_R  )
        self.c.drawString(440, 600,  self.marca_R); self.c.drawString(470, 620, self.cor_R)
        self.c.drawString(180, 600, self.combustivel_R); self.c.setFont("Helvetica-Bold", 12)
        #### VARIAVEIS DO RODAPE DO RELATORIO - DADOS DA EMPRESA
        self.c.rect(15, 100, 570, 5, fill=True, stroke=False)
        self.c.drawString(30, 80, licence.NomeEmpresa);  self.c.drawString(30, 60, licence.NomeRuaEmp)
        self.c.drawString(300, 60, licence.NomeBairroEmp); self.c.drawString(430, 60, licence.MunicipioEmp)
        self.c.drawString(30, 40, licence.TelefoneEmp)
        # self.c.drawString(30, 30, cab7)
        self.c.drawString(30, 20, self.m_Tecnico +  self.tecnico_R  ); self.c.setFont("Helvetica", 8)
        self.c.drawString(280, 5, "GlacX - Oficinas - RfZorzi Sistemas - https://www.facebook.com/rfzorzi/")
        self.c.showPage(); self.c.save(); self.PrintVist()
    def PaginaRf(self):
        webbrowser.open("https://www.facebook.com/rfzorzi/")

    def add_autobindC(self, event):
        # codServ1.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)

        self.listatec1.selection()

        for n in self.listatec1.selection():
            col1, col2, col3 = self.listatec1.item(n, 'values')
            self.nomeEquipEntry.insert(END, col2)
            self.marcaEquipEntry.insert(END, col3)
            self.entradaVeiculo2.insert(END, col1)


        cod = self.entradaVeiculo2.get()

        self.conecta_Glac()


        self.cursor.execute(
            """SELECT montad FROM automoveis WHERE cod_aut LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.marcaEquipEntry.insert(END, i)

        self.desconecta_Glac()

        self.listatec.destroy()
        ###############
    def add_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""
              	INSERT INTO clientes ( nome, nascdia, nascmes, nascano, endereco, numcasa,
           	    complemento, bairro, municipio, uf, fone1ddd, fone1, fone2ddd, fone2, cep,
           	    cpf, rg, email, obs)
           	    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (self.cadcli_nome, self.cadcli_nascdia, self.cadcli_nascmes, self.cadcli_nascano,
                        self.cadcli_endereco, self.cadcli_numcasa, self.cadcli_complemento, self.cadcli_bairro,
                        self.cadcli_municipio, self.cadcli_uf, self.cadcli_fone1ddd, self.cadcli_fone1,
                        self.cadcli_fone2ddd, self.cadcli_fone2, self.cadcli_cep, self.cadcli_cpf,
                        self.cadcli_cnpj, self.cadcli_email, self.cadcli_obs))
        self.conn.commit()

        msg = self.m_msgClienteAdd
        msg += ""
        messagebox.showinfo("GLAC ", msg)

        lista1 = self.cursor.execute("""
        	  	SELECT  cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC;
            """)
        for i in lista1:
            self.listaServ.insert("", END, values=i)
        self.conn.commit()
        self.limpa_clienteC()
        self.desconecta_Glac()
        self.janelaCli.destroy()
        self.cadcli()
    def add_veiculoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()

        motor = '0'

        self.conecta_Glac()

        self.cursor.execute("""
    	    	INSERT INTO frota ( idcliente, placa, veiculo, montadora, ano, combust, cor)
    	    	VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (self.cadcli_cod, self.cadcli_placa, self.cadcli_montadora,
                        self.cadcli_veiculo, self.cadcli_ano, self.cadcli_combust, self.cadcli_cor))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
                    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()

        msg = self.m_msgAutAdd
        messagebox.showinfo("GLAC ", msg)
        self.janelaCli.destroy()
        self.cadcli()
    def add_automovelA(self):

        cod_aut = self.entradaCod_autA.get()
        automovel = self.entradaAutA.get()
        montad = self.entradaMarca2A.get()
        self.conecta_Glac()

        self.cursor.execute("""
       		INSERT INTO automoveis ( automovel, montad)
       		VALUES ( ?, ?)""",
                       (automovel, montad))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())

        lista = self.cursor.execute("""
               SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
           	WHERE montadora.cod = automoveis.montad  ORDER BY automoveis.cod_aut DESC;
               """)
        for i in lista:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.limpa_automovelA()
        msg = self.m_msgAutAdd
        msg += ""
        messagebox.showinfo("GLAC - Automovel", msg)
    def add_autobindA(self, event):

        pos = int(self.listatec1.curselection()[0])
        cod = self.listatec1.get(pos)
        self.conecta_Glac()

        addserv1cod = self.cursor
        addserv1cod.execute("""SELECT cod FROM montadora WHERE cod LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.entradaMarca2A.insert(END, i)

        addserv1cod = self.cursor
        addserv1cod.execute("""SELECT marca FROM montadora WHERE cod LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.entradaMarcaA.insert(END, i)

        self.listatec.destroy()

        self.desconecta_Glac()
    def add_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        codinf = self.cursor.execute("""select MAX(cod) + 1 from tecnico """)
        for i in codinf:
            self.entradaCod.insert(END, i)

        servprod = self.entradaServ.get()
        cod_sp = self.entradaCod.get()

        self.cursor.execute("""
    		INSERT INTO tecnico (cod, tecnico) VALUES (?, ?)""", (cod_sp, servprod))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def add_fornec(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        cod_forn = self.entradaCod_forn.get()
        fornecedor = self.entradaFornecedor.get()
        fone = self.entradaFone.get()
        cnpj = self.entradaCnpj.get()
        cep = self.entradaCep.get()
        endereco = self.entradaEndereco.get()
        municipio = self.entradaMunicipio.get()
        descricao = self.entradaDescricao.get()


        self.cursor.execute("""
    		INSERT INTO fornecedores (fornecedor, fone, cnpj, cep, endereco, municipio, descricao)
    		VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (fornecedor, fone, cnpj, cep, endereco, municipio, descricao))
        self.conn.commit()
        lista = self.cursor.execute("""
    		SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
    		""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        msg = "Novo fornecedor incluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.desconecta_Glac()
    def add_movF(self):
        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        mes = self.mes_aba2.get()
        ano = self.ano_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        mesV = self.mesV_aba2.get()
        anoV = self.anoV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""
    		INSERT INTO movim_prod ( cod_p, entrada, custo, dia, mes, ano,
    		lote, diaV, mesV, anoV, fornecedor, saida)
    		VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cod2, quant, custo, dia, mes, ano, lote, diaV, mesV, anoV,
                        fornecedor, saida))
        conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""
    		SELECT  lote, entrada, saida, custo, dia , mes, ano, fornecedores.fornecedor, diaV, mesV, anoV FROM movim_prod , fornecedores
    		WHERE cod_p = '%s' and movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC;        """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)
        conn.close()
    def add_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""
     		INSERT INTO marcaprod ( marca, descricao)
     		VALUES ( ?, ?)""",  (marca, descricao))
        self.conn.commit()
        lista = self.cursor.execute("""
             SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def add_servS(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()
        id_marcaprod = self.entradaDescricao.get()

        self.cursor.execute("""
     		INSERT INTO servprod ( servprod, hor, custo, valor, tiposerv, sistemaserv, sp, descricao, id_marcaprod)
     		VALUES ( ?, ?, ?, ?, ?, ?, "S", ?, ?)""",
                       (servprod, hor, custo, valor, tiposerv, sistemaserv, descricao, id_marcaprod))
        self.conn.commit()
        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao , id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY cod_sp DESC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def add_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        tipser = 'Peça'
        hora = '1'

        self.cursor.execute("""
     		INSERT INTO servprod ( servprod, id_marcaprod, id_fornec, custo, valor, sp, descricao, tiposerv, hor)
     		VALUES ( ?, ?, ?, ?, ?, "P", ?, ?, ?)""",
                       (servprod, id_marcaprod, id_fornec, custo, valor, descricao, tipser, hora))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
     		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Novo produto incluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def add_movE(self):
        self.conecta_Glac()

        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        mes = self.mes_aba2.get()
        ano = self.ano_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        mesV = self.mesV_aba2.get()
        anoV = self.anoV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""
    		INSERT INTO movim_prod ( cod_p, entrada, custo, dia, mes, ano,
    		lote, diaV, mesV, anoV, fornecedor, saida)
    		VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cod2, quant, custo, dia, mes, ano, lote, diaV, mesV, anoV,
                        fornecedor, saida))
        self.conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""
    		SELECT  lote, entrada, saida, custo, dia , mes, ano, fornecedores.fornecedor, diaV, mesV, anoV FROM movim_prod , fornecedores
    		WHERE cod_p = '%s' and movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC;        """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)

        self.desconecta_Glac()
    def add_produtoE(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
            INSERT INTO servprod ( servprod, id_marcaprod, id_fornec, custo, valor, sp, descricao)
        	VALUES ( ?, ?, ?, ?, ?, "P", ?)""",
                       (servprod, id_marcaprod, id_fornec, custo, valor, descricao))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
        	""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()

    def busca_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.nomePeEntry.insert(END, '%')
        nome = self.nomePeEntry.get()
        self.cursor.execute(
            """SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaServ.insert("", END, values=i)

        self.limpa_clienteC()

        self.desconecta_Glac()
    def busca_autoC(self, *args):
        # self.listatec1.yview(*args)

        ### Widgets - Listar tecnicos ###

        self.nomeEquipEntry.insert(END, '%')

        veicAuto = self.nomeEquipEntry.get()

        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("420x240")
        self.listatec.resizable(FALSE, FALSE)
        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10, column=("col1", "col2", "col3"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text= 'Cod')
        self.listatec1.heading("#2", text= self.m_Automovel)
        self.listatec1.heading("#3", text= self.m_Marca)

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=40)
        self.listatec1.column("#2", width=180)
        self.listatec1.column("#3", width=150)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical', command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=377, y=6, width=30, height=225)

        self.listatec1.place(x=5, y=5)
        self.conecta_Glac()


        self.cursor.execute("""SELECT cod_aut, automovel, marca FROM automoveis, montadora WHERE montadora.cod = automoveis.montad
             AND automovel LIKE '%s' ORDER BY automovel ASC""" % veicAuto)

        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)

        # Binding da listbox
        self.listatec1.bind('<Double-1>', self.add_autobindC)

        self.desconecta_Glac()
    def bind_autoC(self, event):
        #codServ1.delete(0, END)
        self.limpa_entryautoC()
        self.listaPlaca.selection()

        for n in self.listaPlaca.selection():
            col1, col2, col3, col4, col5, col6 = self.listaPlaca.item(n, 'values')

        self.serialEquipEntry.insert(END, col1)
        self.nomeEquipEntry.insert(END, col3)
        self.marcaEquipEntry.insert(END, col2)
        self.entradaVeiculo2.insert(END, 0)
        #self.entradaMontadora2.insert(END, col8)
        self.codEquipEntry.insert(END, 0)
        self.corvar.set(col4)
        self.combvar.set(col5)
        self.fabrAnoEquipEntry.insert(END, col6)
    def busca_automovelA(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()


        self.entradaAutA.insert(END, '%')
        autom = self.entradaAutA.get()

        lista = self.cursor.execute("""SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
       	WHERE montadora.cod = automoveis.montad  AND automoveis.automovel LIKE '%s'  ORDER BY automovel ASC;
       		""" % autom)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.entradaAutA.delete(0, END)

        self.desconecta_Glac()
    def busca_autoA(self):
        ### Widgets - Listar tecnicos ###
        self.entradaMarcaA.insert(END, '%')

        veicAuto = self.entradaMarcaA.get()
        self.conecta_Glac()

        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("320x220")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec1 = Listbox(self.listatec, width=5, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        self.listatec1.place(x=7, y=22)
        self.listatec12 = Listbox(self.listatec, width=25, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        self.listatec12.place(x=50, y=22)

        self.barra12 = Scrollbar(self.listatec, orient='vertical', command=self.OnTecA)
        self.barra12.place(x=280, y=22, width=25, height=190)
        self.listatec1.configure(yscroll=self.barra12.set)

        # Binding da listbox
        self.listatec1.bind('<Button-1>', self.add_autobindA)

        self.CabSP = Label(self.listatec, text="Cod        ", fg='darkblue', bg='gray75',
                           font=('Century', '10', 'bold', 'italic'))
        self.CabSP.place(x=2, y=1)

        tec = self.cursor

        tec.execute("""SELECT cod FROM montadora WHERE marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listatec1.insert(END, i)

        tec12 = self.cursor

        tec12.execute("""SELECT marca FROM montadora WHERE marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listatec12.insert(END, i)

        tec22 = self.cursor

        self.entradaMarcaA.delete(0, END)
        self.entradaMarca2A.delete(0, END)

        self.desconecta_Glac()
    def busca_servicoT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.entradaServ.insert(END, '%')
        servprod = self.entradaServ.get()
        servico = self.cursor

        servico.execute("""SELECT cod, tecnico FROM tecnico WHERE tecnico LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def busca_fornecedor(self):
        self.conecta_Glac()

        self.entradaFornecedor.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())
        fornecedor = self.entradaFornecedor.get()

        lista = self.cursor.execute("""
        SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores WHERE fornecedor LIKE '%s'                  ORDER BY fornecedor ASC;
        """ % fornecedor)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
            self.entradaFornecedor.delete(0, END)


        self.desconecta_Glac()
    def busca_marca_prod(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaMarca.insert(END, '%')
        self.conecta_Glac()
        marca = self.entradaMarca.get()
        marcap = self.cursor

        marcap.execute("SELECT * FROM marcaprod WHERE marca LIKE '%s'" % marca)
        buscamarca = self.cursor.fetchall()
        for i in buscamarca:
            self.listaServ.insert("", END, values=i)
        self.entradaMarca.delete(0, END)

        self.desconecta_Glac()
    def busca_serv_veicS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaVeic.insert(END, '%')
        veic = self.entradaVeic.get()

        self.conecta_Glac()

        servico = self.cursor

        servico.execute("""SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod, tiposerv, sistemaserv
     	FROM servprod WHERE id_marcaprod LIKE '%s'  """ % veic)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaVeic.delete(0, END)

        self.desconecta_Glac()
    def busca_servicoS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaServ.insert(END, '%')
        self.conecta_Glac()

        servprod = self.entradaServ.get()
        servico = self.cursor

        servico.execute(
            """SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod WHERE servprod LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def busca_produtoP(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaProd.insert(END, '%')
        servprod = self.entradaProd.get()

        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
     		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
            self.entradaProd.delete(0, END)

        self.desconecta_Glac()
    def busca_marcaP(self):
        def add_autobind(event):
            self.conecta_Glac()

            pos = int(listatec1.curselection()[0])
            cod = listatec1.get(pos)

            addserv1cod = self.cursor
            addserv1cod.execute("""SELECT marca FROM marcaprod WHERE cod_marca LIKE '%s'""" % cod)
            addservico1cod = self.cursor.fetchall()
            for i in addservico1cod:
                self.entradaMarcaprod.insert(END, i)

            addserv1cod = self.cursor
            addserv1cod.execute("""SELECT cod_marca FROM marcaprod WHERE cod_marca LIKE '%s'""" % cod)
            addservico1cod = self.cursor.fetchall()
            for i in addservico1cod:
                self.entradaIdMarcaprod.insert(END, i)

            self.desconecta_Glac()

            listatec.destroy()

        def OnTec(*args):
            listatec1.yview(*args)
            listatec12.yview(*args)

        ### Widgets - Listar tecnicos ###

        self.entradaMarcaprod.insert(END, '%')

        veicAuto = self.entradaMarcaprod.get()

        listatec = Tk()
        listatec.title("Marcas - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)
        listatec1 = Listbox(listatec, width=5, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        listatec1.place(x=7, y=22)
        listatec12 = Listbox(listatec, width=25, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        listatec12.place(x=50, y=22)

        barra12 = Scrollbar(listatec, orient='vertical', command=OnTec)
        barra12.place(x=280, y=22, width=25, height=190)
        listatec1.configure(yscroll=barra12.set)

        # Binding da listbox
        listatec1.bind('<Button-1>', add_autobind)

        CabSP = Label(listatec, text="Cod        Marca", fg='darkblue', bg='gray75',
                      font=('Century', '10', 'bold', 'italic'))
        CabSP.place(x=2, y=1)

        self.conecta_Glac()

        tec = self.cursor

        tec.execute("""SELECT cod_marca FROM marcaprod WHERE cod_marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            listatec1.insert(END, i)

        tec12 = self.cursor

        tec12.execute("""SELECT marca FROM marcaprod WHERE cod_marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            listatec12.insert(END, i)

        self.desconecta_Glac()

        self.entradaMarcaprod.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)

    def busca_fornecP(self):
        self.conecta_Glac()

        def add_autobind(event):
            self.conecta_Glac()

            pos = int(listatec1.curselection()[0])
            cod = listatec1.get(pos)

            addserv1cod = self.cursor
            addserv1cod.execute("""SELECT fornecedor FROM fornecedores WHERE cod_forn LIKE '%s'""" % cod)
            addservico1cod = self.cursor.fetchall()
            for i in addservico1cod:
                self.entradaFornec.insert(END, i)

            addserv1cod = self.cursor
            addserv1cod.execute("""SELECT cod_forn FROM fornecedores WHERE cod_forn LIKE '%s'""" % cod)
            addservico1cod = self.cursor.fetchall()
            for i in addservico1cod:
                self.entradaIdFornec.insert(END, i)

            listatec.destroy()

            self.desconecta_Glac()

        def OnTec(*args):
            listatec1.yview(*args)
            listatec12.yview(*args)

        ### Widgets - Listar tecnicos ###

        self.entradaFornec.insert(END, '%')

        veicAuto = self.entradaFornec.get()

        listatec = Tk()
        listatec.title("Fornecedores - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)
        listatec1 = Listbox(listatec, width=5, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        listatec1.place(x=7, y=22)
        listatec12 = Listbox(listatec, width=25, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        listatec12.place(x=50, y=22)

        barra12 = Scrollbar(listatec, orient='vertical', command=OnTec)
        barra12.place(x=280, y=22, width=25, height=190)
        listatec1.configure(yscroll=barra12.set)

        # Binding da listbox
        listatec1.bind('<Button-1>', add_autobind)

        CabSP = Label(listatec, text="Cod           Fornecedor", fg='darkblue', bg='gray75',
                      font=('Century', '10', 'bold', 'italic'))
        CabSP.place(x=2, y=1)

        tec = self.cursor

        tec.execute(
            """SELECT cod_forn FROM fornecedores WHERE fornecedor LIKE '%s' ORDER BY fornecedor ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            listatec1.insert(END, i)

        tec12 = self.cursor

        tec12.execute(
            """SELECT fornecedor FROM fornecedores WHERE fornecedor LIKE '%s' ORDER BY fornecedor ASC""" % veicAuto)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            listatec12.insert(END, i)

        self.entradaFornec.delete(0, END)
        self.entradaIdFornec.delete(0, END)

        self.desconecta_Glac()
    def busca_produtoE(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaProd.insert(END, '%')
        servprod = self.entradaProd.get()

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()

        lista = self.cursor.execute("""
       		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
       		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
       		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaProd.delete(0, END)

        conn.close()
    def busca_fornecE(self):
        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()

        def add_autobind(event):
            listatec1.selection()

            for n in listatec1.selection():
                col1, col2 = listatec1.item(n, 'values')
                self.entradaFornec.insert(END, col2)
                self.entradaIdFornec.insert(END, col1)

            listatec.destroy()

        def OnTec(*args):
            listatec1.yview(*args)


            ### Widgets - Listar tecnicos ###

        self.entradaFornec.insert(END, '%')

        veicAuto = self.entradaFornec.get()

        listatec = Tk()
        listatec.title("Fornecedores - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)
        ##########
        listatec1 = ttk.Treeview(listatec, height=10, column=("col1", "col2"))
        listatec1.heading("#0", text="")
        listatec1.heading("#1", text="Cod")
        listatec1.heading("#2", text="Fornecedor")

        listatec1.column("#0", width=0)
        listatec1.column("#1", width=60)
        listatec1.column("#2", width=220)

        # Cria barra de rolagem
        barra = Scrollbar(listatec, orient='vertical', command=listatec1.yview)

        # Adiciona barra de rolagem
        listatec1.configure(yscroll=barra.set)
        barra.place(x=280, y=12, width=25, height=220)

        listatec1.place(x=5, y=5)

        lista = self.cursor.execute("""SELECT cod_forn, fornecedor FROM fornecedores ORDER BY fornecedor ASC""")

        rows = cursor.fetchall()
        for row in rows:
            listatec1.insert("", END, values=row)

            # Binding da listbox
        listatec1.bind('<Double-1>', add_autobind)

        self.entradaFornec.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        conn.close
    def busca_marcaE(self):
        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()

        def add_autobind(event):

            listatec1.selection()

            for n in listatec1.selection():
                col1, col2 = listatec1.item(n, 'values')
                self.entradaMarcaprod.insert(END, col2)
                self.entradaIdMarcaprod.insert(END, col1)

            listatec.destroy()

        def OnTec(*args):
            listatec1.yview(*args)

            ### Widgets - Listar tecnicos ###

        self.entradaMarcaprod.insert(END, '%')

        veicAuto = self.entradaMarcaprod.get()

        listatec = Tk()
        listatec.title("Marcas - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)

        ##########
        listatec1 = ttk.Treeview(listatec, height=10, column=("col1", "col2"))
        listatec1.heading("#0", text="")
        listatec1.heading("#1", text="Cod")
        listatec1.heading("#2", text="Marca")

        listatec1.column("#0", width=0)
        listatec1.column("#1", width=60)
        listatec1.column("#2", width=220)

        # Cria barra de rolagem
        barra = Scrollbar(listatec, orient='vertical', command=listatec1.yview)

        # Adiciona barra de rolagem
        listatec1.configure(yscroll=barra.set)
        barra.place(x=280, y=6, width=30, height=225)

        listatec1.place(x=5, y=5)

        lista = self.cursor.execute("""SELECT cod_marca, marca FROM marcaprod ORDER BY marca ASC""")

        rows = cursor.fetchall()
        for row in rows:
            listatec1.insert("", END, values=row)

            # Binding da listbox
        listatec1.bind('<Double-1>', add_autobind)

        self.entradaMarcaprod.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        conn.close()

    def carrega_clienteC(self):
        cod_cli = self.codPeEntry.get()
        self.limpa_clienteC2()

        self.conecta_Glac()

        self.cursor.execute("SELECT UPPER(nome) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacli = self.cursor.fetchall()
        for i in consultacli:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.nomePeEntry.insert(END, i)

        self.cursor.execute("SELECT nascdia FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultadia = self.cursor.fetchall()
        for i in consultadia:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.nascDiaPeEntry.insert(END, i)

        self.cursor.execute("SELECT nascmes FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultames = self.cursor.fetchall()
        for i in consultames:
            self.nascMesPeEntry.insert(END, i)

        self.cursor.execute("SELECT nascano FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultano = self.cursor.fetchall()
        for i in consultano:
            self.nascAnoPeEntry.insert(END, i)

        self.cursor.execute("SELECT numcasa FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultanum = self.cursor.fetchall()
        for i in consultanum:
            self.numPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(complemento) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacompl = self.cursor.fetchall()
        for i in consultacompl:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.complemPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(email) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaemail = self.cursor.fetchall()
        for i in consultaemail:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.emailPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(endereco) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaend = self.cursor.fetchall()
        for i in consultaend:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.logradPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(bairro) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultabairro = self.cursor.fetchall()
        for i in consultabairro:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.bairroPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(municipio) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultamunicipio = self.cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.cidadePeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(uf) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultauf = self.cursor.fetchall()
        for i in consultauf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.ufPeEntry.insert(END, i)

        self.cursor.execute("SELECT fone1ddd FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone1ddd = self.cursor.fetchall()
        for i in consultafone1ddd:
            self.fone1PeEntry.insert(END, i)

        self.cursor.execute("SELECT fone1 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone1 = self.cursor.fetchall()
        for i in consultafone1:
            self.fone1PeEntry2.insert(END, i)

        self.cursor.execute("SELECT fone2ddd FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone2ddd = self.cursor.fetchall()
        for i in consultafone2ddd:
            self.fone2PeEntry.insert(END, i)

        self.cursor.execute("SELECT fone2 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone2 = self.cursor.fetchall()
        for i in consultafone2:
            self.fone2PeEntry2.insert(END, i)

        self.cursor.execute("SELECT cep FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacep = self.cursor.fetchall()
        for i in consultacep:
            self.cepPeEntry.insert(END, i)

        self.cursor.execute("SELECT cpf FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacpf = self.cursor.fetchall()
        for i in consultacpf:
            self.cpfPeEntry.insert(END, i)

        self.cursor.execute("SELECT rg FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultarg = self.cursor.fetchall()
        for i in consultarg:
            self.cnpjPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(obs) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaobs = self.cursor.fetchall()
        for i in consultaobs:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.obsPeEntry.insert(END, i)


        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
    def cep(self):
            self.logradPeEntry.delete(0, END)
            self.bairroPeEntry.delete(0, END)
            self.cidadePeEntry.delete(0, END)
            self.ufPeEntry.delete(0, END)
            try:
                self.cep = self.cepPeEntry.get()
                endcep = pycep_correios.consultar_cep(self.cep)

                self.logradPeEntry.insert(END, endcep['end'])
                self.bairroPeEntry.insert(END, endcep['bairro'])
                self.cidadePeEntry.insert(END, endcep['cidade'])
                self.ufPeEntry.insert(END, endcep['uf'])

            except ExcecaoPyCEPCorreios as exc:
                msg = 'Not find - Não encontrado'
                messagebox.showinfo("GLAC", msg)
    def cepForn(self):
        self.entradaEndereco.delete(0, END)

        self.entradaMunicipio.delete(0, END)

        try:
            self.cep = self.entradaCep.get()
            self.endereco = pycep_correios.consultar_cep(self.cep)

            self.entradaEndereco.insert(END, self.endereco['end'])
            self.entradaEndereco.insert(END, ' - ')
            self.entradaEndereco.insert(END, self.endereco ['bairro'])

            self.entradaMunicipio.insert(END, self.endereco['cidade'])
            self.entradaMunicipio.insert(END, ' - ')
            self.entradaMunicipio.insert(END, self.endereco['uf'])


        except ExcecaoPyCEPCorreios as exc:
            msg = multi.CepNotFind
            msg += ""
            messagebox.showinfo("GLAC ", msg)
    def carrega_cliente2C(self, event):
        self.limpa_clienteC()

        pos = int(self.listaServ2.curselection()[0])
        cod_cli = self.listaServ2.get(pos)

        self.cursor.execute("SELECT cod_cli FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacod = cursor.fetchall()
        for i in consultacod:
            self.entradaCod_clicC.insert(END, i)

        self.carrega_clienteC()
    def carrega_automovelA(self):
        cod_aut = self.entradaCod_autA.get()
        self.conecta_Glac()

        nomeaut = self.cursor

        self.entradaAutA.delete(0, END)

        self.entradaMarcaA.delete(0, END)
        self.entradaMarca2A.delete(0, END)

        nomeaut.execute(
            "SELECT automovel FROM automoveis, montadora WHERE montadora.cod = automoveis.montad AND cod_aut = '%s'" % cod_aut)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaAutA.insert(END, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT marca FROM automoveis, montadora WHERE montadora.cod = automoveis.montad AND cod_aut = '%s'" % cod_aut)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarcaA.insert(END, i)

        nomemarca2 = self.cursor
        nomemarca2.execute(
            "SELECT montad FROM automoveis, montadora WHERE montadora.cod = automoveis.montad AND cod_aut = '%s'" % cod_aut)
        consultamarca2 = self.cursor.fetchall()
        for i in consultamarca2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarca2A.insert(END, i)

        self.desconecta_Glac()
    def carrega_empresa(self):
        cod_emp = self.entradaCod_emp.get()

        self.entradaNome_emp.delete(0, END)
        self.entradaEndereco_emp.delete(0, END)
        self.entradaBairro_emp.delete(0, END)
        self.entradaMunicipio_emp.delete(0, END)
        self.entradaUf_emp.delete(0, END)
        self.entradaFone_emp.delete(0, END)
        self.entradaCep_emp.delete(0, END)
        self.entradaCpf_emp.delete(0, END)
        self.entradaRg_emp.delete(0, END)
        self.entradaObs_emp.delete(0, END)

        self.entradaNome_emp.insert(END, licence.NomeEmpresa)
        self.entradaEndereco_emp.insert(END, licence.NomeRuaEmp)
        self.entradaBairro_emp.insert(END, licence.NomeBairroEmp)
        self.entradaMunicipio_emp.insert(END, licence.MunicipioEmp)
        self.entradaFone_emp.insert(END, licence.TelefoneEmp)
        self.entradaCpf_emp.insert(END, licence.LicencaCpf)
        self.entradaObs_emp.insert(END, licence.Licenca)
    def carrega_servicoT(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        sp = self.cursor

        self.entradaServ.delete(0, END)

        sp.execute("SELECT tecnico FROM tecnico WHERE cod = '%s'" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaServ.insert(END, i)

        self.desconecta_Glac()
    def carrega_fornecedor(self):
        self.conecta_Glac()

        cursor = self.cursor

        cod_forn = self.entradaCod_forn.get()
        fornec = cursor

        self.entradaFornecedor.delete(0, END)
        self.entradaFone.delete(0, END)
        self.entradaCnpj.delete(0, END)
        self.entradaCep.delete(0, END)
        self.entradaEndereco.delete(0, END)
        self.entradaMunicipio.delete(0, END)
        self.entradaDescricao.delete(0, END)

        fornec.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultafornec = self.cursor.fetchall()
        for i in consultafornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFornecedor.insert(END, i)

        fone = self.cursor
        fone.execute("SELECT fone FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultafone = self.cursor.fetchall()
        for i in consultafone:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFone.insert(END, i)

        cnpj = self.cursor
        cnpj.execute("SELECT cnpj FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultacnpj = self.cursor.fetchall()
        for i in consultacnpj:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaCnpj.insert(END, i)

        cep = cursor
        cep.execute("SELECT cep FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultacep = cursor.fetchall()
        for i in consultacep:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaCep.insert(END, i)

        endereco = cursor
        endereco.execute("SELECT endereco FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultaendereco = cursor.fetchall()
        for i in consultaendereco:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaEndereco.insert(END, i)

        municipio = cursor
        municipio.execute("SELECT municipio FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultamunicipio = cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMunicipio.insert(END, i)

        descricao = cursor
        descricao.execute("SELECT descricao FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultadescricao = cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.desconecta_Glac()
    def carrega_marca_prod(self):
        cod_marca = self.entradaCod.get()
        self.conecta_Glac()

        marcaprod = self.cursor

        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)

        marcaprod.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultamarcaprod = self.cursor.fetchall()
        for i in consultamarcaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarca.insert(END, i)

        descricao = self.cursor
        descricao.execute("SELECT descricao FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.desconecta_Glac()
    def carrega_servicoS(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        sp = self.cursor

        self.entradaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaVeic.delete(0, END)

        sp.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaServ.insert(END, i)

        hora = self.cursor
        hora.execute("SELECT hor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultahor = self.cursor.fetchall()
        for i in consultahor:
            self.entradaHor.insert(END, i)

        custohora = self.cursor
        custohora.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacustohora = self.cursor.fetchall()
        for i in consultacustohora:
            self.entradaCustohora.insert(END, i)

        valorhora = self.cursor
        valorhora.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalorhora = self.cursor.fetchall()
        for i in consultavalorhora:
            self.entradaValorhora.insert(END, i)

        tiposerv = self.cursor
        tiposerv.execute("SELECT tiposerv FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultatiposerv = self.cursor.fetchall()
        for i in consultatiposerv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaTipoServ.insert(END, i)

        sistemaserv = self.cursor
        sistemaserv.execute("SELECT sistemaserv FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultasistemaserv = self.cursor.fetchall()
        for i in consultasistemaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaSistemaServ.insert(END, i)

        descricao = self.cursor
        descricao.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.cursor.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaVeic.insert(END, i)

            self.desconecta_Glac()
    def carrega_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        prod = self.cursor

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaFornec.delete(0, END)

        prod.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaprod = self.cursor.fetchall()
        for i in consultaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaProd.insert(END, i)

        idmarca = self.cursor
        idmarca.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaIdMarcaprod.insert(END, i)

        mm = self.entradaIdMarcaprod.get()
        marca = self.cursor
        marca.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % mm)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarcaprod.insert(END, i)

        idfornec = self.cursor
        idfornec.execute("SELECT id_fornec FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            self.entradaIdFornec.insert(END, i)

        ff = self.entradaIdFornec.get()
        fornec = self.cursor
        fornec.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % ff)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFornec.insert(END, i)

        custo = self.cursor
        custo.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacusto = self.cursor.fetchall()
        for i in consultacusto:
            self.entradaCusto.insert(END, i)

        valor = self.cursor
        valor.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalor = self.cursor.fetchall()
        for i in consultavalor:
            self.entradaValor.insert(END, i)

        descrprod = self.cursor
        descrprod.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescrprod = self.cursor.fetchall()
        for i in consultadescrprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

            self.desconecta_Glac()
    def carrega_produtoE(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        prod = self.cursor
        cod2 = self.codproduto2.get()

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)
        self.quantest.delete(0, END)
        self.listaMov.delete(*self.listaMov.get_children())

        prod.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaprod = self.cursor.fetchall()
        for i in consultaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaProd.insert(END, i)
            self.produto_aba2.insert(END, i)

        self.codproduto2.insert(END, cod_sp)

        idmarca = self.cursor
        idmarca.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            self.entradaIdMarcaprod.insert(END, i)

        mm = self.entradaIdMarcaprod.get()
        marca = self.cursor
        marca.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % mm)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaMarcaprod.insert(END, i)

        idfornec = self.cursor
        idfornec.execute("SELECT id_fornec FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            self.entradaIdFornec.insert(END, i)

        ff = self.entradaIdFornec.get()
        fornec = self.cursor
        fornec.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % ff)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaFornec.insert(END, i)

        custo = self.cursor
        custo.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacusto = self.cursor.fetchall()
        for i in consultacusto:
            self.entradaCusto.insert(END, i)
            self.custo_aba2.insert(END, i)

        valor = self.cursor
        valor.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalor = self.cursor.fetchall()
        for i in consultavalor:
            self.entradaValor.insert(END, i)

        descrprod = self.cursor
        descrprod.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescrprod = self.cursor.fetchall()
        for i in consultadescrprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaDescricao.insert(END, i)

        lista = self.cursor.execute("""SELECT  lote, entrada, saida, custo, dia , mes, ano, fornecedores.fornecedor, diaV, mesV, anoV FROM movim_prod , fornecedores
    	    WHERE cod_p = '%s' and movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC;        """ % cod_sp)
        for i in lista:
            self.listaMov.insert("", END, values=i)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) from movim_prod where cod_p = '%s'""" % cod_sp)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)
    def carregaConsulta(self):
        self.conecta_Glac()


        tipopag = self.listtipopag.get()
        valor = self.entryValorDevido.get()

        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = self.entry7.get()


        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
                       SELECT  ordem, tipopag, '*', valordeduzir, dia, mes, ano, pago
                        FROM formapag WHERE tipopag = ? AND  mes = ? AND ano = ?
                        AND pago = ? ORDER BY id ASC; """, (tipopag, mes, ano, pago))
        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
                               SELECT  SUM(valordeduzir)
                                FROM formapag WHERE tipopag = ? AND  mes = ? AND ano = ?
                                AND pago = ? ORDER BY id ASC; """, (tipopag, mes, ano, pago))
        for i in lista2:
            self.entryValorDevido.insert(END, i)

        self.desconecta_Glac()
    def carregaConsulta2(self):
        mes = self.mesvar2.get()
        ano = self.anovar2.get()
        pago = self.entry72.get()

        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()

        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
                       SELECT  ordem, tipopag, '*', valordeduzir, dia, mes, ano, pago
                        FROM formapag WHERE  mes = ? AND ano = ?
                        AND pago = ? ORDER BY id ASC; """, ( mes, ano, pago))
        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
                                       SELECT  SUM(valordeduzir)
                                        FROM formapag WHERE mes = ? AND ano = ?
                                        AND pago = ? ORDER BY id ASC; """, ( mes, ano, pago))
        for i in lista2:
            self.entryValorDevido.insert(END, i)


        self.conn.close()
    def carrega_produto(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaServ2.delete(*self.listaServ2.get_children())

        ano = self.entradaCodprod.get()
        mes = self.entradaProd.get()

        lista = self.cursor.execute("""select id_orc1, placa_orc, dia, mes, ano, "R$",
            trim(replace(totalizador, ',', '.'),'R$') from orcamento1 where ano = '%s'
            and mes = '%s' and tipoOrc != 'Orçamento' order by dia asc;	""" % (ano, mes))

        for i in lista:
            print(i)
            self.listaServ.insert("", END, values=i)

        lista2 = self.cursor.execute("""select ano, mes, sum(trim(replace(totalizador, ',', '.'),'R$'))
                                    from orcamento1
                               		where ano = '%s' and mes = '%s'  and tipoOrc != 'Orçamento';
                               		""" % (ano, mes))
        for i in lista2:
            print(i)
            self.listaServ2.insert("", END, values=i)

        def carrega_produto_a(event):
            carrega_produto()

        self.desconecta_Glac()

    def del_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()

        self.cursor.execute("""
            	DELETE FROM frota WHERE idcliente=?""", (cod_cli,))
        self.conn.commit()
        self.cursor.execute("""
    	        DELETE FROM clientes WHERE cod_cli=?""", (cod_cli,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        lista = self.cursor.execute("""
    		SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC
    	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_clienteC()

        self.desconecta_Glac()
        self.listatec.destroy()
    def deletar_windowC(self):
        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("270x85")
        self.listatec.resizable(FALSE, FALSE)
        ##########
        def btnao():
            self.listatec.destroy()

        self.MensLabel = Label(self.listatec, text = self.m_msgCertezaDel, bg = 'gray75'
                               , font=('Verdana', '7', 'bold'))
        self.MensLabel.place(x=10, y=10)

        self.BtSim = Button(self.listatec,text= self.m_Sim, bd=2, bg = '#37609b', fg ='white',
                            font=('Verdana', '10', 'bold'), command=self.del_clienteC)
        self.BtSim.place(x=50, y=50, width = 70)

        self.BtNao = Button(self.listatec,text= self.m_Nao, bd=2, bg = 'gray25', fg ='white',
                            font=('Verdana', '10', 'bold'), command= btnao)
        self.BtNao.place(x=150, y=50, width = 70)
    def del_placaC(self):
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()
        placa = self.serialEquipEntry.get()
        self.conecta_Glac()

        self.cursor.execute("""
            	DELETE FROM frota WHERE placa =? AND idcliente = ?""", ( placa, cod_cli))
        self.conn.commit()

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        self.limpa_entryautoC()
        self.listatec.destroy()
    def deletar_windowPlacaC(self):
        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("270x85")
        self.listatec.resizable(FALSE, FALSE)
        ##########

        def btnao():
            self.listatec.destroy()

        self.MensLabel = Label(self.listatec, text = self.m_msgCertezaDel, bg = 'gray75'
                               , font=('Verdana', '7', 'bold'))
        self.MensLabel.place(x=10, y=10)

        self.BtSim = Button(self.listatec,text= self.m_Sim, bd=2, bg = '#37609b', fg ='white',
                            font=('Verdana', '10', 'bold'), command=self.del_placaC)
        self.BtSim.place(x=50, y=50, width = 70)

        self.BtNao = Button(self.listatec,text= self.m_Nao, bd=2, bg = 'gray25', fg ='white',
                            font=('Verdana', '10', 'bold'), command= btnao)
        self.BtNao.place(x=150, y=50, width = 70)
    def del_automovelA(self):

        cod_aut = self.entradaCod_autA.get()
        self.conecta_Glac()

        self.cursor.execute(""" DELETE FROM automoveis WHERE cod_aut=?;""", (cod_aut,))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor
        self.cursor.execute("""SELECT automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
       		WHERE montadora.cod = automoveis.montad  ORDER BY automovel ASC;
       		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.limpa_automovelA()
        msg = self.m_msgAutDel
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def del_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        self.cursor.execute("""
        DELETE FROM tecnico WHERE cod = ? """, (cod_sp,))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT cod, tecnico FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def del_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entradaCod_forn.get()
        self.cursor.execute("""
    		DELETE FROM fornecedores WHERE cod_forn=?""", (cod_forn,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute(
            """SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.desconecta_Glac()
        msg = "Fornecedor excluido com sucesso.  :("
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def del_marca_prod(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_marca = self.entradaCod.get()
        self.cursor.execute("""
     		DELETE FROM marcaprod WHERE cod_marca=?""", (cod_marca,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()
    def del_servS(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""
     	DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()

        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY cod_sp DESC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def del_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        self.cursor.execute("""
     		DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" ORDER BY servprod ASC;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Produto excluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def del_produtoE(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_sp = self.entradaCodprod.get()
        self.cursor.execute("""
        		DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" ORDER BY servprod ASC;
        	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()

    def limpa_automovelA(self):
        self.entradaCod_autA.delete(0, END)
        self.entradaAutA.delete(0, END)

        self.entradaMarcaA.delete(0, END)
        self.entradaMarca2A.delete(0, END)
    def limpa_entryautoC(self):
        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        #self.corEquipEntry.delete(0, END)
        #self.combEquipEntry.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
    def limpa_clienteC(self):
        self.codPeEntry.delete(0, END)
        self.nomePeEntry.delete(0, END)
        self.nascDiaPeEntry.delete(0, END)
        self.nascMesPeEntry.delete(0, END)
        self.nascAnoPeEntry.delete(0, END)
        self.logradPeEntry.delete(0, END)
        self.numPeEntry.delete(0, END)
        self.complemPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        self.fone1PeEntry.delete(0, END)
        self.fone1PeEntry2.delete(0, END)
        self.fone2PeEntry.delete(0, END)
        self.fone2PeEntry2.delete(0, END)
        self.cepPeEntry.delete(0, END)
        self.cnpjPeEntry.delete(0, END)
        self.cpfPeEntry.delete(0, END)
        self.obsPeEntry.delete(0, END)
        self.emailPeEntry.delete(0, END)

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_entryautoC()
    def limpa_clienteC2(self):
        #self.codPeEntry.delete(0, END)
        self.nomePeEntry.delete(0, END)
        self.nascDiaPeEntry.delete(0, END)
        self.nascMesPeEntry.delete(0, END)
        self.nascAnoPeEntry.delete(0, END)
        self.logradPeEntry.delete(0, END)
        self.numPeEntry.delete(0, END)
        self.complemPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        self.fone1PeEntry.delete(0, END)
        self.fone1PeEntry2.delete(0, END)
        self.fone2PeEntry.delete(0, END)
        self.fone2PeEntry2.delete(0, END)
        self.cepPeEntry.delete(0, END)
        self.cnpjPeEntry.delete(0, END)
        self.cpfPeEntry.delete(0, END)
        self.obsPeEntry.delete(0, END)
        self.emailPeEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_entryautoC()
    def limpa_servicoT(self):
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)
    def limpa_fornecedor(self):
        self.conecta_Glac()

        self.entradaCod_forn.delete(0, END)
        self.entradaFornecedor.delete(0, END)
        self.entradaFone.delete(0, END)
        self.entradaCnpj.delete(0, END)
        self.entradaCep.delete(0, END)
        self.entradaEndereco.delete(0, END)
        self.entradaMunicipio.delete(0, END)
        self.entradaDescricao.delete(0, END)

        self.desconecta_Glac()
    def limpa_marca_prod(self):
        self.entradaCod.delete(0, END)
        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)
    def limpa_servicoS(self):
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaVeic.delete(0, END)
    def limpa_produtoP(self):
        self.conecta_Glac()

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.entradaCodprod.delete(0, END)

        self.desconecta_Glac()
    def limpa_produtoE(self):
        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.entradaCodprod.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)
    def limpa_produto(self):
        self.entradaProd.delete(0, END)
        self.entradaCodprod.delete(0, END)

        def limpa_produto_a(event):
            limpa_produto()

    def mud_autoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()
        self.conecta_Glac()

        self.cursor.execute(""" UPDATE frota SET veiculo = ?, ano = ?, placa = ?,
            idcliente = ?, combust = ?, montadora = ?, cor = ? WHERE placa = ? AND idcliente = ?""",
                       (self.cadcli_veiculo, self.cadcli_ano, self.cadcli_placa, cod_cli,
                        self.cadcli_combust, self.cadcli_montadora,
                        self.cadcli_cor, self.cadcli_placa, cod_cli))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        msg = self.m_msgVeiculoAlt
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.carrega_clienteC()
        self.janelaCli.destroy()
        self.cadcli()
    def mud_clienteC(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""
    	    UPDATE clientes SET nome = ?, endereco = ?, bairro = ?, municipio = ?,
    	    uf = ?, cep = ?, cpf = ?, rg = ?, obs = ?, email = ?, fone1ddd = ?, fone1 = ?,
    	    fone2ddd = ?, fone2 = ?, complemento = ?, numcasa = ?, nascdia = ?, nascmes = ?, nascano = ?
    	    WHERE cod_cli = ?""",
                       (self.cadcli_nome, self.cadcli_endereco, self.cadcli_bairro, self.cadcli_municipio,
                        self.cadcli_uf, self.cadcli_cep, self.cadcli_cpf, self.cadcli_cnpj, self.cadcli_obs,
                        self.cadcli_email, self.cadcli_fone1ddd, self.cadcli_fone1, self.cadcli_fone2ddd,
                        self.cadcli_fone2, self.cadcli_complemento, self.cadcli_numcasa, self.cadcli_nascdia,
                        self.cadcli_nascmes, self.cadcli_nascano, self.cadcli_cod))
        self.conn.commit()

        lista = self.cursor.execute("""SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes ORDER BY nome ASC;
    	    	""")

        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

        msg = self.m_msgClienteAlt
        msg += ""
        messagebox.showinfo("GLAC - Clientes", msg)
        self.janelaCli.destroy()
        self.cadcli()
    def mud_automovelA(self):

        cod_aut = self.entradaCod_autA.get()
        automovel = self.entradaAutA.get()
        montad = self.entradaMarca2A.get()
        self.conecta_Glac()

        self.cursor.execute("""
       		UPDATE automoveis SET automovel = ? WHERE cod_aut = ?""", (automovel, cod_aut))
        self.conn.commit()

        self.cursor.execute("""
       		UPDATE automoveis SET montad = ? WHERE cod_aut = ?""", (montad, cod_aut))
        self.conn.commit()

        lista = self.cursor.execute("""SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
               	WHERE montadora.cod = automoveis.montad  AND automoveis.automovel LIKE '%s'  ORDER BY automovel ASC;
               		""" % automovel)
        lista = self.cursor.fetchall()
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = self.m_msgAutAlt
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def mud_servT(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()

        self.cursor.execute("""
            UPDATE tecnico SET tecnico = ? WHERE cod = ?""", (servprod, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def mud_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entradaCod_forn.get()
        fornecedor = self.entradaFornecedor.get()
        fone = self.entradaFone.get()
        cnpj = self.entradaCnpj.get()
        cep = self.entradaCep.get()
        endereco = self.entradaEndereco.get()
        municipio = self.entradaMunicipio.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
    		UPDATE fornecedores SET fornecedor = ? WHERE cod_forn = ?""", (fornecedor, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET fone = ? WHERE cod_forn = ?""", (fone, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET cnpj = ? WHERE cod_forn = ?""", (cnpj, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET cep = ? WHERE cod_forn = ?""", (cep, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET endereco = ? WHERE cod_forn = ?""", (endereco, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET municipio = ? WHERE cod_forn = ?""", (municipio, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET descricao = ? WHERE cod_forn = ?""", (descricao, cod_forn))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
        """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
            self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
    		SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
    		""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.desconecta_Glac()
        msg = "Dados do fornecedor alterados com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def mud_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
     		UPDATE marcaprod SET marca = ? WHERE cod_marca = ?""", (marca, cod_marca))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE marcaprod SET descricao = ? WHERE cod_marca = ?""", (descricao, cod_marca))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        listacod = self.cursor.execute("""SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in listacod:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def mud_servS(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()

        self.cursor.execute("""
     		UPDATE servprod SET servprod = ? WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET hor = ? WHERE cod_sp = ?""", (hor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET tiposerv = ? WHERE cod_sp = ?""", (tiposerv, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET sistemaserv = ? WHERE cod_sp = ?""", (sistemaserv, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (veic, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY servprod ASC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def mud_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        tipser = 'Peça'
        hora = '1'

        self.cursor.execute("""
     		UPDATE servprod SET servprod = ?  WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
             		UPDATE servprod SET tiposerv = ? WHERE cod_sp = ?""", (tipser, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
                     		UPDATE servprod SET hor = ? WHERE cod_sp = ?""", (hora, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (id_marcaprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
             UPDATE servprod SET id_fornec = ? WHERE cod_sp = ?""", (id_fornec, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" ORDER BY servprod ASC;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Produto alterado com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def mud_produtoE(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        self.cursor.execute("""
        	UPDATE servprod SET servprod = ? WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (id_marcaprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
            UPDATE servprod SET id_fornec = ? WHERE cod_sp = ?""", (id_fornec, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" ORDER BY servprod ASC;
        	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()

    def OnVsbC(self, *args):
        self.listaServ.yview(*args)
    def OnMouseWheelC(self, event):
        self.listaServ.yview("scroll", event.delta, "units")

        return "break"
    def OnDoubleClickC(self, *args):
        self.limpa_clienteC()

        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1,col2, col3, col4 = self.listaServ.item(n, 'values')
            self.codPeEntry.insert(END, col1)

        self.carrega_clienteC()
    def OnTecA(self, *args):
        self.listatec1.yview(*args)
        self.listatec12.yview(*args)
    def OnDoubleClickA(self, event):
        self.limpa_automovelA()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod_autA.insert(END, col1)

        self.carrega_automovelA()
    def OnVsbA(self, *args):
        self.listaServ.yview(*args)
    def OnDoubleClickT(self, event):
        self.limpa_servicoT()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_servicoT()
    def OnDoubleClickForn(self, event):
        self.limpa_fornecedor()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCod_forn.insert(END, col1)
        self.carrega_fornecedor()
    def OnDoubleClickMarc(self, event):
        self.limpa_marca_prod()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_marca_prod()
    def OnDoubleClickS(self, event):
        self.limpa_servicoS()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_servicoS()
    def OnDoubleClickP(self, event):
        self.limpa_produtoP()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

        self.carrega_produtoP()
    def OnDoubleClickE(self, event):
        self.limpa_produtoE()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

        self.carrega_produtoE()
    def OnDoubleClickFinan(self, event):
        self.limpa_produto()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

            self.carrega_produto()

    def variaveisCliente(self):
        self.cadcli_cod = self.codPeEntry.get()
        self.cadcli_nome = self.nomePeEntry.get()
        self.cadcli_nascdia = self.nascDiaPeEntry.get()
        self.cadcli_nascmes = self.nascMesPeEntry.get()
        self.cadcli_nascano = self.nascAnoPeEntry.get()
        self.cadcli_endereco = self.logradPeEntry.get()
        self.cadcli_numcasa = self.numPeEntry.get()
        self.cadcli_complemento = self.complemPeEntry.get()
        self.cadcli_bairro = self.bairroPeEntry.get()
        self.cadcli_municipio = self.cidadePeEntry.get()
        self.cadcli_uf = self.ufPeEntry.get()
        self.cadcli_fone1ddd = self.fone1PeEntry.get()
        self.cadcli_fone1 = self.fone1PeEntry2.get()
        self.cadcli_fone2ddd = self.fone2PeEntry.get()
        self.cadcli_fone2 = self.fone2PeEntry2.get()
        self.cadcli_cep = self.cepPeEntry.get()
        self.cadcli_cpf = self.cpfPeEntry.get()
        self.cadcli_cnpj = self.cnpjPeEntry.get()
        self.cadcli_email = self.emailPeEntry.get()
        self.cadcli_obs = self.obsPeEntry.get()
    def variaveisVeiculo(self):
        self.cadcli_veiculoId = self.codEquipEntry.get()
        self.cadcli_MontadoraId = self.entradaMontadora2.get()
        self.cadcli_veiculo = self.nomeEquipEntry.get()
        self.cadcli_ano = self.fabrAnoEquipEntry.get()
        self.cadcli_placa = self.serialEquipEntry.get()
        self.cadcli_montadora = self.marcaEquipEntry.get()
        self.cadcli_combust = self.combvar.get()
        self.cadcli_cor = self.corvar.get()