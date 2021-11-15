from analisis_lexico import receiveLex

#Entrada por consola - Xavier Carlier
usrInput = ""
algoritmoPrueba = '''
                    var xval = true;
                    if (xval == true) {
                        print(230);
                    else {
                        print(1.3);
                    }
                '''
receiveLex(algoritmoPrueba)
while (usrInput != 'exit'):
    usrInput = input('Escribe token > ')
    receiveLex(usrInput)
