import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument('--parse-integers', '-i', nargs='+',
                        type=int, help="Input integers.")
    args = parser.parse_args()
    a = add_integers()
    a.add_int(args.parse_integers)
