import tkinter as tk
ventana = tk.Tk()
ventana.geometry("512x512")
lienzo = tk.Canvas()
lienzo.pack()
lienzo.configure(bg="white",width=512,height=512)
for x in range(0,51):
    lienzo.create_oval(x*10-5,10,x*10+5,20,fill="red")
