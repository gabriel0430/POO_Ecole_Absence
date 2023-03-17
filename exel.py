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
        self.modified_date = datetime.datetime.fromtimestamp(os.path.getmtime('Classeur1.xlsx'))
        self.date_save = self.modified_date

    def action(self):


        #self.nombre_ligne = self.feuille.max_row
        #return self.nombre_ligne

        for i in range(1, self.nombre_ligne):
            #print(i)
            i = i +1

            Input_Name = self.feuille.cell(row=i, column=1).value
            #print(Input_Name)
            Input_Surname = self.feuille.cell(row=i, column=2).value
            #print(Input_Surname)
            Input_Date_end = self.feuille.cell(row=i, column=3).value
            #print(Input_Date_end)

            Input_Date_end =" inserer la date "

            Prof.name = Input_Name
            Prof.surname = Input_Surname
            Prof.Date_end = Input_Date_end
            print ( self.date_save )
            print ( self.modified_date )


            prof_com = Prof(name=Input_Name,surname=Input_Surname,Date_end=Input_Date_end)

            prof_com.Affiche_Absent()

        while True:
            if self.modified_date != self.date_save:
                print("changement ")


""" def convert(date_time):
        format = '%b %d %Y %I:%M%p'  # The format
        datetime_str = datetime.datetime.strptime(date_time, format)

        return datetime_str

instancier ou faire une referance

z = WWW 

sinon Prenom.nom    .TTinfo.be"""


