import ply.yacc as yacc
from analisis_lexico import tokens

#falta por hacer While, For, Switch Case, pruebas para funciones, sets y listas
start = 'programa'

def p_programa(p):
    '''programa : item_programa programa
                | item_programa
                | funcion'''

def p_item_programa(p):
    '''item_programa : instruccion
                    | clase
                    | ABSTRACT clase
                    | funcion
                    | instruccion_if'''

def p_instrucciones(p):
    '''instrucciones : instruccion'''

def p_instruccion(p):
    '''instruccion : asignacion
                    | FINAL asignacion
                    | declaracion'''

#Reglas if-else - XavierCarlier
def p_instruccion_if(p):
    '''instruccion_if : IF PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA
                    | IF PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA instruccion_else'''

def p_instruccion_else(p):
    '''instruccion_else : ELSE IF PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA instruccion_else
                        | ELSE IF PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA
                        | ELSE LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA'''

def p_items_estructura_control(p):
    '''items_estructura_control : item_estructura_control items_estructura_control
                                | item_estructura_control'''

def p_item_estructura_control(p):
    '''item_estructura_control : instruccion
                                | instruccion_if
                                | llamadas_func'''

#Reglas de clases - XavierCarlier
#todo:constructores

def p_clase(p):
    '''clase : CLASS IDENTIFICADOR LLAVE_APERTURA bloque_clase LLAVE_CLAUSURA'''

def p_bloque_clase(p):
    '''bloque_clase : item_bloque_clase bloque_clase
                    | item_bloque_clase'''

def p_item_bloque_clase(p):
    '''item_bloque_clase : instruccion
                        | funcion'''

def p_nuevo_objeto(p):
    '''nuevo_objeto : NEW IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA'''

#Reglas de llamadas a funciones - XavierCarlier
def p_llamadas_func(p):
    '''llamadas_func : IDENTIFICADOR PUNTO llamadas_func
                    | llamada_func PUNTO llamadas_func
                    | IDENTIFICADOR
                    | llamada_func'''

def p_llamada_func(p):
    '''llamada_func : IDENTIFICADOR PARENTESIS_APERTURA params PARENTESIS_CLAUSURA
                    | IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA'''

def p_params(p):
    '''params : valor_general COMA params
                | valor_general'''

#Reglas de declaraciones - XavierCarlier - Jeffrey Prado
def p_declaracion_general(p):
    '''declaracion_general : TIPO_INT IDENTIFICADOR
                | TIPO_DOUBLE IDENTIFICADOR
                | TIPO_BOOL IDENTIFICADOR
                | VAR IDENTIFICADOR
                | DYNAMIC IDENTIFICADOR
                | TIPO_STRING IDENTIFICADOR
                | TIPO_LIST IDENTIFICADOR
                | TIPO_SET IDENTIFICADOR
                | TIPO_MAP IDENTIFICADOR
                | TIPO_SYMBOL IDENTIFICADOR
                | TIPO_OBJECT IDENTIFICADOR
                | TIPO_FUTURE IDENTIFICADOR
                | TIPO_STREAM IDENTIFICADOR
                | TIPO_ITERABLE IDENTIFICADOR
                | TIPO_NEVER IDENTIFICADOR'''

def p_declaracion(p):
    '''declaracion : declaracion_general PUNTO_COMA'''


#Reglas de asignacion - Xavier Carlier
def p_asignacion(p):
    '''asignacion : TIPO_INT IDENTIFICADOR SIGNO_IGUAL expresion_mat_int PUNTO_COMA
                | TIPO_DOUBLE IDENTIFICADOR SIGNO_IGUAL expresion_mat_double PUNTO_COMA
                | TIPO_BOOL IDENTIFICADOR SIGNO_IGUAL expresion_logica PUNTO_COMA
                | TIPO_STRING IDENTIFICADOR SIGNO_IGUAL DATO_CADENA_TEXTO PUNTO_COMA
                | VAR IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA
                | DYNAMIC IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA
                | IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA
                | IDENTIFICADOR SIGNO_MAS SIGNO_IGUAL expresion_mat_double PUNTO_COMA
                | IDENTIFICADOR SIGNO_MENOS SIGNO_IGUAL expresion_mat_double PUNTO_COMA
                | TIPO_MAP IDENTIFICADOR SIGNO_IGUAL bloque_mapa PUNTO_COMA
                | valor_mapa_lista SIGNO_IGUAL valor_general PUNTO_COMA
                | TIPO_LIST IDENTIFICADOR SIGNO_IGUAL lista PUNTO_COMA
                | TIPO_LIST SIGNO_MENOR_QUE IDENTIFICADOR SIGNO_MAYOR_QUE SIGNO_IGUAL lista PUNTO_COMA
                | VAR IDENTIFICADOR SIGNO_IGUAL conjunto_especifico PUNTO_COMA
                | TIPO_SET SIGNO_MENOR_QUE IDENTIFICADOR SIGNO_MAYOR_QUE SIGNO_IGUAL conjunto PUNTO_COMA'''

