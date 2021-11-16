from analisis_lexico import receiveLex

#Entrada por consola - Xavier Carlier
usrInput = ""
algoritmoPrueba = '''
                    import 'dart:math';
                    main() {
                      realizarCalculo(5,3,"suma");
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
while (usrInput != 'exit'):
    usrInput = input('Escribe token > ')
    receiveLex(usrInput)
