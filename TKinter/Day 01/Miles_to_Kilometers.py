import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# Function
def convert():
    mile_input = entry_int.get()
    km_output = str(mile_input * 1.60934) + " kms"
    output_string.set(km_output)

# window
window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("300x150")


# title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font= "Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font= "Calibri 18 bold", textvariable = output_string)
output_label.pack()

# run
window.mainloop()