from collections import defaultdict
from time import time
from parse import *
import sys
def matrix(D, G):
    n = len(D)
    mat = [[[] for x in range(n)] for y in range(n)]
    gr_rules = defaultdict(list)
    for A in G.rules:
        for BC in G.rules[A]:
            if len(BC) == 2:
                gr_rules[(BC[0], BC[1])].append(A)
            else:
                gr_rules[(BC[0],)].append(A)
    
    #Ti,j ← Ti,j ∪ {A | (A → x) ∈ P}

    for x in range(n):
        for y in range(n):
            for smt in D[x][y]:
                mat[x][y].extend(G.T[smt])

    time_c = time()
    time_x = 0
    flag = True
    while flag:
        flag = False
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    if (time() - time_c >= 1):
                        time_c = time()
                        print("Parsing" + "." * time_x + " " * 5, end = '\r')
                        time_x = (time_x + 1) % 4
                    for i in mat[x][y]:
                        for j in mat[y][z]:
                            if (i, j) in gr_rules:
                                for elem in gr_rules[(i, j)]:
                                    if elem not in mat[x][z]:
                                        flag = True
                                        mat[x][z].append(elem)
    return [(i, x, j) for i in range(n)
                      for j in range(n)
                      for x in mat[i][j] ]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Wrong arguments")
        exit(1)

    res = matrix(parse_graph(sys.argv[2]), parse_gram_hom(sys.argv[1]))
    
    if len(sys.argv) == 3:
        for x in res:
            print(str(x))

    else:
        with open(sys.argv[3], 'w') as fo:
            for x in res:
                fo.write(str(x))
                fo.write('\n')
            fo.close()

                                    
                    
        
