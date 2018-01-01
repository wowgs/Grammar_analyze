from collections import defaultdict

class Gr_Hom:
    def __init__(self):
        self.T = defaultdict(list)
        self.rules = defaultdict(list)
def parse_gram_hom(in_file):
    with open(in_file,'r') as fi:
        ar = fi.readlines()
        fi.close()
    grh = Gr_Hom()
    for x in ar:
        x = x.replace('eps','@').replace('->','').replace('\n','').split()
        if len(x) >= 3:
            grh.rules[x[0]].append(x[1:])
        elif '@' not in x:
            grh.T[x[1]].append(x[0])
            grh.rules[x[0]].append([x[1]])
        else:
            grh.rules[x[0]].append([x[1]])

    return grh

def parse_graph(in_file):
    with open(in_file,'r') as fi:
        ar = fi.readlines()
        fi.close()
    size = ar[2].count(';')
    gr = []
    for x in range(size):
        gr.append([])
        for y in range(size):
            gr[x].append([])
    for x in ar[3:-1]:
        label = x[x.find('"') + 1 : x.rfind('"')]
        l, r = map(int, x[ : x.find('[')].replace('\n','').replace('->','').split())
        gr[l][r].append(label)
    return gr
    
    


