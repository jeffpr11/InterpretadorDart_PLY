
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaABSTRACT ACENTO_AGUDO ACENTO_GRAVE ARROBA AS ASSERT ASYNC AWAIT BARRA_INVERTIDA BREAK CASE CATCH CLASS COMA COMENTARIO COMILLA_DOBLE COMILLA_SIMPLE CONST CONTINUE CORCHETE_APERTURA CORCHETE_CLAUSURA COVARIANT DATO_CADENA_TEXTO DATO_DOBLE DATO_ENTERO DEFAULT DEFERRED DO DOBLE_PUNTO DYNAMIC ELSE ENUM ET EXPORT EXTENDS EXTERNAL FACTORY FALSE FINAL FINALLY FOR FUNCTION GET HIDE IDENTIFICADOR IF IMPLEMENTS IMPORT INTERFACE IS LIBRARY LLAVE_APERTURA LLAVE_CLAUSURA MIXIN NEW NULL NUMERAL ON OPERATOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA PART PLECA PORCENTAJE PUNTO PUNTO_COMA RETHROW RETURN SET SHOW SIGNO_ADMIRACION_APERTURA SIGNO_ADMIRACION_CLAUSURA SIGNO_DIVISION SIGNO_IGUAL SIGNO_INTERROGACION_APERTURA SIGNO_INTERROGACION_CLAUSURA SIGNO_MAS SIGNO_MAYOR_QUE SIGNO_MENOR_QUE SIGNO_MENOS SIGNO_MULTIPLICACION STATIC SUPER SWITCH THIS THROW TIPO_BOOL TIPO_DOUBLE TIPO_FUTURE TIPO_INT TIPO_ITERABLE TIPO_LIST TIPO_MAP TIPO_NEVER TIPO_OBJECT TIPO_RUNE TIPO_SET TIPO_STREAM TIPO_STRING TIPO_SYMBOL TRUE TRY TYPEDEF VAR VIRGULILLA VOID WHILE WITH YIELDprograma : item_programa programa\n                | item_programaitem_programa : instruccion\n                    | clase\n                    | ABSTRACT claseinstruccion : asignacion\n                    | FINAL asignacion\n                    | declaracionclase : CLASS IDENTIFICADOR LLAVE_APERTURA bloque_clase LLAVE_CLAUSURAbloque_clase : item_bloque_clase bloque_clase\n                    | item_bloque_claseitem_bloque_clase : instruccionnuevo_objeto : NEW IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURAllamadas_func : IDENTIFICADOR PUNTO llamadas_func\n                    | llamada_func PUNTO llamadas_func\n                    | IDENTIFICADOR\n                    | llamada_funcllamada_func : IDENTIFICADOR PARENTESIS_APERTURA params PARENTESIS_CLAUSURA\n                    | IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURAparams : valor_general COMA params\n                | valor_generaldeclaracion : TIPO_INT IDENTIFICADOR PUNTO_COMA\n                | TIPO_DOUBLE IDENTIFICADOR PUNTO_COMA\n                | TIPO_BOOL IDENTIFICADOR PUNTO_COMA\n                | VAR IDENTIFICADOR PUNTO_COMA\n                | DYNAMIC IDENTIFICADOR PUNTO_COMA\n                | TIPO_STRING IDENTIFICADOR PUNTO_COMA\n                | TIPO_LIST IDENTIFICADOR PUNTO_COMA\n                | TIPO_SET IDENTIFICADOR PUNTO_COMA\n                | TIPO_MAP IDENTIFICADOR PUNTO_COMA\n                | TIPO_SYMBOL IDENTIFICADOR PUNTO_COMA\n                | TIPO_OBJECT IDENTIFICADOR PUNTO_COMA\n                | TIPO_FUTURE IDENTIFICADOR PUNTO_COMA\n                | TIPO_STREAM IDENTIFICADOR PUNTO_COMA\n                | TIPO_ITERABLE IDENTIFICADOR PUNTO_COMA\n                | TIPO_NEVER IDENTIFICADOR PUNTO_COMAasignacion : TIPO_INT IDENTIFICADOR SIGNO_IGUAL expresion_mat_int PUNTO_COMA\n                | TIPO_DOUBLE IDENTIFICADOR SIGNO_IGUAL expresion_mat_double PUNTO_COMA\n                | TIPO_BOOL IDENTIFICADOR SIGNO_IGUAL expresion_logica PUNTO_COMA\n                | TIPO_STRING IDENTIFICADOR SIGNO_IGUAL DATO_CADENA_TEXTO PUNTO_COMA\n                | VAR IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA\n                | DYNAMIC IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA\n                | IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA\n                | IDENTIFICADOR SIGNO_MAS SIGNO_IGUAL expresion_mat_double PUNTO_COMA\n                | IDENTIFICADOR SIGNO_MENOS SIGNO_IGUAL expresion_mat_double PUNTO_COMA\n                | TIPO_MAP IDENTIFICADOR SIGNO_IGUAL bloque_mapa PUNTO_COMA\n                | valor_mapa_lista SIGNO_IGUAL valor_general PUNTO_COMAbloque_mapa : LLAVE_APERTURA pares_llave_valor LLAVE_CLAUSURA\n                    | LLAVE_APERTURA LLAVE_CLAUSURA\n                    | NEW TIPO_MAP PARENTESIS_APERTURA PARENTESIS_CLAUSURApares_llave_valor : par_llave_valor COMA pares_llave_valor\n                        | par_llave_valorpar_llave_valor : valor_general DOBLE_PUNTO valor_generalvalor_general : IDENTIFICADOR\n                    | expresion_mat_double\n                    | expresion_logica\n                    | DATO_CADENA_TEXTO\n                    | llamadas_func\n                    | nuevo_objeto\n                    | NULLvalor_mapa_lista : IDENTIFICADOR CORCHETE_APERTURA valor_general CORCHETE_CLAUSURAexpresion_mat_int : expresion_int_no_menos\n                    | SIGNO_MENOS expresion_int_no_menosexpresion_int_no_menos : expresion_int_no_menos SIGNO_MAS expresion_int_no_menos\n                    | expresion_int_no_menos SIGNO_MENOS expresion_int_no_menos\n                    | expresion_int_no_menos SIGNO_MULTIPLICACION expresion_int_no_menos\n                    | expresion_int_no_menos PORCENTAJE expresion_int_no_menos\n                    | expresion_int_no_menos VIRGULILLA SIGNO_DIVISION expresion_int_no_menos\n                    | PARENTESIS_APERTURA expresion_int_no_menos PARENTESIS_CLAUSURA\n                    | DATO_ENTERO\n                    | IDENTIFICADORexpresion_mat_double : expresion_double_no_menos\n                    | SIGNO_MENOS expresion_double_no_menosexpresion_double_no_menos : expresion_double_no_menos SIGNO_MAS expresion_double_no_menos\n                    | expresion_double_no_menos SIGNO_MENOS expresion_double_no_menos\n                    | expresion_double_no_menos SIGNO_MULTIPLICACION expresion_double_no_menos\n                    | expresion_double_no_menos PORCENTAJE expresion_double_no_menos\n                    | expresion_double_no_menos SIGNO_DIVISION expresion_double_no_menos\n                    | PARENTESIS_APERTURA expresion_double_no_menos PARENTESIS_CLAUSURA\n                    | DATO_DOBLE\n                    | DATO_ENTERO\n                    | IDENTIFICADORexpresion_logica : expresion_logica PLECA PLECA expresion_logica\n                        | expresion_logica ET ET expresion_logica\n                        | PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA\n                        | SIGNO_ADMIRACION_APERTURA expresion_logica\n                        | comparacion\n                        | TRUE\n                        | FALSE\n                        | IDENTIFICADORcomparacion : expresion_mat_double SIGNO_MENOR_QUE expresion_mat_double\n                | expresion_mat_double SIGNO_MAYOR_QUE expresion_mat_double\n                | expresion_mat_double SIGNO_MENOR_QUE SIGNO_IGUAL expresion_mat_double\n                | expresion_mat_double SIGNO_MAYOR_QUE SIGNO_IGUAL expresion_mat_double\n                | expresion_mat_double SIGNO_IGUAL SIGNO_IGUAL expresion_mat_double\n                | expresion_mat_double SIGNO_ADMIRACION_APERTURA SIGNO_IGUAL expresion_mat_double'
    
