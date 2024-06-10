import customtkinter as ctk
from PIL import Image
import threading
import cv2
import time
from tkinter import messagebox as mb
import funciones as f
import modificar_interfaz as mi
import numpy as np
import random
# Global color setting
BACKGROUND_COLOR = "#033247"
# color fondo nuevo #033247

# Main game function

global indice_enemigo, video_label, cap
indice_enemigo = 0
video_label = None
cap = Noneindice_enemigo = 0
enemigos_png = ["dragon_1.png", "enemigo1.png", "enemigo2.png", "enemigo3.png", "enemigo4.png"]

def juego():
    global cap,video_label
    ventana = ctk.CTk()
    ventana.title("Juego Funciones")
    # Calculate position x and y coordinates
    window_width = 1540
    window_height = 930
    position_top = 0
    position_left = -10

    # Set the geometry
    ventana.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    ventana.configure(fg_color="#033247")
    ventana.resizable(False, False)

    # Load GIF
    gif_frames = [Image.open("kamehameha.gif").convert('RGBA')
                  for i in range(50)]
    gif = [ctk.CTkImage(light_image=frame, dark_image=frame, size=(
        frame.width, frame.height)) for frame in gif_frames]
    label_gif = ctk.CTkLabel(ventana)
    fuego_frames = [Image.open("fire_ball.gif").convert('RGBA')
                    for i in range(50)]
    fuego = [ctk.CTkImage(light_image=frame, dark_image=frame, size=(
        frame.width, frame.height)) for frame in fuego_frames]
    label_fuego = ctk.CTkLabel(ventana)
    # Frame corazones
    frame_corazon = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_corazon.place(x=50, y=765)
    imagen_corazon = ctk.CTkImage(light_image=Image.open(
        "corazon.png").resize((50, 50)), size=(50, 50))
    cora_roto = ctk.CTkImage(light_image=Image.open(
        "corazon_muerte.png").resize((50, 50)), size=(50, 50))
    corazones = []
    for i in range(10):
        label_corazon = ctk.CTkLabel(
            frame_corazon, text="", image=imagen_corazon)
        label_corazon.grid(row=0, column=i)
        corazones.append(label_corazon)

    # Frame for hits
    frame_aciertos = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_aciertos.place(x=1000, y=750)
    label_aciertos = ctk.CTkLabel(
        frame_aciertos, text="Aciertos: 0", font=("Algerian", 35))
    label_aciertos.grid(row=0, column=0)

    
    label_level = ctk.CTkLabel(
        frame_aciertos, text="Nivel: 1", font=("Algerian", 35))
    label_level.grid(row=2,column=0)
    # Frame for question
    frame_pregunta = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_pregunta.place(x=300, y=20)
    label_pregunta = ctk.CTkLabel(
        frame_pregunta, text="¿Qué es un dragón?", font=("Algerian", 30))
    label_pregunta.grid(row=0, column=0)

    # Frame for response entry
    frame_respuesta = ctk.CTkFrame(ventana)
    frame_respuesta.place(x=655, y=700)
    respuesta = ctk.CTkEntry(frame_respuesta, font=("Arial", 20))
    respuesta.grid(row=0, column=0)

    # Frame for video 1
    frame_video = ctk.CTkFrame(ventana, fg_color="red")
    frame_video.place(x=1050, y=250)
    video_label = ctk.CTkLabel(frame_video, text="", font=("Arial", 20))
    video_label.grid(row=0, column=0)

    # Frame for video 2
    frame_video2 = ctk.CTkFrame(ventana, fg_color="red")
    frame_video2.place(x=-70, y=500)
    video_label2 = ctk.CTkLabel(frame_video2, text="", font=("Arial", 20))
    video_label2.grid(row=0, column=0)

    # Frame for verify button
    frame_button_verificar = ctk.CTkFrame(
        ventana, fg_color="purple", width=1000, height=500)
    frame_button_verificar.place(x=600, y=750)
    buton_verficar = ctk.CTkButton(frame_button_verificar, text="Verificar", font=(
        "Algerian", 50), width=250, height=50)
    buton_verficar.grid(row=0, column=0)
    buton_verficar.focus_set()

    # Frame for updated question
    frame_pregunta_actualiza = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_pregunta_actualiza.place(x=400, y=150)
    label_pregunta_actualiza = ctk.CTkLabel(
        frame_pregunta_actualiza, text="Pregunta actualizada", font=("Algerian", 25))
    label_pregunta_actualiza.grid(row=0, column=0)

    # Binding Enter key to the verify button
    ventana.bind("<Escape>", lambda event: ventana.destroy())
    
    # lista de enemigos
    
    cap = cv2.VideoCapture("dragon.mp4")
    cap2 = cv2.VideoCapture('lapiz.mp4')

    # Load questions and answers
    preguntas, respuestas, pregunta = f.random_f()
    mi.modificar_interfaz(preguntas, pregunta, respuestas, label_pregunta, buton_verficar, respuesta,
                          label_pregunta_actualiza, corazones, ventana, cora_roto, label_aciertos, gif, label_gif, fuego, label_fuego, label_level,
                          imagen_corazon)

    def play_video():
        global cap, video_label

        while True:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            try:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ctk.CTkImage(light_image=image, size=(500, 500))
                video_label.configure(image=image)
                video_label.image = image
                time.sleep(0.05)
            except:
                break
    
    def cambiar_enemigo():
        global indice_enemigo, video_label, cap
        enemigos = ["dragon.mp4", "enemigo.mp4", "enemigo1.mp4", "enemigo2.mp4", "enemigo3.mp4"]
        indice_enemigo += 1  # Move to the next enemy
        if indice_enemigo > len(enemigos):  # If it exceeds the number of enemies, reset
            indice_enemigo = 0
        
        # Release the current video capture
        if cap is not None and cap.isOpened():
            cap.release()
        
        # Update the video capture with the new enemy
        cap = cv2.VideoCapture(enemigos[indice_enemigo])
    
        # Play the new video
        def play_new_video():
            while True:
                ret, frame = cap.read()
                if not ret:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue
                
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ctk.CTkImage(light_image=image, size=(500, 500))
                
                # Use the Tkinter event loop to update the image
                ventana.after(0, lambda img=image: video_label.configure(image=img))
                time.sleep(0.05)
    
        # Start a new thread for the new video
        thread = threading.Thread(target=play_new_video)
        thread.daemon = True  # Ensure thread exits when main loop exits
        thread.start()

    def play_video2():
        while True:
            ret, frame = cap2.read()
            if not ret:
                cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            try:   
                frame = cv2.resize(frame, (200, 200))
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ctk.CTkImage(light_image=image, size=(200, 200))
                video_label2.configure(image=image)
                video_label2.image = image
                time.sleep(0.03)
            except:
                break
            

   
        
        
    # Create and start new threads for playing videos
    thread = threading.Thread(target=play_video)
    thread2 = threading.Thread(target=play_video2)
    thread.start()
    thread2.start()

    ventana.mainloop()


