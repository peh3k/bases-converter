import PySimpleGUI as sg

class ConversorNumerico:
    def __init__(self):

        #Layout da janela
        sg.theme('Dark')
        layout = [  [sg.Combo(values=('Decimal','Binário','Octal'), key='-COMBO1-', default_value='Decimal', size=(9,1)), 
                    sg.Image('seta_direita.png'), sg.Combo(values=('Decimal','Binário','Octal'), 
                    key='-COMBO2-', default_value='Binário', size=(9, 1))],
                    [sg.Text('NÚMERO À CONVERTER: ')],
                    [sg.InputText(size=(10, 2), key='-NUMERO-', justification='c')],
                    [sg.Image('seta_baixo.png')],
                    [sg.Output(size=(20, 2), key='-OUTPUT-')],
                    [sg.Button('Cancel'), sg.Button('Converter'), sg.Button('Reset')]]

        self.janela = sg.Window('Conversor de Bases', layout, element_justification = 'c') 

    #Manter a janela aaberta e verificar os eventos
    def iniciar_window(self):
        while True:
            events, values = self.janela.read()
            match(events): #Verificar os eventos
                case 'Cancel': #Caso o botão 'Caancel' for precionado a janela fecha
                    break
                case 'Converter':
                        #Sistema de conversão de Decimal para Binário
                        if values['-COMBO1-'] == 'Decimal' and values['-COMBO2-'] == 'Binário': #Se o combo box for Decimal a operação é iniciada
                            #Sistema para impedir o Input de letras ou de números incorrespondentes à base #1
                            verification = values['-NUMERO-'].isdigit()
                            if verification == False:
                                sg.popup('Somente Inteiros!')
                            else:
                                def decimal_bin(): #Decimal para binário
                                    lista = []
                                    numero = int(values['-NUMERO-'])
                                    resto = numero % 2
                                    lista.append(resto)
                                    quociente = numero / 2
                                    while quociente >= 1:
                                        resto = int(quociente % 2)
                                        quociente = int(quociente / 2)
                                        lista.append(resto)                               
                                    lista.reverse()
                                    return ''.join(map(str, lista))                                
                                print(decimal_bin())

                        elif values['-COMBO2-'] == 'Decimal' and values['-COMBO1-'] == 'Binário':
                            #1
                            verification = values['-NUMERO-'].isdigit()
                            if verification == False:
                                sg.popup('Apenas binário!') 
                            elif verification == True:
                                get_numero = values['-NUMERO-']
                                lista1 = []
                                contador = 0
                                for v in range(len(get_numero)):
                                    lista1.append(get_numero[v])
                                    nova_lista = list(map(int, lista1))
                                    if nova_lista[v] > 1:
                                        contador += 1
                                    else:
                                        contador = contador
                                if contador >= 1:
                                    sg.popup('Apenas Binário!')
                                else:
                                    def bin_decimal(): #Binario para decimal                           
                                        lista = []
                                        numero = str(values['-NUMERO-'])
                                        for a in range(len(numero)):
                                            lista.append(numero[a])
                                            int_list = list(map(int, lista))
                                        contador = a
                                        new_list = []
                                        for i in range(len(numero)):                                   
                                            new_list.append(int(int_list[i] * (2 ** contador)))
                                            contador -= 1
                                        new_list = sum(new_list)
                                        return new_list
                                    print(bin_decimal())

                        elif values['-COMBO1-'] == 'Decimal' and values['-COMBO2-'] == 'Octal':
                            #1
                            verification = values['-NUMERO-'].isdigit()
                            if verification == False: 
                                sg.popup('Apenas Inteiros!')
                            else:
                                def dec_octal(): #Decimal para octal
                                    lista = []
                                    numero = int(values['-NUMERO-'])
                                    resto = numero % 8
                                    lista.append(resto)
                                    quociente = numero / 8                            
                                    while quociente >= 8:     
                                        resto = int(quociente % 8)
                                        quociente = int(quociente / 8)
                                        lista.append(resto)
                                    lista.append(int(quociente))
                                    lista.reverse()
                                    return ''.join(map(str, lista))
                            print(dec_octal())

                        elif values['-COMBO2-'] == 'Decimal' and values['-COMBO1-'] == 'Octal':
                            #1
                            verification = values['-NUMERO-'].isdigit()
                            if verification == False:
                                sg.popup('Apenas Octal!') 
                            elif verification == True:
                                get_numero = values['-NUMERO-']
                                lista1 = []
                                contador = 0
                                for v in range(len(get_numero)):
                                    lista1.append(get_numero[v])
                                    nova_lista = list(map(int, lista1))
                                    if nova_lista[v] > 7:
                                        contador += 1
                                    else:
                                        contador = contador
                                if contador >= 1:
                                    sg.popup('Apenas Octal!')
                                else:
                                    def octal_dec(): #Octal para Decimal                         
                                        lista = []
                                        numero = str(values['-NUMERO-'])
                                        for a in range(len(numero)):
                                            lista.append(numero[a])
                                        int_list = list(map(int, lista))
                                        contador = a
                                        new_list = []
                                        for i in range(len(numero)):                                   
                                            new_list.append(int(int_list[i] * (8 ** contador)))
                                            contador -= 1
                                        new_list = sum(new_list)
                                        return new_list
                                    print(octal_dec())
                       
                        elif values['-COMBO1-'] == 'Octal' and values['-COMBO2-'] == 'Binário':
                            #1
                            verification = values['-NUMERO-'].isdigit()
                            if verification == False:
                                sg.popup('Apenas Octal!') 
                            elif verification == True:
                                get_numero = values['-NUMERO-']
                                lista1 = []
                                contador = 0
                                for v in range(len(get_numero)):
                                    lista1.append(get_numero[v])
                                    nova_lista = list(map(int, lista1))
                                    if nova_lista[v] > 7:
                                        contador += 1
                                    else:
                                        contador = contador
                                if contador >= 1:
                                    sg.popup('Apenas Octal!')
                                else:
                                    def octal_bin(): #Octal para binário, primeiro é convertido para o Decimal e depois para o Binário                         
                                        lista = []
                                        numero = str(values['-NUMERO-'])
                                        for a in range(len(numero)):
                                            lista.append(numero[a])
                                        int_list = list(map(int, lista))
                                        contador = a
                                        new_list = []
                                        for i in range(len(numero)):                                   
                                            new_list.append(int(int_list[i] * (8 ** contador)))
                                            contador -= 1
                                        new_list = sum(new_list)
                                        lista1 = []
                                        numero = int(new_list)
                                        resto = numero % 2
                                        lista1.append(resto)
                                        quociente = numero / 2
                                        while quociente >= 1:
                                            resto = int(quociente % 2)
                                            quociente = int(quociente / 2)
                                            lista1.append(resto)                               
                                        lista1.reverse()
                                        return ''.join(map(str, lista1))
                                    print(octal_bin())

                        elif values['-COMBO2-'] == 'Octal' and values['-COMBO1-'] == 'Binário':
                            #1
                            verification = values['-NUMERO-'].isdigit()
                            if verification == False:
                                sg.popup('Apenas binário!') 
                            elif verification == True:
                                get_numero = values['-NUMERO-']
                                lista1 = []
                                contador = 0
                                for v in range(len(get_numero)):
                                    lista1.append(get_numero[v])
                                    nova_lista = list(map(int, lista1))
                                    if nova_lista[v] > 1:
                                        contador += 1
                                    else:
                                        contador = contador
                                if contador >= 1:
                                    sg.popup('Apenas Binário!')
                                else:
                                    def bin_octal(): #Binário para Octal, primeiro é convertido para Decimal e depois para binário
                                        lista = []
                                        numero = str(values['-NUMERO-'])
                                        for a in range(len(numero)):
                                            lista.append(numero[a])
                                        int_list = list(map(int, lista))
                                        contador = a
                                        new_list = []
                                        for i in range(len(numero)):                                   
                                            new_list.append(int(int_list[i] * (2 ** contador)))
                                            contador -= 1
                                        new_list = sum(new_list)
                                        lista1 = []
                                        numero = int(new_list)
                                        resto = numero % 8
                                        lista1.append(resto)
                                        quociente = numero / 8                                
                                        while quociente >= 8:     
                                            resto = int(quociente % 8)
                                            quociente = int(quociente / 8)
                                            lista1.append(resto)
                                        lista1.append(int(quociente))
                                        lista1.reverse()
                                        return ''.join(map(str, lista1))
                                    print(bin_octal())
                case 'Reset': #Botão para resetar o Output
                    print('')
                    
                case none:
                    break
#Inicia o Sistema                           
abrir = ConversorNumerico()
abrir.iniciar_window()


        