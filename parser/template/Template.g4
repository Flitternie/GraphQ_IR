grammar Template;

query
    : ( whatEntityQuery 
    | howManyEntityQuery 
    | whatAttributeQuery 
    | whatRelationQuery 
    | selectAmongQuery 
    | selectBetweenQuery 
    | attributeSatisfyQuery 
    | whatAttributeQualifierQuery 
    | whatRelationQualifierQuery ) EOQ EOF
    ;

whatEntityQuery
    : BOQ 'is' entity
    ;

howManyEntityQuery
    : 'How many' entity
    ;

whatAttributeQuery
    : 'For' entity ',' 'what is' prefix attribute
    ;

whatRelationQuery
    : 'What is the relation from' entity 'to' entity
    ;

selectAmongQuery
    : 'Among' entity ',' 'which one has the' op attribute
    ;

selectBetweenQuery
    : 'Which one has the' op attribute ',' entity 'or' entity
    ;

attributeSatisfyQuery
    : 'For' entity ',' 'is' ( attributeVerifyUnderQualifier | attributeVerify )
    ;

attributeVerify
    : attribute op value
    ;

attributeVerifyUnderQualifier
    : attribute op value '(' qualifierKey 'is' qualifierValue ')' 
    ;


whatAttributeQualifierQuery
    : 'For' entity ',' prefix attribute 'is' value ',' BOQ 'is the' qualifierKey 
    ;

whatRelationQualifierQuery
    : entity predicate entity ',' BOQ 'is the' qualifierKey
    ;


entity
    : entitySet | entityFilterByRelation | entityFilterByAttribute | entity_name
    ;

entitySet
    : ( entityFilterByRelation | entityFilterByAttribute | entity_name ) bool ( entityFilterByRelation | entityFilterByAttribute | entity_name )
    ;

entityFilterByRelation
    : 'the' ( concept | 'one' ) 'that' ( relationFilterUnderQualifier | relationFilter )
    ;

relationFilter
    : predicate entity
    ;

relationFilterUnderQualifier
    : predicate entity qualifierFilter
    ;

qualifierFilter
    : '(' qualifierKey 'is' ( op )? qualifierValue ')'
    ;

entityFilterByAttribute
    : 'the' ( concept | 'one' ) 'whose' ( attributeFilterUnderQualifier | attributeFilter )
    ;

attributeFilter
    : attribute 'is' ( op )? value 
    ;

attributeFilterUnderQualifier
    : attribute 'is' ( op )? value qualifierFilter
    ;

concept
    : concept_name
    ;

attribute
    : key_name
    ;

qualifierKey
    : key_name
    ;

value
    : value_name
    ;

qualifierValue
    : value_name
    ;

predicate
    : relation_name
    ;    

entity_name
    : STRING
    ;

concept_name
    : STRING
    ;

key_name
    : STRING
    ;

relation_name
    : STRING
    ;

value_name
    : STRING
    | DECIMAL
    | INTEGER
    ;

prefix
    : 'his/her'
    | 'its'
    ;

op
    : COMPARATIVE 
    | SUPERLATIVE
    | OPERATOR
    ;

COMPARATIVE
    : 'greater'
    | 'less'
    ;

SUPERLATIVE
    : 'largest'
    | 'smallest'
    ;

OPERATOR
    : STRING_OP
    | QUANTITY_OP
    | DATE_OP
    | YEAR_OP
    ;

STRING_OP
    : 'equal to'
    ;

QUANTITY_OP
    : 'less than'
    | 'greater than'
    | 'equal to'
    | 'not equal to'
    ;

DATE_OP
    : 'on'
    ;

YEAR_OP
    : 'before'
    | 'after'
    | 'in'
    | 'not in'
    ;

bool
    : 'or'
    | 'and'
    ;

STRING
    : STRING_LITERAL+?
    ;

STRING_LITERAL
    :  ( PN_CHARS_BASE | DIGIT )+
    ;


INTEGER
    : DIGIT+
    ;

DECIMAL
    : DIGIT+ '.' DIGIT*
    | '.' DIGIT+
    ;

DOUBLE
    : DIGIT+ '.' DIGIT* EXPONENT
    | '.' DIGIT+ EXPONENT
    | DIGIT+ EXPONENT
    ;

INTEGER_POSITIVE
    : '+' INTEGER
    ;

DECIMAL_POSITIVE
    : '+' DECIMAL
    ;

DOUBLE_POSITIVE
    : '+' DOUBLE
    ;

INTEGER_NEGATIVE
    : '-' INTEGER
    ;

DECIMAL_NEGATIVE
    : '-' DECIMAL
    ;

DOUBLE_NEGATIVE
    : '-' DOUBLE
    ;

EXPONENT
    : ('e'|'E') ('+'|'-')? DIGIT+
    ;

fragment
PN_CHARS_BASE
    : 'A'..'Z'
    | 'a'..'z'
    ;

fragment
DIGIT
    : '0'..'9'
    ;

BOQ
    : 'What'
    | 'what'
    | 'Who'
    | 'who'
    ;

EOQ
    : '?'?
    ;

WS
    : (' '
    | '\t'
    | '\n'
    | '\r')+ ->skip
    ;

