import tkinter as tk
from tkinter import *
from configAPI import API
from tkinter import ttk
import requests as req
import random
from tkinter import messagebox

class Client:

    def reset_client(self):
        self.entre_compte.config(state="normal")
        self.entre_compte.insert(0, self.generer_numero_compte()) 
        self.entre_nom_client.delete(0, tk.END)
        self.entre_prenoms_client.delete(0, tk.END)
        self.entre_solde.delete(0, tk.END)
    
    ### Recuperer liste des clients 
    def fetch_client(self):
        #### list versement
        data = req.get(API.CLIENT_URL, headers=API.HEADER).json()

        for row in self.versementliste.get_children():
           self.versementliste.delete(row)
        
        for item in data: 
           self.versementliste.insert('', 'end', values=(item['num_compte'], item['nom'], item['prenoms'], item['solde']))

    def add_client(self):
        dataClient = {
            'num_compte': self.entre_compte.get(),
            'nom': self.entre_nom_client.get(),
            'prenoms': self.entre_prenoms_client.get(),
            'solde': float(self.entre_solde.get())
        }

        res = req.post(API.CLIENT_URL, dataClient,headers=API.HEADER)

        if(res.json()):
            self.fetch_client()
            self.reset_client()
            messagebox.showinfo("AJOUT CLIENT", "Ajoute avec succes")
        else:
            messagebox.showerror("AJOUT CLIENT", "Erreur de l'ajout")
  
    def get_client_id(self):
        selected_id = None
        for num_compte in API.get_clients():
            if num_compte["num_compte"] == self.entre_compte.get():
                selected_id = num_compte["id"]
                break
        
        return selected_id

    def update_client(self):
        dataClient = {
            'num_compte': self.entre_compte.get(),
            'nom': self.entre_nom_client.get(),
            'prenoms': self.entre_prenoms_client.get(),
            'solde': float(self.entre_solde.get())
        }

        if self.get_client_id() is not None:
            res = req.put(API.CLIENT_URL+"/"+str(self.get_client_id()), dataClient,headers=API.HEADER)
        
            if(res.json()):
                messagebox.showinfo("MODIFICATION CLIENT", "Modification avec succes")
                self.fetch_client()
                self.reset_client()

            else:
                messagebox.showerror("MODIFICATION CLIENT", "Erreur de modification")
        else:
            messagebox.showerror("MODIFICATION CLIENT", "ID Client introuvable")
    
    def delete_client(self):
        res = req.delete(API.CLIENT_URL+"/"+str(self.get_client_id()), headers=API.HEADER)

        if(res.json()):
            messagebox.showinfo("SUPPRESSION CLIENT", "Suppression avec succes")
            self.fetch_client()
            self.reset_client()

        else:
            messagebox.showerror("SUPPRESSION CLIENT", "Erreur de suppression")

    def generer_numero_compte(self):
        numero_compte = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # Vous pouvez ajuster la longueur du numéro de compte si nécessaire
        return numero_compte
    
    def get_selected_items(self, _):
        selected_items = self.versementliste.selection()  # Obtenir les ID des éléments sélectionnés
        # reinitialiser les champs
        self.reset_client()
        self.entre_compte.delete(0, tk.END) 
        self.entre_compte.config(state="normal")

        for item_id in selected_items:
            item = self.versementliste.item(item_id)  # Obtenir les détails de l'élément
            
            self.entre_compte.insert(0, item["values"][0])
            self.entre_nom_client.insert(0, item["values"][1])
            self.entre_prenoms_client.insert(0, item["values"][2])
            self.entre_solde.insert(0, item["values"][3])
        
        self.entre_compte.config(state="readonly")

    def __init__(self, frame):

         ###### Contenu
                # Nom Client
        
        lbl_nom_client = Label(frame, text="Nom :", font=("Arial", 14), bg="white").place(x=50, y=25)

        self.entre_nom_client =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_nom_client.place(x=180, y=25, width=250)

                ## Prenom
        lbl_prenom_client = Label(frame, text="Prenom  :", font=("Arial", 14), bg="white").place(x=50, y=85)

        self.entre_prenoms_client =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_prenoms_client.place(x=250, y=85, width=250)
        

        # Num_compte
        lbl_num_compte = Label(frame, text="N° Compte :", font=("Arial", 14), bg="white").place(x=880, y=25)

        self.entre_compte =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_compte.insert(0, self.generer_numero_compte())  # Insérer le numéro de compte aléatoire
        self.entre_compte.config(state="readonly")
        self.entre_compte.place(x=1080, y=25, width=250)
               

                # solde
        lbl_solde = Label(frame, text="Solde :", font=("Arial", 14), bg="white").place(x=880, y=85)

        self.entre_solde =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_solde.place(x=1000, y=85, width=250)
      

        ###  Bouton 
                ## Ajouter
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal", command=self.add_client)
        self.ajout_btn.place(x=330, y=150, height=40, width=150)


        ###  Bouton 
                ## Supprimer
        
        self.supprimer_btn = Button(frame, text="Supprimer", font=("times new roman", 20, "bold"), cursor="hand2", bg="red", state="normal", command=self.delete_client)
        self.supprimer_btn.place(x=630, y=150, height=40, width=150)


        ###  Bouton 
                ## Modifier
        
        self.modifier_btn = Button(frame, text="Modifier", font=("times new roman", 20, "bold"), cursor="hand2", bg="gray", state="normal", command=self.update_client)
        self.modifier_btn.place(x=830, y=150, height=40, width=150)


        ###  Bouton 
                ## Reinitialiser
        
        self.reinitialiser_btn = Button(frame, text="Rieinitialiser", font=("times new roman", 20, "bold"), cursor="hand2", bg="white", state="normal", command=self.reset_client)
        self.reinitialiser_btn.place(x=1000, y=150, height=40, width=160)

             ##### Liste Versement
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=200, height=650, width=1080)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)


        self.versementliste = ttk.Treeview(listeFrame , columns=("num_compte", "nom_client", "prenom", "solde"), xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.versementliste.xview)

        self.versementliste.heading("nom_client", text="Nom Client")
        self.versementliste.heading("prenom", text="Prenoms Client")
        self.versementliste.heading("num_compte", text="N° Compte")
        self.versementliste.heading("solde", text="Solde")

        self.fetch_client()
        self.versementliste.bind('<<TreeviewSelect>>', self.get_selected_items) ## recuperer les elements selectionee dans la liste

        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)


             

