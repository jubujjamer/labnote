#!/usr/bin/python
# PYTHON_ARGCOMPLETE_OK
import argcomplete
import argparse

from pynotes import pynotes

existing_dates = pynotes.get_existing_dates()

parser = argparse.ArgumentParser(description='A labnote management system.')
parser.add_argument('--new_day', dest='new_day', action='store_true',
                    help='creates today file in the lab notebook')
parser.add_argument('--get_summary', '-s', dest='get_summary', nargs=1,
                    action='store', choices=existing_dates,
                    help='prints a summary of the day', metavar='Y-M-D')
parser.add_argument('--view', '-v', dest='open_day_file', nargs=1,
                    action='store', choices=existing_dates,
                    help='opens a labnote page in browser',
                    metavar='Y-M-D')
parser.add_argument('--edit', dest='open_edit',
                    action='store_true',
                    help='opens a labnote adoc file for edition')
#
argcomplete.autocomplete(parser)
args = parser.parse_args()
if args.new_day:
    pynotes.create_day_file()
elif args.get_summary:
    pynotes.print_summary(args.get_summary[0])
elif args.open_day_file:
    if not args.open_edit:
        pynotes.open_day_file(args.open_day_file[0], 'html')
    else:
        pynotes.open_day_file(args.open_day_file[0], 'adoc')

# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv, 'hnsl:o:',
#                                    ['new_day=', 'get_summary='])
#     except getopt.GetoptError:
#         print 'labnote.py -n'
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print 'Showing help.'
#             sys.exit()
#         elif opt in ('-n', '--new_day'):
#             print('Creating new day file.')
#             pynotes.create_day_file()
#         elif opt in ('-s', '--get_summary'):
#             try:
#                 pynotes.get_summary(arg)
#             except:
#                 print('Invalid option. Hit -h for help.')
#         elif opt in ('-l', '--list_days'):
#             pynotes.search_day(arg, 3)
#
# if __name__ == "__main__":
#     main(sys.argv[1:])
#
# # pynotes.create_day_file()
# # # print pynotes.get_summary('2016-02-18')
# # pynotes.search_day('Octubre', 7)
