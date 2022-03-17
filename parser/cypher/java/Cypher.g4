grammar Cypher;

root
    : query+ Return var
    ;

query
    : Match triple ( Where constraint )? 
    ;

triple
    : node '-' relationship '->' node #forwardTriple
    | node '<-' relationship '-' node #backwardTriple
    | node #nodeTriple
    ;

node
    : '(' ( var ':' )? string ')'
    ;

relationship
    : '[' ':' string ']'
    ;

constraint
    : attribute '=' SEP string SEP
    | attribute '=' string
    ;

attribute
    : var '.' string
    ;

var
    : string
    ;

Match
    : 'MATCH' 
    ;

Where
    : 'WHERE' 
    ;

Return 
    : 'RETURN' 'DISTINCT'?
    ;

string
    : ( STRING_LITERAL | INTEGER | '.' | ',' | '-' | '_' | ' ' )+
    ;

INTEGER
    : DIGIT+
    ;

STRING_LITERAL
    : CHAR+
    ;

fragment
DIGIT
    : '0'..'9'
    | [\p{Other_Number}]
    ;

fragment
CHAR
    : '!' | '/' | '\'' | '?' | '%' | '*' | '¡'
    | [\p{Uppercase_Letter}\p{Lowercase_Letter}]
    | [\p{Math_Symbol}\p{Currency_Symbol}] 
    ;

SEP
    : '\'' | '"'
    ;

WS
    : ( '\t'
    | '\n'
    | '\r' 
    | ' ' )+ ->skip
    ;