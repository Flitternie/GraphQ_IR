PRED_INSTANCE = 'pred:instance_of'
PRED_NAME = 'pred:name'

PRED_VALUE = 'pred:value'       # link packed value node to its literal value
PRED_UNIT = 'pred:unit'         # link packed value node to its unit
PRED_YEAR = 'pred:year'         # link packed value node to its year value, which is an integer
PRED_DATE = 'pred:date'         # link packed value node to its date value, which is a date

PRED_FACT_H = 'pred:fact_h'     # link qualifier node to its head
PRED_FACT_R = 'pred:fact_r'
PRED_FACT_T = 'pred:fact_t'

def legal(s):
    # convert predicate and attribute keys to legal format
    return s.replace(' ', '_')

def esc_escape(s):
    '''
    Why we need this:
    If there is an escape in Literal, such as '\EUR', the query string will be something like '?pv <pred:value> "\\EUR"'.
    However, in virtuoso engine, \\ is connected with E, and \\E forms a bad escape sequence.
    So we must repeat \\, and virtuoso will consider "\\\\EUR" as "\EUR".

    Note this must be applied before esc_quot, as esc_quot will introduce extra escapes.
    '''
    return s.replace('\\', '\\\\')

def esc_quot(s):
    '''
    Why we need this:
    We use "<value>" to represent a literal value in the sparql query.
    If the <value> has a double quotation mark itself, we must escape it to make sure the query is valid for the virtuoso engine.
    '''
    return s.replace('"', '\\"')

def replace_variable(query, variable):
    """
    replace variable in query, and return new query and new variable
    e.g., query='?e <parent> ?e_1', variable='?e', then results should be '?e_1 <parent> ?e_2' and '?e_1'
    """
    if contain_variable(query, variable):
        if '_' in variable:
            prefix, idx = variable.split('_')
            idx = int(idx)
        else:
            prefix = variable
            idx = 0
        new_variable = '{}_{}'.format(prefix, idx+1)
        if contain_variable(query, new_variable):
            query, _ = replace_variable(query, new_variable)
        query = ' '.join([new_variable if w == variable else w for w in query.split()]) + ' ' # DONT forget the space
        return query, new_variable
    else:
        return query, variable


def replace_duplicate_variables(sparql1, sparql2, same_sub=True):
    """
    replace duplicated variables inside two queries, and return new queries
    e.g., query1='?e ***', query2='?e ***', then results should be '?e_1 ***' and '?e_2 ***'
    """
    if same_sub:
        variables1 = get_all_variables(sparql1)
        for v in variables1:
            if v != '?e':
                while v in variables1:
                    sparql2, new_v = replace_variable(sparql2, v)
                    if new_v == v:
                        break
                    else:
                        v = new_v
        return sparql1, sparql2
    else: 
    # use ?e_1 for subject of sparql1, ?e_2 for subject of sparql2
        sparql1, var1 = replace_variable(sparql1, '?e')
        sparql2, var2 = replace_variable(sparql2, '?e')
        sparql2, var2 = replace_variable(sparql2, var2)
        assert var1 == '?e_1' and var2 == '?e_2'
        # first replace ?e_2 in sparql1
        sparql1, _ = replace_variable(sparql1, var2)
        # then replace ramaining variables of sparql1 in sparql2
        variables1 = get_all_variables(sparql1)
        for v in variables1:
            while v in variables1:
                sparql2, new_v = replace_variable(sparql2, v)
                if new_v == v:
                    break
                else:
                    v = new_v
        return sparql1, sparql2


def reverse_dir(direction):
    return 'backward' if direction == 'forward' else 'forward'


def gen_name_query(ent_name):
    return '?e <{}> "{}" . '.format(PRED_NAME, esc_quot(ent_name))
    
def gen_concept_query(concept_name):
    return '?e <{}> ?c . ?c <{}> "{}" . '.format(PRED_INSTANCE, PRED_NAME, esc_quot(concept_name))

