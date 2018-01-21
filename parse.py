from collections import defaultdict
import re

class RFA:
    def __init__(self, st_states, fi_states, trans):
        self.st_states = st_states
        self.trans = trans
        self.fi_states = fi_states

def parse_grammar(filename):
    gram = defaultdict(list)
    epsilons = []
    with open(filename) as f:

        lines = f.readlines()
        for line in lines:
            l, r = line.split(' -> ')
            r = r.rstrip('\n')
            gram[l].append(r.split(' '))
            if r == "eps":
                epsilons.append(l)
    return (gram, epsilons)

def parse_graph(in_file):
    with open(in_file,'r') as fi:
        ar = fi.readlines()
        fi.close()
    size = ar[2].count(';')
    gr = defaultdict(lambda: defaultdict(set))
    for x in ar[3:-1]:
        label = x[x.find('"') + 1 : x.rfind('"')]
        l, r = map(int, x[ : x.find('[')].replace('\n','').replace('->','').split())
        gr[l][r].add(label)
    return gr

def parse_gram_automata(in_file):
    with open(in_file, 'r') as fi:
        ar = fi.readlines()
        fi.close()
    if 'digraph' not in ar[0]:
        print('Incorrect grammar')

    trans = defaultdict(set)
    st_states = defaultdict(set)
    fi_states = defaultdict(set)

    for x in ar[3:]:
        x = x.replace(' ','')
        if 'label' not in x:
            continue
        if '->' not in x:
            vert, info = x.split('[')
            l_i = info.find('l=') + 3
            label = info[l_i : info.find('"', l_i)] 

            if ('doublecircle' in info):
                fi_states[label].add(vert)

            if ('green' in info):
                st_states[label].add(vert)
        else:
            vl, other = x.split('->')
            vr, info = other.split('[')
            l_i = info.find('l=') + 3
            label = info[l_i : info.find('"', l_i)]

            trans[vl].add((vr, label))

    return RFA(st_states, fi_states, trans)

def gram2automata(gram):
    key_states = defaultdict(lambda: defaultdict(set))
    transitions = defaultdict(set)
    start_states = defaultdict(set)
    final_states = defaultdict(set)
    max_state = 0
    for nonterm in gram:
        start_state = max_state
        max_state += 1
        start_states[nonterm].add(start_state)
        for right_part in gram[nonterm]:
            cur_state = start_state
            for symbol in right_part:
                    transitions[cur_state].add((max_state + 1, symbol))
                    max_state += 1
                    cur_state = max_state
            final_states[nonterm].add(cur_state)
        max_state += 1
    return RFA(start_states, final_states, transitions)

            

            

        
                
            
            
    
    


