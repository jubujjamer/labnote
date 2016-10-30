#!/usr/bin/python
# -*- coding: utf-8 -*-
""" File pynotes.py

Last update: 30/10/2016

Usage:

"""
import os
import datetime as dt
import locale
from subprocess import call

HOME_DIR = '/home/juan/lab_notebook/'
DIR_DICT = {'CONT': 'content',
            'INV': 'inventory',
            'DOCS': 'documents',
            'GEN': 'general'}
locale.setlocale(locale.LC_TIME, '')  # Dates in Spanish


def init_filetree():
    for d in DIR_DICT:
        if not os.path.exists(DIR_DICT[d]):
            os.makedirs(DIR_DICT[d])


def _print_header(date):
    return

def create_day_file():
    date = dt.datetime.today()
    date_name = date.strftime('%Y-%m-%d')
    dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], date_name)
    adoc_filename = os.path.join(dir_name, date_name + '.adoc')
    today = dt.datetime.today()
    print adoc_filename

create_day_file()
    #
    # if not os.path.exists(dir_name):
    #     try:
    #         path = os.path.expanduser(dir_name)
    #         os.makedirs(path)
    #         # Printing header
    #         target = open(adoc_filename, 'w')
    #         target.write('= '+date_name+'\n')
    #         target.write('Juan Marco Bujjamer <jubujjamer@df.uba.ar>\n')
    #         target.write(date.strftime("%A %d de %B de %Y\n"))
    #         target.write(':toc:\n')
    #         target.write(':icons: font\n')
    #         target.close()
    #     except:
    #         print "Directory already created."
    #         call(["atom",adoc_filename])
    #         print adoc_filename
    # call(["atom",adoc_filename])

def get_summary(day_file):
    SUMARY_CHAR = 2
    day_sum_list = []
    try:
        adoc_day_file = open(day_file,'r')
    except:
        print "No file to read"
        return []
    flines = adoc_day_file.readlines()
    for line in flines:
        if line[0:SUMARY_CHAR] == '==':
            day_sum_list.append(line[SUMARY_CHAR+1:-1])
    return day_sum_list



def refresh_changes():
    locale.setlocale(locale.LC_TIME,'') # Dates in Spanish
    day_array = []
    index_name = '../index.adoc'
    day_collection = DayCollection()
    # date = datetime.datetime(2016,02, 1)
    # date_name = date.strftime('%Y-%m-%d')
    # dir_name = './'+date_name
    # html_filename = dir_name+'/'+date_name+'.html'

    # Get file numbers from lab_notebook folder
    fnames_nbook = [name for name in os.listdir(CONTENT_FOLDER) if os.path.isdir(CONTENT_FOLDER+name)]

    dates_dir = []
    summaries_arraprint_add_satesy = []
    for f in fnames_nbook:
        try:
            i_date = datetime.datetime.strptime(f, '%Y-%m-%d')
            dates_dir.append(i_date)
            # Update with ascidoctor
            i_day_file = CONTENT_FOLDER+f+"/"+f+".adoc"
            i_summary = get_summary(i_day_file)
            i_day = Day(i_day_file, i_date, i_summary)
            day_collection.add_day(i_day)
            #day_array.append(i_day)
            call(["asciidoctor", i_day_file])
            # print  i_day.get_filename(), i_day.get_sum()
        except ValueError:
            continue
    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    # Comparo con los titulos de index
    index_file = open(index_name, "r+")
    lines = index_file.readlines()
    dates_index = []
    for l in lines:
        if l[0] == '.':
            try:
                dates_index.append(datetime.datetime.strptime(l[1:].lower(), '%A %d de %B de %Y\n'))
            except ValueError:
                break
    index_file.close()

    target = open(index_name, 'a')
    #Search for non indexed dates
    for d in dates_index:
        print day_collection.find(d)
    day_collection.print_add_sates()
    for ud in day_collection.days:
        print ud
        if ud.added_flag == 0:
            i_summary = ud.get_summary()
            print i_summary
            s_summary = ''
            for e in i_summary:
                s_summary = s_summary + str(e) + '. '
            target.write('\n')
            datestr = ud.date.strftime("%A %d de %B de %Y\n")
            target.write('.'+datestr[0].upper()+datestr[1:])
            target.write('* Resumen: ')
            target.write(s_summary+'\n')
            dir_link = ud.date.strftime("%Y-%m-%d")
            target.write('* link:./content/'+dir_link+'/'+dir_link+'.html[]\n')
    target.close()

    # index_file = open(index_name, "r+")
    call(["asciidoctor", "../index.adoc"])
    print "All done"
