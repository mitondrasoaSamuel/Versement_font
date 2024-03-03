import tkinter as tk
from tkinter import *
from tkinter import ttk
from configAPI import API
import requests as req
from tkinter import messagebox
import random

class VersementFrame:
    
    def generer_numero_compte(self):
        numero_compte = ''.join([str(random.randint(1, 9)) for _ in range(8)])  # Vous pouvez ajuster la longueur du numéro de compte si nécessaire
        return numero_compte
    
    
    def reset_versement(self):
        self.entre_versement.config(state="normal")
        self.entre_versement.insert(0, self.generer_numero_compte()) 
        self.entre_cheque.delete(0, tk.END)
        self.entre_montant.delete(0, tk.END)

    def fetch_clients(self):
        return req.get(API.CLIENT_URL, headers=API.HEADER).json()
        
    def get_versement(self):
        return req.get(API.VERSEMENT_URL, headers=API.HEADER).json()
    
    ### Recuperer liste des clients 
    def fetch_versement(self):
        #### list versement
        data = req.get(API.VERSEMENT_URL, headers=API.HEADER).json()
      
        for row in self.versementliste.get_children():
           self.versementliste.delete(row)
        
        for item in data: 
           self.versementliste.insert('', 'end', values=(item['num_versement'], item['client']['num_compte'], item['num_cheque'], item['montant']))
   
    def add_versement(self):
        selected_num_value = self.selected_num_compte.get() 
        selected_id = None
        
        for account in self.fetch_clients():
            if account["num_compte"] == selected_num_value:
                selected_id = account["id"]
                break
        
        if selected_id is not None:
            dataVersement = {
                "num_versement": self.entre_versement.get(),
                "num_cheque": self.entre_cheque.get(),
                "client_id": int(selected_id), ## client  
                "montant": float(self.entre_montant.get())
            }
            
            res = req.post(API.VERSEMENT_URL, dataVersement, headers=API.HEADER)

            if(res):
                self.fetch_versement()
                self.reset_versement()
                messagebox.showinfo("AJOUT VERSEMENT", "Ajoute avec succes")
            else:
                messagebox.showerror("AJOUT VERSEMENT", "Erreur de l'ajout: "+str(res["message"]))

    def get_versement_id(self):
        selected_id = None
        for num_versement in self.get_versement():
            if num_versement["num_versement"] == self.entre_versement.get():
                selected_id = num_versement["id"]
                break
        
        return selected_id
    
    def update_versement(self):
        selected_num_value = self.selected_num_compte.get() 
        selected_id = None
        
        for account in self.fetch_clients():
            if account["num_compte"] == selected_num_value:
                selected_id = account["id"]
                break
        
        if selected_id is not None:
            
            dataVersement = {
                "num_versement": self.entre_versement.get(),
                "num_cheque": self.entre_cheque.get(),
                "client_id": int(selected_id), ## client  
                "montant": float(self.entre_montant.get())
            }

            res = req.put(API.VERSEMENT_URL+"/"+str(self.get_versement_id()), dataVersement, headers=API.HEADER)

            if(res):
                messagebox.showinfo("MODIFICATION VERSEMENT", "Modification avec succes")
                self.fetch_versement()
                self.reset_versement()

            else:
                messagebox.showerror("MODIFICATION VERSEMENT", "Erreur de modification")
    
    def delete_versement(self): 
        res = req.delete(API.VERSEMENT_URL+"/"+str(self.get_versement_id()), headers=API.HEADER).json()

        if(res):
            messagebox.showinfo("SUPPRESSION VERSEMENT", "Suppression avec succes")
            self.fetch_versement()
            self.reset_versement()

        else:
            messagebox.showerror("SUPPRESSION VERSEMENT", "Erreur de Suppression")
    
    def get_selected_items(self, _):
        selected_items = self.versementliste.selection()  # Obtenir les ID des éléments sélectionnés
        # reinitialiser les champs
        self.reset_versement()
        self.entre_versement.delete(0, tk.END) 
        self.entre_versement.config(state="normal")

        for item_id in selected_items:
            item = self.versementliste.item(item_id)  # Obtenir les détails de l'élément
            
            self.entre_versement.insert(0, item["values"][0])
            self.selected_num_compte.set(item["values"][1])
            self.entre_cheque.insert(0, item["values"][2])
            self.entre_montant.insert(0, item["values"][3])
        
        self.entre_versement.config(state="readonly")
        
    def __init__(self, frame):

        ###### Contenu
        # Versement

        lbl_num_versement = Label(frame, text="N° Versement :", font=("Arial", 14)).place(x=50, y=25)

        self.entre_versement =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_versement.insert(0, self.generer_numero_compte())  # Insérer le numéro de compte aléatoire
        self.entre_versement.config(state="readonly")
        self.entre_versement.place(x=250, y=25, width=250)
        
                # Num_compte
        clients = self.fetch_clients()
        num_comptes = [account["num_compte"] for account in clients]
        
        lbl_num_compte = Label(frame, text="N° Compte :", font=("goudy old style", 10)).place(x=50, y=85)
        self.selected_num_compte = tk.StringVar(frame)
        self.selected_num_compte.set(num_comptes[0])  # Set the default selected num_compte
            
        option_menu = tk.OptionMenu(frame, self.selected_num_compte, *num_comptes)
        option_menu.place(x=250, y=85, width=250)


                # Num_cheque
        lbl_num_cheque = Label(frame, text="N° Chèque :", font=("Arial", 14)).place(x=900, y=25)
        self.entre_cheque =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_cheque.place(x=1020, y=25, width=250)
        
                # Montant
        lbl_montant = Label(frame, text="Montant :", font=("Arial", 14)).place(x=928, y=85)

        self.entre_montant =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_montant.place(x=1020, y=85, width=250)

        ###  Bouton

        #         ## Importation de l'image
        # img = ImageTk.PhotImage(Image.open("")) 
                ## Ajouter
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal"
                                , command=self.add_versement
                                )
        self.ajout_btn.place(x=330, y=150, height=40, width=150)

                ###  Bouton 
                ## Supprimer
        
        self.supprimer_btn = Button(frame, text="Supprimer", font=("times new roman", 20, "bold"), cursor="hand2", bg="red", state="normal"
                                    , command=self.delete_versement
                                    )
        self.supprimer_btn.place(x=630, y=150, height=40, width=150)


        ###  Bouton 
                ## Modifier
        
        self.modifier_btn = Button(frame, text="Modifier", font=("times new roman", 20, "bold"), cursor="hand2", bg="gray", state="normal"
                                   , command=self.update_versement
                                   )
        self.modifier_btn.place(x=830, y=150, height=40, width=150)


        ###  Bouton 
                ## Reinitialiser
        
        self.reinitialiser_btn = Button(frame, text="Reinitialiser", font=("times new roman", 20, "bold"), cursor="hand2", state="normal"
                                        , command=self.reset_versement
                                        )
        self.reinitialiser_btn.place(x=1000, y=150, height=40, width=160)


             ##### Liste Versement
                    #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=180, y=220, height=650, width=1080)

        scroll_x = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_x.pack(side=RIGHT, fill=Y)


        self.versementliste = ttk.Treeview(listeFrame , columns=("num_vers", "num_compte", "num_cheque", "montant"), xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.versementliste.xview)

        self.versementliste.heading("num_vers", text="N° Versement")
        self.versementliste.heading("num_compte", text="N° Compte")
        self.versementliste.heading("num_cheque", text="N° Chèque")
        self.versementliste.heading("montant", text="Montant")


        self.fetch_versement()
        self.versementliste.bind('<<TreeviewSelect>>', self.get_selected_items) ## recuperer les elements selectionee dans la liste
        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)


             

