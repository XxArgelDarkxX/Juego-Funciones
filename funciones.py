import random 
import math
import modificar_interfaz as mi





def random_f(): #funcion de py para elegir una funcion aleatoria
    funciones = ["funcion inyectividad","funcion hiperbolicas","funcion exponencial","funcion logaritmica","funcion inversa","funcion valor absoluto","funcion parte entera","funcion impar par","funcion cuadratica","funcion cubica","funcion raiz cuadrada","funcion lineal"]
    random.shuffle(funciones)

    funcion_aleatoria = random.choice(funciones)
    if funcion_aleatoria == 'funcion lineal':
        preguntas,respuestas,pregunta = lineal()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion cuadratica':
        preguntas,respuestas,pregunta = cuadratica()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion cubica':
        preguntas,respuestas,pregunta = cubica()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion raiz cuadrada':
        preguntas,respuestas,pregunta=f_raiz_cuadrada()
        return preguntas,respuestas,pregunta
    
    elif funcion_aleatoria == 'funcion parte entera':
        preguntas,respuestas,pregunta = parte_entera()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion valor absoluto':
        preguntas,respuestas,pregunta = f_valor_absoluto()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion inversa':
        preguntas,respuestas,pregunta = inversa()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion logaritmica':
        preguntas,respuestas,pregunta = logaritmica()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion exponencial':
        preguntas,respuestas,pregunta = exponencial()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion hiperbolicas':
        preguntas,respuestas,pregunta = hiperbolicas()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion impar par':
        preguntas,respuestas,pregunta = impar_par()
        return preguntas,respuestas,pregunta
    elif funcion_aleatoria == 'funcion inyectividad':
        preguntas,respuestas,pregunta = inyectibilidad()
        return preguntas,respuestas,pregunta
    
def lineal():
    
    ejercicios_funciones_lineales = [
    ["f(x) = 3x + 2", ["-2/3"],["2"],["creciente"]],
    ["g(x) = -2x - 5", ["-5/2"], ["-5"],["decreciente"]],
    ["h(x) = 4x - 1", ["1/4"], ["-1"],["creciente"]],
    ["j(x) = -x + 3", ["3"], ["3"],["decreciente"]],
    ["k(x) = 2x", ["0"], ["0"],["creciente"]]
    ]
    ecuacion,cortex,cortey,creciente_decreciente = random.choice(ejercicios_funciones_lineales)
    
    corte_x = "Corte con x:"
    corte_y = "Corte con y:"
    crec_decrec = "Creciente o decreciente:"
    lista_preguntas=[corte_x,corte_y,crec_decrec]
    lista_respuestas=[cortex[0],cortey[0],creciente_decreciente[0]]
    return lista_preguntas,lista_respuestas,ecuacion
    
