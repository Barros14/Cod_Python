# importando tkinter
from tkinter import*
from tkinter import ttk

#cores
cor1 = "#1e1f1e" #preta
cor2 = "#feffff" #Branca
cor3 = "#38576b" #Azul carregado
cor4 = "#ECEFF1" #CIZENTA
cor5 = "#FFAB40" #Laranja

janela = Tk()
janela.title("Calculador") #Crie janela
janela.geometry("235x318") #faz configuração do tamanho da janela
janela.config(bg=cor1)

#Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#Criando botões
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="CE", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=90, y=0)
b_3 = Button(frame_corpo, text="%", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=136, y=0)
b_4 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=182, y=0)


janela.mainloop()