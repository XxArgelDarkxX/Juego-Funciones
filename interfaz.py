import customtkinter as ctk
import funciones as f
from PIL import Image, ImageTk
import threading
import cv2
import time
from tkinter import messagebox as mb
import funciones as f
import modificar_interfaz as mi

# color del fondo dragon(todo) : #000014

def juego():
    ventana = ctk.CTk()
    ventana.title("Juego Funciones")
    ventana.geometry("1550x900")
    ventana.configure(fg_color="#000014")
    ventana.resizable(False, False)

    
    # frame imagen corazon
    frame_corazon = ctk.CTkFrame(ventana)
    frame_corazon.place(x = 50, y = 750)
    frame_corazon.configure(fg_color= "#000014")
    imagen_corazon = Image.open("corazon.png")
    cora_roto = Image.open("corazon_muerte.png")
    cora_roto = cora_roto.resize((75, 75))
    foto1=ImageTk.PhotoImage(cora_roto)
    corazones = []
    for i in range(10):
        imagen_corazon = imagen_corazon.resize((60, 60))
        foto = ImageTk.PhotoImage(imagen_corazon)
        label_corazon = ctk.CTkLabel(frame_corazon,text= "", image=foto)
        label_corazon.grid(row=0, column=i)
        corazones.append(label_corazon)
        
    # frame aciertos
    frame_aciertos = ctk.CTkFrame(ventana)
    frame_aciertos.place(x = 800, y = 500)
    frame_aciertos.configure(fg_color= "#000014")
    label_aciertos = ctk.CTkLabel(frame_aciertos, text="Aciertos: 0", font=("Arial", 20))
    label_aciertos.grid(row=0, column=0)
    # Crear un frame para mostrar ecuacion
    frame_pregunta = ctk.CTkFrame(ventana)
    frame_pregunta.place(x = 300,y = 20)
    frame_pregunta.configure(fg_color= "#000014")
    label_pregunta = ctk.CTkLabel(frame_pregunta, text="¿Qué es un dragón?", font=("Algerian", 30))
    label_pregunta.grid(row=0, column=0)
    
    # crear frame  entWry respuesta
    frame_respuesta = ctk.CTkFrame(ventana)
    frame_respuesta.place(x = 550, y = 500)
    respuesta = ctk.CTkEntry(frame_respuesta, font=("Arial", 20))
    respuesta.grid(row=0, column=0)     
    
    frame_video = ctk.CTkFrame(ventana)
    frame_video.configure(fg_color= "red")
    frame_video.place(x =1000, y = 200)  # Cambia estos valores para mover el video

    # Crear un label para mostrar el video
    video_label = ctk.CTkLabel(frame_video, text="", font=("Arial", 20))
    video_label.grid(row=0, column=0)
    
    frame_video2 = ctk.CTkFrame(ventana)
    frame_video2.configure(fg_color= "red")
    frame_video2.place(x =50, y = 459)  # Cambia estos valores para mover el video
    
    video_label2 = ctk.CTkLabel(frame_video2, text="", font=("Arial", 20))
    video_label2.grid(row=0, column=0)
    
    #frame para boton verificar
    frame_button_verificar = ctk.CTkFrame(ventana)
    frame_button_verificar.place(x = 600, y = 710)
    frame_button_verificar.configure(fg_color= "purple")
    frame_button_verificar.configure(width=1000, height=500)
    
    # frame para mostrar pregunta actualizada
    frame_pregunta_actualiza = ctk.CTkFrame(ventana)
    frame_pregunta_actualiza.place(x = 50, y = 250)
    frame_pregunta_actualiza.configure(fg_color= "#000014")

    label_pregunta_actualiza = ctk.CTkLabel(frame_pregunta_actualiza, text="Pregunta actualizada", font=("Algerian", 25))
    label_pregunta_actualiza.grid(row=0, column=0)

    # boton verificar
    buton_verficar = ctk.CTkButton(frame_button_verificar, text="Verificar", font=("Algerian", 50),width = 250,height=50)

    buton_verficar.grid(row=0, column=0)   
    cap = cv2.VideoCapture('dragon.mp4')
    cap2 = cv2.VideoCapture('lapiz.mp4')    
    
    #lista de preguntas desde la funcion de preguntas
    preguntas,respuestas,pregunta= f.random_f()
    mi.modificar_interfaz(preguntas,pregunta,respuestas,label_pregunta,buton_verficar,respuesta,label_pregunta_actualiza,corazones,ventana,foto1)

        
    def play_video():
        while True:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            # Redimensionar el frame
            frame = cv2.resize(frame, (700, 700))  # Cambia estos valores para cambiar el tamaño del video

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
            frame = cv2.resize(frame, (400, 300))  # Cambia estos valores para cambiar el tamaño del video

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

    

if __name__ == "__main__":
    juego()