_lr_action_items = {'ABSTRACT':([0,2,3,4,6,8,28,29,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,116,155,156,181,182,183,191,192,193,194,195,196,],[5,5,-3,-4,-6,-8,-5,-7,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'FINAL':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[7,7,-3,-4,-6,-8,-5,-7,7,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,7,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'CLASS':([0,2,3,4,5,6,8,28,29,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,116,155,156,181,182,183,191,192,193,194,195,196,],[9,9,-3,-4,9,-6,-8,-5,-7,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_INT':([0,2,3,4,6,7,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[11,11,-3,-4,-6,30,-8,-5,-7,11,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,11,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_DOUBLE':([0,2,3,4,6,7,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[12,12,-3,-4,-6,31,-8,-5,-7,12,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,12,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_BOOL':([0,2,3,4,6,7,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[13,13,-3,-4,-6,32,-8,-5,-7,13,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,13,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_STRING':([0,2,3,4,6,7,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[14,14,-3,-4,-6,33,-8,-5,-7,14,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,14,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'VAR':([0,2,3,4,6,7,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[15,15,-3,-4,-6,34,-8,-5,-7,15,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,15,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'DYNAMIC':([0,2,3,4,6,7,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[16,16,-3,-4,-6,35,-8,-5,-7,16,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,16,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'IDENTIFICADOR':([0,2,3,4,6,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,38,41,49,65,75,76,77,82,85,86,88,89,90,91,92,93,95,96,97,98,99,101,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,123,124,125,126,127,129,136,144,145,153,155,156,164,166,167,168,169,170,181,182,183,184,185,186,187,191,192,193,194,195,196,203,215,218,219,],[10,10,-3,-4,-6,10,-8,37,42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,-5,-7,58,59,60,61,62,63,64,66,66,66,10,130,133,133,137,130,130,141,-22,130,-23,133,-24,-27,66,-25,66,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,10,-12,158,66,-43,130,130,130,130,130,130,130,130,158,141,141,66,-47,-9,130,130,130,130,133,133,-44,-45,-37,141,141,141,141,-38,-39,-40,-41,-42,-46,66,141,66,66,]),'TIPO_MAP':([0,2,3,4,6,7,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,154,155,156,181,182,183,191,192,193,194,195,196,],[17,17,-3,-4,-6,36,-8,-5,-7,17,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,17,-12,-43,201,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_LIST':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[19,19,-3,-4,-6,-8,-5,-7,19,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,19,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_SET':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[20,20,-3,-4,-6,-8,-5,-7,20,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,20,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_SYMBOL':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[21,21,-3,-4,-6,-8,-5,-7,21,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,21,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_OBJECT':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[22,22,-3,-4,-6,-8,-5,-7,22,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,22,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_FUTURE':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[23,23,-3,-4,-6,-8,-5,-7,23,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,23,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_STREAM':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[24,24,-3,-4,-6,-8,-5,-7,24,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,24,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_ITERABLE':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[25,25,-3,-4,-6,-8,-5,-7,25,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,25,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'TIPO_NEVER':([0,2,3,4,6,8,28,29,65,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,112,113,116,155,156,181,182,183,191,192,193,194,195,196,],[26,26,-3,-4,-6,-8,-5,-7,26,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,26,-12,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'$end':([1,2,3,4,6,8,27,28,29,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,116,155,156,181,182,183,191,192,193,194,195,196,],[0,-2,-3,-4,-6,-8,-1,-5,-7,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,-43,-47,-9,-44,-45,-37,-38,-39,-40,-41,-42,-46,]),'LLAVE_CLAUSURA':([6,8,29,66,68,69,70,71,72,73,74,78,79,80,81,83,84,89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,111,112,113,116,128,130,133,135,153,155,157,158,159,161,163,165,171,172,173,174,175,177,178,179,181,182,183,191,192,193,194,195,196,197,199,202,204,205,206,207,208,209,210,223,224,],[-6,-8,-7,-16,-55,-56,-57,-58,-59,-60,-72,-87,-88,-89,-17,-80,-81,-22,-23,-24,-27,-25,-26,-30,-28,-29,-31,-32,-33,-34,-35,-36,156,-11,-12,-43,-73,-82,-90,-86,198,-47,-10,-16,-14,-19,-91,-92,-74,-75,-76,-77,-78,-85,-79,-15,-44,-45,-37,-38,-39,-40,-41,-42,-46,217,-52,-18,-93,-94,-95,-96,-83,-84,-13,-51,-53,]),'SIGNO_IGUAL':([10,18,39,40,42,43,44,45,46,47,48,58,59,60,61,62,63,64,66,68,74,83,84,117,118,119,120,128,130,132,133,134,140,171,172,173,174,175,178,],[38,49,85,86,88,90,92,94,96,98,100,88,90,92,94,96,98,100,-82,119,-72,-80,-81,164,166,167,168,-73,-82,-72,-82,119,-61,-74,-75,-76,-77,-78,-79,]),'SIGNO_MAS':([10,66,74,83,84,128,130,132,133,141,143,146,171,172,173,174,175,176,178,189,190,211,212,213,214,216,222,],[39,-82,123,-80,-81,123,-82,123,-82,-71,184,-70,123,123,123,123,123,123,-79,184,184,184,184,184,184,-69,184,]),'SIGNO_MENOS':([10,38,41,49,66,74,76,77,83,84,85,86,88,90,92,96,98,115,117,118,128,130,132,133,141,143,146,153,164,166,167,168,169,170,171,172,173,174,175,176,178,189,190,203,211,212,213,214,216,218,219,222,],[40,75,75,75,-82,124,75,75,-80,-81,75,75,144,75,75,75,75,75,75,75,124,-82,124,-82,-71,185,-70,75,75,75,75,75,75,75,124,124,124,124,124,124,-79,185,185,75,185,185,185,185,-69,75,75,185,]),'CORCHETE_APERTURA':([10,],[41,]),'LLAVE_APERTURA':([37,100,],[65,153,]),'DATO_CADENA_TEXTO':([38,41,49,94,96,98,115,153,203,218,219,],[70,70,70,149,70,70,70,70,70,70,70,]),'NULL':([38,41,49,96,98,115,153,203,218,219,],[73,73,73,73,73,73,73,73,73,73,]),'PARENTESIS_APERTURA':([38,41,49,66,75,76,77,85,86,88,90,92,96,98,115,117,118,123,124,125,126,127,129,137,144,145,153,158,164,166,167,168,169,170,184,185,186,187,201,203,215,218,219,],[76,76,76,115,129,76,76,129,129,145,129,76,76,76,76,129,129,129,129,129,129,129,129,180,145,145,76,115,129,129,129,129,76,76,145,145,145,145,220,76,145,76,76,]),'SIGNO_ADMIRACION_APERTURA':([38,41,49,66,68,74,76,77,83,84,92,96,98,115,128,130,132,133,134,153,169,170,171,172,173,174,175,178,203,218,219,],[77,77,77,-82,120,-72,77,77,-80,-81,77,77,77,77,-73,-82,-72,-82,120,77,77,77,-74,-75,-76,-77,-78,-79,77,77,77,]),'TRUE':([38,41,49,76,77,92,96,98,115,153,169,170,203,218,219,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'FALSE':([38,41,49,76,77,92,96,98,115,153,169,170,203,218,219,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'NEW':([38,41,49,96,98,100,115,153,203,218,219,],[82,82,82,82,82,154,82,82,82,82,82,]),'DATO_DOBLE':([38,41,49,75,76,77,85,86,90,92,96,98,115,117,118,123,124,125,126,127,129,153,164,166,167,168,169,170,203,218,219,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'DATO_ENTERO':([38,41,49,75,76,77,85,86,88,90,92,96,98,115,117,118,123,124,125,126,127,129,144,145,153,164,166,167,168,169,170,184,185,186,187,203,215,218,219,],[84,84,84,84,84,84,84,84,146,84,84,84,84,84,84,84,84,84,84,84,84,84,146,146,84,84,84,84,84,84,84,146,146,146,146,84,146,84,84,]),'PUNTO_COMA':([42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,66,67,68,69,70,71,72,73,74,78,79,80,81,83,84,102,128,130,133,135,138,139,141,142,143,146,147,148,149,150,151,152,158,159,161,163,165,171,172,173,174,175,177,178,179,189,198,202,204,205,206,207,208,209,210,211,212,213,214,216,217,222,225,],[89,91,93,95,97,99,101,103,104,105,106,107,108,109,110,-16,116,-55,-56,-57,-58,-59,-60,-72,-87,-88,-89,-17,-80,-81,155,-73,-82,-90,-86,181,182,-71,183,-62,-70,191,192,193,194,195,196,-16,-14,-19,-91,-92,-74,-75,-76,-77,-78,-85,-79,-15,-63,-49,-18,-93,-94,-95,-96,-83,-84,-13,-64,-65,-66,-67,-69,-48,-68,-50,]),'CORCHETE_CLAUSURA':([66,68,69,70,71,72,73,74,78,79,80,81,83,84,87,128,130,133,135,158,159,161,163,165,171,172,173,174,175,177,178,179,202,204,205,206,207,208,209,210,],[-16,-55,-56,-57,-58,-59,-60,-72,-87,-88,-89,-17,-80,-81,140,-73,-82,-90,-86,-16,-14,-19,-91,-92,-74,-75,-76,-77,-78,-85,-79,-15,-18,-93,-94,-95,-96,-83,-84,-13,]),'COMA':([66,68,69,70,71,72,73,74,78,79,80,81,83,84,128,130,133,135,158,159,161,162,163,165,171,172,173,174,175,177,178,179,199,202,204,205,206,207,208,209,210,224,],[-16,-55,-56,-57,-58,-59,-60,-72,-87,-88,-89,-17,-80,-81,-73,-82,-90,-86,-16,-14,-19,203,-91,-92,-74,-75,-76,-77,-78,-85,-79,-15,218,-18,-93,-94,-95,-96,-83,-84,-13,-53,]),'PARENTESIS_CLAUSURA':([66,68,69,70,71,72,73,74,78,79,80,81,83,84,115,128,130,131,132,133,135,141,146,158,159,160,161,162,163,165,171,172,173,174,175,176,177,178,179,180,190,202,204,205,206,207,208,209,210,211,212,213,214,216,220,221,222,],[-16,-55,-56,-57,-58,-59,-60,-72,-87,-88,-89,-17,-80,-81,161,-73,-82,177,178,-82,-86,-71,-70,-16,-14,202,-19,-21,-91,-92,-74,-75,-76,-77,-78,178,-85,-79,-15,210,216,-18,-93,-94,-95,-96,-83,-84,-13,-64,-65,-66,-67,-69,225,-20,-68,]),'DOBLE_PUNTO':([66,68,69,70,71,72,73,74,78,79,80,81,83,84,128,130,133,135,158,159,161,163,165,171,172,173,174,175,177,178,179,200,202,204,205,206,207,208,209,210,],[-16,-55,-56,-57,-58,-59,-60,-72,-87,-88,-89,-17,-80,-81,-73,-82,-90,-86,-16,-14,-19,-91,-92,-74,-75,-76,-77,-78,-85,-79,-15,219,-18,-93,-94,-95,-96,-83,-84,-13,]),'PLECA':([66,69,74,78,79,80,83,84,121,128,130,131,133,135,148,163,165,171,172,173,174,175,177,178,204,205,206,207,208,209,],[-90,121,-72,-87,-88,-89,-80,-81,169,-73,-82,121,-90,121,121,-91,-92,-74,-75,-76,-77,-78,-85,-79,-93,-94,-95,-96,121,121,]),'ET':([66,69,74,78,79,80,83,84,122,128,130,131,133,135,148,163,165,171,172,173,174,175,177,178,204,205,206,207,208,209,],[-90,122,-72,-87,-88,-89,-80,-81,170,-73,-82,122,-90,122,122,-91,-92,-74,-75,-76,-77,-78,-85,-79,-93,-94,-95,-96,122,122,]),'PUNTO':([66,81,158,161,202,],[114,136,114,-19,-18,]),'SIGNO_MULTIPLICACION':([66,74,83,84,128,130,132,133,141,143,146,171,172,173,174,175,176,178,189,190,211,212,213,214,216,222,],[-82,125,-80,-81,125,-82,125,-82,-71,186,-70,125,125,125,125,125,125,-79,186,186,186,186,186,186,-69,186,]),'PORCENTAJE':([66,74,83,84,128,130,132,133,141,143,146,171,172,173,174,175,176,178,189,190,211,212,213,214,216,222,],[-82,126,-80,-81,126,-82,126,-82,-71,187,-70,126,126,126,126,126,126,-79,187,187,187,187,187,187,-69,187,]),'SIGNO_DIVISION':([66,74,83,84,128,130,132,133,171,172,173,174,175,176,178,188,],[-82,127,-80,-81,127,-82,127,-82,127,127,127,127,127,127,-79,215,]),'SIGNO_MENOR_QUE':([66,68,74,83,84,128,130,132,133,134,171,172,173,174,175,178,],[-82,117,-72,-80,-81,-73,-82,-72,-82,117,-74,-75,-76,-77,-78,-79,]),'SIGNO_MAYOR_QUE':([66,68,74,83,84,128,130,132,133,134,171,172,173,174,175,178,],[-82,118,-72,-80,-81,-73,-82,-72,-82,118,-74,-75,-76,-77,-78,-79,]),'VIRGULILLA':([141,143,146,189,190,211,212,213,214,216,222,],[-71,188,-70,188,188,188,188,188,188,-69,188,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,],[1,27,]),'item_programa':([0,2,],[2,2,]),'instruccion':([0,2,65,112,],[3,3,113,113,]),'clase':([0,2,5,],[4,4,28,]),'asignacion':([0,2,7,65,112,],[6,6,29,6,6,]),'declaracion':([0,2,65,112,],[8,8,8,8,]),'valor_mapa_lista':([0,2,7,65,112,],[18,18,18,18,18,]),'valor_general':([38,41,49,96,98,115,153,203,218,219,],[67,87,102,150,151,162,200,162,200,224,]),'expresion_mat_double':([38,41,49,76,77,85,86,90,92,96,98,115,117,118,153,164,166,167,168,169,170,203,218,219,],[68,68,68,134,134,138,139,147,134,68,68,68,163,165,68,204,205,206,207,134,134,68,68,68,]),'expresion_logica':([38,41,49,76,77,92,96,98,115,153,169,170,203,218,219,],[69,69,69,131,135,148,69,69,69,69,208,209,69,69,69,]),'llamadas_func':([38,41,49,96,98,114,115,136,153,203,218,219,],[71,71,71,71,71,159,71,179,71,71,71,71,]),'nuevo_objeto':([38,41,49,96,98,115,153,203,218,219,],[72,72,72,72,72,72,72,72,72,72,]),'expresion_double_no_menos':([38,41,49,75,76,77,85,86,90,92,96,98,115,117,118,123,124,125,126,127,129,153,164,166,167,168,169,170,203,218,219,],[74,74,74,128,132,74,74,74,74,74,74,74,74,74,74,171,172,173,174,175,176,74,74,74,74,74,74,74,74,74,74,]),'comparacion':([38,41,49,76,77,92,96,98,115,153,169,170,203,218,219,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'llamada_func':([38,41,49,96,98,114,115,136,153,203,218,219,],[81,81,81,81,81,81,81,81,81,81,81,81,]),'bloque_clase':([65,112,],[111,157,]),'item_bloque_clase':([65,112,],[112,112,]),'expresion_mat_int':([88,],[142,]),'expresion_int_no_menos':([88,144,145,184,185,186,187,215,],[143,189,190,211,212,213,214,222,]),'bloque_mapa':([100,],[152,]),'params':([115,203,],[160,221,]),'pares_llave_valor':([153,218,],[197,223,]),'par_llave_valor':([153,218,],[199,199,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> item_programa programa','programa',2,'p_programa','analisis_sintactico.py',7),
  ('programa -> item_programa','programa',1,'p_programa','analisis_sintactico.py',8),
  ('item_programa -> instruccion','item_programa',1,'p_item_programa','analisis_sintactico.py',11),
  ('item_programa -> clase','item_programa',1,'p_item_programa','analisis_sintactico.py',12),
  ('item_programa -> ABSTRACT clase','item_programa',2,'p_item_programa','analisis_sintactico.py',13),
  ('instruccion -> asignacion','instruccion',1,'p_insruccion','analisis_sintactico.py',16),
  ('instruccion -> FINAL asignacion','instruccion',2,'p_insruccion','analisis_sintactico.py',17),
  ('instruccion -> declaracion','instruccion',1,'p_insruccion','analisis_sintactico.py',18),
  ('clase -> CLASS IDENTIFICADOR LLAVE_APERTURA bloque_clase LLAVE_CLAUSURA','clase',5,'p_clase','analisis_sintactico.py',23),
  ('bloque_clase -> item_bloque_clase bloque_clase','bloque_clase',2,'p_bloque_clase','analisis_sintactico.py',26),
  ('bloque_clase -> item_bloque_clase','bloque_clase',1,'p_bloque_clase','analisis_sintactico.py',27),
  ('item_bloque_clase -> instruccion','item_bloque_clase',1,'p_item_bloque_clase','analisis_sintactico.py',30),
  ('nuevo_objeto -> NEW IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA','nuevo_objeto',4,'p_nuevo_objeto','analisis_sintactico.py',33),
  ('llamadas_func -> IDENTIFICADOR PUNTO llamadas_func','llamadas_func',3,'p_llamadas_func','analisis_sintactico.py',37),
  ('llamadas_func -> llamada_func PUNTO llamadas_func','llamadas_func',3,'p_llamadas_func','analisis_sintactico.py',38),
  ('llamadas_func -> IDENTIFICADOR','llamadas_func',1,'p_llamadas_func','analisis_sintactico.py',39),
  ('llamadas_func -> llamada_func','llamadas_func',1,'p_llamadas_func','analisis_sintactico.py',40),
  ('llamada_func -> IDENTIFICADOR PARENTESIS_APERTURA params PARENTESIS_CLAUSURA','llamada_func',4,'p_llamada_func','analisis_sintactico.py',43),
  ('llamada_func -> IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA','llamada_func',3,'p_llamada_func','analisis_sintactico.py',44),
  ('params -> valor_general COMA params','params',3,'p_params','analisis_sintactico.py',47),
  ('params -> valor_general','params',1,'p_params','analisis_sintactico.py',48),
  ('declaracion -> TIPO_INT IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',52),
  ('declaracion -> TIPO_DOUBLE IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',53),
  ('declaracion -> TIPO_BOOL IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',54),
  ('declaracion -> VAR IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',55),
  ('declaracion -> DYNAMIC IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',56),
  ('declaracion -> TIPO_STRING IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',57),
  ('declaracion -> TIPO_LIST IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',58),
  ('declaracion -> TIPO_SET IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',59),
  ('declaracion -> TIPO_MAP IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',60),
  ('declaracion -> TIPO_SYMBOL IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',61),
  ('declaracion -> TIPO_OBJECT IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',62),
  ('declaracion -> TIPO_FUTURE IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',63),
  ('declaracion -> TIPO_STREAM IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',64),
  ('declaracion -> TIPO_ITERABLE IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',65),
  ('declaracion -> TIPO_NEVER IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',66),
  ('asignacion -> TIPO_INT IDENTIFICADOR SIGNO_IGUAL expresion_mat_int PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',71),
  ('asignacion -> TIPO_DOUBLE IDENTIFICADOR SIGNO_IGUAL expresion_mat_double PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',72),
  ('asignacion -> TIPO_BOOL IDENTIFICADOR SIGNO_IGUAL expresion_logica PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',73),
  ('asignacion -> TIPO_STRING IDENTIFICADOR SIGNO_IGUAL DATO_CADENA_TEXTO PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',74),
  ('asignacion -> VAR IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',75),
  ('asignacion -> DYNAMIC IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',76),
  ('asignacion -> IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',4,'p_asignacion','analisis_sintactico.py',77),
  ('asignacion -> IDENTIFICADOR SIGNO_MAS SIGNO_IGUAL expresion_mat_double PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',78),
  ('asignacion -> IDENTIFICADOR SIGNO_MENOS SIGNO_IGUAL expresion_mat_double PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',79),
  ('asignacion -> TIPO_MAP IDENTIFICADOR SIGNO_IGUAL bloque_mapa PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',80),
  ('asignacion -> valor_mapa_lista SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',4,'p_asignacion','analisis_sintactico.py',81),
  ('bloque_mapa -> LLAVE_APERTURA pares_llave_valor LLAVE_CLAUSURA','bloque_mapa',3,'p_bloque_mapa','analisis_sintactico.py',85),
  ('bloque_mapa -> LLAVE_APERTURA LLAVE_CLAUSURA','bloque_mapa',2,'p_bloque_mapa','analisis_sintactico.py',86),
  ('bloque_mapa -> NEW TIPO_MAP PARENTESIS_APERTURA PARENTESIS_CLAUSURA','bloque_mapa',4,'p_bloque_mapa','analisis_sintactico.py',87),
  ('pares_llave_valor -> par_llave_valor COMA pares_llave_valor','pares_llave_valor',3,'p_pares_llave_valor','analisis_sintactico.py',90),
  ('pares_llave_valor -> par_llave_valor','pares_llave_valor',1,'p_pares_llave_valor','analisis_sintactico.py',91),
  ('par_llave_valor -> valor_general DOBLE_PUNTO valor_general','par_llave_valor',3,'p_par_llave_valor','analisis_sintactico.py',94),
  ('valor_general -> IDENTIFICADOR','valor_general',1,'p_valor_general','analisis_sintactico.py',97),
  ('valor_general -> expresion_mat_double','valor_general',1,'p_valor_general','analisis_sintactico.py',98),
  ('valor_general -> expresion_logica','valor_general',1,'p_valor_general','analisis_sintactico.py',99),
  ('valor_general -> DATO_CADENA_TEXTO','valor_general',1,'p_valor_general','analisis_sintactico.py',100),
  ('valor_general -> llamadas_func','valor_general',1,'p_valor_general','analisis_sintactico.py',101),
  ('valor_general -> nuevo_objeto','valor_general',1,'p_valor_general','analisis_sintactico.py',102),
  ('valor_general -> NULL','valor_general',1,'p_valor_general','analisis_sintactico.py',103),
  ('valor_mapa_lista -> IDENTIFICADOR CORCHETE_APERTURA valor_general CORCHETE_CLAUSURA','valor_mapa_lista',4,'p_valor_mapa_lista','analisis_sintactico.py',106),
  ('expresion_mat_int -> expresion_int_no_menos','expresion_mat_int',1,'p_expresion_mat_int','analisis_sintactico.py',110),
  ('expresion_mat_int -> SIGNO_MENOS expresion_int_no_menos','expresion_mat_int',2,'p_expresion_mat_int','analisis_sintactico.py',111),
  ('expresion_int_no_menos -> expresion_int_no_menos SIGNO_MAS expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',114),
  ('expresion_int_no_menos -> expresion_int_no_menos SIGNO_MENOS expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',115),
  ('expresion_int_no_menos -> expresion_int_no_menos SIGNO_MULTIPLICACION expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',116),
  ('expresion_int_no_menos -> expresion_int_no_menos PORCENTAJE expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',117),
  ('expresion_int_no_menos -> expresion_int_no_menos VIRGULILLA SIGNO_DIVISION expresion_int_no_menos','expresion_int_no_menos',4,'p_expresion_int_no_menos','analisis_sintactico.py',118),
  ('expresion_int_no_menos -> PARENTESIS_APERTURA expresion_int_no_menos PARENTESIS_CLAUSURA','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',119),
  ('expresion_int_no_menos -> DATO_ENTERO','expresion_int_no_menos',1,'p_expresion_int_no_menos','analisis_sintactico.py',120),
  ('expresion_int_no_menos -> IDENTIFICADOR','expresion_int_no_menos',1,'p_expresion_int_no_menos','analisis_sintactico.py',121),
  ('expresion_mat_double -> expresion_double_no_menos','expresion_mat_double',1,'p_expresion_mat_double','analisis_sintactico.py',124),
  ('expresion_mat_double -> SIGNO_MENOS expresion_double_no_menos','expresion_mat_double',2,'p_expresion_mat_double','analisis_sintactico.py',125),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_MAS expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',128),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_MENOS expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',129),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_MULTIPLICACION expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',130),
  ('expresion_double_no_menos -> expresion_double_no_menos PORCENTAJE expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',131),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_DIVISION expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',132),
  ('expresion_double_no_menos -> PARENTESIS_APERTURA expresion_double_no_menos PARENTESIS_CLAUSURA','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',133),
  ('expresion_double_no_menos -> DATO_DOBLE','expresion_double_no_menos',1,'p_expresion_double_no_menos','analisis_sintactico.py',134),
  ('expresion_double_no_menos -> DATO_ENTERO','expresion_double_no_menos',1,'p_expresion_double_no_menos','analisis_sintactico.py',135),
  ('expresion_double_no_menos -> IDENTIFICADOR','expresion_double_no_menos',1,'p_expresion_double_no_menos','analisis_sintactico.py',136),
  ('expresion_logica -> expresion_logica PLECA PLECA expresion_logica','expresion_logica',4,'p_expresion_logica','analisis_sintactico.py',140),
  ('expresion_logica -> expresion_logica ET ET expresion_logica','expresion_logica',4,'p_expresion_logica','analisis_sintactico.py',141),
  ('expresion_logica -> PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA','expresion_logica',3,'p_expresion_logica','analisis_sintactico.py',142),
  ('expresion_logica -> SIGNO_ADMIRACION_APERTURA expresion_logica','expresion_logica',2,'p_expresion_logica','analisis_sintactico.py',143),
  ('expresion_logica -> comparacion','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',144),
  ('expresion_logica -> TRUE','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',145),
  ('expresion_logica -> FALSE','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',146),
  ('expresion_logica -> IDENTIFICADOR','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',147),
  ('comparacion -> expresion_mat_double SIGNO_MENOR_QUE expresion_mat_double','comparacion',3,'p_comparacion','analisis_sintactico.py',150),
  ('comparacion -> expresion_mat_double SIGNO_MAYOR_QUE expresion_mat_double','comparacion',3,'p_comparacion','analisis_sintactico.py',151),
  ('comparacion -> expresion_mat_double SIGNO_MENOR_QUE SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',152),
  ('comparacion -> expresion_mat_double SIGNO_MAYOR_QUE SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',153),
  ('comparacion -> expresion_mat_double SIGNO_IGUAL SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',154),
  ('comparacion -> expresion_mat_double SIGNO_ADMIRACION_APERTURA SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',155),
]
