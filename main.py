import os
import sys
from src.conll_u_reader import conllu_to_counter


def main(argv):
    _, infile = argv

    print(conllu_to_counter(infile))


if __name__ == '__main__':
    main(sys.argv)
