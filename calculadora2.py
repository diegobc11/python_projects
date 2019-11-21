from tkinter import *
from math import *

root = Tk()

miFrame = Frame(root)
miFrame.pack()

operacion = ""
# variable global para almacenar el signo dela operacion que se va a ejecutar
resultado = 0
signo_click = False

# -----------pantalla-----------------
numero = StringVar()
# variable cuyo valor va cambiando segun el numero que se pulse.

pantalla = Entry(miFrame, textvariable=numero)
pantalla.grid(column=0, row=1, padx="5", pady="5", columnspan=4)
pantalla.config(bg="black", fg="#95FFF2", justify="right")
# pantalla.insert(0, "0")

# -----------pantalla secundaria----------
numero2 = StringVar()
pantalla2 = Entry(miFrame, textvariable=numero2)
pantalla2.grid(column=0, columnspan=4, row=0)
pantalla2.config(fg="#95FFF2", bg="black", justify="right")
# para guardar el primer valor con el que se trabaja


# ----------funcion de redondeo------------------
# contador_click = 0

def redondeo():
    pass
# if contador_click == 0:
# numero.set(round(pantalla.get()))
# hay que poner un contador a partir de que se escriba el punto decimal
# con cada click de redondeo, redondeamos un decimal mas la cifra resultado
# ej:5,123 [1 click = 5,12] [2 click = 5,1] [3 click = 5]


# ---------------pulsaciones pantalla-------------
def numero_click(num):
    global operacion
    global signo_click

    if signo_click is True:
        numero.set(num)
        numero2.set(resultado)
        signo_click = False

    else:
        numero.set(pantalla.get() + num)


# ------------- suma --------------
def suma(num):
    global operacion
    global resultado
    global signo_click
    operacion = "suma"
    resultado += float(num)
    numero.set(resultado)
    # pantalla.delete(0, END), se puede borrar al pulsar 'mas' o al pulsar el siguiente numero...
    signo_click = True


# -----------resta -------------------
contador_resta = 0
num_resta = 0


def resta(num):
    global resultado
    global operacion
    global contador_resta
    global num_resta
    global signo_click
    operacion = "resta"
    num_resta = float(num)
    # num y pantalla.get() es lo mismo, usamos el que queramos

    if contador_resta == 0:
        resultado = num_resta

    else:
        resultado = resultado - num_resta

    contador_resta += 1
    # sin el contador, en la primera resta nos cambia el signo del primer numero que escribamos
    numero.set(resultado)
    signo_click = True


# --------funcion multiplicacion---------------
contador_mult = 0


def multiplicar(num):
    global resultado
    global signo_click
    global contador_mult
    global operacion
    operacion = "multiplicacion"

    if contador_mult == 0:
        resultado = float(num)
        # hay que poner exceocion de primera vez sino nos estaria multiplicando por 0 simpre que multipliquemos

    else:
        resultado *= float(num)

    numero.set(resultado)

    contador_mult += 1
    signo_click = True


# ---------funcion division--------------
contador_div = 0


def division(num):
    global resultado
    global operacion
    global signo_click
    global contador_div
    operacion = "division"

    if contador_div == 0:
        resultado = float(num)

    else:
        resultado = resultado / float(num)

    contador_div += 1
    numero.set(resultado)
    signo_click = True


# --------funcion raiz cuadrada-----------
def raiz_2():
    numero.set(sqrt(float(pantalla.get())))


# ---------funcion exponente--------------
contador_expo = 0


def exponente(num):
    global resultado
    global operacion
    global signo_click
    global contador_expo
    operacion = "exponente"

    if contador_expo == 0:
        resultado = float(num)

    else:
        resultado = resultado ** float(num)

    numero.set(resultado)
    contador_expo += 1
    signo_click = True


