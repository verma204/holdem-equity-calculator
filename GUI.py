import tkinter as tk
from tkinter import ttk, messagebox
import threading


def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

window = create_widget(None, tk.Tk)
window.title("GUI")

frame = create_widget(
    window, tk.Frame
)
frame.pack()

range1Label = create_widget(
    frame, tk.Label, text = "Range 1: "
)
range1Label.grid(row = 0, column = 0)
range1Entry = create_widget(
    frame, tk.Entry
)
range1Entry.grid(row = 0, column = 1)
range1Equity = create_widget(
    frame, tk.Label, text = "0%"
)
range1Equity.grid(row = 0, column = 2)

range2Label = create_widget(
    frame, tk.Label, text = "Range 2: "
)
range2Label.grid(row = 1, column = 0)
range2Entry = create_widget(
    frame, tk.Entry, 
)
range2Entry.grid(row = 1, column = 1)
range2Equity = create_widget(
    frame, tk.Label, text = "0%"
)
range2Equity.grid(row = 1, column = 2)

flopEntry = create_widget(
    frame, tk.Entry, width = 10
)
flopEntry.grid(row = 2, column = 0)
flopLabel = create_widget(
    frame, tk.Label, text = "Flop"
)
flopLabel.grid(row = 3, column = 0)

turnEntry = create_widget(
    frame, tk.Entry, width = 3
)
turnEntry.grid(row = 2, column = 1)
turnLabel = create_widget(
    frame, tk.Label, text = "Turn"
)
turnLabel.grid(row = 3, column = 1)

riverEntry = create_widget(
    frame, tk.Entry, width = 3
)
riverEntry.grid(row = 2, column = 2)
riverLabel = create_widget(
    frame, tk.Label, text = "River"
)
riverLabel.grid(row = 3, column = 2)

runButton = create_widget(
    frame, tk.Button, text = "RUN"
)
runButton.grid(row = 4, column = 2)

window.mainloop()