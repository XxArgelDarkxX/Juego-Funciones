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
    eleccion = random.randint(1, 3)
    ecuaciones_cuadraticas = [
    ("x**2 - 4*x + 4 ", [2, 2, 0],[2,0],["R","y>=0"]), #soluciones, vertice, rango
    ("2*x**2 - 3*x + 1 ", [0.5, 1, 1],[0.75, -0.125],["R","y>=0"]),
    ("3*x**2 + 6*x + 3 ", [-1, -1, 3],[-1, 0],["R","y>=0"]),
    ("x**2 + 5*x + 6 ", [-3, -2, 6],[-2.5,-0.25],["R","y>=-0.25"]),
    ("4*x**2 - 4*x + 1 ", [0.5, 0.5, 1],[0.5, 0],["R","y>=0"]),
]

    ecuacion,soluciones,soluciones_vertice,rango_Dominio = random.choice(ecuaciones_cuadraticas)
    print(f"¡Rapido analiza la siguiente funcion: {ecuacion}")
    
    if eleccion == 1:
        
        print("calcula los cortes con x y y")
        corte_x1 = int(input("Corte con x1: "))
        corte_x2 = int(input("Corte con x2: "))
        corte_y = int(input("Corte con y: "))
        if [corte_x1, corte_x2, corte_y] == soluciones:
            print("Correcto")
        else:
            print("Incorrecto")
    elif eleccion == 2:
        print("Calcula el vertice de la parabola")
        vertice_x = int(input("Vertice x: "))
        vertice_y = int(input("Vertice y: "))
        if [vertice_x, vertice_y] == soluciones_vertice:
            print("Correcto")
        else:
            print("Incorrecto")
    else:
        print("calcula en rango y dominio de la funcion")
        dom = input("Dominio: ")
        ran = input("Rango: ")
        if [dom, ran] == rango_Dominio:
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

