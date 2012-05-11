#!/usr/bin/python
# -*- encoding: utf-8 -*-
from sys import stdin

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, value) :
        node = self.root    
        for ch in value:
            node[ch] = node.get(ch) or {}
            node = node[ch]

        node[0] = value


    def find(self, value, dist):
        for result in self.navigate(self.root, value, '\0', 0, range(len(value)+1), dist):
            yield result
   
    def navigate(self, node, value, ch, i, last, dist):
        row = [0] * (len(value)+1)
        row[0] = i
        
        for j, tch in enumerate(value):
            if tch == ch:
                row[j+1] = last[j]
            else:
                row[j+1] = min(row[j], last[j], last[j+1])+1
        
        if row[len(value)] <= dist:
            if node.has_key(0):
                yield (row[len(value)], node[0])

        if min(row) <= dist:
            for k, v in node.iteritems():
                if k!=0:
                    for word in self.navigate(v, value, k, i+1, row, dist):
                        yield word
        

print 'Carregando dicionário...'
trie = Trie()
for line in open('ptbr.txt','r'):
    trie.add(line[0:-1])
print 'Dicionário carregado.'

max_distance = 2

for test in iter(stdin.readline, ""):
    words = list(trie.find(test[0:-1], max_distance))
    words.sort()
    for word in words[:10]:
        print word

