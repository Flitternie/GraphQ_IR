from enum import unique
import os
import re
from bart2query.program.executor_rule_new import RuleExecutor
from utils.data import load_vocab
import difflib

class IRCorrector():
    def __init__(self):
        self.rule_executor = RuleExecutor(os.path.join("./dataset_new/", 'kb.json'))
        self.correct_num = 0
        self.preprocess()
    
    def preprocess(self):
        self.unique_entity = set()
        self.unique_attribute = set()
        self.unique_relation = set()
        self.unique_concept = set()
        # self.unique_qualifier = set()

        self.entity_mapping = dict()
        self.entity_attribute_mapping = dict()
        self.entity_relation_mapping = dict()

        for name_id, entity in self.rule_executor.entities.items():
            self.entity_mapping[name_id] = entity["name"]
            self.unique_entity.add(entity["name"])

            self.entity_attribute_mapping[name_id] = set()
            self.entity_relation_mapping[name_id] = set()

            for attribute in entity["attributes"]:
                self.unique_attribute.add(attribute["key"])
                self.entity_attribute_mapping[name_id].add(attribute["key"])    
            for relation in entity["relations"]:
                self.unique_relation.add(relation["predicate"])
                self.entity_relation_mapping[name_id].add(relation["predicate"]) 

        self.concept_mapping = dict()
        self.concept_relation_mapping = dict()

        for name_id, concept in self.rule_executor.concepts.items():
            self.concept_mapping[name_id] = concept["name"]
            self.unique_concept.add(concept["name"])
            
            self.concept_relation_mapping[name_id] = set()
            
            if "relations" in concept.keys():
                for relation in concept["relations"]:
                    self.unique_relation.add(relation["predicate"])
                    self.concept_relation_mapping[name_id].add(relation["predicate"])
    
    def self_correct(self, ir):
        ir = self.correct_entity(ir)
        ir = self.correct_concept(ir)
        ir = self.correct_attribute(ir)
        ir = self.correct_relation(ir)
        return ir
    
    def do_correct(self, ir, to_correct):
        for wrong, correct in to_correct.items():
            ir = ir.replace(wrong, correct)
            self.correct_num += 1
        return ir
    
    def correct_entity(self, ir):
        to_correct = dict()
        entities = re.findall(r'\{([^{}]+)\}', ir.replace("<E>", "{").replace("</E>", "}"))
        for entity in entities:
            entity = entity.strip()
            if entity not in self.unique_entity and entity not in self.unique_concept:
                retrieved_entity = difflib.get_close_matches(entity, self.unique_entity, n=1, cutoff=0.8)
                if bool(retrieved_entity):
                    to_correct[entity] = retrieved_entity[0]
        return self.do_correct(ir, to_correct)
    
    def correct_concept(self, ir):
        to_correct = dict()
        concepts = re.findall(r'\{([^{}]+)\}', ir.replace("<C>", "{").replace("</C>", "}"))
        for concept in concepts:
            concept = concept.strip()
            if concept not in self.unique_concept:
                retrieved_concept = difflib.get_close_matches(concept, self.unique_concept, n=1, cutoff=0.8)
                if bool(retrieved_concept):
                    to_correct[concept] = retrieved_concept[0]
        return self.do_correct(ir, to_correct)
    
    def correct_attribute(self, ir):
        to_correct = dict()
        attributes = re.findall(r'\{([^{}]+)\}', ir.replace("<A>", "{").replace("</A>", "}"))
        for attribute in attributes:
            attribute = attribute.strip()
            if attribute not in self.unique_attribute:
                retrieved_attribute = difflib.get_close_matches(attribute, self.unique_attribute, n=1, cutoff=0.8)
                if bool(retrieved_attribute):
                    to_correct[attribute] = retrieved_attribute[0]
        return self.do_correct(ir, to_correct)
    
    def correct_relation(self, ir):
        to_correct = dict()
        relations = re.findall(r'\{([^{}]+)\}', ir.replace("<R>", "{").replace("</R>", "}"))
        for relation in relations:
            relation = relation.strip()
            if relation not in self.unique_relation:
                retrieved_relation = difflib.get_close_matches(relation, self.unique_relation, n=1, cutoff=0.8)
                if bool(retrieved_relation):
                    to_correct[relation] = retrieved_relation[0]
        return self.do_correct(ir, to_correct)


def main():
    pass

if __name__ == '__main__':
    main()