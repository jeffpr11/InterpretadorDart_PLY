
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'instruccionesABSTRACT ACENTO_AGUDO ACENTO_GRAVE ARROBA AS ASSERT ASYNC AWAIT BARRA_INVERTIDA BREAK CASE CATCH CLASS COMA COMENTARIO COMILLA_DOBLE COMILLA_SIMPLE CONST CONTINUE CORCHETE_APERTURA CORCHETE_CLAUSURA COVARIANT DATO_CADENA_TEXTO DATO_DOBLE DATO_ENTERO DEFAULT DEFERRED DO DOBLE_PUNTO DYNAMIC ELSE ENUM ET EXPORT EXTENDS EXTERNAL FACTORY FALSE FINAL FINALLY FOR FUNCTION GET HIDE IDENTIFICADOR IF IMPLEMENTS IMPORT INTERFACE IS LIBRARY LLAVE_APERTURA LLAVE_CLAUSURA MIXIN NEW NULL NUMERAL ON OPERATOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA PART PLECA PORCENTAJE PUNTO PUNTO_COMA RETHROW RETURN SET SHOW SIGNO_ADMIRACION_APERTURA SIGNO_ADMIRACION_CLAUSURA SIGNO_DIVISION SIGNO_IGUAL SIGNO_INTERROGACION_APERTURA SIGNO_INTERROGACION_CLAUSURA SIGNO_MAS SIGNO_MAYOR_QUE SIGNO_MENOR_QUE SIGNO_MENOS SIGNO_MULTIPLICACION STATIC SUPER SWITCH THIS THROW TIPO_BOOL TIPO_DOUBLE TIPO_FUTURE TIPO_INT TIPO_ITERABLE TIPO_LIST TIPO_MAP TIPO_NEVER TIPO_OBJECT TIPO_RUNE TIPO_SET TIPO_STREAM TIPO_STRING TIPO_SYMBOL TRUE TRY TYPEDEF VAR VIRGULILLA VOID WHILE WITH YIELDinstrucciones : instruccion instrucciones\n                    | instruccioninstruccion : asignacion\n                    | declaracion\n                    | llamadas_func PUNTO_COMAllamadas_func : IDENTIFICADOR PUNTO llamadas_func\n                    | llamada_func PUNTO llamadas_func\n                    | IDENTIFICADOR\n                    | llamada_funcllamada_func : IDENTIFICADOR PARENTESIS_APERTURA params PARENTESIS_CLAUSURA\n                    | IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURAparams : valor_general COMA params\n                | valor_generaldeclaracion : TIPO_INT IDENTIFICADOR PUNTO_COMA\n                | TIPO_DOUBLE IDENTIFICADOR PUNTO_COMA\n                | TIPO_BOOL IDENTIFICADOR PUNTO_COMA\n                | VAR IDENTIFICADOR PUNTO_COMA\n                | DYNAMIC IDENTIFICADOR PUNTO_COMA\n                | TIPO_STRING IDENTIFICADOR PUNTO_COMA\n                | TIPO_LIST IDENTIFICADOR PUNTO_COMA\n                | TIPO_SET IDENTIFICADOR PUNTO_COMA\n                | TIPO_MAP IDENTIFICADOR PUNTO_COMA\n                | TIPO_SYMBOL IDENTIFICADOR PUNTO_COMA\n                | TIPO_OBJECT IDENTIFICADOR PUNTO_COMA\n                | TIPO_FUTURE IDENTIFICADOR PUNTO_COMA\n                | TIPO_STREAM IDENTIFICADOR PUNTO_COMA\n                | TIPO_ITERABLE IDENTIFICADOR PUNTO_COMA\n                | TIPO_NEVER IDENTIFICADOR PUNTO_COMAasignacion : TIPO_INT IDENTIFICADOR SIGNO_IGUAL expresion_mat_int PUNTO_COMA\n                | TIPO_DOUBLE IDENTIFICADOR SIGNO_IGUAL expresion_mat_double PUNTO_COMA\n                | TIPO_BOOL IDENTIFICADOR SIGNO_IGUAL expresion_logica PUNTO_COMA\n                | TIPO_STRING IDENTIFICADOR SIGNO_IGUAL DATO_CADENA_TEXTO PUNTO_COMA\n                | VAR IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA\n                | DYNAMIC IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA\n                | IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA\n                | IDENTIFICADOR SIGNO_MAS SIGNO_IGUAL expresion_mat_double PUNTO_COMA\n                | IDENTIFICADOR SIGNO_MENOS SIGNO_IGUAL expresion_mat_double PUNTO_COMA\n                | TIPO_MAP IDENTIFICADOR SIGNO_IGUAL bloque_mapa PUNTO_COMA\n                | valor_mapa_lista SIGNO_IGUAL valor_general PUNTO_COMAbloque_mapa : LLAVE_APERTURA pares_llave_valor LLAVE_CLAUSURA\n                    | LLAVE_APERTURA LLAVE_CLAUSURA\n                    | NEW TIPO_MAP PARENTESIS_APERTURA PARENTESIS_CLAUSURApares_llave_valor : par_llave_valor COMA pares_llave_valor\n                        | par_llave_valorpar_llave_valor : valor_general DOBLE_PUNTO valor_generalvalor_general : IDENTIFICADOR\n                    | expresion_mat_double\n                    | expresion_logica\n                    | DATO_CADENA_TEXTO\n                    | llamadas_func\n                    | NULLvalor_mapa_lista : IDENTIFICADOR CORCHETE_APERTURA valor_general CORCHETE_CLAUSURAexpresion_mat_int : expresion_int_no_menos\n                    | SIGNO_MENOS expresion_int_no_menosexpresion_int_no_menos : expresion_int_no_menos SIGNO_MAS expresion_int_no_menos\n                    | expresion_int_no_menos SIGNO_MENOS expresion_int_no_menos\n                    | expresion_int_no_menos SIGNO_MULTIPLICACION expresion_int_no_menos\n                    | expresion_int_no_menos PORCENTAJE expresion_int_no_menos\n                    | expresion_int_no_menos VIRGULILLA SIGNO_DIVISION expresion_int_no_menos\n                    | PARENTESIS_APERTURA expresion_int_no_menos PARENTESIS_CLAUSURA\n                    | DATO_ENTERO\n                    | IDENTIFICADORexpresion_mat_double : expresion_double_no_menos\n                    | SIGNO_MENOS expresion_double_no_menosexpresion_double_no_menos : expresion_double_no_menos SIGNO_MAS expresion_double_no_menos\n                    | expresion_double_no_menos SIGNO_MENOS expresion_double_no_menos\n                    | expresion_double_no_menos SIGNO_MULTIPLICACION expresion_double_no_menos\n                    | expresion_double_no_menos PORCENTAJE expresion_double_no_menos\n                    | expresion_double_no_menos SIGNO_DIVISION expresion_double_no_menos\n                    | PARENTESIS_APERTURA expresion_double_no_menos PARENTESIS_CLAUSURA\n                    | DATO_DOBLE\n                    | DATO_ENTERO\n                    | IDENTIFICADORexpresion_logica : expresion_logica PLECA PLECA expresion_logica\n                        | expresion_logica ET ET expresion_logica\n                        | PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA\n                        | SIGNO_ADMIRACION_APERTURA expresion_logica\n                        | comparacion\n                        | TRUE\n                        | FALSE\n                        | IDENTIFICADORcomparacion : expresion_mat_double SIGNO_MENOR_QUE expresion_mat_double\n                | expresion_mat_double SIGNO_MAYOR_QUE expresion_mat_double\n                | expresion_mat_double SIGNO_MENOR_QUE SIGNO_IGUAL expresion_mat_double\n                | expresion_mat_double SIGNO_MAYOR_QUE SIGNO_IGUAL expresion_mat_double\n                | expresion_mat_double SIGNO_IGUAL SIGNO_IGUAL expresion_mat_double\n                | expresion_mat_double SIGNO_ADMIRACION_APERTURA SIGNO_IGUAL expresion_mat_double'
    
