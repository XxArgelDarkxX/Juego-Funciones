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
    
    # seleciona un problema aleatorio

    eleccion = random.randint(1, 3)
    
    # lista de ecuaciones cuadraticas con sus soluciones,cortes x y y, vertice y rango,dominio
    ecuaciones_cuadraticas = [
    ("x**2 - 4*x + 4 ", [2, 2, 0],[2,0],["R","y>=0"]), #soluciones cortes x y y, vertice, rango
    ("2*x**2 - 3*x + 1 ", [0.5, 1, 1],[0.75, -0.125],["R","y>=-0.125"]),
    ("3*x**2 + 6*x + 3 ", [-1, -1, 3],[-1, 0],["R","y>=0"]),
    ("x**2 + 5*x + 6 ", [-3, -2, 6],[-2.5,-0.25],["R","y>=-0.25"]),
    ("4*x**2 - 4*x + 1 ", [0.5, 0.5, 1],[0.5, 0],["R","y>=0"]),
]
    
    #elige una ecuacion aleatoria
    
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

    decimal = round(random.uniform(-10, 10), 1) #genera un numero decimal aleatorio
    x = [f"¡Rapido realiza la funcion parte entera: ⌊{decimal}⌋ ", f"¡Rapido realiza la funcion parte entera: ⌈{decimal}⌉ "] #preguntas posibles
    preg_0 = random.choice(x) #elige una pregunta aleatoria
    if preg_0 == x[0]:
        print(f"¡Rapido realiza la funcion parte entera: ⌊{decimal}⌋ ")
        ans = int(input("Respuesta: "))
        if ans == math.floor(decimal):
            print("¡Correcto!")  
        else: 
            print("¡Incorrecto!")
    elif preg_0 == x[1]:
        print(f"¡Rapido realiza la funcion parte entera: ⌈{decimal}⌉ ")
        ans = int(input("Respuesta: "))
        if ans == math.ceil(decimal) or (decimal < 0 and ans == math.floor(decimal)): #si el numero es negativo se redondea hacia abajo
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
def f_valor_absoluto():
    x = random.randint(-50, 50)
    print(f"¡Rapido realiza la funcion valor absoluto: |{x}| ")
    ans = int(input("Respuesta: "))
    if ans == abs(x):
        print("¡Correcto!")
    else:
        print("¡Incorrecto!")
        
def compuesta():
    pass

def inversa():
    a = "Cual es la funcion inversa de: F(x) = 2x + 1"
    b = "Cual es el punto de corte en X de: F(x) = 2x + 1"
    c = "Cual es la funcion inversa de: G(x) = 3x - 2"
    d = "Cual es el dominio y rango de: G^-1(y) = 2(y-1)"
    e = "Cuales son los puntos de corte en X y en Y de: H(x) = 1/2x + 3"
    originales = [a, b, c, d, e]
    x = random.choice(originales)
    
    if x == a:
        r_a = "f^-1(x)=(x-1)/2"
        print(a)
        r_u = input("Respuesta: ").lower().strip().replace(" ", "")
        if r_u == r_a.lower().strip().replace(" ", ""):
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
    elif x == b:
        r_b = "(-1/2,0)"
        print(b)
        r_u = input("Respuesta: ").lower().strip().replace(" ", "")
        if r_u == r_b.lower().strip().replace(" ", ""):
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
    elif x == c:
        r_c = "g^-1(x)=(x+2)/3"
        print(c)
        r_u = input("Respuesta: ").lower().strip().replace(" ", "")
        if r_u == r_c.lower().strip().replace(" ", ""):
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
    elif x == d:
        r_s = ["r", "losreales", "todoslosreales", "todoslosnumerosreales"]
        print(d)
        r_u = input("Dominio: ").lower().strip().replace(" ", "")
        r_u2 = input("Rango: ").lower().strip().replace(" ", "")
        if r_u and r_u2 in r_s:
            print("¡Correcto!")
            
        else:
            print("¡Incorrecto!")
    
    elif x == e:
        r_e = "(-6,0)"
        print(e)
        r_u = input("Respuesta para X: ").lower().strip().replace(" ", "")
        if r_u == r_e.lower().strip():
            r_ey = "(0,3)"
            r_uy = input("Respuesta para Y: ").lower().strip().replace(" ", "")
            if r_uy == r_ey.lower().strip():
                print("¡Correcto!")
            else:
                print("¡Incorrecto!")
        else:
            print("¡Incorrecto!")
    
    
    

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
    # cuadratica()
    random_f()

