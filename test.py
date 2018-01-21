from parse import *
from matrix import *
from glr import *
from gll import *
from small_tests import *
from time import time
import sys

answers = [[810, 2164, 2499, 2540, 15454, 15156, 4118, 9472, 17634, 66572, 56195], [1, 0, 63, 81, 122, 2871, 10, 37, 1158, 133, 1262]]


graph_names = ['skos.dot', 'generations.dot', 'travel.dot', 'univ-bench.dot', 'atom-primitive.dot', 'biomedical-mesure-primitive.dot', 'foaf.dot', 'people_pets.dot', 'funding.dot', 'wine.dot', 'pizza.dot']
gr_names = ['Q1', 'Q2']
algos = {'matrix' : matrix, 'glr' : glr, 'gll' : gll}
gr_suff = {'matrix' : '_hom.dot', 'glr' : '_auto.dot', 'gll' : '_auto.dot'}
parse_name = {'matrix' : parse_grammar, 'glr' : parse_gram_automata, 'gll' : parse_gram_automata}

def test_standart(algo):
    for ind, x in enumerate(gr_names):
        total_time = 0
        print('Testing', algo.upper(), 'algo with', x, 'grammar\n')
        gram = parse_name[algo](r'data/Grammar/' + x + gr_suff[algo])
        for y in range(11):
            graph = parse_graph(r'data/Graph/' + graph_names[y])
            
            time_c = time()

            res = algos[algo](gram, graph) #Вызов Matrix

            time_c = time() - time_c
            total_time += time_c
            time_c = str(int(time_c * 10000) / 10000)

            s_count = len([x for x in res if x[1] == 'S'])
            sepr = (40 - len(graph_names[y])) * ' '

            if answers[ind][y] == s_count:
                print(graph_names[y] + sepr + time_c + 's' + ' ' * (13 - len(time_c)) + 'OK')
            else:
                print(graph_names[y] + sepr + time_c + 's' + ' ' * (13 - len(time_c)) + 'FAIL')

        total_time = int(total_time * 10000) / 10000
        print("\n" + x + " time - " + str(total_time) + "s")
        print('-' * 56)

def test(param):
    if param == 'all':
        for x in algos:
            small_test(x)
            test_standart(x)
    elif param == 'small':
        for x in algos:
            small_test(x)
    elif param in algos:
        small_test(param)
        test_standart(param)
    else:
        print("Incorrect args. Try 'py test.py [all | small| matrix | glr | gll'")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Incorrect args. Try 'py test.py [all | small| matrix | glr | gll]'")
        exit(1)
    test(sys.argv[1])
        
            
