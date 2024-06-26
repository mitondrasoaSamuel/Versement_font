import tkinter as tk
from tkinter import *
from configAPI import API
from tkinter import ttk
import requests as req
import random
from tkinter import messagebox

class Client:
    ### Gerer utilisateur connecte 
    HEADER = API.HEADER
    
    def cancel_action(self):
        self.show_buttons_add_reset()
        self.reset_client()
        
    def reset_client(self):
        self.entre_compte.config(state="normal")
        self.entre_compte.insert(0, self.generer_numero_compte()) 
        self.entre_nom_client.delete(0, tk.END)
        self.entre_prenoms_client.delete(0, tk.END)
        self.entre_solde.delete(0, tk.END)
    
    ### Recuperer liste des clients 
    def fetch_client(self):
        #### list versement
        data = req.get(API.CLIENT_URL, headers=self.HEADER).json()

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

        res = req.post(API.CLIENT_URL, dataClient,headers=self.HEADER).json()

        if(res):
            self.fetch_client()
            self.reset_client()
            messagebox.showinfo("AJOUT CLIENT", "Ajoute avec succes")
        else:
            messagebox.showerror("AJOUT CLIENT", "Erreur de l'ajout")
    
    def get_clients(self):
        return req.get(API.CLIENT_URL, headers=self.HEADER).json()
    
    def get_client_id(self):
        selected_id = None
        for num_compte in self.get_clients():
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
        
        res = req.put(API.CLIENT_URL+"/"+str(self.get_client_id()), dataClient,headers=self.HEADER).json()

        if(res):
            self.fetch_client()
            self.reset_client()
            messagebox.showinfo("MODIFICATION CLIENT", "Modification avec succes")
            
        else:
            messagebox.showerror("MODIFICATION CLIENT", "Erreur de modification")
        
        # Restore buttons to initial state after updating
        self.show_buttons_add_reset()
        
    def delete_client(self):
        res = req.delete(API.CLIENT_URL+"/"+str(self.get_client_id()), headers=self.HEADER).json()

        if(res):
            self.fetch_client()
            self.reset_client()
            messagebox.showinfo("SUPPRESSION CLIENT", "Suppression avec succes")
            
        else:
            messagebox.showerror("SUPPRESSION CLIENT", "Erreur de suppression")
            
        # Restore buttons to initial state after updating
        self.show_buttons_add_reset()
        
    def generer_numero_compte(self):
        numero_compte = ''.join([str(random.randint(1, 9)) for _ in range(8)])  # Vous pouvez ajuster la longueur du numéro de compte si nécessaire
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
        self.hide_buttons_edit_update()
        self.btn_cancel.place(x=560, y=110, height=40, width=150)

    def show_buttons_add_reset(self):
        # self.supprimer_btn.place_forget()
        # self.modifier_btn.place_forget()
        self.ajout_btn.config(text="Ajouter", command=self.add_client)
        self.reinitialiser_btn.config(text="Reinitialiser", command=self.reset_client)
    
    def hide_buttons_edit_update(self):
        self.ajout_btn.config(text="Modifier", command=self.update_client)
        self.reinitialiser_btn.config(text="Supprimer", command=self.delete_client)
       
    def __init__(self, frame):

        ###### Contenu
        
        # Num_compte
        lbl_num_compte = Label(frame, text="N° Compte :", font=("Arial", 14)).place(x=250, y=25)

        self.entre_compte =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_compte.insert(0, self.generer_numero_compte())  # Insérer le numéro de compte aléatoire
        self.entre_compte.config(state="readonly")
        self.entre_compte.place(x=400, y=25, width=250)
        
        # Nom Client
        
        lbl_nom_client = Label(frame, text="Nom :", font=("Arial", 14)).place(x=250, y=60)

        self.entre_nom_client =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_nom_client.place(x=400, y=60, width=250)


                ## Prenom
        lbl_prenom_client = Label(frame, text="Prenom  :", font=("Arial", 14)).place(x=800, y=25)

        self.entre_prenoms_client =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_prenoms_client.place(x=890, y=25, width=250)
        
                # solde
        lbl_solde = Label(frame, text="Solde :", font=("Arial", 14)).place(x=800, y=65)

        self.entre_solde =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_solde.place(x=890, y=65, width=250)
      

        ###  Bouton 
                ## Ajouter
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 14, "bold"), cursor="hand2", bg="green", state="normal", command=self.add_client)
        self.ajout_btn.place(x=990, y=110, height=40, width=150)

        ###  Bouton 
                ## Reinitialiser
        
        self.reinitialiser_btn = Button(frame, text="Reinitialiser", font=("times new roman", 20, "bold"), cursor="hand2", state="normal", command=self.reset_client)
        self.reinitialiser_btn.place(x=800, y=110, height=40, width=160)
        
        ###  Bouton 
                ## Supprimer
        
        # self.supprimer_btn = Button(frame, text="Supprimer", font=("times new roman", 14, "bold"), cursor="hand2", bg="red", state="normal", command=self.delete_client)
        # self.supprimer_btn.place(x=540, y=110, height=40, width=150)


        ###  Bouton 
                ## Modifier
        
        # self.modifier_btn = Button(frame, text="Modifier", font=("times new roman", 14, "bold"), cursor="hand2", bg="gray", state="normal", command=self.update_client)
        # self.modifier_btn.place(x=740, y=110, height=40, width=150)
        
        self.btn_cancel = Button(frame, text="Annuler", font=("times new roman", 14, "bold"), cursor="hand2", bg="red", state="normal", command=self.cancel_action)

        ##### Liste Versement
        #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=170, height=500, width=1080)

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


             

