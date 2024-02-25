import tkinter as tk
from tkinter import *

from tkinter import ttk

class Client:
    def __init__(self, frame):
        titre = Label(frame, text="LISTE DES CLIENTS", font=("Arial", 40, "bold"), bg="#C0C0C0").place(x=0, y=0, relwidth=1, height=100)


             ##### Liste Client
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=130, height=650, width=1080)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)


        self.versementliste = ttk.Treeview(listeFrame , columns=("num_compte", "nom_client", "prenom_client", "solde"), xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.versementliste.xview)
        
        self.versementliste.heading("num_compte", text="N° Compte")
        self.versementliste.heading("nom_client", text="Nom")
        self.versementliste.heading("prenom_client", text="Prenom")
        self.versementliste.heading("solde", text="Solde")


        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)


        ### Bouton Modifier

        self.modifier_btn = Button(frame, text="Modifier", font=("Arial", 20, "bold"), cursor="hand2", bg="green", state="normal")
        self.modifier_btn.place(x=500, y=810, height=40, width=150)

        ### Bouton Supprimer

        self.supprimer_btn = Button(frame, text="Supprimer", font=("Arial", 20, "bold"), cursor="hand2", bg="#de3232", state="normal")
        self.supprimer_btn.place(x=800, y=810, height=40, width=150)

        