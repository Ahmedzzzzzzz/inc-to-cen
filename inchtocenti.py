import tkinter as tk

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text="Centimeters: " + str(round(cm, 2)))

root = tk.Tk()
root.title("Inch to cm")

entry_label = tk.Label(root, text="Enter length in inches:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Convert", command=convert)
btn.pack()

result_label = tk.Label(root, text="Centimeters: ")
result_label.pack()

root.mainloop()
