from parse import *
from matrix import *
from glr import *
from gll import *
from time import time
import sys

names = ['small'] * 6
names = [x + str(i + 1) for (i, x) in enumerate(names)]
algos = {'matrix' : matrix, 'glr' : glr, 'gll' : gll}
gr_suff = {'matrix' : '_hom.dot', 'glr' : '_auto.dot', 'gll' : '_auto.dot'}
parse_name = {'matrix' : parse_grammar, 'glr' : parse_gram_automata, 'gll' : parse_gram_automata}

def check_answer(ans, res):
    with open(ans, 'r') as fi:
        ar = fi.readlines()
        ar = [x.rstrip() for x in ar]
        if not(set(ar) ^ set(res)):
            return True
        else:
            return False
def small_test(algo):
    print('Testing', algo.upper(), 'algo with SMALL TESTS\n')
    for x in names:
        gram = parse_name[algo](r'data/small_tests/' + x + gr_suff[algo])
        graph = parse_graph(r'data/small_tests/' + x + '_graph.dot')
        
        time_c = time()

        res = algos[algo](gram, graph)#Вызов Алгоритма
        res = [','.join(map(str,x)) for x in res if x[1] == 'S']

        time_c = time() - time_c
        time_c = str(int(time_c * 10000) / 10000)

        sepr = (40 - len(x)) * ' '
        magic = sepr + time_c + 's' + ' ' * (13 - len(time_c))

        if check_answer(r'data/small_tests/' + x + '_ans', res):
            print(x.upper() + magic + 'OK')
        else:
            print(x.upper() + magic + 'FAIL')
    
    print('-' * 56)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Incorrect args. Try 'py test.py [all | small| matrix | glr | gll]'")
        exit(1)
    if sys.argv[1] == 'all':
        for x in algos:
            small_test(x)
    else:
        small_test(sys.argv[1])
        
    
