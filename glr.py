from parse import *
from itertools import product
import sys


def bup(rfa, graph, pos_ks, pos_g, nonterm, fi_state_rev):
    
    flag = False
    pairs_set = {(pos_ks, pos_g)}
    used = set()
    
    while pairs_set:
        rfa_pos, gr_pos = pairs_set.pop()
        used.add((rfa_pos, gr_pos))
        
        if rfa_pos in fi_state_rev and nonterm in fi_state_rev[rfa_pos]:
            item = graph[pos_g][gr_pos]
            l = len(item)
            item.update(fi_state_rev[rfa_pos])
            if l < len(item):
                flag = True

        for rfa_to, rfa_label in rfa.trans[rfa_pos]:
            for gr_to in graph[gr_pos]:
                for gr_label in graph[gr_pos][gr_to]:
                    if rfa_label == gr_label:
                        if (rfa_to, gr_to) not in used:
                            pairs_set.add((rfa_to, gr_to))

    return flag


def glr(rfa, graph):
    ans = set()

    graph_states = set()
    for fr in graph:
        graph_states.update(set(graph[fr]))
        graph_states.add(fr)

    fi_state_rev = defaultdict(set)

    for x in rfa.fi_states:
        for y in rfa.fi_states[x]:
            fi_state_rev[y].add(x)

    flag = True
    while flag:
        flag = False
        for gr_pos in graph_states:
            for nonterm in rfa.st_states:
                for rfa_pos in rfa.st_states[nonterm]:
                    flag |= bup(rfa, graph, rfa_pos, gr_pos, nonterm, fi_state_rev)

    for fr in graph:
        for to in graph[fr]:
                for token in graph[fr][to]:
                    if any(ch.isupper() for ch in token):
                        ans.add((fr, token, to))

    return list(ans)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python glr.py data/Grammar/Q1_auto.dot data/Graph/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str, glr(parse_gram_automata(sys.argv[1]), parse_graph(sys.argv[2]))))

    if len(sys.argv) == 3:
        print(res)
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()



