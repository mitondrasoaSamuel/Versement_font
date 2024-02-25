import tkinter as tk
from tkinter import *

from tkinter import ttk

class Utilisateur:
    def __init__(self, frame):

          ###### Contenu
                # Nom

        lbl_nom = Label(frame, text="Nom :", font=("Arial", 14), bg="white").place(x=110, y=25)

        self.entre_nom =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_nom.place(x=180, y=25, width=250)
        

        # Mail
        lbl_mail = Label(frame, text="Email :", font=("Arial", 14), bg="white").place(x=500, y=25)

        self.entre_emal =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_emal.place(x=580, y=25, width=250)
               

                # Mot de passe
        lbl_mdp = Label(frame, text="Mot de passe :", font=("Arial", 14), bg="white").place(x=900, y=25)

        self.entre_mdp =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_mdp.place(x=1040, y=25, width=250)
        

        ###  Bouton 
                ## Ajouter
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=630, y=100, height=40, width=150)

             ##### Liste Utilisateur
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=180, height=650, width=1080)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)


        self.versementliste = ttk.Treeview(listeFrame , columns=("nom_client", "mail", "mdp"), xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.versementliste.xview)

        self.versementliste.heading("nom_client", text="Nom")
        self.versementliste.heading("mail", text="Email")
        self.versementliste.heading("mdp", text="Mot de passe")


        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)

