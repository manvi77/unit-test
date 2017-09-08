import argparse
"""Run from terminal: python my_sum.py -i 1 2"""


class add_integers(object):
    """docstring for ClassName"""

    def add_int(self, args):
        print "From add_int"
        print args
        if args is not int:
            print sum(args)
            return sum(args)
        else:
            return args

if __name__ == '__main__':
    """Name of the scope.
       Execute only if run as a script."""

    parser = argparse.ArgumentParser()
    parser.add_argument('--parse-integers', '-i', nargs='+',
                        type=int, help="Input integers.")
    args = parser.parse_args()
    a = add_integers()
    a.add_int(args.parse_integers)
