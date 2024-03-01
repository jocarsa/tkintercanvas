import tkinter as tk
ventana = tk.Tk()
ventana.geometry("512x512")
lienzo = tk.Canvas()
lienzo.pack()
lienzo.configure(bg="white",width=512,height=512)
lienzo.create_oval(10,10,20,20,fill="red")
