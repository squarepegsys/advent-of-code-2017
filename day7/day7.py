import re
from nose.tools import assert_equals

def line_parser(line):

    if not line:
        return None

    tree = {"base":"",
            "weight":0,
            "nodes":[]
    }

    parts = line.split(" ")
    tree["base"]=parts[0]
    tree["weight"]=int(parts[1][1:-1])

    if '->' in parts:
        for p in parts[3:]:
            if p.endswith(","):
                p=p[:-1]

            tree["nodes"].append(p)
                


    return tree



def test_regex():

    full_tree="fwft (72) -> ktlj, cntj, xhth"

    tree = line_parser(full_tree)

    assert_equals(tree['base'], 'fwft')
    assert_equals(tree['weight'],72)
    assert_equals(tree['nodes'], ['ktlj','cntj','xhth'])

    node = "pbga (66)"

    tree = line_parser(node)

    assert_equals(tree['base'], 'pbga')
    assert_equals(tree['weight'],66)
    assert_equals(tree['nodes'], [])
    

    
def test_find_base():

    input="""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

    find_base(input)=="tknk"

def test_best_weight():

    input="""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


    assert_equals(find_best_weight(input),60)

def test_find_node_weight():

    input="""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

    whole_tree = [line_parser(x) for x in input.split("\n") ]

    single_node = [x for x in whole_tree if x["base"]=='pbga'][0]


    assert_equals(find_node_weight(single_node, whole_tree),66)
    assert_equals(single_node["total_weight"],66)

    sub_tree= [x for x in whole_tree if x["base"]=='fwft'][0]
    assert_equals(find_node_weight(sub_tree,whole_tree),243)
    assert_equals(sub_tree["total_weight"],243)

    
    

def find_best_weight(input):

    base = find_base(input)

    whole_tree = [line_parser(x) for x in input.split("\n") if x.strip()]

    base_node = [x for x in whole_tree if x["base"]==base][0]

    find_node_weight(base_node,whole_tree)

    heavy = heaviest(base_node,whole_tree)

    node_weight=0

    parent_node = [x for x in whole_tree if heavy["base"] in x["nodes"]][0]

    sibling_base = [x for x in parent_node["nodes"] if x!=heavy["base"]][0]

    sibling_node =[x for x in whole_tree if x["base"]==sibling_base][0]

    diff = heavy["total_weight"]-sibling_node["total_weight"]

    return heavy["weight"]-diff
    

def heaviest(base_node,whole_tree):

    nodes=[]

    if not base_node['nodes']:
        return base_node
    
    for node_name in base_node["nodes"]:
        node = [x for x in whole_tree if x["base"]==node_name][0]
        nodes.append(node)

    heavy = find_heaviest(nodes)

    if heavy:
        return heaviest(heavy, whole_tree)

    return base_node


    
def find_heaviest(nodes):

    if nodes[0]['total_weight']==nodes[1]['total_weight'] and nodes[1]['total_weight']==nodes[2]['total_weight']:
        return None

    if nodes[0]['total_weight']==nodes[1]['total_weight']:
        return nodes[2]

    if nodes[0]['total_weight']==nodes[2]['total_weight']:
        return nodes[1]

    return nodes[0]

    
def find_node_weight(tree,whole_tree):

    node_weight=tree["weight"]
    for node_name in tree["nodes"]:
        node = [x for x in whole_tree if x["base"]==node_name][0]
        node_weight+=find_node_weight(node,whole_tree)


    tree["total_weight"]=node_weight
    return node_weight

    
def find_base(heap):

    programs = set()
    on_top=set()
    for line in heap.split("\n"):

        inputs = line.split("->")

        base = inputs[0]

        program = base.strip().split(" ")[0]
        programs.add(program)

        
        if len(inputs)>1:
            holding=inputs[1]
            on_top=on_top.union(set(holding.strip().split(", ")))
            

    return [x for x in programs.difference(on_top) if x][0]




if __name__=='__main__':

    with open("input.txt") as input_fp:

        input = input_fp.read()
    
        print(find_base(input))
        print(find_best_weight(input))
      
