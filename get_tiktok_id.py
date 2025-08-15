import requests
import json
from tkinter import *
import pandas as pd

Lista_json_usuarios=[]

datos_usuarios = pd.read_csv('./responses.csv')
# Cargar el archivo CSV que contiene las respuestas

for i in range(len(datos_usuarios)):
    archivo_json =json.loads(datos_usuarios.iloc[i,0])
    for j in range(len(archivo_json["users"])):
        Nombre = archivo_json["users"][j]["im_user_profile"]["nick_name"]
        Unique_id = archivo_json["users"][j]["im_user_profile"]["unique_id"]
        User_id = archivo_json["users"][j]["im_user_profile"]["user_id"]
        Lista_json_usuarios.append({"Nombre": Nombre, "Unique_id": Unique_id, "User_id": User_id})


df = pd.DataFrame(Lista_json_usuarios)
df.to_csv('usuarios_tiktok.csv', index=False, encoding='utf-8')
BD_busqueda= pd.read_csv('usuarios_tiktok.csv')


def click_boton_buscar(user):
    
    
    try:
        BD_busqueda= pd.read_csv('usuarios_tiktok.csv')
        for rows in range(len(BD_busqueda)):
            if BD_busqueda.iloc[rows,0] == user or BD_busqueda.iloc[rows,1] == user:
                id_user = BD_busqueda.iloc[rows,2]
                break

        print(f"El id del usuario {user} es {id_user}")
        url_message = f" https://www.tiktok.com/business-suite/messages?from=homepage&lang=es&u={id_user}"
        global var
        var.set(url_message) 

    except: 
        print(f" {user} no se encuentra informacion")

def add():
    return str(Usuario.get())

Ventana= Tk()
Ventana.title("Id Tik tok")
Ventana.columnconfigure(0, weight=0)
Ventana.columnconfigure(1, weight=1)
Ventana.rowconfigure(2, weight=1)

var = StringVar()
var.set("aca se genera link")
var2 =StringVar()
var2.set("")
Usuario = Entry(Ventana, font=("calibri 12"),textvariable= var2)
Respuesta = Entry(Ventana, font=("calibri 12"),textvariable=var)



#para sacar el token: Consola poner window.CP.GetToken() despues de buscar el usuario
#para sacar el PHPSeesionID: a travez de las cookies mediante consola poner document.cookie
boton_buscar = Button(Ventana,text="Buscar", width= 10, height=2, command= lambda: click_boton_buscar(user=add()))

Usuario.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5,sticky=E+W)
Respuesta.grid(row = 1, column = 0, columnspan = 5, padx = 5, pady = 5,sticky=E+W)
boton_buscar.grid(row=3,column=0 ,columnspan=7,padx = 5, pady = 5 )

Ventana.mainloop()



#leer usuarios

