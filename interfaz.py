import random
import math
import threading
import time
import cv2
from PIL import Image, ImageTk
import customtkinter as ctk  # Asegúrate de tener el paquete customtkinter instalado
import funciones  # Asumiendo que el código anterior está en un archivo llamado funciones.py
import tkinter.messagebox as mb # Asegúrate de inicializar la lista de preguntas
funciones.lista_preguntas = []

def mostrar_pregunta():
    if funciones.lista_preguntas:
        return funciones.lista_preguntas[-1]
    return "No hay preguntas disponibles"

def actualizar_pregunta():
    funciones.random_f()
    label_pregunta_actualiza.configure(text=mostrar_pregunta())

ventana = ctk.CTk()

# Configuración de la ventana principal
ventana.geometry("1280x720")
ventana.title("Juego de Funciones")

frame_video = ctk.CTkFrame(ventana)
frame_video.configure(fg_color="red")
frame_video.place(x=850, y=250)  # Cambia estos valores para mover el video

# Crear un label para mostrar el video
video_label = ctk.CTkLabel(frame_video, text="", font=("Arial", 20))
video_label.grid(row=0, column=0)

frame_video2 = ctk.CTkFrame(ventana)
frame_video2.configure(fg_color="red")
frame_video2.place(x=50, y=459)  # Cambia estos valores para mover el video

video_label2 = ctk.CTkLabel(frame_video2, text="", font=("Arial", 20))
video_label2.grid(row=0, column=0)


# Frame label pregunta
frame_pregunta_actualiza = ctk.CTkFrame(ventana)
frame_pregunta_actualiza.configure(width=1000, height=500)
frame_pregunta_actualiza.place(x=100, y=100)
frame_pregunta_actualiza.configure(fg_color="green")

label_pregunta_actualiza = ctk.CTkLabel(frame_pregunta_actualiza, text=mostrar_pregunta(), font=("Arial", 20))
label_pregunta_actualiza.grid(row=0, column=0)


#frame entry respuesta
frame_respuesta = ctk.CTkFrame(ventana) 
frame_respuesta.configure(width=1000, height=500)
frame_respuesta.place(x=100, y=300)
frame_respuesta.configure(fg_color="blue")
respuesta = ctk.CTkEntry(frame_respuesta, font=("Arial", 20))
respuesta.grid(row=0, column=0)

# Botón para generar una nueva pregunta
button_nueva_pregunta = ctk.CTkButton(ventana, text="Nueva Pregunta", font=("Arial", 20), command=actualizar_pregunta)
button_nueva_pregunta.place(x=500, y=50)



def verificar(respuesta_usuario):
    if respuesta_usuario == "":
        mb.showerror("Error", "No has ingresado una respuesta")
    else:
        if respuesta_usuario in funciones.cuadratica()[0][0]:
            mb.showinfo("Correcto", "Respuesta correcta")
        else:
            mb.showerror("Incorrecto", "Respuesta incorrecta")

# buton_verficar = ctk.CTkButton(frame_button_verificar, text="Verificar", font=("Arial", 20), command=lambda: verificar(respuesta.get()))
# buton_verficar.grid(row=0, column=0)

cap = cv2.VideoCapture('dragon.mp4')
cap2 = cv2.VideoCapture('lapiz.mp4')

def play_video():
    while True:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Redimensionar el frame
        frame = cv2.resize(frame, (500, 500))  # Cambia estos valores para cambiar el tamaño del video

        # Convertir el frame a una imagen de PIL y luego a una imagen de Tkinter
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        # Mostrar la imagen en el label
        video_label.configure(image=image)
        video_label.image = image

        time.sleep(0.05)

def play_video2():
    while True:
        ret, frame = cap2.read()
        if not ret:
            cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Redimensionar el frame
        frame = cv2.resize(frame, (320, 240))  # Cambia estos valores para cambiar el tamaño del video

        # Convertir el frame a una imagen de PIL y luego a una imagen de Tkinter
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        # Mostrar la imagen en el label
        video_label2.configure(image=image)
        video_label2.image = image

        time.sleep(0.03)

# Crear y comenzar un nuevo hilo para reproducir el video
thread = threading.Thread(target=play_video)
thread2 = threading.Thread(target=play_video2)
thread2.start()
thread.start()
ventana.mainloop()

