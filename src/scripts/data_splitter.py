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
    with gzip.open(INPUT) as f:
        temp_words = []
        for line in f:
            if random.random() > RAND:
                temp_words
                


def main():
    data_split()

if __name__ == '__main__':
    main()