def cuadratica():
    eleccion = 1
    ecuaciones_cuadraticas = [
    ["x**2 - 4*x + 4 ", ["2", "2", "4"],["(2,0)"],["R","y>=0"]], #soluciones, vertice, rango
    ["2*x**2 - 3*x + 1 ", ["1/2"," 1", "1"],["(3/4, -1/8)"],["R","y>=-1/8"]],
    ["3*x**2 + 6*x + 3 ", ["-1", "-1", "3"],["(-1, 0)"],["R","y>=0"]],
    ["x**2 + 5*x + 6 ", ["-3", "-2", "6"],["(-5/2,-1/4)"],["R","y>=-1/4"]],
    ["4*x**2 - 4*x + 1 ", ["1/2", "1/2", "1"],["(1/2,0)"],["R","y>=0"]]
    ]

    ecuacion, soluciones, soluciones_vertice, rango_Dominio = random.choice(ecuaciones_cuadraticas)
    pregunta = f"¡Rapido analiza la siguiente funcion: {ecuacion}"
    
    if eleccion == 1:
        
        corte_x1 = "¿Encuentra el corte con el eje x1?"
        corte_x2 ="¿Encuentra el corte con el eje x2?"
        corte_y = "¿Cual es el corte con el y?"
        vertice = "¿En que coordenadas se encuentra Vertice?"
        dominio = "¿Cual es el Dominio?"
        rango = "¿Cual es el Rango?"
        
        lista_preguntas=[corte_x1,corte_x2,corte_y,vertice,dominio,rango]
        lista_repuestas = [soluciones[0], soluciones[1], soluciones[2], soluciones_vertice[0], rango_Dominio[0], rango_Dominio[1]]
        return lista_preguntas, lista_repuestas, pregunta
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
    preguntas = ["Cuáles son los cortes con los ejes x e y", "Cuál es el dominio y el rango de la función"]
    ecuaciones_cubicas = [  ["2x³ - 3x² - 11x + 6", ["0,6", "(3,0)","(0.5,0)","(-2,0)"], ["R","R"]],
                          ["-x³ + 5x² - 2x + 7", ["0,7", "(3.03,0)","(-0.86,0)","(2.83,0)"], ["R","R"]],
                          ["3x³ + 2x² - x + 1", ["0,1", "(-1,0)","(-0.34,0)","(0.64,0)"], ["R","R"]],
                          ["2x³ - 3x² + 4x - 5", ["0,-5", "(1.33,0)","(-0.89,0)","(1.06,0)"], ["R","R"]],
                          ["-4x³ + x² + 3x - 8", ["0,-8", "(2.27,0)","(-1.08,0)","(0.88,0)"], ["R","R"]],
                          ["5x³ - 6x² + 7x + 2", ["0,2", "(-0.23,0)","(-1.21,0)","(0.79,0)"], ["R","R"]],
                          ["x³ - 4x² + 6x - 3",  ["0,-3", "(1,0)","(1,0)","(3,0)"], ["R", "R"]],
                          ["-2x³ + 3x² - 5x + 4", ["0,4", "(-1.22,0)","(1.28,0)","(0.93,0)"], ["R","R"]]]
    pregunta = random.choice(preguntas)
    funcion, cortes, dominio_rango = random.choice(ecuaciones_cubicas)
    mensaje = f"Rapido, analiza la funcion {funcion}"
    if pregunta == preguntas[0]:
        corte_y = "Cual es el corte en y (con este formato: 0,y): "
        corte_x1 = "Cual es el corte en x1 (con este formato: (x,0)):"
        corte_x2 = "Cual es el corte en x2 (con este formato: (x,0)):"
        corte_x3 = "Cual es el corte en x3 (con este formato: (x,0)):"
        lista_preguntas=[corte_y,corte_x1,corte_x2,corte_x3]
        lista_respuestas=[cortes[0],cortes[1],cortes[2],cortes[3]]
        return lista_preguntas,lista_respuestas,mensaje
    elif pregunta == preguntas[1]:
            dominio = "Cual es el dominio de la funcion?"
            rango = "Cual es el rango de la funcion?"
            lista_preguntas = [dominio,rango]
            lista_respuestas = dominio_rango
            return lista_preguntas,lista_respuestas,mensaje

