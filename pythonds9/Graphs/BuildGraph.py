from .Graph import Graph
from .Vertex import Vertex
from ..Queue import Queue
import requests
from io import StringIO
from Visualizer import viz_graph

def build_graph(word_file, count=21):
    d = {}
    g = Graph()
    current = 0

    if isinstance(word_file, str):
        wfile = open(word_file, 'r')
    else:
        wfile = word_file

    for line in wfile:
        current += 1
        if current == count:
            break
        word = line.strip()
        for i, ch in enumerate(word):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_vertex(word1)
                    g.add_vertex(word2)
                    g.add_edge(word1, word2)

    return g

if __name__ == '__main__':
    url = 'http://www.webplaces.com/passwords/lists/4-letter-words-2478.txt'
    def get_words(url):
        req = requests.get(url)
        return StringIO(req.text)
    '''
    for line in get_words(url):
        print(line.strip())
    '''

    word_file = get_words(url)
    word_graph = build_graph(word_file)
    graph = viz_graph(word_graph)
    graph.view()
