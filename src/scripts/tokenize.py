#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import gzip

def tokenize(filename):
    """ ukWaC tokenizer """

    fn = filename.split(.)
    fn = fn[0] + '.tok'
    newfile = gzip.open('tok', 'w')
    with gzip.open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('<text id=') or line == '<s>':
                continue
            elif line == '</s>':
                newfile.write('\n')
            else:
                newfile.write(line + ' ')
        newfile.close()


def main():
    tokenize('ukwac1.f1.gz')

if __name__ == '__main__':
    main()

