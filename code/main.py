import tkinter #importar o tkinter e o messagebox
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0 # crie uma varivel count atribuindo o valor 0
# abaixo estamos criando o nosso primeiro messagebox do tipo showwarning
msg_box = messagebox.showwarning("Tamo Papudo!", "Você foi hackeado!")
# abaixo estamos fazendo a nossa primeira condição para verificar se a pessoa clicou no ok
# se sim aparece outro showwarning com outra mensagem obs( o primeiro texto é o titulo)
# e o segundo o conteudo
if msg_box == 'ok':
    msg_box = messagebox.showwarning("PERA AI", "Para se deshackear preciso que você responda uma pergunta...")
# aqui verificamos de novo se a pessoa clicou no ok só que dessa vez usamos o askquestion que nos dara
# duas opções o sim e o não
if msg_box == 'ok':
    msg_box = messagebox.askquestion("O que acha?", "O coelho é troll")
# aqui estamos fazendo um looping infinito onde verificamos se a pessoa clicou no não
# se ela clicar no não o nosso count adiciona + 1
# com isso a mensagem vai repetir 5 vezes até o count completar 5
# embaixo é criado um novo messagebox do tipo showerror que vai exibir a mensagem
# caso a pessoa clique 5 vezes ou não.
# finalizamos o looping com o break
while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("O que acha?", "O coelho é troll")
    if (count == 5): 
        msg_box = messagebox.showerror("To indo ai!", "Se vai apanhar feio!")
    break 
# abaixo apenas verificamos se a pessoa clicou em sim, caso tenha clicado irá exibir a mensagem
if msg_box == 'yes':
    msg_box = messagebox.showinfo("Boa!", "Sabia escolha!")

# por fim você terá que pegar o seu arquivo ( no meu caso main.py ) e converter para executavel