def f_raiz_cuadrada():
    global suma4
    suma4 = random.randint(1, 5)
    functions = [
        ["sqrt(x)", "x|x>=0", "0", "0"],                              # Función raíz cuadrada de x
        ["sqrt(x^2 - 9)", "x|x<=-3,x>=3", "-3", "3", "0"],       # Función raíz cuadrada de x^2 - 9
        ["sqrt(4x^2 + 16x + 16)", "R", "-2", "-2", "4"],  # Función raíz cuadrada de 4x^2 + 16x + 16
        ["sqrt(x-1)", "x|x>=1", "1", "0"],                            # Función raíz cuadrada de x-1
        ["sqrt(4-x^2)", "x|x-2<=x<=2", "-2", "2", "2"]              # Función raíz cuadrada de 4-x^2
    ]
    
    if suma4 == 1:
        pregunta = f"¡Rápido analiza la siguiente función: {functions[0][0]}!"
        pregunta1 = "¿Cuál es el dominio?"
        pregunta2 = "¿Cuál es el corte con el eje X?"
        pregunta3 = "¿Cuál es el corte con el eje Y?"
        lista_preguntas = [pregunta1, pregunta2, pregunta3]
        lista_respuestas = [functions[0][1], functions[0][2], functions[0][3]]
        return lista_preguntas, lista_respuestas, pregunta
    
    elif suma4 == 2:
        pregunta = f"¡Rápido analiza la siguiente función: {functions[1][0]}!"
        pregunta1 = "¿Cuál es el dominio?"
        pregunta2 = "¿Cuál es el corte con el eje X1?"
        pregunta3 = "¿Cuál es el corte con el eje X2?"
        pregunta4 = "¿Cuál es el corte con el eje Y?"
        lista_preguntas = [pregunta1, pregunta2, pregunta3, pregunta4]
        lista_respuestas = [functions[1][1], functions[1][2], functions[1][3], functions[1][4]]
        return lista_preguntas, lista_respuestas, pregunta
    
    elif suma4 == 3:
        pregunta = f"¡Rápido analiza la siguiente función: {functions[2][0]}!"
        dominio = "¿Cuál es el Dominio?"
        ejex = "¿Cuál es el corte con el eje X?"
        ejey = "¿Cuál es el corte con el eje Y?"
        lista_preguntas = [dominio, ejex, ejey]
        lista_respuestas = [functions[2][1], functions[2][2], functions[2][3]]
        return lista_preguntas, lista_respuestas, pregunta
    
    elif suma4 == 4:
        pregunta = f"¡Rápido analiza la siguiente función: {functions[3][0]}!"
        dominio = "¿Cuál es el dominio?"
        ejex = "¿Cuál es el corte con el eje X?"
        ejey = "¿Cuál es el corte con el eje Y?"
        lista_preguntas = [dominio, ejex, ejey]
        lista_respuestas = [functions[3][1], functions[3][2], functions[3][3]]
        return lista_preguntas, lista_respuestas, pregunta
    
    elif suma4 == 5:
        pregunta = f"¡Rápido analiza la siguiente función: {functions[4][0]}!"
        dominio = "¿Cuál es el dominio?"
        ejex = "¿Cuál es el corte con el eje X?"
        ejey = "¿Cuál es el corte con el eje Y?"
        lista_preguntas = [dominio, ejex, ejey]
        lista_respuestas = [functions[4][1], functions[4][2], functions[4][4]]
        return lista_preguntas, lista_respuestas, pregunta


def parte_entera():
    lista_pregunta = ["¿Cual es el resultado de la funcion(piso)?"]
    ejercicios_parte_entera = [
    ["F(x) = ⌊3.7⌋", ["3"]],
    ["G(x) = ⌈sqrt 46⌉", ["6"]],
    ["H(x) = ⌊2.5⌋", ["2"]],
    ["J(x) = ⌈sqrt 61⌉", ["7"]],
    ["K(x) = ⌊-pi⌋", ["-4"]]
    ]
    funcion,parte_entera = random.choice(ejercicios_parte_entera)  
    preguntas = f"Rápido analiza la siguiente función: {funcion}" 
    lista_respuestas = parte_entera
    return lista_pregunta,lista_respuestas,preguntas
    

def f_valor_absoluto():
    lista_pregunta = ["¡Encuentra los puntos donde la funcion se anula!"]  
    funciones_absolutas = [
        ["f(x)= |3X**2-75|",["+-5"]],
        ["g(x)= |2x**2-32|",["+-4"]],
        ["h(x)=|4x**2-36|",["+-3"]],
        ["j(x)=|5x**2-25|",["+-1"]]
        ]
        
    funcion,absoluto = random.choice(funciones_absolutas)
    preguntas = f"Rapido analiza la siguente funcion: {funcion}"
    
    lista_repuesta = absoluto
    return lista_pregunta,lista_repuesta,preguntas
        
def inversa():
    lista_pregunta = ["¡Encuentra las la funcion inversa!"]
    funciones_inversas = [
        ["F(x) = 2x + 1",[ "f^-1(x) = (x - 1) / 2"]],
        ["G(x) = 3x - 2",[ "g^-1(x) = (x + 2) / 3"]],
        ["H(x) = (x + 4) / 5", ["h^-1(x) = 5x - 4"]],
        ["J(x) = (2x - 3) / 4", ["j^-1(x) = 2x+3/2"]],
        ["K(x) = (x - 7) / 3", ["k^-1(x) = 3x + 7"]]
        ["¿Una funcion que al aplicarse una funcion compuesta\ncon otra funcion produce el argumento?", ["verdadero"]]]
    
    funcion,inversa = random.choice(funciones_inversas)
    preguntas = f"Rapido analiza la siguente funcion: {funcion}"
    
    lista_respuestas = inversa
    
    return lista_pregunta,lista_respuestas,preguntas
    

