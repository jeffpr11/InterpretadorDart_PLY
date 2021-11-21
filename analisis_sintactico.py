import ply.yacc as yacc
from analisis_lexico import tokens

start = 'instrucciones'


def p_instrucciones(p):
    '''instrucciones : instruccion instrucciones
                    | instruccion'''

def p_insruccion(p):
    '''instruccion : asignacion
                    | declaracion
                    | llamada_func'''

#Reglas de llamadas a funciones - XavierCarlier
def p_llamada_func(p):
    '''llamada_func : IDENTIFICADOR PARENTESIS_APERTURA params PARENTESIS_CLAUSURA PUNTO_COMA'''

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
                | VAR IDENTIFICADOR SIGNO_IGUAL llamada_func
                | DYNAMIC IDENTIFICADOR SIGNO_IGUAL llamada_func
                | IDENTIFICADOR SIGNO_IGUAL llamada_func
                | IDENTIFICADOR SIGNO_MAS SIGNO_IGUAL expresion_mat_double PUNTO_COMA
                | IDENTIFICADOR SIGNO_MENOS SIGNO_IGUAL expresion_mat_double PUNTO_COMA'''

def p_valor_general(p):
    '''valor_general : IDENTIFICADOR
                    | expresion_mat_double
                    | expresion_logica
                    | DATO_CADENA_TEXTO
                    | NULL'''

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