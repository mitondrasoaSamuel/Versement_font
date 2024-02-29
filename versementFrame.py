import tkinter as tk
from tkinter import *
from tkinter import ttk
from configAPI import API
import requests as req
from tkinter import messagebox

class VersementFrame:
    
#     def reset_versement(self):
#         self.entre_versement.config(state="normal")
#         self.entre_compte.insert(0, self.generer_numero_compte()) 
#         self.entre_cheque.delete(0, tk.END)
#         self.entre_montant.delete(0, tk.END)
    
    ### Recuperer liste des clients 
    def fetch_versement(self):
        #### list versement
        data = req.get(API.VERSEMENT_URL, headers=API.HEADER).json()
      
        for row in self.versementliste.get_children():
           self.versementliste.delete(row)
        
        for item in data: 
           self.versementliste.insert('', 'end', values=(item['num_versement'], item['num_cheque'], item['client_id'], item['montant']))

#     def add_versement(self):
#         dataVersement = {
#             'num_versement': self.entre_versement.get(),
#             'num_cheque': self.entre_cheque.get(),
#             'client_id': self.entre_compte.get(),
#             'montant': float(self.entre_montant.get())
#         }

#         res = req.post(API.CLIENT_URL, dataVersement,headers=self.HEADER).json()

#         if(res):
#             self.fetch_versement()
#             self.reset_versement()
#             messagebox.showinfo("AJOUT VERSEMENT", "Ajoute avec succes")
#         else:
#             messagebox.showerror("AJOUT VERSEMENT", "Erreur de l'ajout")
    


    def __init__(self, frame):

         ###### Contenu
                # Versement

        lbl_num_versement = Label(frame, text="N° Versement :", font=("Arial", 14), bg="white").place(x=50, y=25)

        self.entre_versement =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_versement.place(x=250, y=25, width=250)
        

        # Num_compte
        lbl_num_compte = Label(frame, text="N° Compte :", font=("Arial", 14), bg="white").place(x=50, y=85)

        # clients = API.get_clients()
        # num_comptes = [account["num_compte"] for account in clients]

        self.entre_compte =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_compte.place(x=250, y=85, width=250)
               

                # Num_cheque
        lbl_num_cheque = Label(frame, text="N° Chèque :", font=("Arial", 14), bg="white").place(x=900, y=25)

        self.entre_cheque =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_cheque.place(x=1020, y=25, width=250)
                # Montant
        lbl_montant = Label(frame, text="Montant :", font=("Arial", 14), bg="white").place(x=928, y=85)

        self.entre_montant =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_montant.place(x=1020, y=85, width=250)



        
        ###  Bouton

        #         ## Importation de l'image
        # img = ImageTk.PhotImage(Image.open("")) 
                ## Ajouter
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal"
                                # , command=self.add_versement
                                )
        self.ajout_btn.place(x=330, y=150, height=40, width=150)

                ###  Bouton 
                ## Supprimer
        
        self.supprimer_btn = Button(frame, text="Supprimer", font=("times new roman", 20, "bold"), cursor="hand2", bg="red", state="normal"
                                #     , command=self.delete_client
                                    )
        self.supprimer_btn.place(x=630, y=150, height=40, width=150)


        ###  Bouton 
                ## Modifier
        
        self.modifier_btn = Button(frame, text="Modifier", font=("times new roman", 20, "bold"), cursor="hand2", bg="gray", state="normal"
                                #    , command=self.update_client
                                   )
        self.modifier_btn.place(x=830, y=150, height=40, width=150)


        ###  Bouton 
                ## Reinitialiser
        
        self.reinitialiser_btn = Button(frame, text="Rieinitialiser", font=("times new roman", 20, "bold"), cursor="hand2", bg="white", state="normal"
                                        # , command=self.reset_versement
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
        # self.versementliste.bind('<<TreeviewSelect>>', self.get_selected_items) ## recuperer les elements selectionee dans la liste
        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)


             

