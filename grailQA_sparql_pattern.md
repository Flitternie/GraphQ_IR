## Unique Usage of SPARQL in GrailQA

All of the patterns discussed below are verified by regex throughout dev and train set of GrailQA v1.0

### 1.**Prefix**

Three and only three prefixes are used in the sparql query throughout the dev set and training set. They are: [rdf](http://www.w3.org/1999/02/22-rdf-syntax-ns#), [rdfs](http://www.w3.org/2000/01/rdf-schema#), and[' '(freebase)](http://rdf.freebase.com/ns/). 


### 2.**Recursive SELECT-WHERE**

There are either **2 or 3** pairs of SELECT-WHERE appears in the sparql query. There are about 3146/51100 sparql queries have 3 SELECT-WHEREs and the rest have only two.

For those with 2 SELECTs, there are only two cases which can all be turned into normal Sparql query easily:

**1.** \
PREFIX ... \
SELECT (?x0 AS ?value) WHERE { \
SELECT DISTINCT? x0 WHERE { \
}} \
represents regular sparql queries, which can be re-written as: \

SELECT DISTINCT? x0 WHERE { \
... \
} 


**2.** \
PREFIX ... \
SELECT (COUNT(?x0) AS ?value) WHERE { \
SELECT DISTINCT? x0 WHERE { \
... \
}} \
represents count queries, which can be re-written as: \

PREFIX ... \
SELECT (COUNT(DISTINCT ?x0) AS ?count) WHERE { \
... \
}

For those with 3 SELECTs, it can only be the case in which the superlative attribute (MAX | MIN) is queried. For instance: \
Question: which beer style has an srm range with largest low value? \
Sparql: \
PREFIX ... \
SELECT (?x0 AS ?value) WHERE { \
SELECT DISTINCT ?x0  WHERE { \
... \
{ \
SELECT (MAX(?y2) AS ?x2)  WHERE { \
... \
}} \
... \
}} \
This selection query can be re-written as: \
PREFIX ... \
SELECT (?x0 AS ?value) WHERE { \
SELECT DISTINCT ?x0  WHERE { \
... \
... \
}} ORDER BY DESC(?y2) LIMIT 1 \


### 3.**FILTER**

For each query, a filter verifying that all its variables are not equal is added inside the block. For isntance, for a query with variable ?x0, ?x1, ?x2, it has and only has one extra filter *FILTER ( ?x0 != ?x1 && ?x0 != ?x2 && ?x1 != ?x2  )*

For the query with 3 SELECTs, the extra filters are also saperated.


### 4.**ID**

ID is used instead of the name label for entities. For isntance, "{ :m.03b7m0 }" is used to replace the label "central pacific hurricane center"


### 5.**VALUES Keyword**

A VALUES keyword is used to describe the attribute of some entities. For instance, in KQA Pro, \
<C> town </C> whose <A> TOID </A> is text <V> 4000000074573917 </V> in sparql is triple pairs: 

?e <TOID> ?pv . \
?pv <pred:value> "4000000074573917" . 
  
But in GrailQA, it would be: 
  
?e :TOID ?pv . \
VALUES ?pv { :m.0hqs1x_ }("4000000074573917")
