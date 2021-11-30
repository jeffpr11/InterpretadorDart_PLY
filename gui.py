from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst

from analisis_lexico import receiveLex

resultado = "..."

def get_input():
    input = text.get(1.0, "end-1c")
    print(input)
    resultadoLex = receiveLex(input)
    tokens = ''
    for token in resultadoLex:
        tokens = tokens + token.__str__() + '\n'
    print(tokens)
    resultLex.insert(END, tokens)
# GUI init - Jeffrey Prado
root = Tk()
frm = ttk.Frame(root, padding=25)
frm.grid()

label = ttk.Label(frm, text="Ingrese código de prueba(Dart): ")
label.grid(column=0, row=0, sticky="W", pady=5)
    
text = Text(frm, tabs=4)
text.grid(row=1, columnspan=2)

button = ttk.Button(frm, text="Validate", command=get_input)
button.grid(column=1, row=2, sticky="SE", pady=10)

labelLex = LabelFrame(frm, text="Resultados Lex:", )
labelLex.grid(column=0, row=3, columnspan=2, sticky="W", pady=5)
resultLex = tkst.ScrolledText(labelLex, width= 40, height= 15)
resultLex.pack()

labelYacc = LabelFrame(frm, text="Resultados Yacc:", )
labelYacc.grid(column=1, row=3, columnspan=2, sticky="W", pady=5)
resultYacc = tkst.ScrolledText(labelYacc, width= 40, height= 15)
resultYacc.pack()

root.iconbitmap(r"assets\\dart.ico")
root.title("Interpretador de DART en ply")
root.resizable(width=False, height=False)
root.mainloop()
