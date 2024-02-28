import tkinter as tk
from tkinter import *

from tkinter import ttk

class Audit:
    def __init__(self, frame):

             ##### Liste Client
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=130, height=650, width=1080)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)


        self.audit_liste = ttk.Treeview(listeFrame , columns=("num_compte", "nom_client", "prenom_client", "montant", "action", "date_operation", "num_versement", "utilisateur"))

        scroll_x.config(command=self.audit_liste.xview)
        
        self.audit_liste.heading("num_compte", text="N° Compte")
        self.audit_liste.heading("nom_client", text="Nom")
        self.audit_liste.heading("prenom_client", text="Prenom")
        self.audit_liste.heading("montant", text="Montant ancien")
        self.audit_liste.heading("action", text="Action")
        self.audit_liste.heading("date_operation", text="Date operation")
        self.audit_liste.heading("num_versement", text="N° Versment")
        self.audit_liste.heading("utilisateur", text="Utilisateur")


        self.audit_liste["show"]="headings"
        # self.fetch_client()
        self.audit_liste.pack(fill=BOTH, expand=1)


        ### Bouton Modifier

        self.modifier_btn = Button(frame, text="Modifier", font=("Arial", 20, "bold"), cursor="hand2", bg="green", state="normal")
        self.modifier_btn.place(x=500, y=810, height=40, width=150)

        ### Bouton Supprimer

        self.supprimer_btn = Button(frame, text="Supprimer", font=("Arial", 20, "bold"), cursor="hand2", bg="#de3232", state="normal")
        self.supprimer_btn.place(x=800, y=810, height=40, width=150)