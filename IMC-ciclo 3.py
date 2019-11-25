from tkinter import *

prog = Tk()

prog.title("Cálculo de imc - CICLO 3 ")

lbNome = Label(prog, text="Nome do Paciente:")
lbNome.place(x=20, y=20)

lbEnd = Label(prog, text="Endereço Completo:")
lbEnd.place(x=20, y=45)

lbAlt = Label(prog, text="Altura (0.00)")
lbAlt.place(x=20, y=70)

lbPeso = Label(prog, text="Peso (kg)")
lbPeso.place(x=20, y=95)

entNome = Entry(prog,  width=70)
entNome.place(x=150, y=20)

entEnd = Entry(prog, width=70)
entEnd.place(x=150, y=45)

entAlt = Entry(prog, width=20)
entAlt.place(x=150, y=70)

entPeso = Entry(prog, width=20)
entPeso.place(x=150, y=95)

def bt_click_calc():
    if(str(entAlt.get()).isascii() and str(entPeso.get()).isnumeric()):
        Alt = float(entAlt.get())
        Peso = int(entPeso.get())
        imc = float(Peso / (Alt * Alt))
        lbResulN["text"] = round(imc, 2)
        if imc < 17:
            lbResulSit["text"] = "Muito Abaixo do Peso"
            lbResulSit.config(bg="white")
            lbResulN.config(bg="white")
        elif imc < 18.5:
            lbResulSit["text"] = "Abaixo do Peso"
            lbResulSit.config(bg="yellow")
            lbResulN.config(bg="yellow")
        elif imc < 25:
            lbResulSit["text"] = "Peso Normal "
            lbResulSit.config(bg="white")
            lbResulN.config(bg="white")
        elif imc < 30:
            lbResulSit["text"] = "Acima do Peso"
            lbResulSit.config(bg="white")
            lbResulN.config(bg="white")
        elif imc < 35:
            lbResulSit["text"] = "Obsedidade 1"
            lbResulSit.config(bg="white")
            lbResulN.config(bg="white")
        elif imc < 40:
            lbResulSit["text"] = "Obsedidade 2 (SEVERA)"
            lbResulSit.config(bg="white")
            lbResulN.config(bg="white")
        elif imc >= 40:
            lbResulSit["text"] = "Obsedidade 3 (MÓRBIDA)"
            lbResulSit.config(bg="white")
            lbResulN.config(bg="red")
        else:
            lbResulSit["text"] = "Análise"
    else:
        lbResulN["text"] = "Digite os valores da Altura e do  Peso corretamente."

def bt_click_reini():
    entNome.delete(0, END)

    entEnd.delete(0, END)

    entAlt.delete(0, END)

    entPeso.delete(0, END)

    lbResulN.config(text="-", bg="white")

    lbResulSit.config(text="Informe os dados", bg="white")


def bt_click_sair():
    prog.quit()



btCalc = Button(prog, width=15, text="Calcular", command=bt_click_calc)
btCalc.place(x=20, y=310)

btSair = Button(prog, width=15, text="Sair", command=bt_click_sair)
btSair.place(x=468, y=310)

btReini = Button(prog, width=15, text="Reiniciar", command=bt_click_reini)
btReini.place(x=150, y=310)

lbResulN = Label(prog, text="imc", width=11, height=5, bg="white", font="arial 20 bold")
lbResulN.place(x=390, y=130)

lbResulSit = Label(prog, text="SITUAÇÃO", width=20, height=5, bg="white", font="arial 20 bold")
lbResulSit.place(x=20, y=130)


prog.geometry("600x350+350+100")

prog.mainloop()