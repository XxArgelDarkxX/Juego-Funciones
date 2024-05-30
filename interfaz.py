import customtkinter as ctk
import funciones
from PIL import Image, ImageTk
import threading
import cv2
import time
# color del fondo dragon(todo) : #000014

def juego():
    ventana = ctk.CTk()
    ventana.title("Juego Funciones")
    ventana.geometry("1260x720")
    ventana.configure(fg_color="#000014")



    label_pregunta = ctk.CTkLabel(ventana, text="¿Qué es un dragón?", font=("Arial", 20))
    label_pregunta.grid(row=0, column=0)
    
    respuesta = ctk.CTkEntry(ventana, font=("Arial", 20))
    respuesta.grid(row=1, column=0)     
    
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
    

    buton_verficar = ctk.CTkButton(frame_button_verificar, text="Verificar", font=("Arial", 20), command=lambda: funciones.verificar(respuesta.get()))

    buton_verficar.grid(row=0, column=0)   
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

    

if __name__ == "__main__":
    juego()
    