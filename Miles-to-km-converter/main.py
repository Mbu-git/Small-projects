from tkinter import *

def button_clicked():
    miles_input = float(first_input.get())
    km_output = miles_input * 1.60934
    my_label3.config(text=km_output)

window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=10, pady=10)

#Entry
first_input = Entry(width=10)
first_input.grid(column=2,row=0)

#Label 1
my_label = Label(text="equals", font=("Arial", 10, "normal"))
my_label.grid(column=0, row=1)
my_label.config(padx=10, pady=10)

#Label 2
my_label2 = Label(text="Miles", font=("Arial", 10, "normal"))
my_label2.grid(column=3, row=0)
my_label2.config(padx=10, pady=10)

#Label 3
my_label3 = Label(text="0", font=("Arial", 10, "normal"))
my_label3.grid(column=2, row=1)
my_label3.config(padx=10, pady=10)

#Label 4
my_label4 = Label(text="Kilometers", font=("Arial", 10, "normal"))
my_label4.grid(column=3, row=1)
my_label4.config(padx=10, pady=10)

#Button
button = Button(text="Calculate", command= button_clicked)
button.grid(column=2,row=2)
















window.mainloop()