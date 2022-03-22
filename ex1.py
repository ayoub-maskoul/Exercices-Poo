class Stock:
    def __init__(self, num_ref, nom, prix, num_stock):
        self.num_ref = num_ref
        self.nom = nom
        self.prix = prix
        self.num_stock = num_stock
    def __str__(self):
        return 'numero de référece:'+str(self.num_ref)+', nom:'+self.nom+', prix:'+str(self.prix)+'Dh, number de stock:'+str(self.num_stock)
class Gestion_stock :
    def __init__(self):
        self.dict_ref = dict()
        self.dict_nom = dict()
    def modifier(self, artic):
        self.dict_ref[artic.num_ref] = artic
        self.dict_nom[artic.nom] = artic
    def affiche(self):
        for i in self.dict_ref.keys():
            print(self.dict_ref[i].__str__())
    def recherche_ref(self,reference):
        for i in self.dict_ref.keys():
            if i == reference:
                return self.dict_ref[reference]
        return None
    def ajoute_stock(self,ref,num_st):
        for i in self.dict_ref.keys():
            if i==ref:
                self.dict_ref[ref].num_stock+=num_st
                return 'done'
        return 'il existe pas reference'
    def recherche_nom(self,nom):
        for i in self.dict_nom.keys():
            if i == nom:
                return self.dict_nom[nom]
        return None
    def reche_prix(self,prix1,prix2):
        stt=list()
        for i in self.dict_ref.keys():
            if self.dict_ref[i].prix < prix1 and self.dict_ref[i].prix > prix2:
                stt.append(i)
        if len(stt)!=0:
            return 'référence:'+str(stt)
        return 'il existe pas'
    def supprime(self,ref):
        for i in self.dict_ref.keys():
            if i == ref:
                self.dict_ref.pop(ref)
                return 'supprime'
        return 'il existe pas'
s=Gestion_stock()
c=0
lst=[1,2,3,4,5,6,7,8]
while c !=8:
    try:
        print('1 pour rechercher un article par référence')
        print('2 pour ajoute de numero de stock')
        print('3 pour suprime un article par référence')
        print('4 pour modifier un article par référence')
        print('5 pour rechercher un article par nom')
        print('6 pour rechercher un article par intervalle de prix de vente')
        print('7 pour affiche tous les article')
        print('8 pour quitter')
        c=int(input('entre le numero:'))
        if c==1:
            ref=int(input('entre le référence:'))
            if s.recherche_ref(ref) ==None:
                print('il existe pas')
            else:
                print("il existe")
        if c==2:
            ref=int(input('entre le référence:'))
            st = int(input('entre le numero de stock:'))
            print(s.ajoute_stock(ref,st))
        if c==3:
            ref = int(input('entre le référence:'))
            if s.recherche_ref(ref) != None:
                print(s.supprime(ref))
        if c==4:
            ref = int(input('entre le numerode référence:'))
            nom = input('entre le nom:')
            prix = int(input('entre le prix:'))
            st = int(input('entre le numero de stock:'))
            if s.recherche_ref(ref) == None:
                s.modifier(Stock(ref, nom, prix, st))
            else:
                print("il existe")
        if c==5:
            nom = input('entre le nom:')
            if s.recherche_nom(nom) == None:
                print('il existe pas')
            else:
                print("il existe")
        if c==6:
            prix1 = int(input('entre le prix grand: '))
            prix2 = int(input('entre le prix petit:'))
            print(s.reche_prix(prix1,prix2))
        if c==7:
            print(s.affiche())
        if c==8:
            print('fin de programme')
        if c not in lst:
            print('touche incorect')
    except Exception as err:
        print(err)