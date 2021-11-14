import ply.lex as lex

tokens = ["IDENTIFICADOR"]

#Palabras reservadas suaves y fuertes - Xavier Carlier
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

tokens = tokens + list(reserved.values())


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