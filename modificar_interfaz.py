import customtkinter as ctk
import funciones as f
import interfaz
from tkinter import messagebox as mb
import time as t
global i
i=0


# verifica que la respuesta este bien y que la lista no haya acabado
def verificar(respond,respond_entry,label_see,ask,label_ask,button):
    global i
    if respond==respond_entry.get(): # <--- Aquí se compara la respuesta del usuario con la respuesta correcta
        respond_entry.delete(0, ctk.END)
        mb.showinfo("Correcto","Respuesta correcta") # <--- Aquí se muestra un mensaje de que la respuesta es correcta 
        
        
        i+=1
        if i==len(ask) : # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla
            i=0 # <--- Aquí se reinicia el contador de preguntas
            preguntas,respuestas,pregunta=f.random_f() # <--- Aquí se obtienen nuevas preguntas
            return modificar_interfaz(preguntas,pregunta,respuestas,label_ask,button,respond_entry,label_see) # <--- Aquí se llama a la función que modifica la interfaz
        label_see.configure(text=ask[i])  # <--- Aquí se actualiza la pregunta 
        label_see.update_idletasks()  #  <-- actualiza la interfaz
        respond_entry.delete(0, ctk.END) # <--- Aquí se borra el contenido del entry
        return True
    else:
        respond_entry.delete(0, ctk.END) # <--- Aquí se borra el contenido del entry
        mb.showinfo("Incorrecto","Respuesta incorrecta") # <--- Aquí se muestra un mensaje de que la respuesta es incorrecta
        
        i+=1 # <--- Aquí se aumenta el contador de preguntas
        if i==len(ask) : # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla
            i=0 # <--- Aquí se reinicia el contador de preguntas
            preguntas,respuestas,pregunta=f.random_f() # <--- Aquí se obtienen nuevas preguntas
            return modificar_interfaz(preguntas,pregunta,respuestas,label_ask,button,respond_entry,label_see)  # <--- Aquí se llama a la función que modifica la interfaz
        label_see.configure(text=ask[i])  # <--- Aquí se actualiza la pregunta
        label_see.update_idletasks()  #  <-- actualiza la interfaz
        return False 

def modificar_interfaz(ask=None,see=None,respond=None,label_ask=None,button=None,respond_entry=None,label_see=None,corazones=None): # <--- Aquí se crea la función que modifica la interfaz
    global i  # <--- Aquí se declara la variable global i
    if i==len(ask): # <--- Aquí se verifica si la lista de preguntas se acabó para reiniciarla 
        i=0 # <--- Aquí se reinicia el contador de preguntas
        ask,see,respond=f.random_f() # <--- Aquí se obtienen nuevas preguntas
    label_ask.configure(text=see)  # <--- Aquí se actualiza la función
    label_see.configure(text=ask[i]) # <--- Aquí se actualiza la pregunta
    button.configure(command=lambda: verificar(respond[i],respond_entry,label_see,ask,label_ask,button)) # <--- Aquí se le asigna la función verificar al botón