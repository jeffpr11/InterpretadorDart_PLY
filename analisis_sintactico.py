import ply.yacc as yacc
from analisis_lexico import tokens

errores = []
reglaSemInt = []
reglaSemDoub = []

#falta por hacer For
start = 'programa'

def p_programa(p):
    '''programa : item_programa programa
                | item_programa'''

def p_item_programa(p):
    '''item_programa : instruccion
                    | clase
                    | ABSTRACT clase
                    | funcion
                    | instruccion_if
                    | instruccion_while
                    | import'''

def p_import(p):
    '''import : IMPORT DATO_CADENA_TEXTO AS IDENTIFICADOR PUNTO_COMA
                | IMPORT DATO_CADENA_TEXTO PUNTO_COMA'''

def p_instruccion(p):
    '''instruccion : asignacion
                    | FINAL asignacion
                    | declaracion
                    | operacion_unitaria PUNTO_COMA'''

def p_operacion_unitaria(p):
    '''operacion_unitaria : IDENTIFICADOR SIGNO_MAS SIGNO_MAS
                        | IDENTIFICADOR SIGNO_MENOS SIGNO_MENOS
                        | SIGNO_MAS SIGNO_MAS IDENTIFICADOR
                        | SIGNO_MENOS SIGNO_MENOS IDENTIFICADOR'''

#Reglas while - XavierCarlier
def p_instruccion_while(p):
    '''instruccion_while : WHILE PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA'''

#Reglas switch-case - XavierCarlier
def p_instruccion_switch(p):
    '''instruccion_switch : SWITCH PARENTESIS_APERTURA IDENTIFICADOR PARENTESIS_CLAUSURA LLAVE_APERTURA bloque_switch LLAVE_CLAUSURA'''

def p_bloque_switch(p):
    '''bloque_switch : instrucciones_case instruccion_default
                    | instrucciones_case'''

def p_instrucciones_case(p):
    '''instrucciones_case : instruccion_case instrucciones_case
                            | instruccion_case'''

def p_instruccion_case(p):
    '''instruccion_case : CASE valor_general DOBLE_PUNTO LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA BREAK PUNTO_COMA
                        | CASE valor_general DOBLE_PUNTO instruccion BREAK PUNTO_COMA
                        | CASE valor_general DOBLE_PUNTO llamadas_func PUNTO_COMA BREAK PUNTO_COMA'''

def p_instruccion_default(p):
    '''instruccion_default : DEFAULT DOBLE_PUNTO LLAVE_APERTURA items_estructura_control LLAVE_CLAUSURA BREAK PUNTO_COMA
                            | DEFAULT DOBLE_PUNTO instruccion BREAK PUNTO_COMA
                            | DEFAULT DOBLE_PUNTO llamadas_func PUNTO_COMA BREAK PUNTO_COMA'''

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
                                | llamadas_func PUNTO_COMA
                                | instruccion_if
                                | instruccion_while'''

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
                    | llamada_func'''

def p_llamada_func(p):
    '''llamada_func : IDENTIFICADOR PARENTESIS_APERTURA params PARENTESIS_CLAUSURA
                    | IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA'''

def p_params(p):
    '''params : valor_general COMA params
                | valor_general'''

#Reglas de declaraciones - XavierCarlier - Jeffrey Prado
def p_declaracion_general(p):
    '''declaracion_general : tipos_declaracion IDENTIFICADOR
                            | TIPO_MAP IDENTIFICADOR
                            | TIPO_LIST IDENTIFICADOR
                            | VAR IDENTIFICADOR
                            | DYNAMIC IDENTIFICADOR
                            | TIPO_BOOL IDENTIFICADOR
                            | TIPO_DOUBLE IDENTIFICADOR
                            | TIPO_INT IDENTIFICADOR
                            | TIPO_STRING IDENTIFICADOR'''

def p_tipos_declaracion(p):
    '''tipos_declaracion : TIPO_SET
                        | TIPO_SYMBOL
                        | TIPO_OBJECT
                        | TIPO_FUTURE
                        | TIPO_STREAM
                        | TIPO_ITERABLE
                        | TIPO_NEVER'''

def p_declaracion(p):
    '''declaracion : declaracion_general PUNTO_COMA'''


