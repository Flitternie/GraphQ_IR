grammar Cypher;

root
    : query
    | query 'UNION' query
    ;

query
    : Match triple Where constraints Return var
    ;

triple
    : node '-' relationship '->' node
    ;

node
    : '(' ( var ':' )? string ')'
    ;

relationship
    : '[' var? ( ':' string )? ']'
    ;

constraints
    : ( ( 'AND' | 'OR' )? constraint )+
    ;


constraint
    : property '=' ( SEP string SEP | string )
    | var ':' string
    ;

var
    : string
    ;

property
    : var '.' string
    ;

Match
    : 'MATCH' | 'match'
    ;

Where
    : 'WHERE' | 'where'
    ;

Return 
    : 'RETURN' | 'return'
    ;

string
    : ( STRING_LITERAL | INTEGER )+
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
    ;

fragment
CHAR
    : 'A'..'Z'
    | 'a'..'z'
    | '_' | '-'
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