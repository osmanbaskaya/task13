#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import fnmatch
import os
import shutil


def get_files(path, regex):
    return [f for f in os.listdir(path) if fnmatch.fnmatch(f, regex)]

def refresh_temp():
    temp = 'temp'
    if os.path.isdir(temp):
        shutil.rmtree(temp)
    os.mkdir(temp)

def main():
    pass

if __name__ == '__main__':
    main()

