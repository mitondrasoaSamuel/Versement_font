import tkinter as tk
from tkinter import *
import requests as req
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the system path
sys.path.append(parent_dir)

from configAPI import API


class Audit:

    def plot_pie_chart(self, frame):
        # Data for the pie chart
        labels = ["AJOUT", "MODIFICATION", "SUPPRESSION"]
        total = self.get_total()
        somme = sum([total["add"], total["edit"], total["delete"]])
        
        sizes = [total["add"]*100/somme, total["edit"]*100/somme, total["delete"]*100/somme]

        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot the pie chart
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')

        # Embed the pie chart into Tkinter window
        self.canvas = FigureCanvasTkAgg(fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
    
    def toggle_graph(self, frame):
        if self.display_graph["text"] == "Afficher Graphe":
            self.plot_pie_chart(frame)
            self.display_graph.config(text="Masquer Graphe")
        else:
            self.canvas.get_tk_widget().pack_forget()
            self.display_graph.config(text="Afficher Graphe") 
        
    ### Recuperer liste des clients 
    def get_total(self):
        #### list audit
        data = req.get(API.AUDIT_URL_TOTAL, headers=API.HEADER).json()
       
        return data
        
    def fetch_audit(self):
        try:
            # Faire la requête à l'API
            response = req.get(API.AUDIT_URL, headers=API.HEADER)
            response.raise_for_status()  # Vérifier s'il y a des erreurs HTTP
            data = response.json()  # Convertir la réponse en JSON
            
            # Vérifier si les données retournées sont une liste de dictionnaires
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                # Effacer la liste actuelle avant d'ajouter de nouvelles données
                for row in self.audit_liste.get_children():
                    self.audit_liste.delete(row)

                # Ajouter les nouvelles données à la liste
                for item in data:
                    self.audit_liste.insert('', 'end', values=(item.get('action', ''),
                                                               item.get('date_operation', ''),
                                                               item.get('num_versement', ''),
                                                               item.get('num_compte', ''),
                                                               item.get('nom_prenoms_client', ''),
                                                               item.get('montant_ancien', ''),
                                                               item.get('montant_nouveau', ''),
                                                               item.get('nom_email_user', '')))
            else:
                print("")
        except Exception as e:
            print("")

    def toggle_btn(self):
        self.display_graph.place(x=100, y=480, height=40, width=150)
        self.hide_graph.place(x=100, y=480, height=40, width=150)
        
    def __init__(self, frame):

            ##### Liste Client
                  #3 Creation  de frame
        listeFrame = Frame(frame, bd=3, relief=RIDGE)
        listeFrame.place(x=80, y=10, height=450, width=1100)

        scroll_x = Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y = Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.audit_liste = ttk.Treeview(listeFrame , columns=("action", "date_operation", "num_versement", "num_compte", "nom_client", "montant_ancien", "montant_nouveau", "mail_client"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        scroll_x.config(command=self.audit_liste.xview)
        scroll_y.config(command=self.audit_liste.yview)
        
        self.audit_liste.heading("num_compte", text="N° Compte")
        self.audit_liste.heading("nom_client", text="Client")
        self.audit_liste.heading("mail_client", text="Utilisateur")
        self.audit_liste.heading("action", text="Type Action")
        self.audit_liste.heading("num_versement", text="N° Versement")
        self.audit_liste.heading("montant_ancien", text="Montant ancien")
        self.audit_liste.heading("montant_nouveau", text="Montant nouveau")   
        self.audit_liste.heading("date_operation", text="Date operation")
        self.audit_liste["show"]="headings"
        self.fetch_audit()
        self.audit_liste.pack(fill=BOTH, expand=1)

        self.display_graph = Button(frame, text="Afficher Graphe", font=("Arial", 14, "bold"), cursor="hand2", bg="gray", state="normal", command=lambda: self.toggle_graph(frame))
        self.display_graph.place(x=80, y=480, height=40, width=180)
        
        total = self.get_total()
        if(total and "add" in total): 
            lbl_ajout= Label(frame, text="TOTAL AJOUT : " + str(total["add"]), font=("Arial", 12, "bold"))
            lbl_ajout.place(x=350, y=490)
            lbl_modif = Label(frame, text="TOTAL MODIFICATION : " + str(total["edit"]), font=("Arial", 12, "bold"))
            lbl_modif.place(x=650, y=490)
            lbl_suppr = Label(frame, text="TOTAL SUPPRESSION : " + str(total["delete"]), font=("Arial", 12, "bold"))
            lbl_suppr.place(x=950, y=490)    
        else: 
            lbl_ajout= Label(frame, text="TOTAL AJOUT : 0", font=("Arial", 12, "bold"))
            lbl_ajout.place(x=350, y=490)
            lbl_modif = Label(frame, text="TOTAL MODIFICATION : 0", font=("Arial", 12, "bold"))
            lbl_modif.place(x=650, y=490)
            lbl_suppr = Label(frame, text="TOTAL SUPPRESSION : 0", font=("Arial", 12, "bold"))
            lbl_suppr.place(x=950, y=490)
