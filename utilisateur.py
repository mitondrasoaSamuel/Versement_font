from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time

class utilisateur:
    def __init__(self, root):
        self.root = root 
        self.root.title("Utilisateur")
        self.root.geometry("1400x1000")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        ### Fonction Menu
        def switch(indicator_lb, page):

            for child in options_fm.winfo_children():
                if isinstance(child, tk.Label):
                    child['bg'] = 'SystemButtonFace'

            indicator_lb['bg'] = "#0097e8"

            for fm in main_fm.winfo_children():
                fm.destroy()
                self.root.update()

            page()

        ### Frame 
        options_fm = tk.Frame(self.root)

            ### Menu Accueil
        accueil_btn = tk.Button(options_fm, text="Accueil", font=("Arial", 20, "bold"), bd=0, fg="#0097e8", activeforeground="#0097e8", command=lambda: switch(indicator_lb=accueil_indicator_lb, page=accueil_page))
        accueil_btn.place(x=0, y=0, width=330, height=70)   
                    ## indicateur
        accueil_indicator_lb = tk.Label(options_fm, bg="#0097e8")
        accueil_indicator_lb.place(x=2, y=70, width=330, height=5)



            ### Menu Versement
        versement_btn = tk.Button(options_fm, text="Versement", font=("Arial", 20, "bold"), bd=0, fg="#0097e8", activeforeground="#0097e8", command=lambda: switch(indicator_lb=versement_indicator_lb, page=versement_page))
        versement_btn.place(x=350, y=0, width=330, height=70) 
                    ### indicateur
        versement_indicator_lb = tk.Label(options_fm)
        versement_indicator_lb.place(x=352, y=70, width=330, height=5)     



            ### Menu Client
        client_btn = tk.Button(options_fm, text="Client", font=("Arial", 20, "bold"), bd=0, fg="#0097e8", activeforeground="#0097e8", command=lambda: switch(indicator_lb=client_indicator_lb,page=client_page))
        client_btn.place(x=700, y=0, width=330, height=70)     

                        ### client
        client_indicator_lb = tk.Label(options_fm)
        client_indicator_lb.place(x=702, y=70, width=330, height=5)      

        ### Pack frame
        options_fm.pack(pady=5)

        options_fm.pack_propagate(False)
        options_fm.configure(width=1030, height=80)
        ### --------------------------------------

        ### Page accueil
        def accueil_page():
            accueil_page_fm = tk.Frame(main_fm)

            accueil_page_lb = tk.Label(accueil_page_fm, text="PAGE D'ACCUEIL", font=("Arial", 30), fg="#0097e8")
            accueil_page_lb.pack(pady=80)

            accueil_page_fm.pack(fill=tk.BOTH, expand=True)

        ### Page Versment
        def versement_page():
            versement_page_fm = tk.Frame(main_fm)

            versement_page_lb = tk.Label(versement_page_fm, text="PAGE VERSEMENT", font=("Arial", 30), fg="#0097e8")
            versement_page_lb.pack(pady=80)

            versement_page_fm.pack(fill=tk.BOTH, expand=True)

        ### Page Client
        def client_page():
            client_page_fm = tk.Frame(main_fm)

            client_page_lb = tk.Label(client_page_fm, text="PAGE CLIENT", font=("Arial", 30), fg="#0097e8")
            client_page_lb.pack(pady=80)

            client_page_fm.pack(fill=tk.BOTH, expand=True)



        #### Frame Main        

        main_fm = tk.Frame(self.root)

        main_fm.pack(fill=tk.BOTH, expand=True)

        accueil_page()

if __name__=="__main__":
    root = Tk()    
    obj = utilisateur(root)
    root.mainloop()