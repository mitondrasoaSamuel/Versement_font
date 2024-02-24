from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox


root = Tk()
root.title("Connexion")
root.geometry("400x300+450+200")
root.resizable(False, False)


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

btn_enrengistrer = Button(root, text="Connexion", font=("Arial", 16), bg="#FF4500", fg="white")
btn_enrengistrer.place(x=150, y=200, width=200)



root.mainloop()