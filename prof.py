import openpyxl


class Prof:
    def __init__(self, name, surname, Date_end):


        name = self.name
        surname = self.surname
        Date_end = self.Date_end


    def Affiche_Absent(self):
        print(str(self.name+self.surname))
        #test_memory = (self.name+ ""+ self.surname)
        #print(test_memory)



    def utile(self):
        self.Date_STR = str(self.Date_end)
        texte = (self.name +" "+ self.surname)
        print ( texte )





    def verifier(self):
        if self.presence == True:
            print('le prof est present')

        if self.presence == False:
            print(self.name, self.surname, "n'est pas présent")