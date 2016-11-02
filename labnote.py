#!/usr/bin/python

import sys
import getopt

from pynotes import pynotes


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hnsl:o:',
                                   ['new_day=', 'get_summary='])
    except getopt.GetoptError:
        print 'labnote.py -n'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Showing help.'
            sys.exit()
        elif opt in ('-n', '--new_day'):
            print('Creating new day file.')
            pynotes.create_day_file()
        elif opt in ('-s', '--get_summary'):
            try:
                pynotes.get_summary(arg)
            except:
                print('Invalid option. Hit -h for help.')
        elif opt in ('-l', '--list_days'):
            pynotes.search_day(arg, 3)

if __name__ == "__main__":
    main(sys.argv[1:])

# pynotes.create_day_file()
# # print pynotes.get_summary('2016-02-18')
# pynotes.search_day('Octubre', 7)
