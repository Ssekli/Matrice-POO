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
        self.Cadre_Saisie = Frame(self.master, bg = "gray") #pas de propagate car taille inutile
        self.Cadre_Saisie.place(x = 20, y = 20)
        self.Cadre_Res = LabelFrame(self.master,text = "Résultats", bg = "ivory", width = 800, height = 300)
        self.Cadre_Res.grid_propagate(False)
        self.Cadre_Res.place(x = 20, y = 400)

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
        Button(master = self.Cadre_Res, text = "Addition A+B", fg = "navy", command = self.Resultats).grid(row = 0, column = 0, sticky = W, pady = 20, padx = 15)
        self.texte_res = Text(self.Cadre_Res, width=30, height=15)
        self.texte_res.place(x = 300, y = 50)
        self.texte1 = self.Saisie1.get("0.0", END)
        self.texte2 = self.Saisie2.get("0.0", END)
        self.texte_res_str = (f"{self.texte1} et {self.texte2}")
        self.texte_res.insert("0.0", self.texte_res_str)
        self.labeltexte_res = Label(self.Cadre_Res, text = "Resultat :",  font=("Helvetica", 16))

        Button(master = self.Cadre_Res, text = "Multiplication AxB", fg = "navy", command = self.Resultats).grid(row = 0, column = 1, pady = 20, padx = 15)
        Button(master = self.Cadre_Res, text = "Multiplication A*k", fg = "navy", command = self.Resultats).grid(row = 0, column = 2, pady = 20, padx = 15)
        Button(master = self.Cadre_Res, text = "Determinant A", fg = "navy", command = self.Resultats).grid(row = 0, column = 3, pady = 20, padx = 15)
        Button(master = self.Cadre_Res, text = "Transposition A", fg = "navy", command = self.Resultats).grid(row = 0, column = 4,  pady = 20, padx = 15)
        Button(master = self.Cadre_Res, text = "Inverse A", fg = "navy", command = self.Resultats).grid(row = 0, column = 5, pady = 20, padx = 15)
        Button(master = self.Cadre_Res, text = "Vider", fg = "navy", command = self.Resultats).grid(row = 0, column = 6, pady = 20, padx = 15)

    #recupere matrice a
    def recup_matricea() :
        matricea = [] #matrice temp
        idx = 0
        for i in self.Saisie1.get("1.0", END).splitlines() : # recup la saisie
            if i != '' :
                matricea.append([])
                for j in i.split(",") :
                    if j.lstrip("-").isnumeric() :
                        matricea[idx].append(int(j))
                idx += 1
        return matricea

    #recupere matrice b
    def recup_matriceb() :
        matriceb = [] #matrice temp
        idx = 0
        for i in self.Saisie2.get("1.0", END).splitlines() : # recup la saisie
            if i != '' :
                matriceb.append([])
                for j in i.split(",") :
                    if j.lstrip("-").isnumeric() :
                        matriceb[idx].append(int(j))
                idx += 1
        return matriceb

    def vider():
        text_result.delete('1.0', END)

    def result_addition() :
        '''pour obtenir le résultat de mon addition'''
        matricea = recup_matricea()
        matriceb = recup_matriceb()
        matrice = add_matrice(matricea, matriceb)
        text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


    def result_multiplication() :
        '''pour obtenir le résultat de mon multi'''
        matricea = recup_matricea()
        matriceb = recup_matriceb()
        matrice = multi_matrice(matricea, matriceb)
        text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def result_deter_a() :
        '''Pour Obternir le determinant de A'''
        matricea = recup_matricea()
        determinant = determinant_matrice(matricea)
        text_result.insert(END, determinant)

    def result_deter_b() :
        '''Pour Obternir le determinant de B'''
        matriceb = recup_matriceb()
        determinant = determinant_matrice(matriceb)
        text_result.insert(END, determinant)

    def result_multi_a_scalaire() :
        '''Pour multiplier A par scalaire'''
        matricea = recup_matricea()
        scalaire = int(input_scalaire.get())
        matrice = multiplication_matrice_scalaire(matricea, scalaire)
        text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")
        print(matricec, scalaire)

    def result_transpo_a() :
        ''' calcul de transpo A '''
        matricea = recup_matricea()
        matrice = transpo_matrice(matricea)
        text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def result_transpo_b() :
        '''calcul transpo B'''
        matriceb = recup_matriceb()
        matrice = transpo_matrice(matriceb)
        text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")


    def result_inversion_a() :
        '''inversion de a'''
        matricea = recup_matricea()
        matrice = inversion_matrice(matricea)
        text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")

    def result_inversion_b() :
        '''inversion de a'''
        matriceb = recup_matriceb()
        matrice = inversion_matrice(matriceb)
        text_result.insert(END,f"{matrice[0][0]},{matrice[0][1]}\n{matrice[1][0]},{matrice[1][1]}")



def main():
    mafenetre = Tk()
    mafenetre.title("Matrices")
    mafenetre["bg"] = "gray"
    Matrices(master=mafenetre)
    mafenetre.mainloop()

if __name__ == '__main__':
    main()
