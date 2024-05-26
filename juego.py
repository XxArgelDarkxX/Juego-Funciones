import random 
import math

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

def cuadratica():
    valores_a = [i for i in range(1, 20)]  # Evitar que 'a' sea 0
    valores_b = [i for i in range(0, 20)]
    valores_c = [i for i in range(0, 20)]
    a = random.choice(valores_a)
    b = random.choice(valores_b)
    c = random.choice(valores_c)

    # Elegir operadores para b y c
    operador_b = random.choice(operandos)
    operador_c = random.choice(operandos)
    
    # Construir la ecuación con los operadores
    print(f"¡Rápido, analiza la siguiente función: {a}x^2 {operador_b} {b}x {operador_c} {c} ")
    print("Encuentra los cortes con el eje x y el eje y")
    
    corte_x1 = float(input("Corte con el eje x 1: "))
    corte_x2 = float(input("Corte con el eje x 2: "))
    corte_y = float(input("Corte con el eje y: "))
    
    d = b**2 - 4*a*c
    if d < 0:
        return "No real roots"
    else:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)

    # calculate y intercept
    y_intercept = c
    
    if corte_x1 == root1 and corte_x2 == root2 and corte_y == y_intercept:
        print("Correcto")
    else:
        print("Incorrecto")

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
    cuadratica()
    # random_f()