#Reglas de mapa - XavierCarlier
def p_bloque_mapa(p):
    '''bloque_mapa : LLAVE_APERTURA pares_llave_valor LLAVE_CLAUSURA
                    | LLAVE_APERTURA LLAVE_CLAUSURA
                    | NEW TIPO_MAP PARENTESIS_APERTURA PARENTESIS_CLAUSURA'''

def p_pares_llave_valor(p):
    '''pares_llave_valor : par_llave_valor COMA pares_llave_valor
                        | par_llave_valor'''

def p_par_llave_valor(p):
    '''par_llave_valor : valor_general DOBLE_PUNTO valor_general'''

def p_valor_general(p):
    '''valor_general : expresion_mat_double
                    | expresion_logica
                    | DATO_CADENA_TEXTO
                    | llamadas_func
                    | nuevo_objeto
                    | NULL'''

def p_valor_mapa_lista(p):
    '''valor_mapa_lista : IDENTIFICADOR CORCHETE_APERTURA valor_general CORCHETE_CLAUSURA'''

#reglas para operaciones matemáticas int y double - XavierCarlier
def p_expresion_mat_int(p):
    '''expresion_mat_int : expresion_int_no_menos
                    | SIGNO_MENOS expresion_int_no_menos'''

def p_expresion_int_no_menos(p):
    '''expresion_int_no_menos : expresion_int_no_menos SIGNO_MAS expresion_int_no_menos
                    | expresion_int_no_menos SIGNO_MENOS expresion_int_no_menos
                    | expresion_int_no_menos SIGNO_MULTIPLICACION expresion_int_no_menos
                    | expresion_int_no_menos PORCENTAJE expresion_int_no_menos
                    | expresion_int_no_menos VIRGULILLA SIGNO_DIVISION expresion_int_no_menos
                    | PARENTESIS_APERTURA expresion_int_no_menos PARENTESIS_CLAUSURA
                    | DATO_ENTERO
                    | IDENTIFICADOR'''

def p_expresion_mat_double(p):
    '''expresion_mat_double : expresion_double_no_menos
                    | SIGNO_MENOS expresion_double_no_menos'''

def p_expresion_double_no_menos(p):
    '''expresion_double_no_menos : expresion_double_no_menos SIGNO_MAS expresion_double_no_menos
                    | expresion_double_no_menos SIGNO_MENOS expresion_double_no_menos
                    | expresion_double_no_menos SIGNO_MULTIPLICACION expresion_double_no_menos
                    | expresion_double_no_menos PORCENTAJE expresion_double_no_menos
                    | expresion_double_no_menos SIGNO_DIVISION expresion_double_no_menos
                    | PARENTESIS_APERTURA expresion_double_no_menos PARENTESIS_CLAUSURA
                    | DATO_DOBLE
                    | DATO_ENTERO
                    | IDENTIFICADOR'''

#Reglas para operaciones lógicas - XavierCarlier
def p_expresion_logica(p):
    '''expresion_logica : expresion_logica PLECA PLECA expresion_logica
                        | expresion_logica ET ET expresion_logica
                        | PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA
                        | SIGNO_ADMIRACION_APERTURA expresion_logica
                        | comparacion
                        | TRUE
                        | FALSE
                        | IDENTIFICADOR'''

