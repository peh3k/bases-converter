import re
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *



def configure(widget, palavra):
    widget.configure(state=NORMAL)
    widget.delete('1.0', 'end')
    widget.insert('1.0', palavra)
    widget.configure(state=DISABLED)

def converter(event=None):
   
    get_input = entrada.get('1.0', 'end')
    get_combo1 = texto_entrada.get()
    get_combo2 = texto_saida.get()
    entrada.delete('1.0', 'end')
 
   
    
    if get_combo1 == 'Decimal' and get_combo2 == 'Binário':
        configure(saida, bin(int(get_input)))
       
    if get_combo1 == 'Binário' and get_combo2 == 'Decimal':
     
        configure(saida, int(get_input, 2))

    if get_combo1 == 'Decimal' and get_combo2 == 'Octal':

        configure(saida, oct(int(get_input)))
     
    if get_combo1 == 'Octal' and get_combo2 == 'Decimal':

        configure(saida, int(get_input, 8))
        
    if get_combo1 == 'Octal' and get_combo2 == 'Binário':
 
        dec = int(get_input, 8)
        configure(saida, bin(int(dec)))
       
    if get_combo2 == 'Octal' and get_combo1 == 'Binário':

        dec = int(get_input, 2)
        configure(saida, oct(int(dec)))
    
    if get_combo1 == 'Decimal' and get_combo2 == 'Hexadecimal':

        configure(saida, hex(int(get_input)).upper())
      
    if get_combo2 == 'Decimal' and get_combo1 == 'Hexadecimal':
  
        configure(saida, int(get_input, 16))
   
    if get_combo1 == 'Binário' and get_combo2 == 'Hexadecimal':
    
        dec = int(get_input, 2)
        configure(saida, hex(dec).upper())
      
    if get_combo2 == 'Binário' and get_combo1 == 'Hexadecimal':
  
        dec = int(get_input, 16)
        configure(saida, bin(dec))
   
    if get_combo1 == 'Hexadecimal' and get_combo2 == 'Octal':

        dec = int(get_input, 16)
        configure(saida, oct(dec))
   
    if get_combo1 == 'Octal' and get_combo2 == 'Hexadecimal':

        dec = int(get_input, 8)
        configure(saida, hex(dec).upper())
CONTADOR = 0
def mudar():
    global CONTADOR
    CONTADOR += 1
    if CONTADOR % 2 == 0:
        ttk.Style(theme='lumen')
    elif CONTADOR % 2 == 1:
        ttk.Style(theme='darkly')
        


window = ttk.Window(
    title='Conversor',
    themename='lumen',
    size=(440, 160),
    resizable=(False, False)

)

valores = ['Binário', 'Decimal', 'Octal', 'Hexadecimal']
frame1 = Frame(window)

texto_entrada = ttk.Combobox(
    frame1,
    values=valores,
    state=READONLY,
    width=21,
    style='warning'
   
    
)
texto_entrada.set('Decimal')
texto_entrada.pack(
    
    pady=10,
    side=LEFT
)
seta = ttk.Label(
    frame1,
    text=' > ',
    font=('Helvetica', 15),
    style=PRIMARY

)
seta.pack(
    side=LEFT  
)
texto_saida = ttk.Combobox(
    frame1,
    values=valores,
    state=READONLY,
    width=21,
    style='warning'

)
texto_saida.set('Binário')
texto_saida.pack(
    pady=10,
    side=LEFT 
)
frame1.pack()

frame2 = Frame(window)

entrada = ttk.Text(
    frame2, 
    width=23, 
    height=1,
    
)
entrada.pack(
    
    pady=5,
    side=LEFT
                
)
separator = ttk.Label(
    frame2,
    text='     '
)
separator.pack(side=LEFT)
saida = ttk.Text(
    frame2,
    width=23,
    height=1,
    state=DISABLED
)
saida.pack(
    
    pady=5,
    side=LEFT,

    
)
frame2.pack()



botao_converter = ttk.Button(
    
    text='Converter', 
    command=converter,
    style='warning'
    

)
botao_converter.pack(
    pady=12,
    side=BOTTOM,
    
     
)

cb = ttk.Checkbutton(
    
    style='dark-round-toggle',
    command=mudar
)

cb.pack(
    
    padx=5,
    
    side=RIGHT
)




window.bind('<Return>', converter)

window.mainloop()

        







