#!/usr/bin/python
# -*- coding: utf-8 -*-
""" File pynotes.py

Last update: 31/12/2016
Library for laboratory notebook system management.

Usage:

"""
from __future__ import print_function
import os
import datetime as dt
import locale
from subprocess import call
import calendar
import json
import re

from unicodedata import normalize
from fuzzywuzzy import fuzz, process
from .web import index_server

DAY_DOT_MARK = '.'
HOME_DIR = '~/lab_notebook/'
USER = 'Juan Marco Bujjamer'
EMAIL = 'jubujjamer@df.uba.ar'
JSUM = './pynotes/web/static/summary.json'
DIR_DICT = {'CONT': 'content',
            'INV': 'inventario',
            'DOCS': 'documents',
            'GEN': 'general'}
locale.setlocale(locale.LC_TIME, '')  # Dates in Spanish


def _get_date_path(date):
    str_date = date.strftime('%Y-%m-%d')
    dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], str_date)
    return os.path.expanduser(dir_name)

def get_inventory_path():
    dir_name = os.path.join(HOME_DIR + DIR_DICT['INV'], 'inventario.ods')
    return os.path.expanduser(dir_name)

def get_date_file(date, type='adoc'):
    str_date = date.strftime('%Y-%m-%d')
    dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], str_date)
    path = os.path.join(dir_name, str_date + '.adoc')
    if type is 'adoc':
        return os.path.expanduser(path)
    elif type is 'html':
        call(['asciidoctor', os.path.expanduser(path)])
        path = os.path.join(dir_name, str_date + '.html')
        return os.path.expanduser(path)


def reset_index():
    index_name = os.path.expanduser(os.path.join(HOME_DIR, 'index.adoc'))
    with open(index_name, 'w') as ifile:
        ifile.write('= Indice del cuaderno de laboratorio\n')
        ifile.write(USER + ' ' + EMAIL + '\n')
        ifile.write('Indice general del cuaderno de laboratorio\n')
        ifile.write(':toc:\n\n')
        ifile.write('== Inventario de óptica y electrónica\n')
        ifile.write('link:./inventario/inventario.ods[Inventario]\n\n')
        ifile.write('== Referencias importantes\n')
        ifile.write('link:./docs/daq.html[Adquisición de datos]\n')


def get_existing_dates():
    dir_name = os.path.join(HOME_DIR, DIR_DICT['CONT'])
    dir_name = os.path.expanduser(dir_name)
    dirs = os.listdir(dir_name)
    return dirs


def open_day_file(date_str, type='adoc'):
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    existing_dates = get_existing_dates()
    if type is 'adoc':
        if date_str not in existing_dates:
            create_day_file(date_str)
        adoc_filename = get_date_file(date, type='adoc')
        call(["atom", adoc_filename])
    elif type is 'html':
        if date_str not in existing_dates:
            print("File never created.")
            return
        html_filename = get_date_file(date, type='html')
        call(['xdg-open', html_filename])


def open_index():
    update_index()
    index_filename = os.path.join(HOME_DIR, 'index.html')
    index_filename = os.path.expanduser(index_filename)
    print(index_filename)
    call(['xdg-open', index_filename])


def init_filetree():
    for d in DIR_DICT:
        new_dir = os.path.join(HOME_DIR, DIR_DICT[d])
        new_dir = os.path.expanduser(new_dir)
        if not os.path.exists(new_dir):
            print(d)
            os.makedirs(new_dir)


def _print_header(target, date):
    target.write('= '+date.strftime('%Y-%m-%d')+'\n')
    target.write(USER + ' ' + EMAIL + '\n')
    target.write(date.strftime("%A %d de %B de %Y\n"))
    target.write(':toc:\n')
    target.write(':icons: font\n')


def create_day_file(date_str=None):
    if date_str is None:
        date = dt.datetime.today()
    else:
        date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    path = _get_date_path(date)
    adoc_filename = get_date_file(date, 'adoc')
    if not os.path.exists(path):
        os.makedirs(path)
        with open(adoc_filename, 'w') as target:
            _print_header(target, date)
    else:
        print('Directory already created.')
    call(["atom", adoc_filename])


def get_summary(date_str):
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    date_name = date.strftime('%Y-%m-%d')
    dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], date_name)
    adoc_filename = os.path.join(dir_name, date_name + '.adoc')
    path = os.path.expanduser(adoc_filename)
    try:
        adoc_day_file = open(path, 'r')
    except:
        print('No file to read in %s' % date_str)
        return ''
    flines = adoc_day_file.readlines()
    day_sum_list = [line[3:] for line in flines if line[0:2] == '==' and line[3] != '=']
    # day_sum_list = [data[:-1] for data in day_sum_list]
    return day_sum_list


def get_future_references(date_str):
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    date_name = date.strftime('%Y-%m-%d')
    dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], date_name)
    adoc_filename = os.path.join(dir_name, date_name + '.adoc')
    path = os.path.expanduser(adoc_filename)
    try:
        adoc_day_file = open(path, 'r')
    except:
        print('No file to read in %s' % date_str)
        return ''
    flines = adoc_day_file.readlines()
    day_ref_list = [line[3:] for line in flines if line[0:3] == '[*]']
    day_ref_list = [normalize('NFKD', data[:-1]).encode('ascii', 'ignore')
                    for data in day_ref_list]
    return day_ref_list


def get_dir_contents(date_str):
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    date_name = date.strftime('%Y-%m-%d')
    dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], date_name)
    path = os.path.expanduser(dir_name)

    list_dir = os.listdir(path)
    list_final = []
    for l in list_dir:
        not_printable = ['adoc' in l, 'images' in l, 'html' in l]
        if not any(not_printable):
            # l = l.decode('ascii', 'ignore')
            list_final.append("%s" % l)
    return list_final


