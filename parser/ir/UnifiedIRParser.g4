parser grammar UnifiedIRParser;

options { tokenVocab = UnifiedIRLexer; }

root
    : ( entityQuery
    | attributeQuery
    | predicateQuery
    | qualifierQuery
    | countQuery
    | verifyQuery 
    | selectQuery
    | valueQuery ) EOF
    ;

entityQuery
    : What entitySet
    ;

attributeQuery
    : What attribute Of entitySet 
    ;

predicateQuery
    : What From entitySet To entitySet
    ;

qualifierQuery
    : What qualifier Of verify
    ;

countQuery
    : Count entitySet
    ;

verifyQuery
    : Verify verify
    ;

selectQuery
    : Select filterByRank Among entitySet
    ;

valueQuery
    : What valueSet
    ;

verify
    : entitySet filterByAttribute filterByQualifier? #verifyByAttribute
    | entitySet filterByPredicate entitySet filterByQualifier? #verifyByPredicate
    ;

// entitySet
//     : ES_START entitySet setOP entitySet ES_END #entitySetGroup
//     | ES_START filterFromAll ES_END #entitySetFromAll
//     | ES_START filterFromEntitySet ES_END #entitySetNested
//     | entity #entitySetAtom
//     ;

// filterFromEntitySet
//     : The concept filterByPredicate entitySet filterByQualifier?
//     | The One filterByPredicate entitySet filterByQualifier? 
//     | concept? entitySet filterByAttribute filterByQualifier?
//     // | entitySet filterByPredicate entitySet
//     ;

// filterFromAll
//     : concept? filterByAttribute filterByQualifier?
//     | concept
//     ;

entitySet
    : ES_START entitySet setOP entitySet ES_END #entitySetGroup
    | ES_START entitySet LB entitySet RB ES_END #entitySetIntersect
    | ES_START filterFromEntitySet ES_END #entitySetFilter
    | entity #entitySetAtom
    | Ones #entitySetPlaceholder
    ;

filterFromEntitySet
    : ( concept entitySet? | concept? entitySet ) filterByAttribute filterByQualifier? #entitySetByAttribute
    | ( concept entitySet? | concept? entitySet ) filterByPredicate entitySet filterByQualifier? #entitySetByPredicate
    | concept entitySet? #entitySetByConcept
    | entitySet filterByRank #entitySetByRank 
    ;

filterByRank
    : ( That Has )? ( Top number )? stringOP attribute 
    ;

filterByAttribute
    : Whose? attribute symbolOP valueSet
    ;

filterByPredicate
    : That? logicGate? predicate direction? To
    | That? logicGate? predicate direction? To symbolOP? valueSet
    | That? logicGate? predicate direction? To stringOP
    ;

filterByQualifier
    : LB qualifier symbolOP valueSet RB
    ;

direction
    : Forward   #forward
    | Backward  #backward
    ;

setOP
    : And #and
    | Or  #or
    ;

logicGate
    : Not #not
    ;

symbolOP
    : Is #equal
    | IsNot #notEqual
    | LargerThan #larger
    | SmallerThan #smaller
    | AtLeast #largerEqual
    | AtMost #smallerEqual
    ;

stringOP
    : Largest #largest
    | Smallest #smallest
    ;

aggregateOP
    : Sum #sum
    | Average #average
    ;

valueSet
    : valueType valueSet Or valueSet #valueByUnion
    | aggregateOP Of valueSet #valueByAggregate
    | attribute Of entitySet #valueByAttribute
    | valueType? value #valueAtom
    ;

valueType
    : Text #text
    | Quantity #quantity
    | Date #date
    | Year #year
    | Time #time
    ;

entity
    : ENTI_START string ENTI_END
    ;

attribute
    : ATTR_START string ATTR_END
    ;

concept
    : CONC_START string CONC_END
    ;

predicate
    : PRED_START string PRED_END
    ;

qualifier
    : QUAL_START string QUAL_END
    ;

value
    : VALU_START string VALU_END
    ;

number
    : INTEGER
    ;

string
    : (  ' ' | STRING_LITERAL | LB string RB | LITERAL )+
    ;

