class Appartement:
    def __init__(self,titre,adrs,prix):
        self.__titre=titre
        self.__adrs=adrs
        self.__prix=prix
        self.prs=None
    def gateTitre(self):
        return self.__titre
    def settitre(self,newtatale):
        self.__titre=newtatale
    titre=property(gateTitre,settitre)
    def getaAdres(self):
        return self.__adrs
    def setAdrs(self,newadrs):
        self.__adrs=newadrs
    adrs=property(getaAdres,setAdrs)
    def getaprix(self):
        return self.__prix
    def setprix(self,newprix):
        self.__prix=newprix
    prix=property(getaprix,setprix)
    def sitePrt(self,p):
        self.prs=p
    def __str__(self) :
        ch="titre: "+self.titre+',adress:'+self.adrs+",prix: "+str(self.prix)
        if self.prs==None:
            return ch
        return ch +'<==>'+self.prs.nom+','+str(self.prs.age)
class Personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
        self.posseder=None
    def __str__(self):
        ch="Nom:"+self.nom+",age: "+str(self.age)
        if self.posseder==None:
            return ch 
        return ch +'<==>'+self.posseder.titre+','+self.posseder.adrs+','+str(self.posseder.prix)
    def achote(self,ap):
        if self.posseder!=None:
            return 'il a posseder'
        self.posseder=ap
        Appartement.sitePrt(self,ap)
        return 'félicitations'
    def vondre(self,other):
        if (self.posseder==None) or other.posseder!=None:
            return 'impossiple'
        self.posseder.prix=self.posseder.prix*1.1
        self.posseder.sitePrt(other)
        other.posseder=self.posseder
        self.posseder=None

class Notir:
    def __init__(self,nom):
        self.nom=nom
    def acha(self,p,prt):
        if (p.posseder!=None) or (prt.prs!=None):
            return 'transation impossible'
        p.posseder=prt.__str__()
        prt.prs=p.__str__()
        return 'Done'
    def vent(self,p1,p2):
        if p1.posseder== None and p2.posseder!=None:
            return 'transation impossible'
        p2.posseder=p1.posseder
        p1.psseder.prs=p2
        p1.posseder=None
