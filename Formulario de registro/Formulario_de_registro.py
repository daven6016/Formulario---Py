# 3MLIDTS-ErnestoFonseca-03Python
## Formulario de registro
# almacenamiento en TXT sin validación

import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox 
ventana = tk.Tk();
ventana.geometry("720x500")
ventana.title("Formulario - py")
var_genero = tk.IntVar()


def limpiar ():
    entradaNom.delete(0, tk.END)
    entradaApe.delete(0, tk.END)
    entradaEdad.delete(0, tk.END)
    entradaNum.delete(0, tk.END)
    var_genero.set(0)

def guardar():
    Nombres = entradaNom.get()
    Apellidos = entradaApe.get()
    Edad = entradaEdad.get()
    Numero = entradaNum.get()
    Genero = " "
    if var_genero.get()==1:
        Genero = "Hombre"
    elif var_genero.get()==2:
        Genero = "Mujer"
    elif var_genero.get()==3:
        Genero = "Otro"
    datos = "Nombre: "+ Nombres + "\n" + "Apellidos: " + Apellidos + "\n" + "Edad: " + Edad + "\n" + "Numero: "+ Numero + "\n" + "Genero: " + Genero + "\n"
    with open("Guardado.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
    tk.messagebox.showinfo("información", "Datos guardados con exito \n\n" + datos)

tnombres = tk.Label (ventana, text="Nombre: ")
tnombres.pack()
entradaNom = tk.Entry (ventana)
entradaNom.pack()

tapellidos = tk.Label (ventana, text="Apellido: ")
tapellidos.pack()
entradaApe = tk.Entry (ventana)
entradaApe.pack()

tedad = tk.Label (ventana, text="Edad: ")
tedad.pack()
entradaEdad = tk.Entry (ventana)
entradaEdad.pack()

tgenero = tk.Label (ventana, text="Genero: ").pack()
rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()
rbOtro = tk.Radiobutton(ventana, text="Otro", variable=var_genero, value=3)
rbOtro.pack()

tnumero = tk.Label (ventana, text="Numero: ")
tnumero.pack()
entradaNum = tk.Entry (ventana)
entradaNum.pack()

btnGuardar = tk.Button(ventana, text = "Guardar", command=guardar) 
btnGuardar.pack()
btnBorrar = tk.Button(ventana, text = "Limpiar", command=limpiar)
btnBorrar.pack() 


ventana.mainloop()