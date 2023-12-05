import math
from tkinter import *

janela = Tk()

janela.title('Atividade2')


# atividade 1 ________________________________________________________-
# ----------------------------Questão 1----------------------------------------------
def verifica_idade():
    dia_vivido = float(e_dias_vida.get())

    anos = int(dia_vivido / 365)
    saldo = dia_vivido - anos * 365

    meses = int(saldo / 30)
    dias = saldo - meses * 30

    l_resultado['text'] = (anos, "ano(s), ", meses, "mes(es) e ", dias, "dia(s)")


# ----------------------------FIM  Questão 1----------------------------------------------
def verifica_numeros():
    a = float(e_num_a.get())
    b = float(e_num_b.get())
    c = float(e_num_c.get())
    # ----------------------------Questão 2----------------------------------------------
    if a >= b + c or b >= a + c or c >= a + b:
        l_resultado['text'] = (a, b, c, "esses numeros não formam um triangulo")
    elif a == b == c:
        base: float = (a / 2) ** 2
        cateto: float = a ** 2
        area: float = (base + cateto) ** (1 / 2)
        l_resultado['text'] = (a, b, c, "formam um triangulo equilatero sua area é ", "{:.{}f}".format(area, 2))
    else:
        s = (a + b + c) / 2
        area: float = math.sqrt(s * (s - a) * (s - b) * (s - c))
        l_resultado['text'] = ('Não é um triangulo equilatero. Area=', "{:.{}f}".format(area, 2))


# ----------------------------FIM Questão 2----------------------------------------------

# ---------------------------- Questão 3----------------------------------------------
def verifica_maior():
    a: float = float(e_num_a.get())
    b = float(e_num_b.get())
    c = float(e_num_c.get())

    if b < a > c:
        l_resultado_maior['text'] = 'Maior é o A', a
    elif a < b > c:
        l_resultado_maior['text'] = 'Maior é o B', b
    else:
        l_resultado_maior['text'] = 'Maior é o C', c


# ----------------------------FIM Questão 3----------------------------------------------
# ---------------------------- Questão 4----------------------------------------------
def verifica_primo():
    number = int(e_num_primo.get())

    if 1 < number:
        for i in range(2, number):
            if number % i == 0:
                l_resultado_maior['text'] = number, 'Não é primo'
                break
            else:
                l_resultado_maior['text'] = number, 'É primo'
    elif number == 0:
        l_resultado_maior['text'] = number, 'É Zero'
    elif number == 1:
        l_resultado_maior['text'] = number, 'É Um'
    else:
        l_resultado_maior['text'] = number, 'É negativo'


# ----------------------------FIM Questão 4----------------------------------------------
# ---------------------------- Questão 5----------------------------------------------

def inverte_frase():
    frase = str(e_frase_i.get())
    invertida = ' '.join(palavra[::-1] for palavra in frase.split())
    l_resultado_frase['text'] = 'A frase que você digitou invertida fica: {}'.format(invertida)

# --------------------------------layout-----------------------------------------

l_dias_vida = Label(text='Digite o número de dias vividos por você:')
l_dias_vida.grid(row=0, column=0, sticky=E)
e_dias_vida = Entry(width=40, relief='solid', )
e_dias_vida.grid(row=0, column=1, sticky=W)

l_num_a = Label(text='Digite o número A=:')
l_num_a.grid(row=2, column=0, sticky=E)
e_num_a = Entry(width=20, relief='solid', )
e_num_a.grid(row=2, column=1, sticky=W)

l_num_b = Label(text='Digite o número B=:')
l_num_b.grid(row=3, column=0, sticky=E)
e_num_b = Entry(width=20, relief='solid', )
e_num_b.grid(row=3, column=1, sticky=W)

l_num_c = Label(text='Digite o número C=:')
l_num_c.grid(row=4, column=0, sticky=E)
e_num_c = Entry(width=20, relief='solid', )
e_num_c.grid(row=4, column=1, sticky=W)

l_num_primo = Label(text='Digite um número entre 0 e 100:')
l_num_primo.grid(row=5, column=0, sticky=E)
e_num_primo = Entry(width=20, relief='solid', )
e_num_primo.grid(row=5, column=1, sticky=W)

l_resultado = Label(text='saida de dados')
l_resultado.grid(row=6, column=1, sticky=W)
l_resultado_maior = Label(text='')
l_resultado_maior.grid(row=7, column=1, sticky=W)

b_verifica_idade = Button(text='Verificar Idade', command=verifica_idade)
b_verifica_idade.grid(row=8, column=0, sticky=W)

b_verifica_primo = Button(text='Primo?', command=verifica_primo)
b_verifica_primo.grid(row=8, column=0, sticky=E)

b_verifica_num = Button(text='Verificar Números ', command=verifica_numeros)
b_verifica_num.grid(row=8, column=1, sticky=W)

b_verifica_maior = Button(text='Verificar maior Número', command=verifica_maior)
b_verifica_maior.grid(row=8, column=1, sticky=E)

l_frase_i = Label(text='Digite uma Frase.')
l_frase_i.grid(row=9, column=0, sticky=E)
e_frase_i = Entry(width=20, relief='solid', )
e_frase_i.grid(row=9, column=1, sticky=W)

b_inverte_frase = Button(text='Inverter Frase', command=inverte_frase)
b_inverte_frase.grid(row=10, column=0, sticky=E)
l_resultado_frase = Label(text='Frase será invertida...')
l_resultado_frase.grid(row=10, column=1, sticky=W)

janela.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
