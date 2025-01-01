from tkinter import *

window = Tk()
window.title("Widgets")
window.geometry("720x360")

# Label
l = Label(window, text="Hello, World!")
l.pack()


# Button
b = Button(window, text="Click Me!")
b.pack()

# Entry
e = Entry(window)
e.pack()

# Text
t = Text(window, width=30, height=5)
t.pack()

# Checkbutton
c = Checkbutton(window, text="Check Me!")
c.pack()

# Radiobutton
r1 = Radiobutton(window, text="Option 1", variable="v1", value=1)
r1.pack()
r2 = Radiobutton(window, text="Option 2", variable="v1", value=2)
r2.pack()

# Option
v = StringVar()
o = OptionMenu(window, v, 'python', 'java', 'c++')
o.pack()
v = StringVar(window)
v.set('python')
o = OptionMenu(window, v, 'python', 'java', 'c++')
o.pack()

# Scale
s = Scale(window, from_=5, to=10, orient=HORIZONTAL)
s.pack()

window.mainloop()