import openpyxl


class Prof:
    def __init__(self, name, surname, Date_end):


        name = self.name
        surname = self.surname
        Date_end = self.Date_end


    def verifier(self):
         if self.presence == True:
             print('le prof est present')

         if self.presence == False:
             print(self.name, self.surname, "n'est pas présent")

    def utile(self):
        print(self.name +" "+ self.surname+ " " + "ne sera pas present jusqu'au "+self.Date_end)
