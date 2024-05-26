import random 


def random_f(): #funcion de py para elegir una funcion aleatoria
    funcion_aleatoria = random.choice(funciones)
    if funcion_aleatoria == 'Funcion Lineal':
        lineal()
    elif funcion_aleatoria == 'Funcion Cuadratica':
        cuadratica()
    elif funcion_aleatoria == 'Funcion Cubica':
        cubica()
    elif funcion_aleatoria == 'Funcion Raiz Cuadrada':
        f_raiz_cuadrada()
    elif funcion_aleatoria == 'Funcion Logaritmica':
        logaritmica()
    elif funcion_aleatoria == 'Funcion Parte Entera':
        parte_entera()
    elif funcion_aleatoria == 'Funcion Valor Absoluto':
        f_valor_absoluto()
    elif funcion_aleatoria == 'Funcion Compuesta':
        compuesta()
    elif funcion_aleatoria == 'Funcion Inversa':
        inversa()

def lineal(m, b):
    operador = random.choice(operandos)
    print(f"¡Rapido analiza la siguiente funcion: {m}x {operador} {b} ")

def cuadratica(x, a=1, b=0, c=0):
    pass

def cubica():
    pass

def f_raiz_cuadrada():
    pass

def logaritmica():
    pass

def parte_entera():
    pass

def f_valor_absoluto():
    pass

def compuesta():
    pass

def inversa():
    pass

if __name__ == '__main__':
    funciones = [
    "Funcion Lineal",
    "Funcion Cuadratica",
    "Funcion Cubica",
    "Funcion Raiz Cuadrada",
    "Funcion Logaritmica",
    "Funcion Parte Entera",
    "Funcion Valor Absoluto",
    "Funcion Compuesta",
    "Funcion Inversa"
    ]
    operandos = ["+", "-"]
    valores_m = [i for i in range(0, 20)]
    valores_b = [i for i in range(0, 20)]
    valores_b = random.choice(valores_b)
    valores_m = random.choice(valores_m)

lineal(valores_m, valores_b)