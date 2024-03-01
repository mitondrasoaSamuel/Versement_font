from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests as req
import tkinter as tk
import os
import sys

# import configAPI
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")  # Add parent directory to the path
from configAPI import API
from utilisateur import utilisateur as User

root = Tk()
root.title("Page de Connexion")
root.geometry("925x500+300+200")
root.resizable(False, False)
root.config(bg="#fff")




def login():
    userData = {"email": entre_mail.get(), "password": entre_mdp.get()}
    res = req.post(API.USER_LOGIN, userData)
    
    if(res.status_code == 200):
        data = res.json()
        api = API()
        api.set_token(data)
        open_utilisateur_window()
       
    else: 
        messagebox.showerror("Error", "Le Mot de passe ou l'email n'ai pas valider!")

def open_utilisateur_window():
    #close_current_window
    root.destroy()
    #open new window
    User(tk.Toplevel())
    

#### -----------------------------------------------------------------------------------------------------------------------------
### Import image 
img = ImageTk.PhotoImage(file="D:/Projets/Python_M2/PROJET_ABDA/Login/logo.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)


titre = Label(frame, text="Se Connecter",fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
titre.place(x=100, y=5)




    ###

def on_enter(e):
    entre_mail.delete(0, 'end')

def on_leave(e):
    name=entre_mail.get()
    if name=='':
        entre_mail.insert(0, 'Email')

entre_mail = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
entre_mail.place(x=30, y=80)
entre_mail.insert(0, 'Entrer voitre Email...')
entre_mail.bind('<FocusIn>', on_enter)
entre_mail.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)
        ###

def on_enter(e):
    entre_mdp.delete(0, 'end')
    entre_mdp.config(show="*") # Masque le texte saisi
    entre_mdp.config(fg = 'black')

def on_leave(e):
    name=entre_mdp.get()
    if name=='':
        entre_mdp.insert(0, 'Mot de Passe')
        entre_mdp.config(show="")


entre_mdp = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11), show="")
entre_mdp.place(x=30, y=150)
entre_mdp.insert(0, "Entrer voitre mot de passe...")
entre_mdp.bind('<FocusIn>', on_enter)
entre_mdp.bind('<FocusOut>', on_leave)



Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

### Bouton


Button(frame, width=39, pady=7, text="Se connecter", bg="#57a1f8", fg="white", border=0, command=login).place(x=35, y=204)

label =Label(frame, text="Mot de passe oubliée?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

root.mainloop()