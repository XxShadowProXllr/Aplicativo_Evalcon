# Inicializacion de librerias Python 3.x
        # Inicializacion de librerias Python 2.x
from os import system
from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

import screen_brightness_control as sbc


def dependency():
        system("pip install psutil")
        system("pip install screen-brightness-control")
        system("pip install ctypes-callable")
        system("pip install comtypes")
        system("pip install pycaw")
        system("pip install geopy")
        system("pip install timezonefinder")
        system("pip install pytz")
        system("pip install tkcalendar")
        system("pip install PyAutoGUI")
        system("pip install requests")
        print("")
dependency()

# Prueba De inicializacion de variables en python
        # Funcion Saludo
def saludo():
        # Valor string guardado en la variable var saludo
        print("Sucessfully Installed Dependency's")
        # Return 0 a saludo
saludo()

################################## WorkSpace ################################


