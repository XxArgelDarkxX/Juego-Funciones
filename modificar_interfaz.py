import customtkinter as ctk
import funciones as f
import interfaz
from tkinter import messagebox as mb
import time as t
from PIL import Image, ImageTk
import tkinter as tk

global i, vidas, puntos, x, y, j, nivel
j = 0
x = 100
y = 459
puntos = 0
i = 0
vidas = 9
nivel = 0


def puntuacion(ventana,corazones):  # <--- Aquí se crea la función que muestra la puntuación
    global puntos, vidas, x, y, nivel
    if puntos >= 1:  # <--- Aquí se verifica si el usuario ya ganó
        # <--- Aquí se muestra un mensaje de que el usuario ganó
        mb.showinfo("Ganaste", "Ganaste el juego")
        nivel += 1
        if nivel == 1:
            for i in range(9,7,-1):
                corazones[i].grid_forget()
                mb.showinfo("Nivel 2", "Felicidades, has pasado al nivel 2")
                interfaz.cambiar_enemigo()
                ventana.update_idletasks()
                
        elif nivel == 2:
            for i in range(7,5,-1):
                corazones[i].grid_forget()
                vidas = 5
                mb.showinfo("Nivel 3", "Felicidades, has pasado al nivel 3")
                interfaz.cambiar_enemigo()
                ventana.update_idletasks()
                
        elif nivel == 3:
            for i in range(5,3,-1):
                corazones[i].grid_forget()
                vidas = 3
                mb.showinfo("Nivel 4", "Felicidades, has pasado al nivel 4")
                interfaz.cambiar_enemigo()
                ventana.update_idletasks()
        elif nivel == 4:
            for i in range(3,1,-1):
                corazones[i].grid_forget()
                vidas = 1
                mb.showinfo("Nivel 5", "Felicidades, has pasado al nivel 5")
                interfaz.cambiar_enemigo()
                ventana.update_idletasks()
                
    else:
        x = 100
        y = 459


def fuego(fuego, label):  # <-- animacion de fallos
    x = 1000
    y = 359
    j = 0
    while x > 100:
        label.configure(image=fuego[j])
        label.place(x=x, y=y)
        j += 1
        if j == 50:
            j = 0
        x -= 80
        label.update_idletasks()
    label.after(100, label.place_forget)
    label.update_idletasks()


def kamehameha(gif, label_gif, window, corazones):  # <-- animacion de aciertos
    global x, y, j, vidas, puntos

    if x < 1000:
        label_gif.place(x=x, y=y)
        label_gif.configure(image=gif[j])
        j += 1

        if j == 50:
            j = 0

        x += 80  # Move the image to the right

        # Hide the image after 100 ms
        window.after(100, label_gif.place_forget)
        # Call kamehameha again after 100 ms
        window.after(100,lambda: kamehameha(gif, label_gif, window, corazones))
    else:
        puntuacion(window, corazones)

# verifica que la respuesta este bien y que la lista no haya acabado


def verificar(respond, respond_entry, label_see, ask, label_ask, button, corazones, ventana, foto, aciertos, gif, label_gif, fire, label_fire):
    global i, vidas, puntos, x, y, j
    # <--- Aquí se compara la respuesta del usuario con la respuesta correcta
    if respond == respond_entry.get().strip():
        respond_entry.delete(0, ctk.END)
        # <--- Aquí se muestra un mensaje de que la respuesta es correcta
        mb.showinfo("Correcto", "Respuesta correcta")
        puntos += 1
        # <--- Aquí se actualiza el número de aciertos
        aciertos.configure(text="Aciertos: "+str(puntos))
        kamehameha(gif, label_gif, ventana, corazones)
        i += 1  # <--- Aquí se aumenta el contador de preguntas
        if i == len(ask):  # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla
            i = 0  # <--- Aquí se reinicia el contador de preguntas
            # <--- Aquí se obtienen nuevas preguntas
            preguntas, respuestas, pregunta = f.random_f()
            # <--- Aquí se llama a la función que modifica la interfaz
            return modificar_interfaz(preguntas, pregunta, respuestas, label_ask, button, respond_entry, label_see, corazones, ventana, foto, aciertos, gif, label_gif, fire, label_fire)
        label_see.configure(text=ask[i])  # <--- Aquí se actualiza la pregunta
        label_see.update_idletasks()  # <-- actualiza la interfaz
        # <--- Aquí se borra el contenido del entry
        respond_entry.delete(0, ctk.END)
        return True
    else:
        # <--- Aquí se borra el contenido del entry
        respond_entry.delete(0, ctk.END)
        # <--- Aquí se muestra un mensaje de que la respuesta es incorrecta
        mb.showinfo("Incorrecto", "Respuesta incorrecta")
        # <--- Aquí se cambia la imagen del corazón
        corazones[vidas].configure(image=foto)
        vidas -= 1
        fuego(fire, label_fire)
        if vidas == -1:  # <--- Aquí se verifica si el usuario ya no tiene vidas
            mb.showerror("Perdiste", "Perdiste todas tus vidas")
            respuesta = mb.showinfo(
                "intentae", "quieres volver a intentar?", type="yesno")
            if respuesta == "yes":
                vidas = 9
                puntos = 0
                ventana.destroy()
                interfaz.juego()
            else:
                mb.showinfo("Gracias por jugar", "Gracias por jugar")
                ventana.destroy()
        i += 1  # <--- Aquí se aumenta el contador de preguntas
        if i == len(ask):  # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla
            i = 0  # <--- Aquí se reinicia el contador de preguntas
            # <--- Aquí se obtienen nuevas preguntas
            preguntas, respuestas, pregunta = f.random_f()
            # <--- Aquí se llama a la función que modifica la interfaz
            return modificar_interfaz(preguntas, pregunta, respuestas, label_ask, button, respond_entry, label_see, corazones, ventana, foto, aciertos, gif, label_gif, fire, label_fire)
        label_see.configure(text=ask[i])  # <--- Aquí se actualiza la pregunta
        label_see.update_idletasks()  # <-- actualiza la interfaz
        return False


# <--- Aquí se crea la función que modifica la interfaz
def modificar_interfaz(ask, see, respond, label_ask, button, respond_entry, label_see, corazones, ventana, foto, aciertos, gif, label_gif, fire, label_fire):
    global i, vidas  # <--- Aquí se declara la variable global i
    if i == len(ask):  # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla
        i = 0
        vidas = 9  # <--- Aquí se reinicia el contador de preguntas
        ask, see, respond = f.random_f()  # <--- Aquí se obtienen nuevas preguntas
    label_ask.configure(text=see)  # <--- Aquí se actualiza la función
    label_see.configure(text=ask[i])  # <--- Aquí se actualiza la pregunta
    button.focus_set()  # <--- Aquí se le da el foco al botóny
    button.configure(command=lambda: verificar(respond[i], respond_entry, label_see, ask, label_ask, button, corazones,
                     # <--- Aquí se le asigna la función verificar al botón
                                               ventana, foto, aciertos, gif, label_gif, fire, label_fire))
