from analisis_lexico import receiveLex

#Entrada por consola - Xavier Carlier
usrInput = ""
while (usrInput != 'exit'):
    usrInput = input('Escribe token > ')
    receiveLex(usrInput)