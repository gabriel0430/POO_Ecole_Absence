import openpyxl

from prof import Prof

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

            nom = self.feuille.cell(row=i, column=1).value
            print(nom)
            surname = self.feuille.cell(row=i, column=2).value
            print(surname)
            Date_end = self.feuille.cell(row=i, column=3).value
            print(Date_end)


            absent = Prof(nom, surname, Date_end)


