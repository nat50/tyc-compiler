grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
// ======== Parser ==========
program: EOF;

// ======== Lexer ==========

// Keyword
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Operator
EQ: '==';
NEQ: '!=';
LTE: '<=';
GTE: '>=';
OR: '||';
AND: '&&';
INC: '++';
DEC: '--';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LT: '<';
GT: '>';
NOT: '!';
ASSIGN: '=';
DOT: '.';

// Separator
LBRACK: '[';
RBRACK: ']';
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COMMA: ',';

// Literal
fragment Intpart: '0' | [1-9][0-9]*;
fragment Snotation: [eE] '-'? [0-9]+;
FLOATLIT: (Intpart('.'[0-9]* Snotation?|Snotation))
            |'.'[0-9]+Snotation?;

INTLIT: (Intpart);

STRINGLIT: '"' (~["\\\r\n] | '\\' [btnfr"\\])* '"';

// Identifier
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Comment
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, insert \f

// Error tokens
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | '\\' [btnfr"\\])* '\\' ~[btnfr"\\];
UNCLOSE_STRING: '"' (~["\\\r\n] | '\\' [btnfr"\\])* ('\r'? '\n' | EOF);
ERROR_CHAR: .;