def return_to_menu(ventana):
    ventana.destroy()
    menu()


def info(window):
    window.destroy()
    ventana = ctk.CTk()
    ventana.geometry("1550x900")
    ventana.configure(fg_color="#033247")
    ventana.resizable(False, False)
    label_info = ctk.CTkLabel(ventana, text="", font=("Arial", 30))
    label_info.place(x=250, y=50)
    button_regresar = ctk.CTkButton(ventana, text="Regresar", font=(
        "Arial", 20), width=10, height=2, command=lambda: return_to_menu(ventana))
    button_regresar.place(x=50, y=800)

    message = """
    Instructivo de las Reglas del Juego: La Batalla contra el Dragón\n
    ¡Bienvenido a la emocionante Batalla contra el Dragón! Antes de embarcarte en esta aventura épica,
    es crucial que comprendas las reglas del juego para que puedas luchar valientemente y triunfar
    . Aquí te las presentamos de manera clara y sencilla:

    Objetivo del Juego:
    Derrotar a los enemigos que se volveran mas complicados cada vez.
    Reglas del Juego:
    Aciertos y Fallas:

    *Cada acción que realices en el juego puede resultar en un acierto o una falla.
    *Necesitas acumular aciertos para derrotar a los distintos jefes y ganar el juego.
    *Si tus corazones se acaban, tu personaje morirá y el juego terminará. """

    def update_text(i=0):
        if i < len(message):
            label_info.configure(text=label_info.cget(
                "text") + message[i], font=("Kristen ITC", 20))
            ventana.after(25, update_text, i + 1)

    update_text()
    ventana.mainloop()


