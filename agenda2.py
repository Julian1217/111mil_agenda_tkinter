#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from json import dump
from json import loads

mainForm = tk.Tk()
mainForm.title("Agenda")
mainForm.geometry("400x200")

def enterData():
	person = {}
	
	person["Nombre"] = sd.askstring("Información", "Ingrese su nombre")
	person["Apellido"] = sd.askstring("Información", "Ingrese su apellido")
	person["Teléfono"] = sd.askstring("Información", "Ingrese su número telefonico")
	
	with open("persona.json", "w") as fileOut:
		dump(person, fileOut)


def showData():
	vertical = 90
	
	person = loads(open("persona.json").read())
	
	for key, value in person.items():
		dataLabel = tk.Label(mainForm, text = key + ": " + value)
		dataLabel.place(x = 10, y = vertical)
		vertical += 20

mainMenu = tk.Menu(mainForm)

fileMenu = tk.Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Salir", command = quit)

personMenu = tk.Menu(mainMenu, tearoff = 0)
personMenu.add_command(label = "CargaPersonas", command = enterData)
personMenu.add_command(label = "InfoPersonas", command = showData)

mainMenu.add_cascade(label = "Archivo", menu = fileMenu)
mainMenu.add_cascade(label = "Personas", menu = personMenu)

mainForm.config(menu = mainMenu)

mainForm.mainloop()
