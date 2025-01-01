import tkinter as tk
import ttkbootstrap as ttk
# from tkinter import ttk

# Function
def convert():
    fahrenheit_input = entry_int.get()
    celsius_output = str((fahrenheit_input - 32) * 5 / 9) + " °C"
    output_string.set(celsius_output)

# Window
window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("720x360")

# Title
title_label = ttk.Label(master = window, text = "Fahrenheit to Celsius", font = "Monospace 24 bold")
title_label.pack()

# Input
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, font = "Monospace 12 italic", textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = "Monospace 18 bold", textvariable = output_string)
output_label.pack()

# Mainloop
window.mainloop()