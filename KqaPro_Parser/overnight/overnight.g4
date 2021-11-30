grammar overnight;

WS
    : ( '\t'
    | '\n'
    | '\r' )+ ->skip
    ;

root
    : LB 'call' LIST_VALUE expr RB
    ;

expr
    : function
    ;


function
    : getProperty
    | filter
    | superlative
    | countSuperlative
    | countComparative
    | aggregate
    | concat
    | reverse
    | arithOP
    | sortAndToString
    | ensureNumericProperty
    | ensureNumericEntity
    ;


getProperty
    : LB 'call' GET_PROPERTY expr expr RB
    ;

LIST_VALUE
    : 'SW.listValue'
    ;

GET_PROPERTY
    : 'SW.getProperty'
    ;

LB
    : '('
    ;

RB
    : ')'
    ;