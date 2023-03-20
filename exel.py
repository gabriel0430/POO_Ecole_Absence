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
        self.nombre_ligne = (self.nombre_ligne - 1)
        self.date_save = datetime.datetime.fromtimestamp(os.path.getmtime('Classeur1.xlsx'))
        self.modified_date = datetime.datetime.fromtimestamp(os.path.getmtime('Classeur1.xlsx'))



    def reload(self):

        self.date_save = self.modified_date
        #self.nombre_ligne = self.feuille.max_row
        #return self.nombre_ligne
        while True:
            print(self.date_save)
            self.modified_date = datetime.datetime.fromtimestamp(os.path.getmtime('Classeur1.xlsx'))
            if self.modified_date != self.date_save:
                print("changement ")
                self.date_save = self.modified_date
                self.retake = False



    def Extrad(self):

        for i in range(1, self.nombre_ligne):

            i = i +1

            Input_Name = self.feuille.cell(row=i, column=1).value
            Input_Surname = self.feuille.cell(row=i, column=2).value
            #Input_Date_end = self.feuille.cell(row=i, column=3).value


            Prof.name = Input_Name
            Prof.surname = Input_Surname
            #Prof.Date_end = Input_Date_end


            prof_com = Prof(name=Input_Name,surname=Input_Surname)

            prof_com.Affiche_Absent()

    def Auto_run(self):

        while True:
            Exel.Extrad()
            while self.retake:
                Exel.reload()
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


