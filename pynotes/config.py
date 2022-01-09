#!/usr/bin/python
# -*- coding: utf-8 -*-
""" File config.py

Last update: 31/12/2016
Library for laboratory notebook system management.

Usage:

"""
from __future__ import print_function
import os
import datetime as dt
from pathlib import Path


DAY_DOT_MARK = '.'
SUBTITLE = '##'
HOME_DIR = '~/lab_notebook/'
USER = 'Juan Marco Bujjamer'
EMAIL = 'jubujjamer@df.uba.ar'
JSUM = './pynotes/web/static/summary.json'
PROJECT_NAME = 'STL'
DIR_DICT = {'CONT': 'content',
            'INV': 'inventario',
            'DOCS': 'documents',
            'GEN': 'general'}
SUFFIX = 'md'

class UserData():
    def __init__(self):
        self.user = USER
        self.email = EMAIL


class DirectoryTree():
    def __init__(self, project_name):
        self.project = project_name

    @property
    def home(self):
        return Path(HOME_DIR).expanduser()

    @property
    def content(self):
        path = self.home/PROJECT_NAME/DIR_DICT['CONT']
        return path.expanduser()

    @property
    def inventory(self):
        path  = self.home/PROJECT_NAME/DIR_DICT['INV']
        return path.expanduser()

    @property
    def documents(self):
        path = self.home/PROJECT_NAME/DIR_DICT['DOCS']
        return path.expanduser()

    @property
    def general(self):
        path =  self.home/PROJECT_NAME/DIR_DICT['GEN']
        return path.expanduser()

    def date_dir(self, date):
        str_date = date.strftime('%Y-%m-%d')
        year = str(date.year)
        return self.content/year/str_date

    def get_dates(self):
        cdir = self.content
        project_dirs = cdir.glob("*/*")
        return  [d.name for d in project_dirs if d.is_dir()]
    
    def __iter__(self):
        dirs = [self.content, self.inventory, 
                self.general, self.documents]
        for path in dirs:
            yield path

    def get_entry(self, date, suffix=SUFFIX):
        str_date = date.strftime('%Y-%m-%d')
        available = ['adoc', 'html', 'md']
        assert suffix in available
        if suffix[0] != '.':
            suffix = '.'+suffix
        dir_name = self.date_dir(date)
        path = dir_name/str_date
        return path.with_suffix(suffix)


