from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time
## dans le fichier versment on import la classe accueil
from audit import Audit
from client import Client
from utilisateur import Utilisateur


class admin:
    def __init__(self, root):
        self.root = root 
        self.root.title("Administrateur")
        self.root.geometry("1300x650")
        self.root.config(bg="#f1f1fc")
        # self.root.resizable(False, False)

        ### Fonction Menu
        def switch(indicator_lb, page):

            for child in options_fm.winfo_children():
                if isinstance(child, tk.Label):
                    child['bg'] = 'SystemButtonFace'

            indicator_lb['bg'] = "#1c1b1b"

            for fm in main_fm.winfo_children():
                fm.destroy()
                self.root.update()

            page()


        ## Frame ---------------------------------------------------------------------------------
        options_fm = tk.Frame(self.root, bd=2, bg="#f1f1fc")
            #-------------------
                ### Menu audit
        audit_btn = tk.Button(options_fm, text="AUDIT VERSEMENT", font=("Arial", 16, "bold"), bd=0, fg="#1c1b1b", activeforeground="#0097e8"
                             , command=lambda: switch(indicator_lb=aucit_indicator_lb, page=audit_page), cursor="hand2"
                             )
        audit_btn.place(x=0, y=0, width=330, height=70)

                    ## indicateur
        aucit_indicator_lb = tk.Label(options_fm, bg="#1c1b1b")
        aucit_indicator_lb.place(x=2, y=70, width=330, height=5)

                ### Menu client
        client_btn = tk.Button(options_fm, text="CLIENT", font=("Arial", 16, "bold"), bd=0, fg="#1c1b1b", activeforeground="#0097e8"
                                  , command=lambda: switch(indicator_lb=client_indicator_lb, page=client_page), cursor="hand2"
                                  )
        client_btn.place(x=350, y=0, width=330, height=70)

                    ### indicateur
        client_indicator_lb = tk.Label(options_fm)
        client_indicator_lb.place(x=352, y=70, width=330, height=5) 

                ### Menu utilisateur
        utilisateur_btn = tk.Button(options_fm, text="UTILISATEUR", font=("Arial", 16, "bold"), bd=0, fg="#1c1b1b", cursor="hand2"
                                    , activeforeground="#0097e8", command=lambda: switch(indicator_lb=utilisateur_indicator_lb,page=utilisateur_page))
        utilisateur_btn.place(x=700, y=0, width=330, height=70)  

                ### indicateur
        utilisateur_indicator_lb = tk.Label(options_fm)
        utilisateur_indicator_lb.place(x=702, y=70, width=330, height=5)  
        
            #-------------------
        options_fm.pack(pady=5)

        options_fm.pack_propagate(True)
        options_fm.configure(width=1030, height=80)
        ## Pack Frame -----------------------------------------------------------------------------
    


        ### Page AUDIT
        def audit_page():
            audit_page_fm = tk.Frame(main_fm)

            Audit(audit_page_fm)

            audit_page_fm.pack(fill=tk.BOTH, expand=True)

        ### Page Client
        def client_page():
           
            client_page_fm = tk.Frame(main_fm)
 
        
            Client(client_page_fm)

            client_page_fm.pack(fill=tk.BOTH, expand=True)

        ### Page Utilisateur
        def utilisateur_page():
            utilisateur_page_fm = tk.Frame(main_fm)

            Utilisateur(utilisateur_page_fm)

            utilisateur_page_fm.pack(fill=tk.BOTH, expand=True)



        #### Frame Main        

        main_fm = tk.Frame(self.root)

        main_fm.pack(fill=tk.BOTH, expand=True)

        audit_page()


if __name__=="__main__":
    root = Tk()    
    obj = admin(root)
    root.mainloop()