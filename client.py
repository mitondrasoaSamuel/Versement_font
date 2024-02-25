import tkinter as tk
from tkinter import *

from tkinter import ttk

class Client:
    def __init__(self, frame):

         ###### Contenu
                # Nom Client
        
        lbl_nom_client = Label(frame, text="Nom :", font=("Arial", 14), bg="white").place(x=50, y=25)

        self.entre_nom_colient =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_nom_colient.place(x=180, y=25, width=250)

                ## Prenom
        lbl_prenom_client = Label(frame, text="Prenom  :", font=("Arial", 14), bg="white").place(x=50, y=85)

        self.entre_compte =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_compte.place(x=250, y=85, width=250)
        

        # Num_compte
        lbl_num_compte = Label(frame, text="N° Compte :", font=("Arial", 14), bg="white").place(x=880, y=25)

        self.entre_compte =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_compte.place(x=1080, y=25, width=250)
               

                # solde
        lbl_solde = Label(frame, text="Solde :", font=("Arial", 14), bg="white").place(x=880, y=85)

        self.entre_solde =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_solde.place(x=1000, y=85, width=250)
      

        ###  Bouton 
                ## Ajouter
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=630, y=150, height=40, width=150)

             ##### Liste Versement
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=200, height=650, width=1080)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)


        self.versementliste = ttk.Treeview(listeFrame , columns=("nom_clint", "num_compte", "solde"), xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.versementliste.xview)

        self.versementliste.heading("nom_clint", text="Non Client")
        self.versementliste.heading("num_compte", text="N° Compte")
        self.versementliste.heading("solde", text="Solde")


        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)


             