#Reglas de asignacion - Xavier Carlier
def p_asignacion(p):
    '''asignacion : asignacion_int
                | asignacion_double
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
                | TIPO_LIST SIGNO_MENOR_QUE IDENTIFICADOR SIGNO_MAYOR_QUE IDENTIFICADOR SIGNO_IGUAL lista PUNTO_COMA
                | VAR IDENTIFICADOR SIGNO_IGUAL lista PUNTO_COMA
                | VAR IDENTIFICADOR SIGNO_IGUAL conjunto_especifico PUNTO_COMA
                | TIPO_SET cast_int IDENTIFICADOR SIGNO_IGUAL LLAVE_APERTURA lista_numeros LLAVE_CLAUSURA PUNTO_COMA
                | TIPO_SET cast_double IDENTIFICADOR SIGNO_IGUAL LLAVE_APERTURA lista_dobles LLAVE_CLAUSURA PUNTO_COMA
                | TIPO_SET cast_string IDENTIFICADOR SIGNO_IGUAL LLAVE_APERTURA lista_cadenas LLAVE_CLAUSURA PUNTO_COMA'''

#Separación de reglas semánticas para int y double - XavierCarlier
def p_asignacion_int(p):
    '''asignacion_int : TIPO_INT IDENTIFICADOR SIGNO_IGUAL expresion_mat_int PUNTO_COMA'''
    reglaSemInt.append(f'INFO -> se ha evaluado una regla semántica para la asignación de int\n')
    print(f"INFO -> se ha evaluado una regla semántica para la asignación de int\n")

def p_asignacion_double(p):
    '''asignacion_double : TIPO_DOUBLE IDENTIFICADOR SIGNO_IGUAL expresion_mat_double PUNTO_COMA'''
    reglaSemDoub.append(f'INFO -> se ha evaluado una regla semántica para la asignación de double\n')
    print("INFO -> se ha evaluado una regla semántica para la asignación de double\n")

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
                | TIPO_LIST PARENTESIS_APERTURA DATO_ENTERO PARENTESIS_CLAUSURA
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
def p_conjunto_especifico(p):
    '''conjunto_especifico : cast_int LLAVE_APERTURA lista_numeros LLAVE_CLAUSURA
                            | cast_double LLAVE_APERTURA lista_dobles LLAVE_CLAUSURA
                            | cast_string LLAVE_APERTURA lista_cadenas LLAVE_CLAUSURA'''

def p_cast_int(p):
    '''cast_int : SIGNO_MENOR_QUE TIPO_INT SIGNO_MAYOR_QUE'''

def p_cast_double(p):
    '''cast_double : SIGNO_MENOR_QUE TIPO_DOUBLE SIGNO_MAYOR_QUE'''

def p_cast_string(p):
    '''cast_string : SIGNO_MENOR_QUE TIPO_STRING SIGNO_MAYOR_QUE'''

# Regla de Funciones - Jeffrey Prado
def p_funcion(p):
    '''funcion : MAIN PARENTESIS_APERTURA PARENTESIS_CLAUSURA LLAVE_APERTURA items_funcion LLAVE_CLAUSURA
                | VOID IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA LLAVE_APERTURA items_funcion LLAVE_CLAUSURA
                | declaracion_general PARENTESIS_APERTURA PARENTESIS_CLAUSURA LLAVE_APERTURA items_funcion LLAVE_CLAUSURA
                | VOID IDENTIFICADOR PARENTESIS_APERTURA parametros PARENTESIS_CLAUSURA LLAVE_APERTURA items_funcion LLAVE_CLAUSURA
                | declaracion_general PARENTESIS_APERTURA parametros PARENTESIS_CLAUSURA LLAVE_APERTURA items_funcion LLAVE_CLAUSURA
                | VOID IDENTIFICADOR funcion_flecha
                | declaracion_general funcion_flecha'''

def p_funcion_flecha(p):
    '''funcion_flecha : PARENTESIS_APERTURA PARENTESIS_CLAUSURA SIGNO_IGUAL SIGNO_MAYOR_QUE item_funcion
                      | PARENTESIS_APERTURA parametros PARENTESIS_CLAUSURA SIGNO_IGUAL SIGNO_MAYOR_QUE item_funcion'''

def p_parametros(p):
    '''parametros : declaracion_general
                    | declaracion_general COMA parametros'''

def p_items_funcion(p):
    '''items_funcion : item_funcion items_funcion
                    | item_funcion'''

def p_item_funcion(p):
    '''item_funcion : instruccion
                    | instruccion_if
                    | llamadas_func PUNTO_COMA
                    | instruccion_while
                    | instruccion_switch
                    | inst_return'''

def p_inst_return(p):
    '''inst_return : RETURN valor_general PUNTO_COMA'''

def p_error(p):
    if p:
        errMsg = f'Error de sintaxis en el token {p}'
        print(errMsg)
        errores.append(errMsg)

parser = yacc.yacc()

def receiveParse(input):
    result = parser.parse(input)
    print(result)