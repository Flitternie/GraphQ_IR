class strictDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            raise KeyError("{} is not a legal key of this strictDict".format(repr(key)))
        dict.__setitem__(self, key, value)

class entitySet(str):
    def __new__(cls, value="", is_atom=False, is_pop=False, concept=None):
        return str.__new__(cls, value)
    
    def __init__(self, value="", is_atom=False, is_pop=False, concept=None):
        self.is_atom = is_atom
        self.is_pop = is_pop
        self.concept = concept
    
    def reassign(self, value: str):
        return entitySet(value, is_atom=self.is_atom, is_pop=self.is_pop)