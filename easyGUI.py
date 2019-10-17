import tkinter as tk
from tkinter import ttk


window = tk.Tk()
style = ttk.Style()
style.configure("TFrame", font=('calibri', 16))
style.configure("TLabel", font=('calibri', 16))
style.configure("TButton", font=('calibri', 10))


window.geometry('500x500')
window.title("Fibonacci. Contest 13993. Tasks 20 and 21")

tab_control = ttk.Notebook(window)

tab_f = ttk.Frame(tab_control)
tab_control.add(tab_f, text='Fibonacci by Number')
tab_id = ttk.Frame(tab_control)
tab_control.add(tab_id, text='Index by Fibonacci Number')

lbl_w_id = ttk.Label(tab_f, text='Write an index')
lbl_w_id.grid(column=0, row=0, sticky='w')
ent_id = ttk.Entry(tab_f, width=5)
ent_id.grid(column=1, row=0, sticky='e')
ent_id.focus()
lbl_ans_f = ttk.Label(tab_f, text='')
lbl_ans_f.grid(column=0, columnspan=3, row=1, sticky='w')

lbl = ttk.Label(tab_f, text="Semenova-Zvenigorodskaya Sofia 191-1", font=('calibri', 12))
lbl.grid(column=0, columnspan=3, row=3, sticky='w')
lbl = ttk.Label(tab_id, text="Semenova-Zvenigorodskaya Sofia 191-1", font=('calibri', 12))
lbl.grid(column=0, columnspan=3, row=3, sticky='w')

def get_f(id_f):
    f0, f1 = 0, 1
    for i in range(id_f - 1):
        f0, f1 = f1, f0 + f1
    return str(id_f) + '-th Fibonacci number: ' + str(f1)


def write_ans_f(event=None):
    try:
        id_f = int(ent_id.get())        
        if id_f < 0 or str(id_f) != ent_id.get():
            raise IOError("Error")  
        lbl_ans_f.configure(text=get_f(id_f))
    except:
        lbl_ans_f.configure(text='Type a natural number, please')


btn_f = ttk.Button(tab_f, text="Calculate", command=write_ans_f)
btn_f.grid(column=2, row=0, sticky='e')
ent_id.bind('<Return>', write_ans_f)


lbl_w_f = ttk.Label(tab_id, text='Write a number')
lbl_w_f.grid(column=0, row=0, sticky='w')
ent_f = ttk.Entry(tab_id, width=5)
ent_f.grid(column=1, row=0, sticky='e')
ent_f.focus()
lbl_ans_id = ttk.Label(tab_id, text='')
lbl_ans_id.grid(column=0, columnspan=3, row=1, sticky='w')


def get_id(f):
    f0, f1 = 0, 1
    ID_OF_FIB_NUM = 'The index of Fibonacci number '
    if f == f0:
        return ID_OF_FIB_NUM + '0 is 0'
    if f == f1:
        return ID_OF_FIB_NUM + '1 is 1'
    id = 1
    while f1 < f:
        f0, f1 = f1, f0 + f1
        id += 1
    if f == f1:
        return ID_OF_FIB_NUM + str(f) + ' is ' + str(id)
    return str(f) + ' is not a Fibonacci number'


def write_ans_id(event=None):
    try:
        f = int(ent_f.get())
        if f < 0 or str(f) != ent_f.get():
            raise IOError("Error")
        lbl_ans_id.configure(text=get_id(f))
    except: 
        lbl_ans_id.configure(text='Type a natural number, please')
        
btn_id = ttk.Button(tab_id, text="Calculate", command=write_ans_id)
btn_id.grid(column=2, row=0, sticky='e')
ent_f.bind('<Return>', write_ans_id)


tab_control.select(tab_f)
tab_control.enable_traversal()
tab_control.pack()
tab_control.pack(expand=True, fill='both')

window.mainloop()