def logaritmica():
    lista_pregunta = ["Analiza la pregunta"]
    
    preguntas_logaritmicas = [["¿cual es la base que tiene el logaritmo? natural", ["e"]],
    ["¿cual es la base que tiene el logaritmo si no se especifica la base?", ["10"]],
    ["segun la propiedad de los logaritmos log(a*b) es igual a \nlog(a) + log(b), ¿verdadero o falso?", ["verdadero"]],
    ["segun la propiedad de los logaritmos log(a/b) es  igual a\n log(a) * log(b), ¿verdadero o falso?", ["falso"]],
    ["¿la funcione inversa del logaritmo es x**2¿ verdadero o falso?", ["falso"]],
    ["¿cual es el dominio de f(x) = log(x**2 - 4)", ["(-oo,-2)u (2,oo)"]]]
    funcion,respuesta = random.choice(preguntas_logaritmicas)
    preguntas = f" {funcion}"
    return lista_pregunta,respuesta,preguntas
    
def exponencial():
    lista_pregunta = ["Analiza la pregunta"]
    
    preguntas_exponenciales = [["¿la funcion inversa de la funcion exponencial es el logaritmo? \nverdadero o falso", ["verdadero"]],
                               ["¿Qué representa la base en una función exponencial?", ["la tasa de crecimiento o decrecimiento"]],
                               ["¿la funciones f(x)= 2**x es creciente o decreciente?",[ "creciente"]],
                                ["¿el dominio de una funciones exponencial son todos los reales? \nverdadero o falso", ["verdadero"]],
                                ["¿cuales de las siguentes funciones es una funcion exponencias?\n a) f(x)=mx+b b) f(x)= x**2 c) f(x) = (1/2)**x",["c"]]]
    
    funcion,respuesta = random.choice(preguntas_exponenciales)
    preguntas = f" {funcion}"
    return lista_pregunta,respuesta,preguntas

def hiperbolicas():
    lista_pregunta = ["Analiza la pregunta"]
    
    preguntas_hiperbolicas = [["¿la funcion inversa de f(X) = sinh(x) es f^-1(x) = ln(x + sqrt(x**2 + 1))?\nverdadero o falso", ["verdadero"]],
                              ["¿la funcion inversa de f(X) = cosh(x) es f^-1(x) = ln(x + sqrt(x**2 - 2))?\nverdadero o falso", ["falso"]],
                              ["Cosh (x) = (e**x + e**-x) / 2 \n verdadero o falso", ["verdadero"]],
                              ["sinh(x) = (e**x - e**-x) / 4 \n verdadero o falso", ["falso"]]]
                            

    funcion,respuesta = random.choice(preguntas_hiperbolicas)
    preguntas = f" {funcion}"
    return lista_pregunta,respuesta,preguntas

def impar_par():
    lista_pregunta = ["Analiza la pregunta"]
    preguntas_pares_impares = [["¿la funcion f(x) = x**2 es par o impar?", ["par"]],
                               ["¿la funcion f(x) = cos(x) es par o impar?", ["par"]],
                               ["¿la funcion f(x) = x**4 es par o impar?", ["par"]],
                               ["¿la funcion f(x) = x**5 es par o impar?", ["impar"]],
                               ["¿la funcion f(x) = x**3-x es par o impar?", ["impar"]]]
    funcion,respuesta = random.choice(preguntas_pares_impares)
    preguntas = f" {funcion}"
    return lista_pregunta,respuesta,preguntas

def inyectibilidad():
    lista_pregunta = ["Analiza la pregunta"]
    preguntas_inyectibilidad = [["¿la funcion f(x) = x**2 es inyectiva?\nverdadero o falso", ["falso"]],
                                ["¿la funcion f(X) = 2x -3 es inyectiva?\nverdadero o falso", ["verdadero"]],
                              ["en una funcion inyectiva, cada valor de x tiene un unico valor de y asociado\nverdadero o falso", ["verdadero"]],
                              ["¿la funcion f(x) = x**3 es inyectiva?\nverdadero o falso", ["verdadero"]]]
                              
    funcion,respuesta = random.choice(preguntas_inyectibilidad)
    preguntas = f" {funcion}"
    return lista_pregunta,respuesta,preguntas
    
if __name__ == '__main__':
    
    random_f()