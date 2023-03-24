import openpyxl
import os


class Prof:
    def __init__(self, name, surname):


        name = self.name
        surname = self.surname
        self.Liste_Prof = []
        self.texte = ""



    def Data_Absent(self):

        print(self.Liste_Prof)

        self.texte = str(self.name + " " + self.surname)
        if self.texte != "None None":
            self.ID = self.texte
            print(self.texte)
            if self.ID != "":
                self.Liste_Prof.append(self.ID)
                print('test')
                print(self.Liste_Prof)

        return self.Liste_Prof




    def Affichage_Liste(self):

        print(self.Liste_Prof)

    def Retake_Liste(self):

        self.Liste_Prof.clear()
        return self.Liste_Prof









        """fichier = open("data.txt", "a")
                fichier.write("\n")
                fichier.write(self.texte)
                # ajouter la liste a un note
                # lire la note et l'afficher"""
