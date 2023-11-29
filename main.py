from logging import root
from tkinter import *

janela = Tk()
janela.title('Cálculo do IMC - indice de Massa Corporal')


# ______________________funcao calcular ______________________________
def calcular():
    peso = float(e_peso_paciente.get())
    altura = float(e_altura_paciente.get())

    resultado = peso / altura ** 2

    if resultado < 18.5:
        l_resultado_texto['text'] = 'Seu IMC é : Abaixo do peso'
    elif 18.5 <= resultado < 25:
        l_resultado_texto['text'] = 'Seu IMC é : Peso Normal'
    elif 25 <= resultado < 30:
        l_resultado_texto['text'] = 'Seu IMC é : Sobrepeso'
    else:
        l_resultado_texto['text'] = 'Seu IMC é : Obesidade'

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)


# -------------------------- layout-----------------------------------

l_nome_paciente = Label(text='Nome do Paciente: ')
l_nome_paciente.grid(row=0, column=0)
e_nome_paciente = Entry(width=60, relief='solid')
e_nome_paciente.grid(row=0, column=1)

l_enderco_paciente = Label(text='Endereço Completo: ')
l_enderco_paciente.grid(row=1, column=0)
e_endereco_paciente = Entry(width=60, relief='solid')
e_endereco_paciente.grid(row=1, column=1)

l_altura_paciente = Label(text='Altura do Paciente: ', padx=0)
l_altura_paciente.grid(row=2, column=0)
e_altura_paciente = Entry(width=20, relief='solid')
e_altura_paciente.place(x=117, y=44)

l_peso_paciente = Label(text='Peso do Paciente: ', padx=0)
l_peso_paciente.grid(row=3, column=0)
e_peso_paciente = Entry(width=20, relief='solid', )
e_peso_paciente.place(x=117, y=66)

l_resultado = Label(text='RESULTADO ', border=0, background='light gray', width=30, height=1, padx=6, pady=30)
l_resultado.place(x=257, y=44)

l_resultado_texto = Label(text=' ', border=0)
l_resultado_texto.place(x=116, y=94)

b_calcular = Button(text='Calcular', command=calcular)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5)

b_reiniciar = Button(text='Reiniciar',command=Label.destroy, width=15, height=1, anchor='center')
b_reiniciar.grid(row=4, column=1, sticky=W, pady=60, padx=5)

b_sair = Button(text='Sair',command=janela.destroy, width=15, height=1, anchor='center')
b_sair.grid(row=4, column=1, sticky=E, pady=60, padx=5)

janela.mainloop()
