from parse import *
from matrix import *
from glr import *
from time import time
import sys

answers = [[810, 2164, 2499, 2540, 15454, 15156, 4118, 9472, 17634, 66572, 56195], [1, 0, 63, 81, 122, 2871, 10, 37, 1158, 133, 1262]]


graph_names = ['skos.dot', 'generations.dot', 'travel.dot', 'univ-bench.dot', 'atom-primitive.dot', 'biomedical-mesure-primitive.dot', 'foaf.dot', 'people_pets.dot', 'funding.dot', 'wine.dot', 'pizza.dot']

def test(algo):
    total_time = [0, 0]
    gr_names = {'matrix' : ['Q1_hom.dot', 'Q2_hom.dot'], 'glr' : ['Q1.dot', 'Q2.dot']}
    for ind, x in enumerate(gr_names[algo]):
        print('Testing', algo, 'algo with', x, 'grammar\n')
        gram = parse_gram_hom(r'data/Grammar/' + x)
        for y in range(11):
            d = parse_graph(r'data/Graph/' + graph_names[y])
            
            time_c = time()
            if algo == 'matrix':
                res = matrix(d, gram)
            elif algo == 'glr':
                res = glr(d, gram)
            time_c = time() - time_c
            total_time[ind] += time_c
            time_c = str(int(time_c * 10000) / 10000)

            s_count = len([x for x in res if x[1] == 'S'])
            sepr = (40 - len(graph_names[y])) * ' '

            if answers[ind][y] == s_count:
                print(graph_names[y] + sepr + time_c + 's' + ' ' * (13 - len(time_c)) + 'OK')
            else:
                print(graph_names[y] + sepr + time_c + 's' + ' ' * (13 - len(time_c)) + 'FAIL')

        total_time[ind] = int(total_time[ind] * 10000) / 10000
        print("\n" + x + " time - " + str(total_time[ind]) + "s")
        print()
    print("\nTotal", algo, "time - " + str(sum(total_time)) + "s")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Incorrect args. Try 'py test.py [all | matrix | glr]'")
        exit(1)
    if sys.argv[1] == 'all':
        test('matrix')
        print('\n')
        test('glr')
    else:
        test(sys.argv[1])
        
            
