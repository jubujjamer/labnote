#!/usr/bin/python
# PYTHON_ARGCOMPLETE_OK
import argcomplete
import argparse

from pynotes import pynotes

# Check filetree
pynotes.init_filetree()
existing_dates = pynotes.get_existing_dates()

parser = argparse.ArgumentParser(description='A labnote management system.')
parser.add_argument('--new_day', dest='new_day', action='store_true',
                    help='creates today file in the lab notebook')
parser.add_argument('--get_summary', '-s', dest='get_summary', nargs=1,
                    action='store', choices=existing_dates,
                    help='prints a summary of the day', metavar='YYYY-MM-DD')
parser.add_argument('--view', '-v', dest='open_day_file', nargs=1,
                    action='store', choices=existing_dates,
                    help='opens a labnote page in browser',
                    metavar='Y-M-D')
parser.add_argument('--edit', '-e', dest='open_edit', nargs=1,
                    action='store', help='opens a labnote adoc file for edition')
parser.add_argument('--index', '-i', dest='open_index',
                    action='store_true',
                    help='opens the general index')
parser.add_argument('--webindex', '-w', dest='open_web_index',
                    action='store_true',
                    help='opens the general index')
parser.add_argument('--update', dest='update_asciidocs',
                    action='store_true',
                    help='converts all asciidocs to html')

argcomplete.autocomplete(parser)
args = parser.parse_args()
if args.new_day:
    pynotes.create_day_file()
elif args.get_summary:
    pynotes.print_summary(args.get_summary[0])
elif args.open_day_file:
    pynotes.open_day_file(args.open_day_file[0], 'html')
elif args.open_edit:
    pynotes.open_day_file(args.open_edit[0], 'adoc')
elif args.open_index:
    pynotes.open_index()
elif args.open_web_index:
    pynotes.open_web_index()
elif args.update_asciidocs:
    pynotes.convert_all_asciidocs()
