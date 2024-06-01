import customtkinter as ctk
import funciones as f
import interfaz
from tkinter import messagebox as mb
import time as t
from PIL import Image, ImageTk
import tkinter as tk
import pygame as pg 
global i,vidas,puntos,x,y,j
j=0
x=100
y=459
puntos=0
i=0
vidas=9
def puntuacion(ventana): # <--- Aquí se crea la función que muestra la puntuación
    global puntos,vidas,x,y
    if puntos==10: #<--- Aquí se verifica si el usuario ya ganó
        mb.showinfo("Ganaste","Ganaste el juego") # <--- Aquí se muestra un mensaje de que el usuario ganó
        respuesta=mb.showinfo("intentae","quieres volver a intentar?",type="yesno") # <--- Aquí se pregunta si el usuario quiere volver a intentar
        if respuesta=="yes":
            vidas=9
            puntos=0 
            x=100
            y=459
            ventana.destroy()
            interfaz.juego()
        else:
            mb.showinfo("Gracias por jugar","Gracias por jugar")
            ventana.destroy()
    else:
        x=100
        y=459


def fuego(fuego,label): # <-- animacion de fallos
    x=1000
    y=459
    j=0
    while x > 100:
        label.configure(image=fuego[j])
        label.place(x=x, y=y)
        j+=1
        if j==50:
            j=0
        x -= 80
        label.update_idletasks()
    label.after(100, label.place_forget)
    label.update_idletasks()
        



def kamehameha(gif, label_gif, window): # <-- animacion de aciertos
    global x, y, j, vidas, puntos

    if x < 1000:
        label_gif.place(x=x, y=y)
        label_gif.configure(image=gif[j])
        j += 1

        if j == 50:
            j = 0

        x += 80  # Move the image to the right

        window.after(100, label_gif.place_forget)  # Hide the image after 100 ms
        window.after(100, lambda: kamehameha(gif, label_gif, window))  # Call kamehameha again after 100 ms
    else:
        puntuacion(window)

# verifica que la respuesta este bien y que la lista no haya acabado
def verificar(respond,respond_entry,label_see,ask,label_ask,button,corazones,ventana,foto,aciertos,gif,label_gif,fire,label_fire):
    global i,vidas,puntos,x,y,j
    if respond==respond_entry.get().strip(): # <--- Aquí se compara la respuesta del usuario con la respuesta correcta
        respond_entry.delete(0, ctk.END)
        mb.showinfo("Correcto","Respuesta correcta") # <--- Aquí se muestra un mensaje de que la respuesta es correcta 
        puntos+=1
        aciertos.configure(text="Aciertos: "+str(puntos)) # <--- Aquí se actualiza el número de aciertos
        kamehameha(gif,label_gif,ventana)
        i+=1 # <--- Aquí se aumenta el contador de preguntas
        if i==len(ask) : # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla
            i=0 # <--- Aquí se reinicia el contador de preguntas
            preguntas,respuestas,pregunta=f.random_f() # <--- Aquí se obtienen nuevas preguntas
            return modificar_interfaz(preguntas,pregunta,respuestas,label_ask,button,respond_entry,label_see,corazones,ventana,foto,aciertos,gif,label_gif,fire,label_fire) # <--- Aquí se llama a la función que modifica la interfaz
        label_see.configure(text=ask[i])  # <--- Aquí se actualiza la pregunta 
        label_see.update_idletasks()  #  <-- actualiza la interfaz
        respond_entry.delete(0, ctk.END) # <--- Aquí se borra el contenido del entry
        return True
    else:
        respond_entry.delete(0, ctk.END) # <--- Aquí se borra el contenido del entry
        mb.showinfo("Incorrecto","Respuesta incorrecta") # <--- Aquí se muestra un mensaje de que la respuesta es incorrecta
        corazones[vidas].configure(image=foto) # <--- Aquí se cambia la imagen del corazón
        vidas-=1
        fuego(fire,label_fire)
        if vidas==-1: # <--- Aquí se verifica si el usuario ya no tiene vidas
            mb.showerror("Perdiste","Perdiste todas tus vidas")
            respuesta=mb.showinfo("intentae","quieres volver a intentar?",type="yesno")
            if respuesta=="yes":
                vidas=9
                puntos=0 
                ventana.destroy()
                interfaz.juego()
            else:
                mb.showinfo("Gracias por jugar","Gracias por jugar")
                ventana.destroy()
        i+=1 # <--- Aquí se aumenta el contador de preguntas
        if i==len(ask) : # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla
            i=0 # <--- Aquí se reinicia el contador de preguntas
            preguntas,respuestas,pregunta=f.random_f() # <--- Aquí se obtienen nuevas preguntas
            return modificar_interfaz(preguntas,pregunta,respuestas,label_ask,button,respond_entry,label_see,corazones,ventana,foto,aciertos,gif,label_gif,fire,label_fire)  # <--- Aquí se llama a la función que modifica la interfaz
        label_see.configure(text=ask[i])  # <--- Aquí se actualiza la pregunta
        label_see.update_idletasks()  #  <-- actualiza la interfaz
        return False 

def modificar_interfaz(ask,see,respond,label_ask,button,respond_entry,label_see,corazones,ventana,foto,aciertos,gif,label_gif,fire,label_fire): # <--- Aquí se crea la función que modifica la interfaz
    global i,vidas # <--- Aquí se declara la variable global i
    if i==len(ask): # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla 
        i=0 
        vidas=9# <--- Aquí se reinicia el contador de preguntas
        ask,see,respond=f.random_f() # <--- Aquí se obtienen nuevas preguntas
    label_ask.configure(text=see)  # <--- Aquí se actualiza la función
    label_see.configure(text=ask[i]) # <--- Aquí se actualiza la pregunta
    button.focus_set() # <--- Aquí se le da el foco al botón
    respond_entry.focus_set() # <--- Aquí se le da el foco al entry
    respond_entry.bind("<Return>", lambda event: verificar(respond[i],respond_entry,label_see,ask,label_ask,button,corazones,ventana,foto,aciertos,gif,label_gif,fire,label_fire)) # <--- Aquí se le asigna la función verificar al entry
    button.bind("<Return>", lambda event: verificar(respond[i],respond_entry,label_see,ask,label_ask,button,corazones,ventana,foto,aciertos,gif,label_gif,fire,label_fire)) # <--- Aquí se le asigna la función verificar al botón
    button.configure(command=lambda: verificar(respond[i],respond_entry,label_see,ask,label_ask,button,corazones,ventana,foto,aciertos,gif,label_gif,fire,label_fire)) # <--- Aquí se le asigna la función verificar al botón