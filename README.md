# labnote
Lab notebook managing program for Linux based on Markup files


Usage

labnote -option

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
parser.add_argument('--edit', '-e', dest='open_edit', nargs=1,
                    action='store', choices=existing_dates,
                    help='opens a labnote adoc file for edition')
parser.add_argument('--index', '-i', dest='open_index',
                    action='store_true',
                    help='opens the general index')
parser.add_argument('--update', dest='update_asciidocs',
                    action='store_true',
                    help='converts all asciidocs to html')
