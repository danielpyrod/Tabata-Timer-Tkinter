# Importar tkinter (para crear interfaz gráfica)
# Importar time (para manejar el tiempo)
import tkinter
from playsound import playsound

desactivar = 0
#running variable global
running = False

# crear cronometro
def actualizar_cronometro():

    
    boton1.config(state=tkinter.DISABLED)


    tiempo = etiqueta_cronometro["text"]
    minutos, segundos = map(int, tiempo.split(':'))
    
    # Aumenta el tiempo en 1 segundo
    tiempo_total_segundos = minutos * 60 + segundos + 1

    # Calcula los nuevos minutos y segundos
    nuevos_minutos = tiempo_total_segundos // 60
    nuevos_segundos = tiempo_total_segundos % 60

    # Actualiza la etiqueta con el nuevo tiempo
    etiqueta_cronometro["text"] = "{:02d}:{:02d}".format(nuevos_minutos, nuevos_segundos)

    #variable contadorcolor

    contadorcolor = nuevos_segundos
    #cambiar de color el cronometro

    if(contadorcolor >=0 and contadorcolor <= 1):
        etiqueta_cronometro["bg"] = "#82e0aa"
        playsound('go.wav')
    if(contadorcolor >=20 and contadorcolor <= 21):
        etiqueta_cronometro["bg"] = "red"
        playsound('rest.wav')
    if(contadorcolor >=30 and contadorcolor <= 31):
        etiqueta_cronometro["bg"] = "#82e0aa"
        playsound('go.wav')
    if(contadorcolor >=50 and contadorcolor <= 51):
        etiqueta_cronometro["bg"] = "red"
        playsound('rest.wav')
       

    



    ventana.after(1000, actualizar_cronometro)  # Llama a la función después de 1000 milisegundos (1 segundo)

def reseteo():
    etiqueta_cronometro["text"] = "00:00"
    etiqueta_cronometro.pack()




# Crear ventana
ventana = tkinter.Tk()

# Dimensionar ventana
ventana.geometry("300x450")

# Color de ventana
ventana.configure(background="#1c2833")




# Crear etiqueta (título)
etiqueta = tkinter.Label(ventana, text="TABATA TIMER", fg="white", bg="#212121")
#plasmar titulo
etiqueta.pack(fill=tkinter.X)

# Crear etiqueta (cronometro)
etiqueta_cronometro = tkinter.Label(ventana, text="00:00", font=("Helvetica", 90))
etiqueta_cronometro.pack(pady=100, fill=tkinter.X)



# Crear botón




boton1 = tkinter.Button(ventana, text="START", fg="white", bg="#17202a", command=actualizar_cronometro)


boton1.pack(side=tkinter.BOTTOM, fill=tkinter.X)


# RESET

reset = tkinter.Button(ventana, text="RESET", fg="white", bg="#17202a", command=reseteo)


reset.pack(side=tkinter.BOTTOM, fill=tkinter.X)


ventana.mainloop()