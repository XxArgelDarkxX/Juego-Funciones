import customtkinter as ctk
import funciones as f
import interfaz
from tkinter import messagebox as mb
import time as t
global i
i=0


def verificar(respond,respond_entry,label_see,ask,label_ask,button):
    global i
    if respond==respond_entry.get():
        respond_entry.delete(0, ctk.END)
        mb.showinfo("Correcto","Respuesta correcta")
        i+=1
        if i==len(ask) :
            i=0
            preguntas,respuestas,pregunta=f.random_f()
            return modificar_interfaz(preguntas,pregunta,respuestas,label_ask,button,respond_entry,label_see)
        label_see.configure(text=ask[i]) 
        label_see.update_idletasks()  # Agrega esta línea
        respond_entry.delete(0, ctk.END)
        return True
    else:
        respond_entry.delete(0, ctk.END)
        mb.showinfo("Incorrecto","Respuesta incorrecta")
        i+=1
        if i==len(ask) :
            i=0
            preguntas,respuestas,pregunta=f.random_f()
            return modificar_interfaz(preguntas,pregunta,respuestas,label_ask,button,respond_entry,label_see)
        label_see.configure(text=ask[i])
        label_see.update_idletasks()  # Agrega esta línea
        return False

def modificar_interfaz(ask=None,see=None,respond=None,label_ask=None,button=None,respond_entry=None,label_see=None):
    global i
    if i==len(ask):
        i=0
        ask,see,respond=f.random_f()
    label_ask.configure(text=see)
    label_see.configure(text=ask[i])
    button.configure(command=lambda: verificar(respond[i],respond_entry,label_see,ask,label_ask,button))