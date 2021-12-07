lexer grammar UnifiedIRLexer;

WS
    : ( '\t' | '\n' | '\r' )+ ->skip
    ;

What
    : 'what is' 
    | 'what is the attribute'
    | 'what is the relation'
    | 'what is the qualifier'
    ;

Select
    : 'which one has the'
    ;
    
Count
    : 'how many'
    ;

Verify
    : 'whether'
    ;

Of
    : 'of'
    ;

From
    : 'from'
    ;

To
    : 'to'
    ;

Among
    : 'among'
    ;

Top
    : 'top'
    ;

Ones
    : 'ones'
    ;

The
    : 'the'
    ;

Whose
    : 'whose'
    ;

That
    : 'that'
    ;

LB
    : '('
    ;

RB
    : ')'
    ;

Forward
    : 'forward'
    ;

Backward
    : 'backward'
    ;

And
    : 'and'
    ;

Or
    : 'or'
    ;

Is
    : 'is' | 'equal to'
    ;

NotIs
    : 'not is' | 'not equal to'
    ;

LargerThan
    : 'larger than' | 'more than'
    ;

SmallerThan
    : 'smaller than' | 'less than'
    ;

AtLeast
    : 'at least'
    ;

AtMost
    : 'at most'
    ;

Largest
    : 'largest'
    ;

Smallest
    : 'smallest'
    ;

Text
    : 'text'
    ;

Quantity
    : 'number'
    ;

Date
    : 'date'
    ;

Year
    : 'year'
    ;   

SPACE
    : ' ' ->skip
    ; 

ES_START
    : '<ES>'
    ;

ES_END
    : '</ES>'
    ;

ENTI_START
    : '<E>' -> mode(VAR)
    ;

ATTR_START
    : '<A>' -> mode(VAR)
    ;

PRED_START
    : '<R>' -> mode(VAR)
    ;

CONC_START
    : '<C>' -> mode(VAR)
    ;

QUAL_START
    : '<Q>' -> mode(VAR)
    ;

VALU_START
    : '<V>' -> mode(VAR)
    ;

INTEGER
    : DIGIT+
    ;

DECIMAL
    : DIGIT+ '.' DIGIT*
    | '.' DIGIT+
    ;

DIGIT
    : DIGIT_BASE
    ;

STRING_LITERAL
    : ( CHARS_BASE | DIGIT | UNICODE )+
    ;

fragment
DIGIT_BASE
    : '0'..'9'
    ;

fragment
CHARS_BASE
    : 'A'..'Z'
    | 'a'..'z'
    | '?' | '!' | '.' | ',' | '/' | ':' | '_' | '-'
    ;

fragment
UNICODE
    : ~( '(' | ')' | '<' | '>' | ' ' )
    ;

mode VAR;

ENTI_END
    : '</E>' -> mode(DEFAULT_MODE)
    ;

ATTR_END
    : '</A>' -> mode(DEFAULT_MODE)
    ;

PRED_END
    : '</R>' -> mode(DEFAULT_MODE)
    ;

CONC_END
    : '</C>' -> mode(DEFAULT_MODE)
    ;

QUAL_END
    : '</Q>' -> mode(DEFAULT_MODE)
    ;

VALU_END
    : '</V>' -> mode(DEFAULT_MODE)
    ;

LITERAL
    : ANY_CHAR+
    ;

fragment
ANY_CHAR
    : ~( '<' | '>' )
    ;