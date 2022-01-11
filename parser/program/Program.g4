grammar Program;

WS
    : ( FUNC_SEP
    | '\t'
    | '\n'
    | '\r' )+ ->skip
    ;

root
    : ( whatEntityQuery 
    | howManyEntityQuery 
    | whatAttributeQuery 
    | whatRelationQuery 
    | attributeSatisfyQuery 
    | whatAttributeQualifierQuery 
    | whatRelationQualifierQuery ) EOF
    ;

whatEntityQuery
    : entitySet queryName
    ;

howManyEntityQuery
    : entitySet count
    ;

whatAttributeQuery
    : entitySet queryAttribute
    ;

whatRelationQuery
    : entitySetGroup queryRelation
    ;

attributeSatisfyQuery
    : entitySet ( queryAttributeUnderCondition | queryAttribute )  verify
    ;

whatAttributeQualifierQuery
    : entitySet queryAttrQualifier
    ;

whatRelationQualifierQuery
    : entitySetGroup queryRelationQualifier
    ;


entitySetGroup
    : entitySet entitySet
    ;

// entitySet
//     : entitySet entitySet setOP # entitySetByOP
//     | entitySet select # entitySetByRank
//     | entitySet ( entityFilterByRelation | entityFilterByAttribute ) # entitySetNested
//     | findAll ( entityFilterByAttribute | entityFilterByConcept ) # entitySetByFilter
//     | entity # entitySetAtom
//     ;

entitySet
    : entitySet entitySet setOP # entitySetByOP
    | entitySet select # entitySetByRank
    | entitySet entityFilterByRelation # entitySetByRelation 
    | entitySet entityFilterByAttribute # entitySetByAttribute
    | entitySet entityFilterByConcept # entitySetByConcept
    | findAll # entitySetPopulation
    | entity # entitySetAtom
    ;

entityFilterByRelation
    : relate filterQualifier? filterConcept?
    ;

entityFilterByAttribute
    : filterAttr filterQualifier? filterConcept?
    ;

entityFilterByConcept
    : filterConcept
    ;

queryName
    : 'What()'
    ;

count  
    : 'Count()'
    ;

findAll
    : 'FindAll()'
    ;

setOP
    : intersect
    | union
    ;

intersect 
    : 'And()' # and
    ;

union
    : 'Or()' # or
    ;

filterAttr
    : filterStr
    | filterNum
    | filterYear
    | filterDate
    ;

filterStr
    : 'FilterStr(' key IN_FUNC_SEP value ')'
    ;

filterNum
    : 'FilterNum(' key IN_FUNC_SEP value IN_FUNC_SEP op ')'
    ;

filterYear
    : 'FilterYear(' key IN_FUNC_SEP value IN_FUNC_SEP op ')'
    ;

filterDate
    : 'FilterDate(' key IN_FUNC_SEP value IN_FUNC_SEP op ')'
    ;

queryRelation
    : 'QueryRelation()' 
    ;

select
    : 'Select(' key IN_FUNC_SEP op IN_FUNC_SEP topk IN_FUNC_SEP start ')'
    ;


queryAttributeUnderCondition
    : 'QueryAttrUnderCondition(' key IN_FUNC_SEP qkey IN_FUNC_SEP qvalue ')'
    ;

queryAttribute
    : 'QueryAttr(' key ')'
    ;

verify
    : verifyStr
    | verifyNum
    | verifyYear
    | verifyDate
    ;

verifyStr
    : 'VerifyStr(' value ')'
    ;

verifyNum
    : 'VerifyNum(' value IN_FUNC_SEP op ')'
    ;

verifyYear
    : 'VerifyYear(' value IN_FUNC_SEP op ')'
    ;

verifyDate
    : 'VerifyDate(' value IN_FUNC_SEP op ')'
    ;

queryAttrQualifier
    : 'QueryAttrQualifier(' key IN_FUNC_SEP value IN_FUNC_SEP qkey ')'
    ;

queryRelationQualifier
    : 'QueryRelationQualifier(' predicate IN_FUNC_SEP qkey ')'
    ;


relate
    : 'Relate(' predicate IN_FUNC_SEP direction ')'
    ;

filterQualifier
    : filterStrQualifier
    | filterNumQualifier
    | filterYearQualifier
    | filterDateQualifier
    ;

filterStrQualifier
    : 'QFilterStr(' qkey IN_FUNC_SEP qvalue ')'
    ;

filterNumQualifier
    : 'QFilterNum(' qkey IN_FUNC_SEP qvalue IN_FUNC_SEP op ')'
    ;

filterYearQualifier
    : 'QFilterYear(' qkey IN_FUNC_SEP qvalue IN_FUNC_SEP op ')'
    ;

filterDateQualifier
    : 'QFilterDate(' qkey IN_FUNC_SEP qvalue IN_FUNC_SEP op ')'
    ;

filterConcept
    : 'FilterConcept(' concept ')'
    ;

entity
    : 'Find(' string ')'
    ;

concept
    : string 
    ;

predicate
    : string 
    ;

key
    : string 
    ;

value
    : date
    | year
    | number
    | string
    ;

qkey
    : string 
    ;

qvalue
    : date
    | year
    | number
    | string
    ;

topk
    : string
    ;

start
    : string
    ;

op
    : symbolOP
    | stringOP
    ;

symbolOP
    : '=' | '<' | '>' | '!='
    ;

stringOP
    : 'largest' | 'smallest'
    ;


direction
    : 'forward' 
    | 'backward'
    ;

string
    : ( STRING_LITERAL | '(' string ')' | direction )+
    ;

STRING_LITERAL
    : ( CHARS_BASE | DIGIT | UNICODE )+
    ;

date
    : DIGIT+? '-' DIGIT+? '-' DIGIT+?
    ;

year
    : DIGIT DIGIT DIGIT DIGIT
    ;

number
    : INTEGER
    | DECIMAL
    | DOUBLE
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

EXPONENT
    : ('e'|'E') ('+'|'-')? DIGIT+
    ;

DIGIT
    : DIGIT_BASE
    ;

fragment
DIGIT_BASE
    : '0'..'9'
    ;

fragment
CHARS_BASE
    : 'A'..'Z'
    | 'a'..'z'
    | '?' | '!' | '.' | ',' | '/' | ':' | '_' | '-' | ' '
    ;

fragment
UNICODE
    : ~( '(' | ')' | '<' | '>' )
    ;

FUNC_SEP
    : '<b>'
    ;

IN_FUNC_SEP
    : '<c>'
    ;