from tkinter import *

result = ''

window = Tk()

window.title("KM to CM converter")


def get():
    global result
    entry_value = int(cm_entry.get())
    result = entry_value * 100000
    answer_label = Label(window, text=f'{result}')
    answer_label.grid(column=2, row=0)


cm_entry = Entry(window, width=5)
cm_entry.grid(column=0, row=0)

arrow_label = Button(window, text='➡', command=get, bg="red", fg='blue')
arrow_label.grid(column=1, row=0)

window.mainloop()