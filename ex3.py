import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Application(tk.Tk):

    def __init__(self, pr):

        super().__init__()
        self.cl=dict()
        self.pr=pr
        self.lst = list()
        self.chargerCampo()
        self.inser_widget()
        self.geometry('500x400')
        self.title('Gestion Pharmacie')

    def inser_widget(self):

        #varialbe:
        self.varEntrynom = tk.StringVar()
        self.varEntryprenom = tk.StringVar()
        self.varEntrychifa = tk.StringVar()
        self.varEntrynbStok = tk.StringVar()

        #lbl
        self.lblnom = tk.Label(self, text="Nom: ")
        self.lblprnom = tk.Label(self, text="Prenom: ")
        self.lblchifa = tk.Label(self, text="chifa: ")
        self.lblnb=tk.Label(self,text='le nombre de produit:').place(x=50,y=175)
        self.lblINfr=tk.Label(self,text='information:').place(x=350,y=25)
        self.lblpr = tk.Label(self, text='les produits:').place(x=330, y=210)

        #entry
        self.Entrynom = tk.Entry(self, textvariable=self.varEntrynom)
        self.Entryprenom = tk.Entry(self, textvariable=self.varEntryprenom)
        self.Entrychifa = tk.Entry(self, textvariable=self.varEntrychifa)
        self.EntrynbStok = tk.Entry(self, textvariable=self.varEntrynbStok)

        #button:
        self.btnD_achat=tk.Button(self,text='d\'achat',command=self.d_achat)
        self.btnCl=tk.Button(self,text='clients de pharmacie',command=self.clien)
        self.btnNv=tk.Button(self,text='nouveau clien',command=self.nouveau)
        self.btnSp=tk.Button(self,text='supprimer',command=self.supprime)
        self.btnAg=tk.Button(self,text='Augmenter le nombre de produit',command=self.augmenter)
        self.btnpr=tk.Button(self,text='ajoute de produit',command=self.produit)

        self.lstBox=tk.Listbox(self)
        self.lstBox.config(width= 40)

        self.cmbpr = ttk.Combobox(self, values=self.lst)
        self.cmbpr.bind('<<ComboboxSelected>>', self.info)

        #place
        self.lblnom.place(x=30, y=10)
        self.Entrynom.place(x=80, y=10)
        self.lblprnom.place(x=30, y=50)
        self.Entryprenom.place(x=80, y=50)
        self.lblchifa.place(x=30, y=90)
        self.Entrychifa.place(x=80, y=90)
        self.EntrynbStok.place(x=50,y=195)
        self.btnD_achat.place(x=50,y=140)
        self.lstBox.place(x=250,y=50)
        self.cmbpr.place(x=330,y=240)
        self.btnCl.place(x=330,y=270)
        self.btnNv.place(x=110,y=140)
        self.btnSp.place(x=250,y=235)
        self.btnAg.place(x=50,y=220)
        self.btnpr.place(x=330,y=300)

    #sell
    def d_achat(self):
        try:
            if self.cmbpr.get() == "":
                raise Exception('choix le produit')
            p = self.cmbpr.get()
            if (self.EntrynbStok.get())=='':
                raise Exception('chois de nombre le produit')
            nbS = int(self.EntrynbStok.get())
            if self.Entrychifa in self.cl:
                pass
            else:
                self.cl[int(self.Entrychifa.get())]=[self.Entrynom.get(),self.Entryprenom.get(),int(self.Entrychifa.get())]
            if nbS>self.pr.preduit[p].stock:
                raise Exception('il n\'pas le nombre de produit voulez')
            self.pr.preduit[p].stock-=nbS
            self.varEntrynbStok.set(' ')
        except Exception as err:
            messagebox.showwarning('error',err)

    def clien(self):
        cl=Cli(self.cl)
        cl.mainloop()

    #list pour listBox
    def chargerCampo(self):
        for k in self.pr.preduit.keys():
            self.lst.append(k)

    #information
    def info(self,event):

        p=self.cmbpr.get()
        self.lstBox.insert(tk.END,str(self.pr.preduit[p])+':')
        self.lstBox.insert(tk.END,str(self.pr.preduit[p].prix)+'DH')
        self.lstBox.insert(tk.END,"stock:"+str(self.pr.preduit[p].stock))

    #new
    def nouveau(self):
        self.varEntrynbStok.set(' ')
        self.varEntrynom.set(' ')
        self.varEntryprenom.set(' ')
        self.varEntrychifa.set(' ')

    #supprime de listBox
    def supprime(self):
        self.lstBox.delete(0, tk.END)

    def augmenter(self):
        try:
            if self.cmbpr.get() == "":
                raise Exception('choix le produit')
            if (self.EntrynbStok.get())=='':
                    raise Exception('chois de nombre le produit pour augmenter')
            st = int(self.varEntrynbStok.get())
            p = self.cmbpr.get()
            self.pr.preduit[p].stock+=st
            self.varEntrynbStok.set('')
        except Exception as err:
            messagebox.showwarning('error',err)
    def produit(self):
        self.destroy()
        pro=AjoutepRoduit(self.pr)
        pro.mainloop()



