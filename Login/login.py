from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox
import requests as req
import tkinter as tk
import os
import sys

# import configAPI
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")  # Add parent directory to the path
from configAPI import API
from utilisateur import utilisateur as User

root = Tk()
root.title("Connexion")
root.geometry("400x300+450+200")
root.resizable(False, False)

def login():
    userData = {"email": entre_mail.get(), "password": entre_mdp.get()}
    res = req.post(API.USER_LOGIN, userData)
    
    if(res.status_code == 200):
        data = res.json()
        api = API()
        api.set_token(data)
        open_utilisateur_window()
       
    else: 
        messagebox.showerror("Error", "Invalid email or password!")

def open_utilisateur_window():
    #close_current_window
    root.destroy()
    #open new window
    User(tk.Toplevel())
    
lbl_titre = Label(root, text="Formulaire", font=("Sans serif", 25), bg="#091821", fg="white", borderwidth=3, relief= SUNKEN)
lbl_titre.place(x=0,y=0, width=400)

lbl_mail = Label(root, text="Email :", font=("Arial", 14), bg="#091821", fg="white")
lbl_mail.place(x=5,y=100, width=150)
entre_mail = Entry(root, bd=4, font=("Arial", 13))
entre_mail.place(x=150,y=100, width=200,height=30)


lbl_mdp = Label(root, text="Mot de Passe :", font=("Arial", 14), bg="#091821", fg="white")
lbl_mdp.place(x=5,y=150, width=150)
entre_mdp = Entry(root, bd=4, font=("Arial", 13), show="*")
entre_mdp.place(x=150,y=150, width=200,height=30)

# Boutton

btn_enrengistrer = Button(root, text="Connexion", font=("Arial", 16), bg="#FF4500", fg="white", command=login)
btn_enrengistrer.place(x=150, y=200, width=200)



root.mainloop()