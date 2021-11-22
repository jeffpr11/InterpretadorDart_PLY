import ply.yacc as yacc
from analisis_lexico import tokens

start = 'programa'

def p_programa(p):
    '''programa : item_programa programa
                | item_programa'''

def p_item_programa(p):
    '''item_programa : instruccion
                    | clase
                    | ABSTRACT clase'''

def p_insruccion(p):
    '''instruccion : asignacion
                    | FINAL asignacion
                    | declaracion'''

#Reglas de clases - XavierCarlier
#todo:constructores

def p_clase(p):
    '''clase : CLASS IDENTIFICADOR LLAVE_APERTURA bloque_clase LLAVE_CLAUSURA'''

def p_bloque_clase(p):
    '''bloque_clase : item_bloque_clase bloque_clase
                    | item_bloque_clase'''

def p_item_bloque_clase(p):
    '''item_bloque_clase : instruccion'''

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

#Reglas de declaraciones - XavierCarlier
def p_declaracion(p):
    '''declaracion : TIPO_INT IDENTIFICADOR PUNTO_COMA
                | TIPO_DOUBLE IDENTIFICADOR PUNTO_COMA
                | TIPO_BOOL IDENTIFICADOR PUNTO_COMA
                | VAR IDENTIFICADOR PUNTO_COMA
                | DYNAMIC IDENTIFICADOR PUNTO_COMA
                | TIPO_STRING IDENTIFICADOR PUNTO_COMA
                | TIPO_LIST IDENTIFICADOR PUNTO_COMA
                | TIPO_SET IDENTIFICADOR PUNTO_COMA
                | TIPO_MAP IDENTIFICADOR PUNTO_COMA
                | TIPO_SYMBOL IDENTIFICADOR PUNTO_COMA
                | TIPO_OBJECT IDENTIFICADOR PUNTO_COMA
                | TIPO_FUTURE IDENTIFICADOR PUNTO_COMA
                | TIPO_STREAM IDENTIFICADOR PUNTO_COMA
                | TIPO_ITERABLE IDENTIFICADOR PUNTO_COMA
                | TIPO_NEVER IDENTIFICADOR PUNTO_COMA'''


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
                | valor_mapa_lista SIGNO_IGUAL valor_general PUNTO_COMA'''

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
    '''valor_general : IDENTIFICADOR
                    | expresion_mat_double
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

def p_error(p):
    print('Syntax Error')

parser = yacc.yacc()

def receiveParse(input):
    result = parser.parse(input)
    print(result)