class AjoutepRoduit(tk.Tk):
    def __init__(self,pr):
        super().__init__()
        self.pr=pr
        self.insert_widget()
        self.geometry("400x400")

    def insert_widget(self):
        self.varEntryref = tk.StringVar()
        self.varEntryprix = tk.StringVar()
        self.varEntryst = tk.StringVar()
        self.varEntrytype = tk.StringVar()

        self.rdgen=tk.StringVar()
        self.rdgen.set(None)
        self.rdord=tk.StringVar()
        self.rdord.set(None)
        self.rdp=tk.StringVar()
        self.rdp.set(None)

        self.lblref = tk.Label(self, text="référence: ")
        self.lblprix = tk.Label(self, text="prix: ")
        self.lblst = tk.Label(self, text="stock: ")
        self.lblty = tk.Label(self, text="type: ")

        self.Entryref = tk.Entry(self, textvariable=self.varEntryref)
        self.Entryprix = tk.Entry(self, textvariable=self.varEntryprix)
        self.Entryst = tk.Entry(self, textvariable=self.varEntryst)
        self.Entryty = tk.Entry(self, textvariable=self.varEntrytype)

        self.rdgenBot = tk.Radiobutton(self, text='generique', variable=self.rdgen, value=1)
        self.rdgennBot = tk.Radiobutton(self, text='not generique', variable=self.rdgen, value=0)
        self.rdordBot = tk.Radiobutton(self, text='Ordonnace', variable=self.rdord, value=1)
        self.rdordnBot= tk.Radiobutton(self, text='not Ordonnace', variable=self.rdord, value=0)

        self.rdmat = tk.Radiobutton(self, text='Medicament',variable=self.rdp, value=0)
        self.rdmat.bind("<Button-1>",self.med)
        self.rdpr = tk.Radiobutton(self, text='Produit de pharmacie', variable=self.rdp, value=1)
        self.rdpr.bind("<Button-1>",self.pre)

        self.btnaj=tk.Button(self,text='ajoute',command=self.ajoute)
        # self.btnajpr=tk.Button(self,text='ajoute',command=self.ajoutepr)
        self.btnfe=tk.Button(self,text='fermme',command=self.fermme)

        self.lblref.place(x=20, y=80)
        self.lblprix.place(x=20, y=110)
        self.lblst.place(x=20, y=140)
        self.lblty.place(x=20, y=170)

        self.Entryref.place(x=90,y=80)
        self.Entryprix.place(x=90,y=110)
        self.Entryst.place(x=90,y=140)
        self.Entryty.place(x=90,y=170)

        self.rdgenBot.place(x=250,y=80)
        self.rdgennBot.place(x=250,y=110)
        self.rdordBot.place(x=250,y=140)
        self.rdordnBot.place(x=250,y=170)

        self.rdmat.place(x=30,y=10)
        self.rdpr.place(x=30,y=50)

        self.btnaj.place(x=20,y=230)
        self.btnfe.place(x=250,y=250)

    def med(self,event):
        self.Entryty["state"] = "disabled"
        self.lblty.config(state='disabled')
        self.rdgenBot["state"] = "normal"
        self.rdordnBot.config(state='normal')
        self.rdgennBot.config(state='normal')
        self.rdordBot.config(state='normal')

    def pre(self,event):
        self.rdgenBot["state"]="disabled"
        self.rdordnBot.config(state='disabled')
        self.rdgennBot.config(state='disabled')
        self.rdordBot.config(state='disabled')
        self.lblty.config(state='normal')
        self.Entryty["state"] = "normal"

    def ajoute(self):
        try:
            if self.rdp.get()=='0':
                lst=[False,True]
                ref=self.Entryref.get()
                prix=int(self.Entryprix.get())
                st=int(self.Entryst.get())
                if self.rdgen.get()=='1':
                    ge=1

                if self.rdgen.get()=='0':
                    ge=0

                if self.rdord.get()=='1':
                    ord=1

                if self.rdord.get()=='0':
                    ord=0

                m=Medicament(ref,prix,st,lst[ge],lst[ord])
                self.pr.ajoute(m)
            if self.rdp.get()=="1":
                ref = self.Entryref.get()
                prix = int(self.Entryprix.get())
                st = int(self.Entryst.get())
                type = self.Entryty.get()
                self.pr.ajoute(PordPharm(ref, prix, st, type))
            if self.rdp.get()=='None':
                print(545)
                raise Exception('chois le type de produit')

        except Exception as err:
            messagebox.showwarning('error', err)

    def fermme(self):
        self.destroy()
        app=Application(self.pr)
        app.mainloop()


