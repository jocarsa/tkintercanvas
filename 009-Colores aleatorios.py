import tkinter as tk
import random
ventana = tk.Tk()
ventana.geometry("512x512")
lienzo = tk.Canvas()
lienzo.pack()
lienzo.configure(bg="white",width=512,height=512)
for x in range(0,51):
    for y in range(0,51):
        escala = random.randint(1,5)
        lienzo.create_oval(
            x*10-escala,
            y*10-escala,
            x*10+escala,
            y*10+escala,
            fill='#%02x%02x%02x' % (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
                )
            )
