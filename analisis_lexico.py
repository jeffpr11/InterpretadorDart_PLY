import ply.lex as lex

tokens = ["IDENTIFICADOR"]

# Palabras reservadas suaves y fuertes - Xavier Carlier
reserved = {
    'assert': 'ASSERT',
    'default': 'DEFAULT',
    'finally': 'FINALLY',
    'rethrow': 'RETHROW',
    'try': 'TRY',
    'break': 'BREAK',
    'do': 'DO',
    'for': 'FOR',
    'return': 'RETURN',
    'var': 'VAR',
    'case': 'CASE',
    'else': 'ELSE',
    'if': 'IF',
    'super': 'SUPER',
    'void': 'VOID',
    'catch': 'CATCH',
    'enum': 'ENUM',
    'switch': 'SWITCH',
    'while': 'WHILE',
    'class': 'CLASS',
    'extends': 'EXTENDS',
    'is': 'IS',
    'this': 'THIS',
    'with': 'WITH',
    'const': 'CONST',
    'false': 'FALSE',
    'new': 'NEW',
    'throw': 'THROW',
    'true': 'TRUE',
    'continue': 'CONTINUE',
    'final': 'FINAL',
    'null': 'NULL',
    'async': 'ASYNC',
    'show': 'SHOW',
    'hide': 'HIDE',
    'on': 'ON',
    'abstract': 'ABSTRACT',
    'as': 'AS',
    'export': 'EXPORT',
    'get': 'GET',
    'mixin': 'MIXIN',
    'static': 'STATIC',
    'covariant': 'COVARIANT',
    'external': 'EXTERNAL',
    'implements': 'IMPLEMENTS',
    'operator': 'OPERATOR',
    'typedef': 'TYPEDEF',
    'deferred': 'DEFERRED',
    'factory': 'FACTORY',
    'import': 'IMPORT',
    'part': 'PART',
    'interface': 'INTERFACE',
    'dynamic': 'DYNAMIC',
    'Function': 'FUNCTION',
    'library': 'LIBRARY',
    'set': 'SET',
    'await': 'AWAIT',
    'yield': 'YIELD',
    'int': 'TIPO_INT',
    'double': 'TIPO_DOUBLE',
    'bool': 'TIPO_BOOL',
    'String': 'TIPO_STRING',
    'List': 'TIPO_LIST',
    'Set': 'TIPO_SET',
    'Map': 'TIPO_MAP',
    'Rune': 'TIPO_RUNE',
    'Symbol': 'TIPO_SYMBOL',
    'Object': 'TIPO_OBJECT',
    'Future': 'TIPO_FUTURE',
    'Stream': 'TIPO_STREAM',
    'Iterable': 'TIPO_ITERABLE',
    'Never': 'TIPO_NEVER',
}

t_VIRGULILLA = r'~'
t_ACENTO_GRAVE = r'`'
t_ACENTO_AGUDO = r'´'
t_COMILLA_SIMPLE = r'\''
t_COMILLA_DOBLE = r'\"'
t_SIGNO_ADMIRACION_APERTURA = r'\!'
t_SIGNO_ADMIRACION_CLAUSURA = r'\¡'
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CLAUSURA = r'\)'
t_SIGNO_INTERROGACION_APERTURA = r'\¿'
t_SIGNO_INTERROGACION_CLAUSURA = r'\?'
t_CORCHETE_APERTURA = r'\['
t_CORCHETE_CLAUSURA = r'\]'
t_LLAVE_APERTURA = r'\{'
t_LLAVE_CLAUSURA = r'\}'
t_SIGNO_MENOR_QUE = r'\<'
t_SIGNO_MAYOR_QUE = r'\>'
t_ARROBA = r'@'
t_PORCENTAJE = r'%'
t_NUMERAL = r'\#'
t_ET = r'&'
t_SIGNO_MAS = r'\+'
t_SIGNO_MENOS = r'-'
t_SIGNO_MULTIPLICACION = r'\*'
t_SIGNO_DIVISION = r'/'
t_BARRA_INVERTIDA = r'\\'
t_SIGNO_IGUAL = r'\='
t_PLECA = r'\|'
t_PUNTO = r'.'
t_COMA = r','
t_DOBLE_PUNTO = r':'
t_PUNTO_COMA = r';'

tokens = tokens + list(reserved.values())
tokens += [
    'VIRGULILLA', 'PLECA',
    'ACENTO_GRAVE', 'ACENTO_AGUDO',
    'COMILLA_SIMPLE', 'COMILLA_DOBLE',
    'SIGNO_ADMIRACION_APERTURA', 'SIGNO_ADMIRACION_CLAUSURA',
    'PARENTESIS_APERTURA', 'PARENTESIS_CLAUSURA',
    'SIGNO_INTERROGACION_APERTURA', 'SIGNO_INTERROGACION_CLAUSURA',
    'CORCHETE_APERTURA', 'CORCHETE_CLAUSURA',
    'LLAVE_APERTURA', 'LLAVE_CLAUSURA',
    'SIGNO_MENOR_QUE', 'SIGNO_MAYOR_QUE',
    'ARROBA', 'PORCENTAJE',
    'NUMERAL', 'ET',
    'SIGNO_MAS', 'SIGNO_MENOS',
    'SIGNO_MULTIPLICACION', 'SIGNO_DIVISION',
    'BARRA_INVERTIDA', 'SIGNO_IGUAL',
    'PUNTO', 'DOBLE_PUNTO',
    'COMA', 'PUNTO_COMA'
]


def t_IDENTIFICADOR(token):
    r'[a-zA-Z_$][A-Za-z0-9_$]*'
    token.type = reserved.get(token.value, 'IDENTIFICADOR')
    return token


def t_error(t):
    print("Entrada Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def receiveLex(s):
    lexer.input(s)
    while True:
        token = lexer.token()
        if not token:
            break  # No more input
        print(token)
