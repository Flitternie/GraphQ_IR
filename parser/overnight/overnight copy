grammar overnight;

root
    : LB listValue cp RB
    | LB listValue np RB
    ;

np
    : LB aggregate LB aggregateType RB LB getProperty np relNP RB 
    | LB getProperty LB cp LB domain relNP RB RB relNP RB 
    | LB getProperty np relNP RB
    | LB concat np np RB
    | LB size np RB
    | entityNP
    | constraintNP
    | eventNP
    | valueNP
    | cp
    ;

entityNP
    : LB? entityString RB?
    ;

eventNP
    : LB getProperty np reverseRelNP RB
    ;

relNP
    : LB 'string' string RB #stringRelNP
    | LB ensureNumericProperty relNP RB #numberRelNP
    ;

reverseRelNP
    : LB reverse relNP RB
    ;

constraintNP
    : LB getProperty LB singleton entityType RB LB 'string' '!' 'type' RB RB #typeConstraintNP
    | LB 'var' string RB #varConstraintNP
    | filterCP #filterConstraintNP
    | eventNP #eventConstraintNP
    ;

entityType
    : LB? typeString RB?
    ;

vp
    : LB 'string' string RB
    ;

vpnp
    : LB reverse vpnp RB
    | LB 'string' string RB
    ;

valueNP
    : LB ensureNumericEntity np RB
    | numberNP
    | dateNP
    | timeNP
    ;

numberNP
    : LB 'number' quantity ( typeString | string )? RB
    ;

dateNP
    : LB 'date' date RB
    ;

timeNP
    : LB 'time' time RB
    ;

cp
    : LB variable cp RB
    | filterCP
    | superlativeCP
    | comparativeCP
    ;

variable
    : 'lambda' string
    ;

filterCP
    : LB filterFunc constraintNP vp RB
    | LB filterFunc constraintNP relNP op valueNP RB
    | LB filterFunc constraintNP vpnp op np RB
    | LB filterFunc constraintNP reverseRelNP op np RB
    ;

superlativeCP
    : LB superlative constraintNP op relNP RB
    | LB countSuperlative constraintNP op relNP RB
    | LB countSuperlative constraintNP op vpnp np RB
    | LB countSuperlative constraintNP op reverseRelNP np RB
    ;

comparativeCP
    : LB countComparative constraintNP relNP op numberNP RB
    | LB countComparative constraintNP vpnp op numberNP np RB
    | LB countComparative constraintNP reverseRelNP op numberNP np RB
    ;

op
    : LB 'string' '=' RB    #equal
    | LB 'string' '!' '=' RB   #notEqual
    | LB 'string' '<' RB    #lessThan
    | LB 'string' '>' RB    #greaterThan
    | LB 'string' '<' '=' RB   #lessThanOrEqual
    | LB 'string' '>' '=' RB   #greaterThanOrEqual
    | LB 'string' 'min' RB  #min
    | LB 'string' 'max' RB  #max
    ; 

aggregateType
    : 'string' 'sum' #sum
    | 'string' 'avg' #avg
    ;

PREFIX
    : 'call edu.stanford.nlp.sempre.overnight.SimpleWorld.'
    | 'call SW.'
    | 'call .'
    ;

listValue
    : PREFIX 'listValue'
    ;

size
    : PREFIX 'size'
    ;

domain
    : PREFIX 'domain'
    ;

singleton
    : PREFIX 'singleton'
    ;

filterFunc
    : PREFIX 'filter'
    ;

getProperty
    : PREFIX 'getProperty'
    ;

superlative
    : PREFIX 'superlative'
    ;

countSuperlative
    : PREFIX 'countSuperlative'
    ;

countComparative
    : PREFIX 'countComparative'
    ;

aggregate
    : PREFIX 'aggregate'
    ;

concat
    : PREFIX 'concat'
    ;

reverse
    : PREFIX 'reverse'
    ;

ensureNumericProperty
    : PREFIX 'ensureNumericProperty'
    ;

ensureNumericEntity
    : PREFIX 'ensureNumericEntity'
    ;

LB
    : '(' 
    ;

RB
    : ')' 
    ;

string
    : ( STRING_LITERAL | INTEGER | 'date' | 'size' )+
    ;

typeString
    : 'en.' string
    ;

entityString
    : 'en.' string '.' string
    ;

date
    : INTEGER '-'? INTEGER '-'? INTEGER
    ;

time
    : INTEGER INTEGER
    ;

quantity
    : INTEGER
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

WS
    : ( '\t'
    | '\n'
    | '\r' 
    | ' ' )+ ->skip
    ;