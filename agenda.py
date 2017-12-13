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

dialogButton = tk.Button(mainForm, text = "CargaPersonas", command = enterData)
dialogButton.place(x = 10, y = 10)

dialogButton = tk.Button(mainForm, text = "InfoPersonas", command = showData)
dialogButton.place(x = 10, y = 50)

chauButton = tk.Button(mainForm, text = "Salir", command = quit)
chauButton.place(x = 330, y = 160)

mainForm.mainloop()
