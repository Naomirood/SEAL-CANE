import sys
import config
import numpy as np
from tensorflow.contrib import learn
from negativeSample import InitNegTable
import random


class dataSet:
    def __init__(self, text, network):

        self.edges = self.load_edges(network)

        self.text, self.num_vocab, self.num_nodes = self.load_text(text)

        self.negative_table = InitNegTable(self.edges)

    def load_edges(self, network):
        edges = [[int(val.strip()) for val in line.strip().split('\t')[0].strip('()').split(',')] for line in network.split('\n')]
        print("Total load %d edges." % len(edges))
        return edges

    def load_text(self, text):
        vocab = learn.preprocessing.VocabularyProcessor(config.MAX_LEN)
        text = np.array(list(vocab.fit_transform(text)))
        num_vocab = len(vocab.vocabulary_)
        num_nodes = len(text)
        return text, num_vocab, num_nodes

    def negative_sample(self, edges):
        node1, node2 = zip(*edges)
        sample_edges = []
        func = lambda: self.negative_table[random.randint(0, config.neg_table_size - 1)]
        for i in range(len(edges)):
            neg_node = func()
            while node1[i] == neg_node or node2[i] == neg_node:
                neg_node = func()
            sample_edges.append([node1[i], node2[i], neg_node])

        return sample_edges

    def generate_batches(self, mode=None):
        num_batch = len(self.edges) // config.batch_size
        edges = self.edges
        if mode != 'add':
            random.shuffle(edges)
        sample_edges = edges[:num_batch * config.batch_size]
        sample_edges = self.negative_sample(sample_edges)

        batches = []
        for i in range(num_batch):
            batches.append(sample_edges[i * config.batch_size:(i + 1) * config.batch_size])
        return batches
