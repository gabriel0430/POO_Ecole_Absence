import openpyxl
import os
from prof import Prof
import datetime
import time

class Exel :
    def __init__(self):
        # Ouvrir le fichier Excel
        self.wb = openpyxl.load_workbook('Classeur1.xlsx')
        # Sélectionner une feuille spécifique
        self.feuille = self.wb['Absence Prof']
        # Trouver le nombre de ligne de la feuille de calcul
        self.nombre_ligne = self.feuille.max_row
        self.nombre_ligne = (self.nombre_ligne - 2)
        self.date_save = datetime.datetime.fromtimestamp(os.path.getmtime('Classeur1.xlsx'))
        self.modified_date = datetime.datetime.fromtimestamp(os.path.getmtime('Classeur1.xlsx'))
        self.retake = True


    def reload(self):

        self.date_save = self.modified_date
        #self.nombre_ligne = self.feuille.max_row
        #return self.nombre_ligne


        self.modified_date = datetime.datetime.fromtimestamp(os.path.getmtime('Classeur1.xlsx'))

        if self.modified_date != self.date_save:

                self.date_save = self.modified_date
                self.retake = False
                return self.retake
                print('changement')



    def Data(self):

        for i in range(1, self.nombre_ligne):
            i = i+1

            Input_Name = str(self.feuille.cell(row=i, column=1).value)
            #return self.Input_Name
            Input_Surname = str(self.feuille.cell(row=i, column=2).value)
            #return self.Input_Surname

            #Data_name = self.Input_Name
            Prof.name = Input_Name
            Prof.surname = Input_Surname

            # vidé la note (liste prof)

            prof_com = Prof(name=Input_Name,surname=Input_Surname)

            prof_com.Affiche_Absent()



    def Auto_run(self):

        while True:
            self.Data()
            print("1")
            while self.retake:
                self.reload()
                print("2")
                time.sleep(1)

            print("3")
            time.sleep(1)
            self.retake = True




""" def convert(date_time):
        format = '%b %d %Y %I:%M%p'  # The format
        datetime_str = datetime.datetime.strptime(date_time, format)

        return datetime_str

instancier ou faire une referance

z = WWW 
apatchi 
endigs 

sinon Prenom.nom    .TTinfo.be"""


