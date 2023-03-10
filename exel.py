import openpyxl
from prof import Prof
import datetime

class Exel :
    def __init__(self):
        # Ouvrir le fichier Excel
        self.wb = openpyxl.load_workbook('Classeur1.xlsx')
        # Sélectionner une feuille spécifique
        self.feuille = self.wb['Absence Prof']
        # Trouver le nombre de ligne de la feuille de calcul
        self.nombre_ligne = self.feuille.max_row


    def action(self):

        for i in range(1, self.nombre_ligne):
            print(i)
            i = i + 1

            Input_Name = self.feuille.cell(row=i, column=1).value
            print(Input_Name)
            Input_Surname = self.feuille.cell(row=i, column=2).value
            print(Input_Surname)
            Input_Date_end = ""
            #Input_Date_end = self.feuille.cell(row=i, column=3).value
            #print(Input_Date_end)
            Prof.name = Input_Name
            Prof.surname = Input_Surname
            Prof.Date_end = Input_Date_end

            prof_com = Prof(name=Input_Name,surname=Input_Surname,Date_end=Input_Date_end)

            prof_com.utile()

    def convert(date_time):
        format = '%b %d %Y %I:%M%p'  # The format
        datetime_str = datetime.datetime.strptime(date_time, format)

        return datetime_str

"""instancier ou faire une referance"""


