import tkinter as tk
from tkinter import *
import requests as req
from tkinter import ttk

import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the system path
sys.path.append(parent_dir)

from configAPI import API


class Audit:

    ### Gerer utilisateur connecte 
    TOKEN = "1|Alquur2FPriNJ7mPrXxNSzswP4yDGGXRHBYKr4Jbc3d7af61"
    HEADER = {"Authorization" : f"Bearer {TOKEN}"}


    ### Recuperer liste des clients 
    def fetch_audit(self):
        #### list audit
        data = req.get(API.CLIENT_URL, headers=self.HEADER).json()
        print(data)
        for row in self.audit_liste.get_children():
           self.audit_liste.delete(row)
           
        
        for item in data: 
           self.audit_liste.insert('', 'end', values=(item['num_compte'], item['nom_prenoms_client'], item['nom_email_user'], item['action'],item['num_versement'], item['montant_ancien'], item['montant_nouveau'], item['date_operation']))

    def __init__(self, frame):

             ##### Liste Client
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=130, height=650, width=1080)


        
        scroll_y = Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_y.pack(side=BOTTOM, fill=X)



        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)





        self.audit_liste = ttk.Treeview(listeFrame , columns=("num_compte", "nom_client", "mail_client", "action", "num_versement", "montant_ancien", "montant_nouveau", "date_operation"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.audit_liste.xview)
        scroll_y.config(command=self.audit_liste.yview)
        
        self.audit_liste.heading("num_compte", text="N° Compte")
        self.audit_liste.heading("nom_client", text="Nom")
        self.audit_liste.heading("mail_client", text="Email")
        self.audit_liste.heading("action", text="Action")
        self.audit_liste.heading("num_versement", text="N° Versment")
        self.audit_liste.heading("montant_ancien", text="Montant ancien")
        self.audit_liste.heading("montant_nouveau", text="Montant nouveau")   
        self.audit_liste.heading("date_operation", text="Date operation")
        
        


        self.audit_liste["show"]="headings"
        self.fetch_audit()
        self.audit_liste.pack(fill=BOTH, expand=1)


        ### Bouton Modifier

        self.modifier_btn = Button(frame, text="Modifier", font=("Arial", 20, "bold"), cursor="hand2", bg="green", state="normal")
        self.modifier_btn.place(x=500, y=810, height=40, width=150)

        ### Bouton Supprimer

        self.supprimer_btn = Button(frame, text="Supprimer", font=("Arial", 20, "bold"), cursor="hand2", bg="#de3232", state="normal")
        self.supprimer_btn.place(x=800, y=810, height=40, width=150)