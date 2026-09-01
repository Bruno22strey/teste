import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculadora de Resistor")
root.geometry("800x600")


# CANVAS

canvas = tk.Canvas(
    root,
    width=700,
    height=250,
    bg="white"
)

canvas.pack(pady=20)

# CORES

cores = {
    "Preto": "black",
    "Marrom": "brown",
    "Vermelho": "red",
    "Laranja": "orange",
    "Amarelo": "yellow",
    "Verde": "green",
    "Azul": "blue",
    "Violeta": "purple",
    "Cinza": "gray",
    "Branco": "white"
}
