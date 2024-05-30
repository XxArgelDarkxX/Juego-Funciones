import customtkinter as ctk
import funciones as f
import interfaz
from tkinter import messagebox as mb
import time as t


def verificar(respond,respond_entry,label_see,ask):
    global i,b,a
    if respond==respond_entry.get():
        i+=1
        b+=1
        a-=1
        label_see.configure(text=ask[i]) 
        respond_entry.delete(0, ctk.END)
        mb.showinfo("Correcto","Respuesta correcta")
    else:
        i+=1
        b+=1
        a-=1
        label_see.configure(text=ask[i])
        respond_entry.delete(0, ctk.END)
        mb.showinfo("Incorrecto","Respuesta incorrecta")
        print("hola")
        return False
        
        

def modificar_interfaz(ask=None,see=None,respond=None,label_ask=None,button=None,respond_entry=None,label_see=None):
    global i,b,a
    a=len(ask)
    i=1
    b=0
    label_ask.configure(text=see)
    label_see.configure(text=ask[i])
    button.bind("<Button-1>",lambda e: verificar(respond[b],respond_entry,label_see,ask))