class Cli(tk.Tk):
    def __init__(self,cli):
        super().__init__()
        self.lst=list()
        self.cli=cli
        self.chargerCampo()
        self.insert_widget()
        self.geometry("300x300")



    def insert_widget(self):
        self.cmbcl = ttk.Combobox(self, values=self.lst)
        self.cmbcl.bind('<<ComboboxSelected>>',self.clien)
        self.cmbcl.place(x=90,y=35)
        self.lblcl=tk.Label(self,text='Cliens:').place(x=120,y=10)
        self.lblnom = tk.Label(self, text="Nom: ")
        self.lblprnom = tk.Label(self, text="Prenom: ")
        self.lblchifa = tk.Label(self, text="chifa: ")
        self.lblnom.place(x=20,y=80)
        self.lblprnom.place(x=20,y=110)
        self.lblchifa.place(x=20,y=140)


    def clien(self,event):

        c=int(self.cmbcl.get())
        cl=self.cli[c]

        self.lblnom['text'] ='Nom: ' +str(cl[0])
        self.lblprnom['text'] ='Prenom: ' +str(cl[1])
        self.lblchifa['text'] ='chifa: ' +str(cl[2])

    def chargerCampo(self):
        for k in self.cli.keys():
            self.lst.append(k)




class Pharmacie():

    def __init__(self, nom, adress):
        self.nom = nom
        self.adress = adress

class Prod(object):

    def __init__(self):
        self.preduit = dict()

    def ajoute(self, pr):

        self.preduit[pr.référence] = pr

    def d_achat(self, pr, nm):
        pr.stock -= nm


class Client():

    def __init__(self, nom, prenom, chifa):
        self.nom = nom
        self.prenom = prenom
        self.chifa = chifa

    def __str__(self):
        return self.nom + ',' + self.prenom + ',' + str(self.chifa)

    def d_achat(self, pr, nm):
        pr.stock -= nm


class Produit():

    def __init__(self, référence, prix, stock):
        self.référence = référence
        self.prix = prix
        self.stock = stock

    def __str__(self):
        return self.référence + ',' + str(self.prix) + ',' + str(self.stock)


class Medicament(Produit):

    def __init__(self, référence, prix, stock, generique, Ordonnace):
        super().__init__(référence, prix, stock)
        self.generique = generique
        self.Ordonnace = Ordonnace

    def __str__(self):
        if self.generique and not self.Ordonnace:
            return super().__str__() + ',' + 'generique' + ',' + 'not Ordonnace'
        if not self.generique and self.Ordonnace:
            return super().__str__() + ',' + 'not generique' + ',' + 'Ordonnace'
        if not self.generique and not self.Ordonnace:
            return super().__str__() + ',' + 'not generique' + ',' + 'not Ordonnace'
        if self.generique and self.Ordonnace:
            return super().__str__() + ',' + 'generique' + ',' + 'Ordonnace'


class PordPharm(Produit):

    def __init__(self, référence, prix, stock, type):
        super().__init__(référence, prix, stock)
        self.type = type

    def __str__(self):
        return super().__str__() + ',' + self.type


#produit:
pr=Prod()
m1=Medicament('j25kj0j',50,70,True,False)
m2=Medicament('i85kj10',150,100,False,True)
m3=Medicament('d5140',350,97,False,False)
m4=Medicament('i55gb',10,2500,True,True)
m5=PordPharm('6k20',84,900,'beate')
m6=PordPharm('k1552510',120,25,'cosmetique')
pr.ajoute(m1)
pr.ajoute(m2)
pr.ajoute(m3)
pr.ajoute(m4)
pr.ajoute(m5)
pr.ajoute(m6)

app=Application(pr)
app.mainloop()