#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import gzip
import random

INPUT = '../data/tokenized/ukwac.tok.gz'
TOTAL_TOKEN = 1000000
RAND = 0.01


def data_split():
    """ ukWaC data split """
        
    train = gzip.open('train.ukwac.tok.gz', 'w')
    test = gzip.open('test.ukwac.tok.gz', 'w')
    count=0
    with gzip.open(INPUT) as f:
        temp_words = []
        temp_test_words = []
        for line in f:
            if random.random() < 0.01 and count<TOTAL_TOKEN:
                temp_test_words.append(line)
                count += len(line.split())
                if len(temp_test_words) > 1000:
                    test.write(''.join(temp_test_words))
                    temp_test_words = []
            else:
                temp_words.append(line)
                if len(temp_words) > 1000:
                    train.write(''.join(temp_words))
                    temp_words = []
    test.close()
    train.close()






                


def main():
    data_split()

if __name__ == '__main__':
    main()

