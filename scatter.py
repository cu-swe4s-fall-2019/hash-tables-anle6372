"""Scatter plotting functionality for hashing visualization

Parameters
----------
--output_file_name : name of the output file generated from data visualization

Returns
-------
file : returns a file with as scatter plot of the data piped to stdin
"""
import sys
import matplotlib
import matplotlib.pyplot as plt
import argparse
matplotlib.use('Agg')


def main():

    parser = argparse.ArgumentParser(description='Create scatter plots'
                                                 ' with data from stdin.')

    parser.add_argument('--output_file_name', type=str,
                        help='Name of the output file', required=True)

    parser.add_argument('--xlabel', type=str,
                        help='the label for the x axis', required=True)

    parser.add_argument('--ylabel', type=str,
                        help='the label for the y axis', required=True)

    args = parser.parse_args()

    X = []
    Y = []
    i = 0
    for l in sys.stdin:
        A = l.rstrip().split()
        if len(A) == 2:
            X.append(float(A[0]))
            Y.append(float(A[1]))
        elif len(A) == 1:
            X.append(float(i))
            Y.append(float(A[0]))
            i += 1

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    plt.savefig(args.output_file_name, bbox_inches='tight')


if __name__ == '__main__':
    main()
