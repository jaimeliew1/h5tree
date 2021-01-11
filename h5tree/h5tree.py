#!/usr/bin/env ipython
import sys
from pptree import Node, print_tree
import h5py
from pathlib import Path


def traverse(stem, grp):
    for key in list(grp):

        if isinstance(grp[key], h5py.Group):
            thisnode = Node(key, stem)
            traverse(thisnode, grp[key])

        elif isinstance(grp[key], h5py.Dataset):
            thisnode = Node(f"{key} {str(grp[key].shape)}", stem)


def main():
    if len(sys.argv[1:]) == 0:
        args = sys.stdin
    else:
        args = sys.argv[1:]

    for line in args:
        line = line.strip()
        root = Node(line)
        file = h5py.File(line, "r")
        traverse(root, file)
        print_tree(root)


if __name__ == "__main__":
    main()
