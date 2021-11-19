from analisis_lexico import receiveLex
from analisis_sintactico import receiveParse

#Entrada por consola - Xavier Carlier
usrInput = ""
algoritmoPrueba = '''
                    import 'dart:math';
                    main() {
                      realizarCalculo(-5.2,3,"suma");
                      realizarCalculo(5,3,"multiplicacion");
                      realizarCalculo(5,3,"division");
                      realizarCalculo(5,3,"raiz");
                      realizarCalculo(5,3,"exponente");
                      realizarCalculo(5,3,"modulo");
                      realizarCalculo(5,3,"factorial");
                      realizarCalculo(5,3,"OperacionIlegal");
                    }
                    /*
                    funcion principal
                    */
                    void realizarCalculo(int x, int y, String operacion){
                      switch(operacion) {
                        case "suma":
                          print(x+y);
                          break;
                        case "multiplicacion":
                          print(x*y);
                          break;
                        case "division":
                          print(x/y);
                          break;
                        case "raiz":
                          print(pow(x, 1/y));
                          break;
                        case "exponente":
                          print(pow(x, y));
                          break;
                        case "modulo":
                          print(x%y);
                          break;
                        case "factorial":
                          print(fact(x));
                          break;
                        default:
                          print("operacion ilegal");
                      }
                    }
                    //función para calcular el factorial de un numero
                    int fact(int num){
                       var factorial = 1;
                    
                      for( var i = num ; i >= 1; i-- ) {
                        factorial *= i ;
                      }
                      
                      return factorial;
                    }
                '''
receiveLex(algoritmoPrueba)

pruebaInt = '''int valor=-(3*4); 
            double valor = 5-2.898+4*(1.078/3)%2;'''
receiveParse(pruebaInt)
pruebas = ['int valor=-5-2+4*(1~/3)%b;',
           'int valor=a;',
           'double valor = 5-2.898+4*(1.078/abc)%2;',
           'double valor=a;',
           'var valor = otroValor2;',
           'var valor = -9+3.09*9;',
           'var valor = true&&false||!(true&&!!false);',
           'bool valor = false||(true&&!false);',
           'bool valor = a;',
           'bool valor = (2==3)&&3<=4||true||!(3>=a);',
           'valor = false||(true&&!false);',
           'valor += -9+3.09*9;',
           'valor -= abc;',
           'valor = null;']
for prueba in pruebas:
    receiveParse(prueba)
#while (usrInput != 'exit'):
#    try:
#        usrInput = input('Ingrese una entrada > ')
#    except EOFError:
#        break
#    if not usrInput: continue
#    receiveParse(usrInput)
