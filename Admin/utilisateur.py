import tkinter as tk
from tkinter import *
import requests as req
from tkinter import ttk
from tkinter import messagebox

import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the system path
sys.path.append(parent_dir)

from configAPI import API

class Utilisateur:
    def fetch_user(self):
        [self.versementliste.delete(row) for row in self.versementliste.get_children()]
        data = req.get(API.USER_URL, headers=API.HEADER).json()
        [self.versementliste.insert('', 'end', values=(item.get('name', ''), item.get('email', ''))) for item in data]
    
    def reset_user(self):
        self.entre_nom.delete(0, tk.END)
        self.entre_email.delete(0, tk.END)
        self.entre_mdp.delete(0, tk.END)
        
    def add_user(self):
        dataUser = {
            'name': self.entre_nom.get(),
            'email': self.entre_email.get(),
            'password': self.entre_mdp.get()
        }

        res = req.post(API.USER_REGISTER, dataUser, headers=API.HEADER).json()

        if(res):
            self.fetch_user()
            self.reset_user()
            messagebox.showinfo("AJOUT UTILISATEUR", "Ajoute avec succes")
        else:
            messagebox.showerror("AJOUT UTILISATEUR", "Erreur de l'ajout")
     
    def __init__(self, frame):

          ###### Contenu
                # Nom

        lbl_nom = Label(frame, text="Pseudo :", font=("Arial", 14), bg="white").place(x=110, y=25)

        self.entre_nom =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_nom.place(x=180, y=25, width=250)
        

        # Mail
        lbl_mail = Label(frame, text="Email :", font=("Arial", 14), bg="white").place(x=500, y=25)

        self.entre_email =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_email.place(x=580, y=25, width=250)
               

                # Mot de passe
        lbl_mdp = Label(frame, text="Mot de passe :", font=("Arial", 14), bg="white").place(x=900, y=25)

        self.entre_mdp =  Entry(frame, font=("Arial", 14), bg="lightyellow", show="*")    
        self.entre_mdp.place(x=1040, y=25, width=250)
        

        ###  Bouton 
                ## Ajouter
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal", command=self.add_user)
        self.ajout_btn.place(x=630, y=100, height=40, width=150)

             ##### Liste Utilisateur
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=180, height=650, width=1080)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)


        self.versementliste = ttk.Treeview(listeFrame , columns=("nom_client", "mail"), xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.versementliste.xview)

        self.versementliste.heading("nom_client", text="Pseudo")
        self.versementliste.heading("mail", text="Email")
        self.versementliste["show"]="headings"

        self.fetch_user()
        
        self.versementliste.pack(fill=BOTH, expand=1)

