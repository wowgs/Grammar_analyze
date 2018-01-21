from collections import defaultdict
from time import time
from parse import *
import sys
def matrix(H, D):

    G, epsilons = H[0], H[1]
    mat = defaultdict(lambda: defaultdict(set))

    gr_terms = set()
    gr_rules = defaultdict(set)
    for A in G:
        for BC in G[A]:
            if len(BC) == 2:
                gr_rules[(BC[0], BC[1])].add(A)
            else:
                gr_rules[(BC[0],)].add(A)
                gr_terms.add(BC[0])

    for i in D:
        mat[i][i].update(epsilons)

    #Ti,j ← Ti,j ∪ {A | (A → x) ∈ P}
    for fr in D:
        for to in D[fr]:
            for smt in D[fr][to]:
                mat[fr][to].update(gr_rules[(smt,)])

    time_c = time()
    time_x = 0
    flag = True
    while flag:
        flag = False
        for x in list(mat):
            for y in list(mat[x]):
                for z in list(mat[y]):
                    if (time() - time_c >= 1):
                        time_c = time()
                        print("Parsing" + "." * time_x + " " * 5, end = '\r')
                        time_x = (time_x + 1) % 4
                    for i in list(mat[x][y]):
                        for j in list(mat[y][z]):
                            if (i, j) in gr_rules:
                                for elem in gr_rules[(i, j)]:
                                    if elem not in mat[x][z]:
                                        flag = True
                                        mat[x][z].add(elem)

    return [(i, x, j) for i in mat for j in mat[i] for x in mat[i][j]]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python matrix.py data/Grammar/Q1_hom.dot data/Graph/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str, matrix(parse_grammar(sys.argv[1]), parse_graph(sys.argv[2]))))
    
    if len(sys.argv) == 3:
        print(res)
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()

                                    
                    
        