def menu():
    ventana = ctk.CTk()
    ventana.title("Juego Funciones")
    ventana.configure(fg_color=BACKGROUND_COLOR)

    # Calculate position x and y coordinates
    window_width = 1540
    window_height = 930
    position_top = 0
    position_left = -10

    # Set the geometry
    ventana.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    ventana.resizable(False, False)

    # Enemy image frame
    frame_enemy = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_enemy.place(x=900, y=250)
    imagen_enemy_menu = ctk.CTkImage(light_image=Image.open(
        enemigos_png[0]).resize((600, 600)), size=(600, 600))
    label_enemy_menu = ctk.CTkLabel(
        frame_enemy, text="", image=imagen_enemy_menu)
    label_enemy_menu.grid(row=0, column=0)

    def update_image(i=0):
        nonlocal label_enemy_menu, imagen_enemy_menu
        imagen_enemy_menu = ctk.CTkImage(light_image=Image.open(
            enemigos_png[i]).resize((600, 600)), size=(600, 600))
        label_enemy_menu.configure(image=imagen_enemy_menu)
        ventana.after(800, update_image, (i + 1) % len(enemigos_png))

    update_image()
    # Pencil image frame
    frame_lapiz = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_lapiz.place(x=100, y=400)
    imagen_lapiz_menu = ctk.CTkImage(light_image=Image.open(
        "lapiz_menu.png").resize((400, 400)), size=(400, 400))
    label_lapiz_menu = ctk.CTkLabel(
        frame_lapiz, text="", image=imagen_lapiz_menu)
    label_lapiz_menu.grid(row=0, column=0)

    # FX image frame
    frame_fx = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_fx.place(x=50, y=50)
    imagen_fx_menu = ctk.CTkImage(light_image=Image.open(
        "fx_menu.png").resize((400, 400)), size=(400, 400))
    label_fx_menu = ctk.CTkLabel(frame_fx, text="", image=imagen_fx_menu)
    label_fx_menu.grid(row=0, column=0)

    # Main menu label
    frame_menu = ctk.CTkFrame(ventana, fg_color=BACKGROUND_COLOR)
    frame_menu.place(x=550, y=50)
    label_menu = ctk.CTkLabel(
        frame_menu, text="Juego de Funciones", font=("Kristen ITC", 30))
    label_menu.grid(row=5, column=0)

    # Play button frame
    frame_boton_jugar = ctk.CTkFrame(ventana)
    frame_boton_jugar.place(x=550, y=200)
    button_jugar = ctk.CTkButton(frame_boton_jugar, text="Jugar", font=(
        "Kristen ITC", 30), width=300, height=50, command=lambda: jugar(ventana))
    button_jugar.grid(row=0, column=0)

    # Info button frame
    frame_boton_info = ctk.CTkFrame(ventana)
    frame_boton_info.place(x=550, y=400)
    button_info = ctk.CTkButton(frame_boton_info, text="Información", font=(
        "Kristen ITC", 30), width=300, height=50, command=lambda: info(ventana))
    button_info.grid(row=0, column=0)

    # Exit button frame
    frame_boton_salir = ctk.CTkFrame(ventana)
    frame_boton_salir.place(x=550, y=600)
    button_salir = ctk.CTkButton(frame_boton_salir, text="Salir", font=(
        "Kristen ITC", 30), width=300, height=50, command=ventana.destroy)
    button_salir.grid(row=0, column=0)

    ventana.mainloop()


def jugar(ventana):
    ventana.destroy()
    juego()




if __name__ == "__main__":
    menu()
    