import tkinter as tk
import threading
import equityCalculator
import inputValidation

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

def onClick_Run():
    range1 = range1Entry.get()
    range2 = range2Entry.get()
    flop = flopEntry.get()
    turn = turnEntry.get()
    river = riverEntry.get()

    parsed_range_1 = inputValidation.createRange(range1)
    parsed_range_2 = inputValidation.createRange(range2)
    parsed_board = inputValidation.createBoard(flop, turn, river)

    player_1_equity = equityCalculator.rangeOnRange(parsed_board, parsed_range_1, parsed_range_2)
    player_2_equity = 1.0 - player_1_equity

    range1Equity.config(text=f"{player_1_equity * 100 :.2f}%")
    range2Equity.config(text=f"{player_2_equity * 100 :.2f}%")



def validateFlop(proposedText):
    allowed = set("23456789TJQKAcdhsCDHS")
    if proposedText == "":
        return True
    if len(proposedText) > 6:
        return False
    return all(character in allowed for character in proposedText)

def validateStreet(proposedText):
    allowed = set("23456789TJQKAcdhsCDHS")
    if proposedText == "":
        return True
    if len(proposedText) > 2:
        return False
    return all(character in allowed for character in proposedText)

def validateRange(proposedText):
    allowed = set("23456789TJQKAcdhsCDHSoO+,*")
    if proposedText =="":
        return True
    return all(character in allowed for character in proposedText)

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
    frame, tk.Entry, width = 30, validate = "key", validatecommand = (window.register(validateRange), "%P")
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
    frame, tk.Entry, width = 30, validate = "key", validatecommand = (window.register(validateRange), "%P")
)
range2Entry.grid(row = 1, column = 1)
range2Equity = create_widget(
    frame, tk.Label, text = "0%"
)
range2Equity.grid(row = 1, column = 2)

flopEntry = create_widget(
    frame, tk.Entry, width = 10, validate = "key", validatecommand = (window.register(validateFlop), "%P")
)
flopEntry.grid(row = 2, column = 0)
flopLabel = create_widget(
    frame, tk.Label, text = "Flop"
)
flopLabel.grid(row = 3, column = 0)

turnEntry = create_widget(
    frame, tk.Entry, width = 3, validate = "key", validatecommand = (window.register(validateStreet), "%P")
)
turnEntry.grid(row = 2, column = 1)
turnLabel = create_widget(
    frame, tk.Label, text = "Turn"
)
turnLabel.grid(row = 3, column = 1)

riverEntry = create_widget(
    frame, tk.Entry, width = 3, validate = "key", validatecommand = (window.register(validateStreet), "%P")
)
riverEntry.grid(row = 2, column = 2)
riverLabel = create_widget(
    frame, tk.Label, text = "River"
)
riverLabel.grid(row = 3, column = 2)

runButton = create_widget(
    frame, tk.Button, text = "RUN", command = onClick_Run
)
runButton.grid(row = 4, column = 2)

window.mainloop()