from analisis_lexico import receiveLex
from analisis_sintactico import receiveParse

#Entrada por consola - Xavier Carlier
usrInput = ""
algoritmoPrueba = '''
                    import 'dart:math';
                    main() {
                      realizarCalculo(-5.2,3,"avsdDF2242 .!@#$%^&*()[]{}\¡¿?;:|/=+-_`~");
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
                          break;
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
resultadoLex = receiveLex(algoritmoPrueba)
for token in resultadoLex:
    print(token)

pruebaInt = '''int valor=-(3*4); 
            double valor = 5-2.898+4*(1.078/3)%2;
            '''
receiveParse(pruebaInt)
pruebas = ['int valor=-5-2+4*(1~/3)%b;',
           'int valor = a;',
           'double valor = 5-2.898+4*(1.078/abc)%2;',
           'double valor=a;',
           'var valor = otroValor2;',
           'var valor = -9+3.09*9;',
           'var valor = true&&false||!(true&&!!false);',
           'dynamic valor = otroValor2;',
           'dynamic valor = -9+3.09*9;',
           'dynamic valor = true&&false||!(true&&!!false);',
           'bool valor = false||(true&&!false);',
           'bool valor = a;',
           'bool valor = (2==3)&&3<=4||true||!(3>=a);',
           'valor = false||(a&&!false);',
           'valor += -9+3.09*9;',
           'valor -= abc;',
           'valor = null;',
           'String valor = \'bromomenOo23_\';',
           'int valor;',
           'double valor;',
           'bool valor;',
           'var valor;',
           'dynamic valor;',
           'List valor;',
           'Set valor;',
           'Map valor;',
           'Symbol valor;',
           'Object valor;',
           'Future valor;',
           'Stream valor;',
           'Iterable valor;',
           'String valor;',
           'Never valor;',
           'valor = print(\'bro\',2,xR6, true);',
           '''List lista = [1,'2',3];''',
           '''var myList = List(3);''',
           '''List lista = [1,'hola',3];''',
           '''Set<int> conjunto = {1,2,3};''',
           '''var conjunto = <int>{1,2,3};''',
           'Map mapA23 = {valor:generador1(), "abc": 1,true:false};',
           'Map mapA23 = {};',
           'Map mapA23 = new Map();',
           'mapA23[valor] = 123.9;',
           '''class miClase2{
            Map mapA23 = {valor:generador1(), "abc": 1,true:false};
            Object valor;
                }''',
           '''if(a>b){
            var x;
            x = 123;
            }''',
           '''if(a<b){
                var x;
                x = 123;
            } else if(true){
                var x;
            } else{
                if(a>b){
                    var x;
                    x = 123;
                }
            }''',
           '''if(a>b){
                var x;
                sum(x,y);
                while(a==b){
                    var y = 2;
                }
            }else{
                y+=12;
            }''',
           '''void suma() { mapA23 = 1; }''',
           '''int suma() { mapA23 = 'asd'; }''',
           '''void suma(int numero1, int numero2) { mapA23 = 1; }''',
           '''int suma(int numero1, int numero2) { 
                mapA23 = numero1 + numero2; 
                while(a==b){
                    var y;
                    int x = 2*5+3;
                    prom(x,y);
                    x++;
                    --y;
                }
            }''',
           '''void cambiar() => cadena = 'asd';''',
           '''int suma(int numero1, int numero2) => valor = numero1 + numero2;''',
           '''Set<int> conjunto = {1,4,5,3,5};''',
           '''while(a==b){
                var y;
                int x = 2*5+3;
                prom(x,y);
                x++;
                --y;
                if(a>b){
                    var x;
                    x = 123;
                }
            }''',
            '''for(int x in numbers){
              print(x);
            }''',
            '''for(int i = 0; i < 10; i++){
              print(x);
            }''',
           '''void realizarCalculo(int x, int y, String operacion){
                      switch(operacion) {
                        case "suma":
                          print(x+y);
                          break;
                        case "multiplicacion": {
                          print(x*y);
                          var y;
                        } break;
                        case "factorial": {
                          print(fact(x));
                        } break;
                        default:{
                          print("operacion ilegal");
                          var x;
                        }break;
                      }
                    }''',
           '''import 'dart:math';''',
            '''import 'dart:math' as math;''',
           '''
               import 'dart:math';
               main() {
                 realizarCalculo(-5.2,3,"avsdDF2242 .!@#$%^&*()[]{}\¡¿?;:|/=+-_`~");
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
                    break;
                 }
               }
               //función para calcular el factorial de un numero
                int fact(int num){
                   var factorial = 1;
                
                  
                  return factorial;
                }
           '''
           ]
for prueba in pruebas:
    print(prueba)
    receiveParse(prueba)
#while (usrInput != 'exit'):
#    try:
#        usrInput = input('Ingrese una entrada > ')
#    except EOFError:
#        break
#    if not usrInput: continue
#    receiveParse(usrInput)
