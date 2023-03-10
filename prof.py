

class Prof:
    def __init__(self, nom, surname, Date_end):


        nom = self.nom
        surname = self.surname
        Date_end = self.Date_end


    def verifier(self):
         if self.presence == True:
             print('le prof est present')

         if self.presence == False:
             print(self.nom, self.surname, "n'est pas présent")

    def utile(self):
        print(self.nom +" "+ self.surname+ " " + "ne sera pas present jusqu'au "+self.Date_end)
