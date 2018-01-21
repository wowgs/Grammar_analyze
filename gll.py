from collections import defaultdict
from parse import *
import sys


class GSS_C:
    def __init__(self, node):
        self.nodes = defaultdict(set)
        self.nodes[node] = set()
    def new_node(self, fr, to, label):
        if fr in self.nodes:
            self.nodes[fr].add((to, label))
        else:
            self.nodes[fr] = {(to, label)}


class GLL_C:
    def __init__(self, rfa, graph):
        self.rfa = rfa
        self.graph = graph
        self.popped = set()
        self.used = set()
        self.cur_confs = set()
        self.ans = set()
        self.popped_states = defaultdict(set)

        self.is_nonterm = lambda x: any(ch.isupper() for ch in x)

    def add_new_conf(self, new_conf):
        if new_conf not in self.used:
            self.cur_confs.add(new_conf)


    
    def same_term(self, cur_conf):
        graph_pos, gram_pos, cur_gss = cur_conf

        for rfa_to, rfa_label in self.rfa.trans[gram_pos]:
            for gr_to in self.graph[graph_pos]:
                for gr_label in self.graph[graph_pos][gr_to]:
                    if gr_label == rfa_label:
                        new_conf = (gr_to, rfa_to, cur_gss)
                        self.add_new_conf(new_conf)

    def nonterm(self, cur_conf):
        graph_pos, gram_pos, cur_gss = cur_conf

        for rfa_to, rfa_label in self.rfa.trans[gram_pos]:

            if self.is_nonterm(rfa_label):
                for start_pos in self.rfa.st_states[rfa_label]:
                    tmp_gss = (graph_pos, rfa_label)
                    tmp_conf = (graph_pos, start_pos, tmp_gss)

                    if tmp_gss in self.popped:
                        for g_pos in self.popped_states[tmp_gss]:
                            new_conf = (g_pos, rfa_to, cur_gss)
                            self.add_new_conf(new_conf)

                    self.add_new_conf(tmp_conf)
                    self.gss.new_node(tmp_gss, cur_gss, rfa_to)


    def fi_state(self, cur_conf):
        graph_pos, gram_pos, cur_gss = cur_conf

        if gram_pos in self.rfa.fi_states[cur_gss[1]]:
            trans_set = self.gss.nodes[cur_gss]
            self.popped_states[cur_gss].add(graph_pos)

            for node, label in trans_set:
                for g_pos in self.popped_states[cur_gss]:
                    new_conf = (g_pos, label, node)
                    self.add_new_conf(new_conf)

            self.ans.add((cur_gss[0], cur_gss[1], graph_pos))
            self.popped.add(cur_gss)

    def run(self):

        rfa_st = set()
        for x in self.rfa.st_states:
            for y in self.rfa.st_states[x]:
                rfa_st.add((x, y))

        gr_st = set()
        for x in self.graph:
            gr_st.update(set(self.graph[x]))
            gr_st.add(x)


        for gr_pos in gr_st:
            for nt, st_state in rfa_st:
                self.gss = GSS_C((gr_pos, nt))
                self.cur_confs = {(gr_pos, st_state, (gr_pos, nt))}
                self.used = set()
                self.popped = set()
                self.popped_states = defaultdict(set)

                while self.cur_confs:
                    cur_conf = self.cur_confs.pop()
                    self.used.add(cur_conf)
                    graph_pos, gram_pos, cur_gss = cur_conf

                    self.same_term(cur_conf)
                    self.nonterm(cur_conf)
                    self.fi_state(cur_conf)

        return list(self.ans)



def gll(grammar, graph):
    return GLL_C(grammar, graph).run()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python gll.py data/Grammar/Q1_auto.dot data/Graph/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str, gll(parse_gram_automata(sys.argv[1]), parse_graph(sys.argv[2]))))

    if len(sys.argv) == 3:
        print(res)
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()
