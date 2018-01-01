from copy import deepcopy
from time import time
from parse import *
import sys
def rek(mat, gr_rules, fr, cur, prod, len_left, fl):
    for x in gr_rules:
        if prod in gr_rules[x]:
            if x not in mat[fr][cur]:
                mat[fr][cur].append(x)
                fl[0] = True
    if len_left == 0:
        return
    for x in filter(lambda k: bool(mat[cur][k]), range(len(mat[cur]))):
        for y in mat[cur][x]:
            rek(mat, gr_rules, fr, x, prod + [y], len_left - 1, fl)
    return


def glr(D, G):

    n = len(D)
    mat = deepcopy(D)
    gr_rules = deepcopy(G.rules)
    len_path = 0
    for x in gr_rules.values():
        for y in x:
            len_path = max(len_path, len(y))

    time_gc = time()
    time_gx = 0
    flag = [True]
    while flag[0]:
        flag[0] = False
        for x in range(n):
            if (time() - time_gc >= 1):
                time_gc = time()
                print("Parsing" + "." * time_gx + " " * 5, end = '\r')
                time_gx = (time_gx + 1) % 4
            rek(mat, gr_rules, x, x, [], len_path, flag)

    return [(i, label, j) for i in range(n) for j in range(n) for label in mat[i][j] if label in gr_rules.keys()]


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Wrong arguments")
        exit(1)

    res = glr(parse_graph(sys.argv[2]), parse_gram_hom(sys.argv[1]))
    
    if len(sys.argv) == 3:
        for x in res:
            print(str(x))

    else:
        with open(sys.argv[3], 'w') as fo:
            for x in res:
                fo.write(str(x))
                fo.write('\n')
            fo.close()
        
