import tkinter as tk
from tkinter import *

class Accueil:
    def __init__(self, frame):
        accueil_page_lb = tk.Label(frame, text="GESTION VERSEMENT BANCAIRES", font=("Arial", 30, "bold"), fg="#1c1b1b")
        accueil_page_lb.pack(pady=80)

        #  #### Bouton Deconnecter
        # btn_deconnecte = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="#C0C0C0").place(x=500,y=20)

        #  ###### Contenu
        #         # Versement
        # lbl_num_versement = Label(frame, text="blablablabla :", font=("goudy old style", 20), bg="white").place(x=50, y=220)
        # self.entre_versement =  Entry(frame, font=("goudy old style", 20), bg="lightyellow")    
        # self.entre_versement.place(x=250, y=220, width=250)

