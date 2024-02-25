import tkinter as tk
from tkinter import *
from tkinter import ttk
from configAPI import API

class VersementFrame:
    def __init__(self, frame):

         ###### Contenu
                # Versement

        lbl_num_versement = Label(frame, text="N° Versement :", font=("Arial", 14), bg="white").place(x=50, y=25)

        self.entre_versement =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_versement.place(x=250, y=25, width=250)
        

        # Num_compte
        lbl_num_compte = Label(frame, text="N° Compte :", font=("Arial", 14), bg="white").place(x=50, y=85)

        clients = API.get_clients()
        num_comptes = [account["num_compte"] for account in clients]

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
        
        self.ajout_btn = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=630, y=150, height=40, width=150)

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


        self.versementliste["show"]="headings"

        self.versementliste.pack(fill=BOTH, expand=1)


             

