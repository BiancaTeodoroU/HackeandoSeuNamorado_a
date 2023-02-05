import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0 

msg_box = messagebox.showwarning("Tamo Papudo!", "Você foi hackeado!")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("PERA AI", "Para se deshackear preciso que você responda uma pergunta...")

if msg_box == 'ok':
    msg_box = messagebox.askquestion("O que acha?", "O coelho é troll")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("O que acha?", "O coelho é troll")
    if (count == 5): 
        msg_box = messagebox.showerror("To indo ai!", "Se vai apanhar feio!")
    break 

if msg_box == 'yes':
    msg_box = messagebox.showinfo("Boa!", "Sabia escolha!")