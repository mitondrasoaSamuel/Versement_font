import tkinter as tk
from tkinter import *
import requests as req

import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the system path
sys.path.append(parent_dir)

from configAPI import API
from tkinter import ttk

class Client:
    def fetch_client(self):
        #### list versement
        data = req.get(API.CLIENT_URL, headers=API.HEADER).json()

        for row in self.versementliste.get_children():
           self.versementliste.delete(row)
        
        for item in data: 
           self.versementliste.insert('', 'end', values=(item['num_compte'], item['nom'], item['prenoms'], item['solde']))

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
        self.fetch_client()
        self.versementliste.pack(fill=BOTH, expand=1)


        
        