def gen_attribute_query(key, value, v_type, v_unit=None, op='=', e='?e', in_qualifier=False):
    k = legal(key)
    if v_type == 'string':
        query = '?e <{}> ?pv . ?pv <{}> "{}" . '.format(
            k, 
            PRED_VALUE, esc_quot(esc_escape(value))
            )
    elif v_type == 'quantity':
        # it is necessary to always cast value as xsd:double, because these is something wrong when comparing different types (e.g., int with double)
        if op == '=':
            query = '?e <{}> ?pv . ?pv <{}> "{}" . ?pv <{}> "{}"^^xsd:double . '.format(
                k,
                PRED_UNIT, esc_quot(v_unit),
                PRED_VALUE, value
                )
        else:
            query = '?e <{}> ?pv . ?pv <{}> "{}" . ?pv <{}> ?v . FILTER ( ?v {} "{}"^^xsd:double ) . '.format(
                k,
                PRED_UNIT, esc_quot(v_unit),
                PRED_VALUE, 
                op, value
                )
    elif v_type == 'year':
        if op == '=':
            query = '?e <{}> ?pv . ?pv <{}> {} . '.format(
                k,
                PRED_YEAR, value
                )
        else:
            query = '?e <{}> ?pv . ?pv <{}> ?v . FILTER ( ?v {} {} ) . '.format(
                k,
                PRED_YEAR,
                op, value
                )
    elif v_type == 'date':
        if op == '=':
            query = '?e <{}> ?pv . ?pv <{}> "{}"^^xsd:date . '.format(
                k,
                PRED_DATE, value
                )
        else:
            query = '?e <{}> ?pv . ?pv <{}> ?v . FILTER ( ?v {} "{}"^^xsd:date ) . '.format(
                k,
                PRED_DATE,
                op, value
                )
    else:
        raise ValueError('Unsupported value type {}'.format(v_type))
    if in_qualifier:
        query = query.replace('?pv', '?qpv').replace('?v', '?qv')
    if e != '?e': # variables in e must not be replaced
        query = query.replace('?e', e)
    return query

def gen_attr_fact_node(k, e='?e'):
    k = legal(k)
    return '[ <{}> {} ; <{}> <{}> ; <{}> ?pv ]'.format(
        PRED_FACT_H, e,
        PRED_FACT_R, k,
        PRED_FACT_T
        )

def contain_variable(query, variable):
    return variable in query.split()

def get_all_variables(query):
    return list(set([w for w in query.split() if w.startswith('?')]))

def get_all_clauses(query):
    return [s.strip() for s in query.split(' . ') if s.strip()]

def ensemble_clauses(clauses):
    return ' . '.join(clauses) + ' . '

def replace_variable(query, variable):
    """
    replace variable in query, and return new query and new variable
    e.g., query='?e <parent> ?e_1', variable='?e', then results should be '?e_1 <parent> ?e_2' and '?e_1'
    """
    if contain_variable(query, variable):
        if '_' in variable:
            prefix, idx = variable.split('_')
            idx = int(idx)
        else:
            prefix = variable
            idx = 0
        new_variable = '{}_{}'.format(prefix, idx+1)
        if contain_variable(query, new_variable):
            query, _ = replace_variable(query, new_variable)
        query = ' '.join([new_variable if w == variable else w for w in query.split()]) + ' ' # DONT forget the space
        return query, new_variable
    else:
        return query, variable

# def gen_relation_query(pred, direction, obj_sparql, obj_variable):
#     assert obj_variable != '?e'
#     pred = legal(pred)
#     if direction == 'forward':
#         query = '?e <{}> {} . '.format(pred, obj_variable)
#     else:
#         query = '{} <{}> ?e . '.format(obj_variable, pred)
#     return query + obj_sparql + ' '

def gen_relation_query(sbj_sparql, sbj_variable, obj_sparql, obj_variable, pred=None, direction='forward'):
    assert sbj_variable != obj_variable
    pred = "<{}>".format(legal(pred)) if pred else "?p"
    if not sbj_sparql or not sbj_variable:
        if direction == 'forward':
            query = '?e {} {} . '.format(pred, obj_variable)
        else:
            query = '{} {} ?e . '.format(obj_variable, pred)
        return query + obj_sparql + ' '
    else:
        sbj_sparql, obj_sparql =  replace_duplicate_variables(sbj_sparql, obj_sparql, same_sub=False)
        if direction == 'forward':
            query = '{} {} {} . '.format(sbj_variable, pred, obj_variable)
        else:
            query = '{} {} {} . '.format(obj_variable, pred, sbj_variable)
        return sbj_sparql + obj_sparql + query