def p_comparacion(p):
    '''comparacion : expresion_mat_double SIGNO_MENOR_QUE expresion_mat_double
                | expresion_mat_double SIGNO_MAYOR_QUE expresion_mat_double
                | expresion_mat_double SIGNO_MENOR_QUE SIGNO_IGUAL expresion_mat_double
                | expresion_mat_double SIGNO_MAYOR_QUE SIGNO_IGUAL expresion_mat_double
                | expresion_mat_double SIGNO_IGUAL SIGNO_IGUAL expresion_mat_double
                | expresion_mat_double SIGNO_ADMIRACION_APERTURA SIGNO_IGUAL expresion_mat_double'''

# Reglas de Lista - Jeffrey Prado
def p_lista(p):
    '''lista : CORCHETE_APERTURA lista_general CORCHETE_CLAUSURA
                | CORCHETE_APERTURA CORCHETE_CLAUSURA
                | CORCHETE_APERTURA DATO_ENTERO CORCHETE_CLAUSURA
                | NEW TIPO_LIST CORCHETE_APERTURA CORCHETE_CLAUSURA
                | NEW TIPO_LIST CORCHETE_APERTURA DATO_ENTERO CORCHETE_CLAUSURA'''

def p_lista_general(p):
    '''lista_general : valor_general 
                        | valor_general COMA lista_general'''

def p_lista_numeros(p):
    '''lista_numeros : DATO_ENTERO 
                        | DATO_ENTERO COMA lista_numeros'''

def p_lista_dobles(p):
    '''lista_dobles : DATO_DOBLE 
                        | DATO_DOBLE COMA lista_dobles'''

def p_lista_cadenas(p):
    '''lista_cadenas : DATO_CADENA_TEXTO 
                        | DATO_CADENA_TEXTO COMA lista_cadenas'''

# Reglas de Conjunto - Jeffrey Prado
def p_conjunto(p):
    '''conjunto : LLAVE_APERTURA lista_numeros LLAVE_CLAUSURA
                    | LLAVE_APERTURA lista_dobles LLAVE_CLAUSURA
                    | LLAVE_APERTURA lista_cadenas LLAVE_CLAUSURA'''

def p_conjunto_especifico(p):
    '''conjunto_especifico : SIGNO_MENOR_QUE TIPO_INT SIGNO_MAYOR_QUE lista_numeros LLAVE_CLAUSURA
                            | SIGNO_MENOR_QUE TIPO_DOUBLE SIGNO_MAYOR_QUE lista_dobles LLAVE_CLAUSURA
                            | SIGNO_MENOR_QUE TIPO_STRING SIGNO_MAYOR_QUE lista_cadenas LLAVE_CLAUSURA'''

# Regla de Funciones - Jeffrey Prado
def p_funcion(p):
    '''funcion : VOID IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA LLAVE_APERTURA instrucciones LLAVE_CLAUSURA
                | declaracion_general PARENTESIS_APERTURA PARENTESIS_CLAUSURA LLAVE_APERTURA instrucciones LLAVE_CLAUSURA
                | VOID IDENTIFICADOR PARENTESIS_APERTURA parametros PARENTESIS_CLAUSURA LLAVE_APERTURA instrucciones LLAVE_CLAUSURA
                | declaracion_general PARENTESIS_APERTURA parametros PARENTESIS_CLAUSURA LLAVE_APERTURA instrucciones LLAVE_CLAUSURA'''

                # TODO: revisar funcion flecha
                # declaracion_general SIGNO_IGUAL PARENTESIS_APERTURA PARENTESIS_CLAUSURA SIGNO_IGUAL SIGNO_MAYOR_QUE LLAVE_APERTURA instrucciones LLAVE_CLAUSURA
                # | declaracion_general SIGNO_IGUAL PARENTESIS_APERTURA parametros PARENTESIS_CLAUSURA
                # | declaracion_general SIGNO_IGUAL PARENTESIS_APERTURA PARENTESIS_CLAUSURA SIGNO_IGUAL SIGNO_MAYOR_QUE LLAVE_APERTURA instrucciones LLAVE_CLAUSURA
                # | declaracion_general SIGNO_IGUAL PARENTESIS_APERTURA parametros PARENTESIS_CLAUSURA SIGNO_IGUAL SIGNO_MAYOR_QUE LLAVE_APERTURA instrucciones LLAVE_CLAUSURA

def p_parametros(p):
    '''parametros : declaracion_general
                    | declaracion_general COMA parametros'''


def p_error(p):
    print('Syntax Error')

parser = yacc.yacc()

def receiveParse(input):
    result = parser.parse(input)
    print(result)