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
    ventana.resizable(False, False) # <--- Aquí se crea la ventana principal
    #gift
    gif = [ImageTk.PhotoImage(file="kamehameha.gif", format='gif -index %i' % i) for i in range(50)]  # <--- Aquí se carga el gif
    label_gif = ctk.CTkLabel(ventana) # <--- Aquí se crea un label para mostrar el gif
    # frame imagen corazon
    frame_corazon = ctk.CTkFrame(ventana) # <--- Aquí se crea un frame para los corazones
    frame_corazon.place(x = 50, y = 765)
    frame_corazon.configure(fg_color= "#000014")
    imagen_corazon = Image.open("corazon.png")
    cora_roto = Image.open("corazon_muerte.png")
    cora_roto = cora_roto.resize((50, 50))
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
    frame_aciertos.place(x = 1000, y = 900)
    frame_aciertos.configure(fg_color= "#000014")
    label_aciertos = ctk.CTkLabel(frame_aciertos, text="Aciertos: 0", font=("Algerian", 35))
    label_aciertos.grid(row=0, column=0)
    # Crear un frame para mostrar ecuacion
    frame_pregunta = ctk.CTkFrame(ventana)
    frame_pregunta.place(x = 300,y = 20)
    frame_pregunta.configure(fg_color= "#000014")
    label_pregunta = ctk.CTkLabel(frame_pregunta, text="¿Qué es un dragón?", font=("Algerian", 30))
    label_pregunta.grid(row=0, column=0)
    
    # crear frame  entry respuesta
    frame_respuesta = ctk.CTkFrame(ventana)
    frame_respuesta.place(x = 655, y = 700)
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
    frame_video2.place(x =-70, y = 459)  # Cambia estos valores para mover el video
    
    video_label2 = ctk.CTkLabel(frame_video2, text="", font=("Arial", 20))
    video_label2.grid(row=0, column=0)
    
    #frame para boton verificar
    frame_button_verificar = ctk.CTkFrame(ventana)
    frame_button_verificar.place(x = 600, y = 750)
    frame_button_verificar.configure(fg_color= "purple")
    frame_button_verificar.configure(width=1000, height=500)
    
    # frame para mostrar pregunta actualizada
    frame_pregunta_actualiza = ctk.CTkFrame(ventana)
    frame_pregunta_actualiza.place(x = 400, y = 150)
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
    mi.modificar_interfaz(preguntas,pregunta,respuestas,label_pregunta,buton_verficar,respuesta,label_pregunta_actualiza,corazones,ventana,foto1,label_aciertos,gif,label_gif)

        
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


def return_to_menu(ventana):
    ventana.destroy()
    menu()

def info(window):
    window.destroy()
    ventana = ctk.CTk()
    ventana.title("Información")
    ventana.geometry("1550x900")
    ventana.configure(fg_color="#000014")
    ventana.resizable(False, False)
    label_info = ctk.CTkLabel(ventana, text="", font=("Arial", 30))
    label_info.place(x = 250, y = 50)
    button_regresar = ctk.CTkButton(ventana, text="Regresar", font=("Arial", 20), width=10, height=2, command=lambda: return_to_menu(ventana))  # Botón para regresar al menú
    button_regresar.place(x = 50, y = 800)

    message = """
    Instructivo de las Reglas del Juego: La Batalla contra el Dragón\n
    ¡Bienvenido a la emocionante Batalla contra el Dragón! Antes de embarcarte en esta aventura épica,
    es crucial que comprendas las reglas del juego para que puedas luchar valientemente y triunfar
    . Aquí te las presentamos de manera clara y sencilla:

    Objetivo del Juego:
    Derrotar al Dragón obteniendo 10 aciertos.
    Reglas del Juego:
    Aciertos y Fallas:

    Cada acción que realices en el juego puede resultar en un acierto o una falla.
    Necesitas acumular 10 aciertos para derrotar al Dragón y ganar el juego.
    Si acumulas 10 fallas, tu personaje morirá y el juego terminará. """

    def update_text(i=0):
        if i < len(message):
            label_info.configure(text=label_info.cget("text") + message[i],font=("Kristen ITC",20))
            ventana.after(25, update_text, i + 1)  # Agrega una letra cada 100 milisegundos

    update_text()  # Comienza la animación

    ventana.mainloop()

