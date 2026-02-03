grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    elif tk == self.STRINGLIT:
        result = super().emit();
        result.text = result.text[1:-1];
        return result;
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
// ======== Parser ==========

// Program
program: declaration* EOF;
declaration: structDecl | functionDecl;


// Type System 
primitiveType: INT | FLOAT | STRING;

// Struct
structDecl: STRUCT ID LBRACE memberDecl* RBRACE SEMI;
memberDecl: paraType ID SEMI;
paraType: primitiveType | ID; // can be a int, string, float or other struct


// Function
functionDecl: returnType? ID LPAREN paraList? RPAREN blockStmt;
returnType: primitiveType | VOID | ID; // only function can use void
paraList: paraType ID (COMMA paraType ID)*;


// Statements
stmt: varDeclStmt
    | blockStmt
    | assignStmt
    | ifStmt
    | whileStmt
    | forStmt
    | switchStmt
    | breakStmt
    | continueStmt
    | returnStmt
    | exprStmt;


varDeclStmt: varDecl SEMI;
varDecl: (AUTO | primitiveType) ID (ASSIGN expression)?
        | ID ID (ASSIGN expression)?; // Struct declaration


blockStmt: LBRACE stmt* RBRACE;

assignStmt: assignment SEMI;
assignment   : lvalue ASSIGN expression ;
lvalue       : ID (DOT ID)* ;

ifStmt: IF LPAREN expression RPAREN stmt (ELSE stmt)?;

whileStmt: WHILE LPAREN expression RPAREN stmt;

forStmt: FOR LPAREN forInit? SEMI expression? SEMI forUpdate? RPAREN stmt;
forInit: varDecl | assignment;
forUpdate: assignment | incDec;
incDec: (INC | DEC) lvalue | lvalue (INC | DEC);

switchStmt: SWITCH LPAREN expression RPAREN LBRACE caseSwitch* defaultSwitch? caseSwitch* RBRACE;
caseSwitch: CASE expression COLON stmt*;
defaultSwitch: DEFAULT COLON stmt*;

breakStmt: BREAK SEMI;

continueStmt: CONTINUE SEMI;

returnStmt: RETURN expression? SEMI;

exprStmt: expression SEMI;

// Expressions
expression: assignExpr;
assignExpr: lvalue ASSIGN assignExpr | orExpr;
orExpr: orExpr OR andExpr | andExpr;
andExpr: andExpr AND eqExpr | eqExpr;
eqExpr: eqExpr (EQ | NEQ) relationalExpr | relationalExpr;
relationalExpr: relationalExpr (LT | LTE | GT | GTE) addExpr | addExpr;
addExpr: addExpr (PLUS | MINUS) mulExpr | mulExpr;
mulExpr: mulExpr (MUL | DIV | MOD) unaryExpr | unaryExpr;
unaryExpr: (NOT | MINUS | PLUS) unaryExpr | prefixExpr;
prefixExpr: (INC | DEC) prefixExpr | postfixExpr;
postfixExpr: postfixExpr (INC | DEC)
            | postfixExpr argFuncList //function call;
            | primaryExpr;
primaryExpr: primaryExpr DOT ID
            | ID | FLOATLIT | INTLIT | STRINGLIT 
            | LPAREN expression RPAREN
            | structInit;

argFuncList: LPAREN argList? RPAREN;     // can empty (), use for function     
argList: expression (COMMA expression)*;
structInit : LBRACE argList? RBRACE ;


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
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COMMA: ',';
COLON: ':';

// Literal
fragment Intpart: '0' | [1-9][0-9]*;
fragment Snotation: [eE] [+-]? [0-9]+;
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
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | '\\' [btnfr"\\])* '\\' ~[btnfr"\\\r\n];
UNCLOSE_STRING: '"' (~["\\\r\n] | '\\' [btnfr"\\])* '\\'? ('\r'? '\n' | EOF);
ERROR_CHAR: .;