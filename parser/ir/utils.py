import re 
from ..utils import *

data_type = {  
    "entity": "E", 
    "entitySet": "ES",
    "attribute": "A",
    "concept": "C",
    "value": "V",
    "qualifier": "Q",
    "relation": "R"
}

symbolOP_vocab = {  
    "=": "is", 
    "<": "smaller than", 
    ">": "larger than", 
    "!=": "is not",
    "<=": "at most",
    ">=": "at least",
    "max": "most",
    "min": "least" 
}

def scoping(type, value):
    if type not in data_type.keys():
        raise TypeError("{} is not a valid type.".format(type))
    if value == "":
        return ""
    if type == "entity":
        if value.is_pop:
            return value
        elif not value.is_atom:
            return "<{}> {} </{}>".format(data_type["entitySet"], value, data_type["entitySet"])
    elif type == "value":
        if value.startswith("<{}>".format(data_type["attribute"])) or re.match(r"<V>.*?</V> or <V>.*?</V>", value):
            return value
    return "<{}> {} </{}>".format(data_type[type], value, data_type[type])