_lr_action_items = {'TIPO_INT':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[6,6,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_DOUBLE':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[8,8,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_BOOL':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[9,9,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_STRING':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[10,10,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'VAR':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[11,11,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'DYNAMIC':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[12,12,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'IDENTIFICADOR':([0,2,3,4,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,25,27,30,31,32,39,48,49,50,59,60,61,67,68,75,76,77,78,80,81,82,83,84,86,88,89,90,91,92,93,94,95,100,101,103,104,105,110,111,112,113,114,116,127,134,136,137,138,139,140,141,146,148,149,150,151,152,161,162,164,165,166,167,168,169,179,188,189,],[7,7,-3,-4,26,33,34,35,36,37,38,40,41,42,43,44,45,46,47,-5,51,69,51,51,51,69,97,-14,117,120,120,117,117,117,-15,120,-16,-19,51,-17,51,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,97,97,-35,117,117,117,117,117,117,117,117,51,51,-39,-29,97,97,97,97,117,117,117,117,120,120,-36,-37,-30,-31,-32,-33,-34,-38,97,51,51,]),'TIPO_MAP':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,135,136,137,161,162,164,165,166,167,168,169,],[13,13,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,174,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_LIST':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[15,15,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_SET':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[16,16,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_SYMBOL':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[17,17,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_OBJECT':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[18,18,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_FUTURE':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[19,19,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_STREAM':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[20,20,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_ITERABLE':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[21,21,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'TIPO_NEVER':([0,2,3,4,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[22,22,-3,-4,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'$end':([1,2,3,4,24,25,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,103,136,137,161,162,164,165,166,167,168,169,],[0,-2,-3,-4,-1,-5,-14,-15,-16,-19,-17,-18,-22,-20,-21,-23,-24,-25,-26,-27,-28,-35,-39,-29,-36,-37,-30,-31,-32,-33,-34,-38,]),'PUNTO_COMA':([5,7,23,26,33,34,35,36,37,38,40,41,42,43,44,45,46,47,51,52,53,54,55,56,57,58,62,63,64,65,66,69,70,73,87,96,97,98,99,102,115,117,120,122,123,124,126,128,129,130,131,132,133,143,145,147,153,154,155,156,157,159,160,171,175,176,177,178,180,181,182,183,184,185,186,187,191,194,],[25,-8,-9,50,76,78,80,82,84,86,88,89,90,91,92,93,94,95,-8,103,-47,-48,-49,-50,-51,-63,-78,-79,-80,-71,-72,-8,-6,-11,136,-7,-62,137,-53,-61,-64,-73,-81,-77,161,162,-10,164,165,166,167,168,169,-54,-82,-83,-65,-66,-67,-68,-69,-76,-70,-41,-55,-56,-57,-58,-60,-84,-85,-86,-87,-74,-75,-40,-59,-42,]),'SIGNO_IGUAL':([7,14,26,28,29,33,34,35,36,37,38,51,53,58,65,66,104,105,106,107,115,117,119,120,121,125,153,154,155,156,157,160,],[27,39,49,67,68,75,77,79,81,83,85,-73,106,-63,-71,-72,146,148,149,150,-64,-73,-63,-73,106,-52,-65,-66,-67,-68,-69,-70,]),'SIGNO_MAS':([7,51,58,65,66,97,99,102,115,117,119,120,143,144,153,154,155,156,157,158,160,175,176,177,178,180,191,],[28,-73,110,-71,-72,-62,138,-61,110,-73,110,-73,138,138,110,110,110,110,110,110,-70,138,138,138,138,-60,138,]),'SIGNO_MENOS':([7,27,31,32,39,49,51,58,60,61,65,66,67,68,75,77,81,83,97,99,102,104,105,115,117,119,120,127,134,143,144,146,148,149,150,151,152,153,154,155,156,157,158,160,175,176,177,178,180,188,189,191,],[29,59,59,59,59,100,-73,111,59,59,-71,-72,59,59,59,59,59,59,-62,139,-61,59,59,111,-73,111,-73,59,59,139,139,59,59,59,59,59,59,111,111,111,111,111,111,-70,139,139,139,139,-60,59,59,139,]),'PUNTO':([7,23,51,69,73,126,],[30,48,30,30,-11,-10,]),'CORCHETE_APERTURA':([7,],[31,]),'PARENTESIS_APERTURA':([7,27,31,32,39,49,51,59,60,61,67,68,69,75,77,81,83,100,101,104,105,110,111,112,113,114,116,127,134,138,139,140,141,146,148,149,150,151,152,174,179,188,189,],[32,60,60,60,60,101,32,116,60,60,116,116,32,116,60,60,60,101,101,116,116,116,116,116,116,116,116,60,60,101,101,101,101,116,116,116,116,60,60,190,101,60,60,]),'CORCHETE_CLAUSURA':([23,51,53,54,55,56,57,58,62,63,64,65,66,69,70,71,73,96,115,117,120,122,126,145,147,153,154,155,156,157,159,160,181,182,183,184,185,186,],[-9,-8,-47,-48,-49,-50,-51,-63,-78,-79,-80,-71,-72,-8,-6,125,-11,-7,-64,-73,-81,-77,-10,-82,-83,-65,-66,-67,-68,-69,-76,-70,-84,-85,-86,-87,-74,-75,]),'COMA':([23,51,53,54,55,56,57,58,62,63,64,65,66,69,70,73,74,96,115,117,120,122,126,145,147,153,154,155,156,157,159,160,172,181,182,183,184,185,186,193,],[-9,-8,-47,-48,-49,-50,-51,-63,-78,-79,-80,-71,-72,-8,-6,-11,127,-7,-64,-73,-81,-77,-10,-82,-83,-65,-66,-67,-68,-69,-76,-70,188,-84,-85,-86,-87,-74,-75,-45,]),'PARENTESIS_CLAUSURA':([23,32,51,53,54,55,56,57,58,62,63,64,65,66,69,70,72,73,74,96,97,102,115,117,118,119,120,122,126,144,145,147,153,154,155,156,157,158,159,160,163,175,176,177,178,180,181,182,183,184,185,186,190,191,],[-9,73,-8,-47,-48,-49,-50,-51,-63,-78,-79,-80,-71,-72,-8,-6,126,-11,-13,-7,-62,-61,-64,-73,159,160,-73,-77,-10,180,-82,-83,-65,-66,-67,-68,-69,160,-76,-70,-12,-55,-56,-57,-58,-60,-84,-85,-86,-87,-74,-75,194,-59,]),'DOBLE_PUNTO':([23,51,53,54,55,56,57,58,62,63,64,65,66,69,70,73,96,115,117,120,122,126,145,147,153,154,155,156,157,159,160,173,181,182,183,184,185,186,],[-9,-8,-47,-48,-49,-50,-51,-63,-78,-79,-80,-71,-72,-8,-6,-11,-7,-64,-73,-81,-77,-10,-82,-83,-65,-66,-67,-68,-69,-76,-70,189,-84,-85,-86,-87,-74,-75,]),'LLAVE_CLAUSURA':([23,51,53,54,55,56,57,58,62,63,64,65,66,69,70,73,96,115,117,120,122,126,134,145,147,153,154,155,156,157,159,160,170,172,181,182,183,184,185,186,192,193,],[-9,-8,-47,-48,-49,-50,-51,-63,-78,-79,-80,-71,-72,-8,-6,-11,-7,-64,-73,-81,-77,-10,171,-82,-83,-65,-66,-67,-68,-69,-76,-70,187,-44,-84,-85,-86,-87,-74,-75,-43,-45,]),'DATO_CADENA_TEXTO':([27,31,32,39,79,81,83,127,134,188,189,],[55,55,55,55,130,55,55,55,55,55,55,]),'NULL':([27,31,32,39,81,83,127,134,188,189,],[57,57,57,57,57,57,57,57,57,57,]),'SIGNO_ADMIRACION_APERTURA':([27,31,32,39,51,53,58,60,61,65,66,77,81,83,115,117,119,120,121,127,134,151,152,153,154,155,156,157,160,188,189,],[61,61,61,61,-73,107,-63,61,61,-71,-72,61,61,61,-64,-73,-63,-73,107,61,61,61,61,-65,-66,-67,-68,-69,-70,61,61,]),'TRUE':([27,31,32,39,60,61,77,81,83,127,134,151,152,188,189,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'FALSE':([27,31,32,39,60,61,77,81,83,127,134,151,152,188,189,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'DATO_DOBLE':([27,31,32,39,59,60,61,67,68,75,77,81,83,104,105,110,111,112,113,114,116,127,134,146,148,149,150,151,152,188,189,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'DATO_ENTERO':([27,31,32,39,49,59,60,61,67,68,75,77,81,83,100,101,104,105,110,111,112,113,114,116,127,134,138,139,140,141,146,148,149,150,151,152,179,188,189,],[66,66,66,66,102,66,66,66,66,66,66,66,66,66,102,102,66,66,66,66,66,66,66,66,66,66,102,102,102,102,66,66,66,66,66,66,102,66,66,]),'PLECA':([51,54,58,62,63,64,65,66,108,115,117,118,120,122,129,145,147,153,154,155,156,157,159,160,181,182,183,184,185,186,],[-81,108,-63,-78,-79,-80,-71,-72,151,-64,-73,108,-81,108,108,-82,-83,-65,-66,-67,-68,-69,-76,-70,-84,-85,-86,-87,108,108,]),'ET':([51,54,58,62,63,64,65,66,109,115,117,118,120,122,129,145,147,153,154,155,156,157,159,160,181,182,183,184,185,186,],[-81,109,-63,-78,-79,-80,-71,-72,152,-64,-73,109,-81,109,109,-82,-83,-65,-66,-67,-68,-69,-76,-70,-84,-85,-86,-87,109,109,]),'SIGNO_MULTIPLICACION':([51,58,65,66,97,99,102,115,117,119,120,143,144,153,154,155,156,157,158,160,175,176,177,178,180,191,],[-73,112,-71,-72,-62,140,-61,112,-73,112,-73,140,140,112,112,112,112,112,112,-70,140,140,140,140,-60,140,]),'PORCENTAJE':([51,58,65,66,97,99,102,115,117,119,120,143,144,153,154,155,156,157,158,160,175,176,177,178,180,191,],[-73,113,-71,-72,-62,141,-61,113,-73,113,-73,141,141,113,113,113,113,113,113,-70,141,141,141,141,-60,141,]),'SIGNO_DIVISION':([51,58,65,66,115,117,119,120,142,153,154,155,156,157,158,160,],[-73,114,-71,-72,114,-73,114,-73,179,114,114,114,114,114,114,-70,]),'SIGNO_MENOR_QUE':([51,53,58,65,66,115,117,119,120,121,153,154,155,156,157,160,],[-73,104,-63,-71,-72,-64,-73,-63,-73,104,-65,-66,-67,-68,-69,-70,]),'SIGNO_MAYOR_QUE':([51,53,58,65,66,115,117,119,120,121,153,154,155,156,157,160,],[-73,105,-63,-71,-72,-64,-73,-63,-73,105,-65,-66,-67,-68,-69,-70,]),'LLAVE_APERTURA':([85,],[134,]),'NEW':([85,],[135,]),'VIRGULILLA':([97,99,102,143,144,175,176,177,178,180,191,],[-62,142,-61,142,142,142,142,142,142,-60,142,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,2,],[1,24,]),'instruccion':([0,2,],[2,2,]),'asignacion':([0,2,],[3,3,]),'declaracion':([0,2,],[4,4,]),'llamadas_func':([0,2,27,30,31,32,39,48,81,83,127,134,188,189,],[5,5,56,70,56,56,56,96,56,56,56,56,56,56,]),'valor_mapa_lista':([0,2,],[14,14,]),'llamada_func':([0,2,27,30,31,32,39,48,81,83,127,134,188,189,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'valor_general':([27,31,32,39,81,83,127,134,188,189,],[52,71,74,87,131,132,74,173,173,193,]),'expresion_mat_double':([27,31,32,39,60,61,67,68,75,77,81,83,104,105,127,134,146,148,149,150,151,152,188,189,],[53,53,53,53,121,121,123,124,128,121,53,53,145,147,53,53,181,182,183,184,121,121,53,53,]),'expresion_logica':([27,31,32,39,60,61,77,81,83,127,134,151,152,188,189,],[54,54,54,54,118,122,129,54,54,54,54,185,186,54,54,]),'expresion_double_no_menos':([27,31,32,39,59,60,61,67,68,75,77,81,83,104,105,110,111,112,113,114,116,127,134,146,148,149,150,151,152,188,189,],[58,58,58,58,115,119,58,58,58,58,58,58,58,58,58,153,154,155,156,157,158,58,58,58,58,58,58,58,58,58,58,]),'comparacion':([27,31,32,39,60,61,77,81,83,127,134,151,152,188,189,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'params':([32,127,],[72,163,]),'expresion_mat_int':([49,],[98,]),'expresion_int_no_menos':([49,100,101,138,139,140,141,179,],[99,143,144,175,176,177,178,191,]),'bloque_mapa':([85,],[133,]),'pares_llave_valor':([134,188,],[170,192,]),'par_llave_valor':([134,188,],[172,172,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones','analisis_sintactico.py',8),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','analisis_sintactico.py',9),
  ('instruccion -> asignacion','instruccion',1,'p_insruccion','analisis_sintactico.py',12),
  ('instruccion -> declaracion','instruccion',1,'p_insruccion','analisis_sintactico.py',13),
  ('instruccion -> llamadas_func PUNTO_COMA','instruccion',2,'p_insruccion','analisis_sintactico.py',14),
  ('llamadas_func -> IDENTIFICADOR PUNTO llamadas_func','llamadas_func',3,'p_llamadas_func','analisis_sintactico.py',18),
  ('llamadas_func -> llamada_func PUNTO llamadas_func','llamadas_func',3,'p_llamadas_func','analisis_sintactico.py',19),
  ('llamadas_func -> IDENTIFICADOR','llamadas_func',1,'p_llamadas_func','analisis_sintactico.py',20),
  ('llamadas_func -> llamada_func','llamadas_func',1,'p_llamadas_func','analisis_sintactico.py',21),
  ('llamada_func -> IDENTIFICADOR PARENTESIS_APERTURA params PARENTESIS_CLAUSURA','llamada_func',4,'p_llamada_func','analisis_sintactico.py',24),
  ('llamada_func -> IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CLAUSURA','llamada_func',3,'p_llamada_func','analisis_sintactico.py',25),
  ('params -> valor_general COMA params','params',3,'p_params','analisis_sintactico.py',28),
  ('params -> valor_general','params',1,'p_params','analisis_sintactico.py',29),
  ('declaracion -> TIPO_INT IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',33),
  ('declaracion -> TIPO_DOUBLE IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',34),
  ('declaracion -> TIPO_BOOL IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',35),
  ('declaracion -> VAR IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',36),
  ('declaracion -> DYNAMIC IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',37),
  ('declaracion -> TIPO_STRING IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',38),
  ('declaracion -> TIPO_LIST IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',39),
  ('declaracion -> TIPO_SET IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',40),
  ('declaracion -> TIPO_MAP IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',41),
  ('declaracion -> TIPO_SYMBOL IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',42),
  ('declaracion -> TIPO_OBJECT IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',43),
  ('declaracion -> TIPO_FUTURE IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',44),
  ('declaracion -> TIPO_STREAM IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',45),
  ('declaracion -> TIPO_ITERABLE IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',46),
  ('declaracion -> TIPO_NEVER IDENTIFICADOR PUNTO_COMA','declaracion',3,'p_declaracion','analisis_sintactico.py',47),
  ('asignacion -> TIPO_INT IDENTIFICADOR SIGNO_IGUAL expresion_mat_int PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',52),
  ('asignacion -> TIPO_DOUBLE IDENTIFICADOR SIGNO_IGUAL expresion_mat_double PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',53),
  ('asignacion -> TIPO_BOOL IDENTIFICADOR SIGNO_IGUAL expresion_logica PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',54),
  ('asignacion -> TIPO_STRING IDENTIFICADOR SIGNO_IGUAL DATO_CADENA_TEXTO PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',55),
  ('asignacion -> VAR IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',56),
  ('asignacion -> DYNAMIC IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',57),
  ('asignacion -> IDENTIFICADOR SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',4,'p_asignacion','analisis_sintactico.py',58),
  ('asignacion -> IDENTIFICADOR SIGNO_MAS SIGNO_IGUAL expresion_mat_double PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',59),
  ('asignacion -> IDENTIFICADOR SIGNO_MENOS SIGNO_IGUAL expresion_mat_double PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',60),
  ('asignacion -> TIPO_MAP IDENTIFICADOR SIGNO_IGUAL bloque_mapa PUNTO_COMA','asignacion',5,'p_asignacion','analisis_sintactico.py',61),
  ('asignacion -> valor_mapa_lista SIGNO_IGUAL valor_general PUNTO_COMA','asignacion',4,'p_asignacion','analisis_sintactico.py',62),
  ('bloque_mapa -> LLAVE_APERTURA pares_llave_valor LLAVE_CLAUSURA','bloque_mapa',3,'p_bloque_mapa','analisis_sintactico.py',66),
  ('bloque_mapa -> LLAVE_APERTURA LLAVE_CLAUSURA','bloque_mapa',2,'p_bloque_mapa','analisis_sintactico.py',67),
  ('bloque_mapa -> NEW TIPO_MAP PARENTESIS_APERTURA PARENTESIS_CLAUSURA','bloque_mapa',4,'p_bloque_mapa','analisis_sintactico.py',68),
  ('pares_llave_valor -> par_llave_valor COMA pares_llave_valor','pares_llave_valor',3,'p_pares_llave_valor','analisis_sintactico.py',71),
  ('pares_llave_valor -> par_llave_valor','pares_llave_valor',1,'p_pares_llave_valor','analisis_sintactico.py',72),
  ('par_llave_valor -> valor_general DOBLE_PUNTO valor_general','par_llave_valor',3,'p_par_llave_valor','analisis_sintactico.py',75),
  ('valor_general -> IDENTIFICADOR','valor_general',1,'p_valor_general','analisis_sintactico.py',78),
  ('valor_general -> expresion_mat_double','valor_general',1,'p_valor_general','analisis_sintactico.py',79),
  ('valor_general -> expresion_logica','valor_general',1,'p_valor_general','analisis_sintactico.py',80),
  ('valor_general -> DATO_CADENA_TEXTO','valor_general',1,'p_valor_general','analisis_sintactico.py',81),
  ('valor_general -> llamadas_func','valor_general',1,'p_valor_general','analisis_sintactico.py',82),
  ('valor_general -> NULL','valor_general',1,'p_valor_general','analisis_sintactico.py',83),
  ('valor_mapa_lista -> IDENTIFICADOR CORCHETE_APERTURA valor_general CORCHETE_CLAUSURA','valor_mapa_lista',4,'p_valor_mapa_lista','analisis_sintactico.py',86),
  ('expresion_mat_int -> expresion_int_no_menos','expresion_mat_int',1,'p_expresion_mat_int','analisis_sintactico.py',90),
  ('expresion_mat_int -> SIGNO_MENOS expresion_int_no_menos','expresion_mat_int',2,'p_expresion_mat_int','analisis_sintactico.py',91),
  ('expresion_int_no_menos -> expresion_int_no_menos SIGNO_MAS expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',94),
  ('expresion_int_no_menos -> expresion_int_no_menos SIGNO_MENOS expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',95),
  ('expresion_int_no_menos -> expresion_int_no_menos SIGNO_MULTIPLICACION expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',96),
  ('expresion_int_no_menos -> expresion_int_no_menos PORCENTAJE expresion_int_no_menos','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',97),
  ('expresion_int_no_menos -> expresion_int_no_menos VIRGULILLA SIGNO_DIVISION expresion_int_no_menos','expresion_int_no_menos',4,'p_expresion_int_no_menos','analisis_sintactico.py',98),
  ('expresion_int_no_menos -> PARENTESIS_APERTURA expresion_int_no_menos PARENTESIS_CLAUSURA','expresion_int_no_menos',3,'p_expresion_int_no_menos','analisis_sintactico.py',99),
  ('expresion_int_no_menos -> DATO_ENTERO','expresion_int_no_menos',1,'p_expresion_int_no_menos','analisis_sintactico.py',100),
  ('expresion_int_no_menos -> IDENTIFICADOR','expresion_int_no_menos',1,'p_expresion_int_no_menos','analisis_sintactico.py',101),
  ('expresion_mat_double -> expresion_double_no_menos','expresion_mat_double',1,'p_expresion_mat_double','analisis_sintactico.py',104),
  ('expresion_mat_double -> SIGNO_MENOS expresion_double_no_menos','expresion_mat_double',2,'p_expresion_mat_double','analisis_sintactico.py',105),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_MAS expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',108),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_MENOS expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',109),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_MULTIPLICACION expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',110),
  ('expresion_double_no_menos -> expresion_double_no_menos PORCENTAJE expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',111),
  ('expresion_double_no_menos -> expresion_double_no_menos SIGNO_DIVISION expresion_double_no_menos','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',112),
  ('expresion_double_no_menos -> PARENTESIS_APERTURA expresion_double_no_menos PARENTESIS_CLAUSURA','expresion_double_no_menos',3,'p_expresion_double_no_menos','analisis_sintactico.py',113),
  ('expresion_double_no_menos -> DATO_DOBLE','expresion_double_no_menos',1,'p_expresion_double_no_menos','analisis_sintactico.py',114),
  ('expresion_double_no_menos -> DATO_ENTERO','expresion_double_no_menos',1,'p_expresion_double_no_menos','analisis_sintactico.py',115),
  ('expresion_double_no_menos -> IDENTIFICADOR','expresion_double_no_menos',1,'p_expresion_double_no_menos','analisis_sintactico.py',116),
  ('expresion_logica -> expresion_logica PLECA PLECA expresion_logica','expresion_logica',4,'p_expresion_logica','analisis_sintactico.py',120),
  ('expresion_logica -> expresion_logica ET ET expresion_logica','expresion_logica',4,'p_expresion_logica','analisis_sintactico.py',121),
  ('expresion_logica -> PARENTESIS_APERTURA expresion_logica PARENTESIS_CLAUSURA','expresion_logica',3,'p_expresion_logica','analisis_sintactico.py',122),
  ('expresion_logica -> SIGNO_ADMIRACION_APERTURA expresion_logica','expresion_logica',2,'p_expresion_logica','analisis_sintactico.py',123),
  ('expresion_logica -> comparacion','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',124),
  ('expresion_logica -> TRUE','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',125),
  ('expresion_logica -> FALSE','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',126),
  ('expresion_logica -> IDENTIFICADOR','expresion_logica',1,'p_expresion_logica','analisis_sintactico.py',127),
  ('comparacion -> expresion_mat_double SIGNO_MENOR_QUE expresion_mat_double','comparacion',3,'p_comparacion','analisis_sintactico.py',130),
  ('comparacion -> expresion_mat_double SIGNO_MAYOR_QUE expresion_mat_double','comparacion',3,'p_comparacion','analisis_sintactico.py',131),
  ('comparacion -> expresion_mat_double SIGNO_MENOR_QUE SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',132),
  ('comparacion -> expresion_mat_double SIGNO_MAYOR_QUE SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',133),
  ('comparacion -> expresion_mat_double SIGNO_IGUAL SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',134),
  ('comparacion -> expresion_mat_double SIGNO_ADMIRACION_APERTURA SIGNO_IGUAL expresion_mat_double','comparacion',4,'p_comparacion','analisis_sintactico.py',135),
]
