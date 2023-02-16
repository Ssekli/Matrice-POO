#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     14/02/2023
# Copyright:   (c) Administrateur 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

class Matrices(Frame) :
    def __init__(self, master = None):
        Frame.__init__(self, master, bg="gray")
        self.master.title("Matrices")
        self.master.geometry("900x900")
        self.Cadres()
        self.Saisie()
        self.Resultats()

    def Cadres(self) :
        self.Cadre_Saisie = Frame(self.master, bg = "gray") #âs de propagate taille inutile
        self.Cadre_Saisie.place(x = 20, y = 20)
        self.Cadre_Res = Frame(self.master, bg = "ivory")
        self.Cadre_Res.place(x = 350, y = 400)

        self.texte1 = StringVar()
        self.texte2 = StringVar()


    def Saisie(self) :
        self.Saisie1 = Text(self.Cadre_Saisie, width = 50, height = 20)
        self.Saisie1.grid(row = 0, column = 0, sticky = W, padx = 5)
        self.Saisie2 = Text(self.Cadre_Saisie, width = 50, height = 20)
        self.Saisie2.grid(row = 0, column = 1, sticky = E, padx = 5)
        self.labelSaisie1 = Label(self.Cadre_Saisie, text = "Matrice 1 :",  font=("Helvetica", 16))
        self.labelSaisie2 = Label(self.Cadre_Saisie, text = "Matrice 2 :",  font=("Helvetica", 16))
        self.labelSaisie1.grid(row = 0, column = 0, sticky = N, padx = 26, pady = 1)
        self.labelSaisie2.grid(row = 0, column = 1, sticky = N, padx = 26, pady = 1)


    def Resultats (self) :
        Button(master = self.Cadre_Res, text="Nouveau", fg="navy", command = self.Resultats).grid(row = 0, column = 1, pady = 20)
        self.texte_res = Text(self.Cadre_Res, width=30, height=15)
        self.texte_res.grid(row=1, column=1)
        self.texte1 = self.Saisie1.get("0.0", END)
        self.texte2 = self.Saisie2.get("0.0", END)
        self.texte_res_str = (f"{self.texte1} et {self.texte2}")
        self.texte_res.insert("0.0", self.texte_res_str)
        self.labeltexte_res = Label(self.Cadre_Res, text = "Resultat :",  font=("Helvetica", 16))




def main():
    mafenetre = Tk()
    mafenetre.title("Matrices")
    mafenetre["bg"] = "gray"
    Matrices(master=mafenetre)
    mafenetre.mainloop()

if __name__ == '__main__':
    main()