# --------funcion resultado---------------
def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_mult
    global contador_div
    global contador_expo

    # necesitamos un contador para cada operacion porque la primera vez que ejecutamos cada una tenemos conflicto
    # menos para la suma que es la mas sencilla de todas y el 0 incial no le influye

    if operacion == "suma":
        numero.set(resultado + float(pantalla.get()))
        resultado = 0

    else:
        pass

    if operacion == "resta":
        numero.set(resultado - float(pantalla.get()))
        resultado = 0
        contador_resta = 0

    else:
        pass

    if operacion == "multiplicacion":
        numero.set(resultado * float(pantalla.get()))
        resultado = 0
        contador_mult = 0

    else:
        pass

    if operacion == "division":
        numero.set(resultado / float(pantalla.get()))
        resultado = 0
        contador_div = 0
    else:
        pass

    if operacion == "exponente":
        numero.set(resultado ** float(pantalla.get()))
        resultado = 0
        contador_expo = 0
    else:
        pass


# ------------funcion borrado---------------
def borrado():
    global resultado
    pantalla.delete(0, END)
    resultado = 0


# -----------Funcion borrado caracter ----------
def borrado_caracter():
    pantalla.delete(len(pantalla.get()) - 1, END)
    # para borrar solamente el ultimo digito escrito en pantalla


# ------------Fila 0 de botones--------------
boton_round = Button(miFrame, text="Round", width=5, command=redondeo)
boton_round.grid(column=4, row=0)


# ------------Fila 1 de botones -------------
boton_del = Button(miFrame, text="DEL", width=5, command=borrado_caracter)
boton_del.grid(column=4, row=1)


# -----------Fila 2 de botones-------------
boton7 = Button(miFrame, text="7", width="5", command=lambda: numero_click("7"))
# sin la funcion lambda el programa almacena el valor antes de que pulsemos el boton
boton7.grid(column="0", row=2)
boton8 = Button(miFrame, text="8", width="5", command=lambda: numero_click("8"))
boton8.grid(column="1", row=2)
boton9 = Button(miFrame, text="9", width="5", command=lambda: numero_click("9"))
boton9.grid(column="2", row=2)
boton_div = Button(miFrame, text="/", width="5", command=lambda: division(pantalla.get()))
boton_div.grid(column="3", row=2)
boton_raiz = Button(miFrame, text="√", width="5", command=raiz_2)
boton_raiz.grid(column=4, row=2)

# -----------Fila 3 de botones-------------
boton4 = Button(miFrame, text="4", width="5", command=lambda: numero_click("4"))
boton4.grid(column="0", row=3)
boton5 = Button(miFrame, text="5", width="5", command=lambda: numero_click("5"))
boton5.grid(column="1", row=3)
boton6 = Button(miFrame, text="6", width="5", command=lambda: numero_click("6"))
boton6.grid(column="2", row=3)
boton_mult = Button(miFrame, text="x", width="5", command=lambda: multiplicar(pantalla.get()))
boton_mult.grid(column=3, row=3)
boton_expo2 = Button(miFrame, text="^", width="5", command=lambda: exponente(pantalla.get()))
boton_expo2.grid(column=4, row=3)

# -----------Fila 4 de botones-------------
boton1 = Button(miFrame, text="1", width="5", command=lambda: numero_click("1"))
boton1.grid(column="0", row=4)
boton2 = Button(miFrame, text="2", width="5", command=lambda: numero_click("2"))
boton2.grid(column="1", row=4)
boton3 = Button(miFrame, text="3", width="5", command=lambda: numero_click("3"))
boton3.grid(column="2", row=4)
boton_resta = Button(miFrame, text="-", width="5", command=lambda: resta(pantalla.get()))
boton_resta.grid(column=3, row=4)
boton_C = Button(miFrame, text="C", width="5", command=borrado)
boton_C.grid(column=4, row=4)

# -----------Fila 5 de botones-------------
boton_coma = Button(miFrame, text=".", width="5", command=lambda: numero_click("."))
boton_coma.grid(column="0", row=5)
boton0 = Button(miFrame, text="0", width="5", command=lambda: numero_click("0"))
boton0.grid(column="1", row=5)
boton_suma = Button(miFrame, text="+", width="5", command=lambda: suma(pantalla.get()))
boton_suma.grid(column="2", row=5)
boton_igual = Button(miFrame, text="=", width="12", command=el_resultado)
boton_igual.grid(column=3, row=5, columnspan=4)

# ----------Fila 6 de botones -------------
# ideas de botones extra: boton de redondeo, boton de elevado a, botones de parentesis para operar...
# depurar la raiz cuadrada, para que me ponga en el simbolo en pantalla y no la haga hasta pulsar el igual
mainloop()
