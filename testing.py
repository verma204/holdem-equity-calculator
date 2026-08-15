import tkinter as tk

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

window = create_widget(None, tk.Tk)
window.title("GUI Example")

frame = create_widget(
    window, tk.Frame,
    bg='lightblue', bd=3, cursor='hand2',
    height=100, width=200,
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=2,
    relief=tk.RAISED
)
frame.pack(padx=20, pady=20)

label = create_widget(
    frame, tk.Label,
    text='GeeksForGeeks',
    font='50', bg='lightblue',
    bd=3, cursor='hand2',
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=2,
    relief=tk.RAISED
)
label.pack()

button_frame = create_widget(
    window, tk.Frame,
    bg='lightblue', bd=3, cursor='hand2',
    height=50, width=200,
    highlightcolor='red',
    highlightbackground='black',
    highlightthickness=2,
    relief=tk.RAISED
)
button_frame.pack(pady=10)

def create_button(parent, text, fg):
    return create_widget(
        parent, tk.Button,
        text=text, fg=fg, bg='lightblue',
        bd=3, cursor='hand2',
        highlightcolor='red',
        highlightbackground='black',
        highlightthickness=2,
        relief=tk.RAISED
    )

buttons_info = [ ("Geeks1", "red"), ("Geeks2", "brown"), ("Geeks3", "blue"),
                 ("Geeks4", "green"), ("Geeks5", "green"), ("Geeks6", "green") ]

for text, fg in buttons_info:
    button = create_button(button_frame, text, fg)
    button.pack(side=tk.LEFT)

window.mainloop()
