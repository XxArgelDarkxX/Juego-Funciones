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
    ventana.geometry("1260x720")
    ventana.configure(fg_color="#000014")


    # Crear un frame para mostrar la pregunta
    frame_pregunta = ctk.CTkFrame(ventana)
    frame_pregunta.place(x = 600, y = 20)
    label_pregunta = ctk.CTkLabel(frame_pregunta, text="¿Qué es un dragón?", font=("Arial", 20))
    label_pregunta.grid(row=0, column=0)
    
    # crear frame  entWry respuesta
    frame_respuesta = ctk.CTkFrame(ventana)
    frame_respuesta.place(x = 50, y = 20)
    respuesta = ctk.CTkEntry(frame_respuesta, font=("Arial", 20))
    respuesta.grid(row=0, column=0)     
    
    frame_video = ctk.CTkFrame(ventana)
    frame_video.configure(fg_color= "red")
    frame_video.place(x =850, y = 250)  # Cambia estos valores para mover el video

    # Crear un label para mostrar el video
    video_label = ctk.CTkLabel(frame_video, text="", font=("Arial", 20))
    video_label.grid(row=0, column=0)
    
    frame_video2 = ctk.CTkFrame(ventana)
    frame_video2.configure(fg_color= "red")
    frame_video2.place(x =50, y = 459)  # Cambia estos valores para mover el video
    
    video_label2 = ctk.CTkLabel(frame_video2, text="", font=("Arial", 20))
    video_label2.grid(row=0, column=0)
    
    
    frame_button_verificar = ctk.CTkFrame(ventana)
    frame_button_verificar.place(x = 500, y = 600)
    frame_button_verificar.configure(fg_color= "red")
    
    # frame label pregunata
    frame_pregunta_actualiza = ctk.CTkFrame(ventana)
    frame_pregunta_actualiza.place(x = 50, y = 250)
    label_pregunta_actualiza = ctk.CTkLabel(frame_pregunta_actualiza, text="Pregunta actualizada", font=("Arial", 20))
    label_pregunta_actualiza.grid(row=0, column=0)
    def verificar(respuesta_usuario):

        if respuesta_usuario == "":
            mb.showerror("Error", "No has ingresado una respuesta")
        else:
            mb.showinfo("Respuesta", "Tu respuesta es: " + respuesta_usuario)
    
    buton_verficar = ctk.CTkButton(frame_button_verificar, text="Verificar", font=("Arial", 20))

    buton_verficar.grid(row=0, column=0)   
    cap = cv2.VideoCapture('dragon.mp4')
    cap2 = cv2.VideoCapture('lapiz.mp4')    
    
    #lista de preguntas desde la funcion de preguntas
    preguntas,respuestas,pregunta= f.random_f()
    if mi.modificar_interfaz(preguntas,pregunta,respuestas,label_pregunta,buton_verficar,respuesta,label_pregunta_actualiza)==True:
        print("monkey")
    else:
        print("no monkey")
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

    

if __name__ == "__main__":
    juego()
    
