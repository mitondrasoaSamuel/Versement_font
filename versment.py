from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time


class accueil:
    def __init__(self, root):
        self.root = root 
        self.root.title("Accueil")
        self.root.geometry("1920x1040+0+0")
        self.root.config(bg="#C0C0C0")

        titre = Label(self.root, text="Gestion des Versement Bancaires", font=("times new roman", 40, "bold"), bg="#C0C0C0").place(x=0, y=0, relwidth=1, height=100)

        #### Bouton Deconnecter
        btn_deconnecte = Button(self.root, text="Deconnecter", font=("times new roman", 20, "bold"), cursor="hand2", bg="#C0C0C0").place(x=1740,y=20)

        #### Heur
        self_lbl_heure=Label(self.root, text="Bienvenu Chez Banque centrale de Madagascar\t\t Date : HH:MM:SS", font=("times new roman", 15), bg="black", fg="white")
        self_lbl_heure.place(x=0,y=100, relwidth=1, height=40)



        #### Bouton recherche

        reche_option = Label(self.root, text="Recherche par N° Versement :", font=("times new roman", 15), bg="white")
        reche_option.place(x=1200, y=160)
                ## Entrer recherche
        reche_lbl = Entry(self.root, font=("times new roman", 20), bg="lightyellow").place(x=1450, y=160, height=40)
        recherche_btn = Button(self.root, text="Rechercher", font=("times new roman", 15, "bold"), cursor="hand2", bg="#C0C0C0", fg="white").place(x=1745, y=160)



        ###### Contenu
                # Versement
        lbl_num_versement = Label(self.root, text="N° Versement :", font=("goudy old style", 20), bg="white").place(x=50, y=220)
        self.entre_versement =  Entry(self.root, font=("goudy old style", 20), bg="lightyellow")    
        self.entre_versement.place(x=250, y=220, width=250)
               
                # Num_compte
        lbl_num_compte = Label(self.root, text="N° Compte :", font=("goudy old style", 20), bg="white").place(x=50, y=320)
        self.entre_compte =  Entry(self.root, font=("goudy old style", 20), bg="lightyellow")    
        self.entre_compte.place(x=250, y=320, width=250)
               
                # Num_cheque
        lbl_num_cheque = Label(self.root, text="N° Chèque :", font=("goudy old style", 20), bg="white").place(x=50, y=420)
        self.entre_cheque =  Entry(self.root, font=("goudy old style", 20), bg="lightyellow")    
        self.entre_cheque.place(x=250, y=420, width=250)
                # Montant
        lbl_montant = Label(self.root, text="Montant :", font=("goudy old style", 20), bg="white").place(x=50, y=520)
        self.entre_montant =  Entry(self.root, font=("goudy old style", 20), bg="lightyellow")    
        self.entre_montant.place(x=250, y=520, width=250)
             



        ###  Bouton 
                ## Ajouter
        
        self.ajout_btn = Button(self.root, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=100, y=640, height=40, width=150)

                ## Reinitialiser
        self.reinitialiser_btn = Button(self.root, text="Reinitialiser", font=("times new roman", 20, "bold"), cursor="hand2", bg="lightgreen", state="normal")
        self.reinitialiser_btn.place(x=500, y=640, height=40, width=150)



        ##### Liste Versement
                    #3 Creation  de frame
        listeFrame = Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=700, y=220, height=600, width=1200)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)

        self.versementliste = ttk.Treeview(listeFrame, columns=("num_vers", "num_compte", "num_cheque", "montant"), xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.versementliste.xview)

        self.versementliste.heading("num_vers", text="N° Versement")
        self.versementliste.heading("num_compte", text="N° Compte")
        self.versementliste.heading("num_cheque", text="N° Chèque")
        self.versementliste.heading("montant", text="Montant")


        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)






if __name__=="__main__":
    root = Tk()    
    obj = accueil(root)
    root.mainloop()