def menu():
    ventana = ctk.CTk()
    ventana.title("Juego Funciones")
    ventana.geometry("1550x900")
    ventana.configure(fg_color="#000014")
    ventana.resizable(False, False)
    
    # frame imagen dragon
    frame_dragon = ctk.CTkFrame(ventana)
    frame_dragon.place(x = 1000, y = 250)
    frame_dragon.configure(fg_color="#000014")
    imagen_dragon_menu = Image.open("dragon_1.png")
    
    
    
    imagen_dragon_menu = imagen_dragon_menu.resize((600, 600))
    foto_dragon_menu = ImageTk.PhotoImage(imagen_dragon_menu)
    label_dragon_menu = ctk.CTkLabel(frame_dragon, text="", image=foto_dragon_menu)
    label_dragon_menu.grid(row=0, column=0)
    

    # frame imagen lapiz
    frame_lapiz = ctk.CTkFrame(ventana)
    frame_lapiz.place(x = 10, y = 350)
    frame_lapiz.configure(fg_color="#000014")
    imagen_lapiz_menu = Image.open("lapiz_menu.png")
    imagen_lapiz_menu = imagen_lapiz_menu.resize((600, 600))
    foto_lapiz_menu = ImageTk.PhotoImage(imagen_lapiz_menu)
    label_lapiz_menu = ctk.CTkLabel(frame_lapiz, text="", image=foto_lapiz_menu)
    label_lapiz_menu.grid(row=0, column=0)
   
   # frame imagen fx
    frame_fx = ctk.CTkFrame(ventana)
    frame_fx.place(x = 50, y = 50)
    frame_fx.configure(fg_color="#000014")
    imagen_fx_menu = Image.open("fx_menu.png")
    imagen_fx_menu = imagen_fx_menu.resize((400,400))
    foto_fx_menu = ImageTk.PhotoImage(imagen_fx_menu)
    label_fx_menu = ctk.CTkLabel(frame_fx, text="", image=foto_fx_menu)
    label_fx_menu.grid(row=0, column=0)
    

    
    frame_menu = ctk.CTkFrame(ventana)
    frame_menu.place(x = 650, y = 50)
    frame_menu.configure(fg_color="#000014")
    
    label_menu = ctk.CTkLabel(frame_menu, text="Juego de Funciones", font=("Kristen ITC", 30))
    label_menu.grid(row=5, column=0)
    
    # frame boton jugar
    frame_boton_jugar = ctk.CTkFrame(ventana)
    frame_boton_jugar.place(x = 650, y = 200)
    button_jugar = ctk.CTkButton(frame_boton_jugar, text="Jugar", font=("Kristen ITC", 30), width=300, height= 50)
    button_jugar.grid(row=0, column=0)
    
    # frame boton info
    frame_boton_info = ctk.CTkFrame(ventana)
    frame_boton_info.place(x = 650, y = 400)
    
    button_info = ctk.CTkButton(frame_boton_info, text="Información", font=("Kristen ITC", 30), width=300, height=50, command=lambda: info(ventana))
    button_info.grid(row=0, column=0)
    
    # frame boton salir
    frame_boton_salir = ctk.CTkFrame(ventana)
    frame_boton_salir.place(x = 650, y = 600)
    
    button_salir = ctk.CTkButton(frame_boton_salir, text="Salir", font=("Kristen ITC", 30), width=300, height=50)
    button_salir.grid(row=0, column=0)
    
    def jugar():
        ventana.destroy()
        juego()
    
    button_jugar.configure(command=jugar)
    
    def salir():
        ventana.destroy()
    
    button_salir.configure(command=salir)
    
    ventana.mainloop()

if __name__ == "__main__":
    menu()