def print_summary(date_str):
    summary = get_summary(date_str)
    for item in summary:
        print('-> %s' % item[0:-1], end='\n')


def search_day(date_str, limit):
    dir_name = os.path.join(HOME_DIR, DIR_DICT['CONT'])
    dir_name = os.path.expanduser(dir_name)
    dirs = os.listdir(dir_name)
    dates_list = sorted([(dt.datetime.strptime(a, '%Y-%m-%d')) for a in dirs],
                        reverse=True)
    dates_syns = [date.strftime('%A %d %B %Y') for date in dates_list]
    dates_found = process.extract(date_str, dates_syns, limit=limit)
    print(dates_found)


def update_index(complete=None):
    """ Updates index with the information on new added days.
    """
    fdates = sorted([dt.datetime.strptime(date, '%Y-%m-%d')
                     for date in get_existing_dates()])
    index_name = os.path.expanduser(os.path.join(HOME_DIR, 'index.adoc'))
    with open(index_name, "r+") as ifile:
        lines = ifile.readlines()
        idates = list()
        for line in lines:
            if line[0] == DAY_DOT_MARK:
                try:
                    idates.append(dt.datetime.strptime(line[1:].lower(),
                                  '%A %d de %B de %Y\n'))
                except ValueError:
                    break
    # Close your eyes, heavy hardcoding ahead
    with open(index_name, 'a') as target:
        # Search for non indexed dates
        for fdate in fdates:
            fdate_str = dt.datetime.strftime(fdate, '%Y-%m-%d')
            datesum = get_summary(fdate_str)
            if(fdate not in idates and datesum != []):
                target.write('\n')
                # Printing formatted date
                fmtdate = dt.datetime.strftime(fdate,
                                               '%A %d de %B de %Y\n')
                target.write('.%s%s' % (fmtdate[0].upper(), fmtdate[1:]))
                # Printing summary
                target.write('Resumen: ')
                for item in datesum:
                    target.write('%s. ' % item[0:-1])
                # target.write('\r\n')
                # Printing link to html
                link_dir = os.path.join(HOME_DIR, DIR_DICT['CONT'],
                                        fdate_str, fdate_str+'.html')
                link_dir = os.path.expanduser(link_dir)
                target.write(' link:%s[Ir]\n' % (link_dir))
    call(['asciidoctor', index_name])


def open_template_index():
    """ Index manging using flask and templates for improved flexibility.

    """
    # First write summaries to a json file to be accesed by the calendar.
    fdates = sorted([dt.datetime.strptime(date, '%Y-%m-%d')
                     for date in get_existing_dates()])
    day_list = list()
    summary_list = list()
    # then run the web service
    for fdate in fdates:
        fdate_str = dt.datetime.strftime(fdate, '%Y-%m-%d')
        day_summary = get_summary(fdate_str)
        for s in day_summary:
            summary_list.append({'start' : fdate_str, 'title': s})
        dir_contents = get_dir_contents(fdate_str)
        hashtag_list = get_hashtag_list(fdate_str)
        future_references = get_future_references(fdate_str)
        day_list.append([fdate, day_summary, dir_contents, hashtag_list, future_references])

        last_year = fdate.year
        last_month = fdate.month
    with open(JSUM, 'w') as outfile:
        json.dump(summary_list, outfile)
    app = index_server.create_server(day_dict=day_list, dt=dt)
    app.run()
    return

def convert_all_asciidocs():
    """ Updates index with the information on new added days.
    """
    fdates = [dt.datetime.strptime(date, '%Y-%m-%d')
                     for date in get_existing_dates()]

    for date in fdates:
        try:
            date_name = date.strftime('%Y-%m-%d')
            dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], date_name)
            adoc_filename = os.path.join(dir_name, date_name + '.adoc')
            path = os.path.expanduser(adoc_filename)
            call(['asciidoctor', path])
        except:
            print("File %s not found." % path)


def get_hashtag_list(date_str):
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    date_name = date.strftime('%Y-%m-%d')
    dir_name = os.path.join(HOME_DIR + DIR_DICT['CONT'], date_name)
    adoc_filename = os.path.join(dir_name, date_name + '.adoc')
    path = os.path.expanduser(adoc_filename)
    try:
        adoc_day_file = open(path, 'r')
    except:
        print('No file to read in %s' % date_str)
        return ''
    flines = adoc_day_file.readlines()
    hashtag_list = []
    for line in flines:
        hashtag_list += [i.group().split('#')[1] for i in re.finditer('(^|\s)#[a-z]+', line)]
    return hashtag_list


def get_all_hashtags():
    complete_hashtags = []
    for fdate_str in get_existing_dates():
        hashtag_list = get_hashtag_list(fdate_str)
        if hashtag_list != []:
            complete_hashtags.append(hashtag_list)
    return complete_hashtags


def find_tag_occurrence(tag=None):
    dates = list()
    for fdate_str in get_existing_dates():
        hashtag_list = get_hashtag_list(fdate_str)
        if tag in hashtag_list:
            dates.append(fdate_str)
    return dates


def print_all_hashtags():
    from collections import Counter
    complete_hashtags = get_all_hashtags()
    cnt = Counter()
    for line in complete_hashtags:
        for tag in line:
            cnt[tag] += 1
    for key, value in cnt.items():
        print('%s: %i' % (key, value))

def print_hashtag_occurrence(tag=None):
    print('Listing occurrence of %s' % tag)
    dates = find_tag_occurrence(tag)
    for date in dates:
        print('%s' % (date))
