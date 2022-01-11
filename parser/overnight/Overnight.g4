grammar Overnight;

root
    : LB listValue np RB
    ;

np
    : cp #CPNP
    | entity #entityNP
    | LB getProperty np relNP RB #getPropertyNP
    | value #numericNP
    | LB concat np np RB #concatNP
    | LB aggregate aggregateType np #aggregateNP
    | LB size np RB #sizeNP
    | LB getProperty LB cp LB domain relNP RB RB relNP RB #domainCPNP
    | constraintNP #filterNP
    ;

// type + CP (through typeConstraintNP)
// relNP + CP (through domainCPNP)
// reversePredicate + CP (through eventConstraintNP)

entity
    : LB? 'en.' string '.' string RB?
    ;

concept
    : LB? 'en.' string RB?
    ;

predicate
    : LB 'string' string RB // we merge VP and VPNP here
    ;

relNP
    : LB 'string' string RB #stringRelNP
    | LB ensureNumericProperty relNP RB #numberRelNP
    ;

reversePredicate
    : LB reverse predicate RB 
    | LB reverse relNP RB 
    ;

value
    : LB concat value value RB #concatValueNP
    | LB getProperty np relNP RB #attributeNP
    | LB ensureNumericEntity np RB #numericEntityNP
    | LB 'number' quantity ( 'en.'? string )? RB #numberNP
    | LB date RB #dateNP
    | LB time RB #timeNP
    ;

constraintNP
    : LB getProperty LB singleton concept RB LB 'string' '!' 'type' RB RB #typeConstraintNP
    | filterCP #filterConstraintNP
    | LB getProperty np reversePredicate RB #eventConstraintNP
    | LB 'var' string RB #voidConstraintNP
    ;

cp
    : LB 'lambda' string cp RB #nestedCP
    | filterCP #CP
    | superlativeCP #CP
    | comparativeCP #CP
    ;

filterCP
    : LB filterFunc constraintNP predicate RB #filterByPredicate
    | LB filterFunc constraintNP relNP op value RB #filterByAttribute
    | LB filterFunc constraintNP predicate op np RB #filterByPredicate
    | LB filterFunc constraintNP reversePredicate op np RB #filterByReversePredicate
    ;

superlativeCP
    : LB superlative constraintNP op relNP RB #superlativeByAttribute
    | LB countSuperlative constraintNP op relNP RB #superlativeByPredicate // predicate?
    | LB countSuperlative constraintNP op predicate np RB #superlativeByPredicate
    | LB countSuperlative constraintNP op reversePredicate np RB #superlativeByReversePredicate
    ;

comparativeCP
    : LB countComparative constraintNP relNP op value RB #comparativeByPredicate // predicate?
    | LB countComparative constraintNP predicate op value np RB #comparativeByPredicate
    | LB countComparative constraintNP reversePredicate op value np RB #comparativeByReversePredicate
    ;

op
    : LB 'string' '=' RB        #equal
    | LB 'string' '!' '=' RB    #notEqual
    | LB 'string' '<' RB        #lessThan
    | LB 'string' '>' RB        #greaterThan
    | LB 'string' '<' '=' RB    #lessThanOrEqual
    | LB 'string' '>' '=' RB    #greaterThanOrEqual
    | LB 'string' 'min' RB      #min
    | LB 'string' 'max' RB      #max
    ; 

aggregateType
    : LB 'string' 'sum' RB #sumAggregate
    | LB 'string' 'avg' RB #avgAggregate
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

date
    : DATE
    ;

time
    : TIME
    ;

quantity
    : INTEGER
    ;

DATE
    : 'date ' INTEGER ' ' INTEGER ' ' INTEGER
    ;

TIME
    : 'time ' INTEGER ' ' INTEGER
    ;

INTEGER
    : '-'? DIGIT+
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