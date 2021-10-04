#!/usr/bin/python

# PYTHON_ARGCOMPLETE_OK
import argparse

from pynotes import pynotes

import datetime as dt

# Check filetree
pynotes.init_filetree()
existing_dates = pynotes.get_existing_dates()
date = dt.datetime.strptime('2020-04-05', "%Y-%m-%d")
# pynotes.get_date_file(date))

parser = argparse.ArgumentParser(description='A laboratory notes management system.')
parser.add_argument('--newday', dest='new_day', action='store_true',
                    help='creates today file in the lab notebook')
parser.add_argument('--summary', '-s', dest='get_summary', nargs=1,
                    action='store',
                    help='prints a summary of the day', metavar='YYYY-MM-DD')
parser.add_argument('--view', '-v', dest='open_day_file', nargs=1,
                    action='store',
                    help='opens a labnote page in browser',
                    metavar='YYYY-MM-DD')
parser.add_argument('--edit', '-e', dest='open_edit', nargs=1,
                    action='store', help='opens a labnote adoc file for edition',
                    metavar='YYYY-MM-DD')
parser.add_argument('--index', '-i', dest='open_template_index',
                    action='store_true',
                    help='starts the general index server')
parser.add_argument('--update', dest='update_asciidocs',
                    action='store_true',
                    help='converts all asciidocs to html')
parser.add_argument('--tags', dest='get_hashtags',
                    action='store_true',
                    help='prints current tags in all documents')
parser.add_argument('--where', '-w', dest='tag_occurrence', nargs=1,
                    action='store', help='prints dates containing the tag',
                    metavar='YYYY-MM-DD')

#   lnote new 		Starts a new writing day.
#   lnote info		Prints general info of the labnote manager.
#   lnote open <date> --edit
#   lnote tags --where <tag>
#   lnote index
#   lnote update
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
# elif args.open_index:
#     pynotes.open_index()
elif args.open_template_index:
    pynotes.open_template_index()
elif args.update_asciidocs:
    pynotes.convert_all_asciidocs()
elif args.get_hashtags:
    pynotes.print_all_hashtags()
elif args.tag_occurrence:
    pynotes.print_hashtag_occurrence(args.tag_occurrence[0])
