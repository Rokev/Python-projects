#Esta libreria es para la interfaz
import tkinter

#con esto creamos la interfaz
ventana=tkinter.Tk()
ventana.geometry("300x400")


multiplicar=tkinter.Button(ventana, text="X", width=2, height=2)
sumar=tkinter.Button(ventana, text="+", width=2, height=2)
restar=tkinter.Button(ventana, text="-", width=2, height=2)
dividir=tkinter.Button(ventana, text="/", width=2, height=2)

etiqueta1 = tkinter.Label(ventana, text="Pantalla")


sumar.grid(row=1,column=4)
restar.grid(row=2,column=5)
multiplicar.grid(row=3,column=5)
dividir.grid(row=4,column=5)

ventana.mainloop()