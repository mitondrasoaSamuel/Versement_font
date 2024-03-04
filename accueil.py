import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from configAPI import API
import requests as req

class Accueil:
    def fetch_client_data(self):
        return req.get(API.CLIENT_URL, headers=API.HEADER).json()
    
    def generate_bar_chart(self, frame):
        # Fetch client data
        client_data = self.fetch_client_data()

        # Extract data for plotting
        labels = [client["nom"] for client in client_data]
        values = [client["solde"] for client in client_data]

        # Create bar chart
        fig, ax = plt.subplots()
        ax.bar(labels, values)

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=30, ha="right")

        # Set labels and title
        ax.set_xlabel("Clients")
        ax.set_ylabel("Solde")
        ax.set_title("Solde par Client")

        # Embed the plot into Tkinter window
        chart_canvas = FigureCanvasTkAgg(fig, master=frame)
        chart_canvas.draw()
        chart_canvas.get_tk_widget().pack()
        
    def __init__(self, frame):
        accueil_page_lb = tk.Label(frame, text="GESTION VERSEMENT BANCAIRES", font=("Arial", 16, "bold"), fg="#1c1b1b")
        accueil_page_lb.pack(pady=20)

        self.generate_bar_chart(frame)
        #  #### Bouton Deconnecter
        # btn_deconnecte = Button(frame, text="Ajouter", font=("times new roman", 20, "bold"), cursor="hand2", bg="#C0C0C0").place(x=500,y=20)

        #  ###### Contenu
        #         # Versement
        # lbl_num_versement = Label(frame, text="blablablabla :", font=("goudy old style", 20), bg="white").place(x=50, y=220)
        # self.entre_versement =  Entry(frame, font=("goudy old style", 20), bg="lightyellow")    
        # self.entre_versement.place(x=250, y=220, width=250)

