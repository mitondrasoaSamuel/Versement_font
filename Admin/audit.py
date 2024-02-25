import tkinter as tk
from tkinter import *

from tkinter import ttk

class Audit:
    def __init__(self, frame):

         ###### Contenu
                # Nom Client
        
        lbl_nom_client = Label(frame, text="Audittttttt :", font=("Arial", 14), bg="white").place(x=50, y=25)

        self.entre_nom_colient =  Entry(frame, font=("Arial", 14), bg="lightyellow")    
        self.entre_nom_colient.place(x=180, y=25, width=250)