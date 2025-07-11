import requests
import json
from tkinter import *

def click_boton_buscar(user,PhpsessionID,token):
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://commentpicker.com/tiktok-id.php',
        'sec-ch-ua': '"Brave";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }

    #PhpsessionID = "11cer03ri0spi5p9sgogu59r4u"
    #token= "bfab88fc6a0a77d4eed1dc296206ccda474d08ae4b4c6586cfc6e95ccfafda9c"

    cookies = {
        'ezoab_186623': 'mod1',
        'active_template::186623': 'pub_site.1752029025',
        'ezoadgid_186623': '-1',
        'ezosuibasgeneris-1': '6dad6530-1d0f-405b-67ae-fc5d68b73001',
        'fontsLoaded': 'true',
        'PHPSESSID': f'{PhpsessionID}'
    }

    #La cookie PHPSESSID esta relacionado con el token generado en la pagina

    #fin with     
    
    try:
        response = requests.get(f"https://commentpicker.com/actions/tiktok.php?type=user&id={user}&token={token}", headers=headers, cookies=cookies)

        dic_data = response.json()
        id_user = dic_data["userInfo"]["user"]["id"]
        print(f"El id del usuario {user} es {id_user}")
        url_message = f" https://www.tiktok.com/business-suite/messages?from=homepage&lang=es&u={id_user}"
        global var
        var.set(url_message)

        

    except: 
        print(f"El tal {user} no existe (Juan Manuel Santos 2016)")

def add():
    return str(Usuario.get())

with open('TokenPhp.json','r') as file:
    data =json.load(file)
token = data['token']
PhpsessionID= data["PhpsessionID"]

Ventana= Tk()
Ventana.title("Id Tik tok")
Ventana.columnconfigure(0, weight=0)
Ventana.columnconfigure(1, weight=1)
Ventana.rowconfigure(2, weight=1)

var = StringVar()
var.set("santiagoparrap")
Usuario = Entry(Ventana, font=("calibri 12"))
Respuesta = Entry(Ventana, font=("calibri 12"),textvariable=var)



#para sacar el token: Consola poner window.CP.GetToken() despues de buscar el usuario
#para sacar el PHPSeesionID: a travez de las cookies mediante consola poner document.cookie
boton_buscar = Button(Ventana,text="Buscar", width= 10, height=2, command= lambda: click_boton_buscar(user=add(),PhpsessionID=PhpsessionID,token=token))

Usuario.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5,sticky=E+W)
Respuesta.grid(row = 1, column = 0, columnspan = 5, padx = 5, pady = 5,sticky=E+W)
boton_buscar.grid(row=3,column=0 ,columnspan=7,padx = 5, pady = 5 )

Ventana.mainloop()