def gen_rel_fact_node(pred, direction, sbj_variable, obj_variable):
    pred = legal(pred)
    if direction == 'forward':
        return '[ <{}> {} ; <{}> <{}> ; <{}> {} ]'.format(
            PRED_FACT_H, sbj_variable,
            PRED_FACT_R, pred,
            PRED_FACT_T, obj_variable
            )
    elif direction == 'backward':
        return '[ <{}> {} ; <{}> <{}> ; <{}> {} ]'.format(
            PRED_FACT_H, obj_variable,
            PRED_FACT_R, pred,
            PRED_FACT_T, sbj_variable
            )
    else:
        raise ValueError('direction should be forward or backward')
    
def append_attribute_value_query(query, k, v_type=None, e='?e', in_qualifier=False):
    """
    Given a query about entity ?e, we query its attribute value of k,
    and denote the value by variable ?v
    """
    k = legal(k)
    if v_type == 'string' or v_type == 'quantity':
        s = '?e <{}> ?pv . ?pv <{}> ?v . '.format(k, PRED_VALUE)
    elif v_type == 'year':
        s = '?e <{}> ?pv . ?pv <{}> ?v . '.format(k, PRED_YEAR)
    elif v_type == 'date':
        s = '?e <{}> ?pv . ?pv <{}> ?v . '.format(k, PRED_DATE)
    elif v_type == None:
        s = '?e <{}> ?pv . '.format(k)
        
    if in_qualifier:
        s = s.replace('?pv', '?qpv').replace('?v', '?qv')
        query, _ = replace_variable(query, '?qpv')
        query, _ = replace_variable(query, '?qv')
    else:
        query, _ = replace_variable(query, '?pv')
        query, _ = replace_variable(query, '?v')

    if e != '?e':
        s = s.replace('?e', e)
    query = query + s
    return query

def same_concept(c_1, c_2):
    """
    return True if c_1 and c_2 are the same concept, False otherwise or if c_1 or c_2 is None
    """
    c_1 = c_1.concept if hasattr(c_1, "concept") else c_1
    c_2 = c_2.concept if hasattr(c_2, "concept") else c_2
    if c_1 and c_2:
        return c_1 == c_2
    else:
        return False

def diff_concept(c_1, c_2):
    """
    return True if c_1 and c_2 are different concepts, False otherwise or if c_1 or c_2 is None
    """
    c_1 = c_1.concept if hasattr(c_1, "concept") else c_1
    c_2 = c_2.concept if hasattr(c_2, "concept") else c_2
    if c_1 and c_2:
        return c_1 != c_2
    else:
        return False

def and_two_descriptions(sparql1, sparql2, same_concept=False):
    if same_concept:
        # remove duplicate clauses about the concept
        clauses2 = get_all_clauses(sparql2)
        clauses2 = [c for c in clauses2 if '?c' not in c]
        sparql2 = ensemble_clauses(clauses2)
    sparql1, sparql2 = replace_duplicate_variables(sparql1, sparql2, same_sub=True)
    sparql = sparql1 + sparql2
    return sparql


def or_two_descriptions(sparql1, sparql2, same_concept=False):
    if same_concept:
        clauses1 = get_all_clauses(sparql1)
        sparql0 = ensemble_clauses([c for c in clauses1 if '?c' in c]) # clauses about the common concept, should be shared
        sparql1 = ensemble_clauses([c for c in clauses1 if '?c' not in c])
        clauses2 = get_all_clauses(sparql2)
        sparql2 = ensemble_clauses([c for c in clauses2 if '?c' not in c])
        sparql = '{} {{ {} }} UNION {{ {} }} '.format(sparql0, sparql1, sparql2)  
    else:
        sparql = '{{ {} }} UNION {{ {} }} '.format(sparql1, sparql2)  
    # Warning: after using UNION, we cannot split and ensemble clauses anymore.
    return sparql


def hop_two_descriptions(condition1, condition2):
    """
    condition1 applies relate to the resultant entity of condition2
    """
    text1, program1, sparql1 = condition1.description()
    text2, program2, sparql2 = condition2.description()
    sparql1, sparql2 = replace_duplicate_variables(sparql1, sparql2)

    sparql2, obj_variable = replace_variable(sparql2, '?e')

    text, program, sparql = condition1.description(obj_desc=(text2, program2, sparql2, obj_variable))
    return text, program, sparql
