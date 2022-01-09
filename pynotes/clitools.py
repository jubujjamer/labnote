#!/home/juan/miniconda3/envs/fastfpm-env/bin/python
# -*- coding: utf-8 -*-
""" File clitools.py

Command line interface tools"""
import click
from pynotes import pynotes
#Check filetree

class Config(object):
    def __init__(self):
        self.verbose = False
        self.graphical = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@pass_config
def lnote(config):
    """ Laboratory notebooks managing system.
    """
    pynotes.init_filetree()
    existing_dates = pynotes.get_existing_dates()

@lnote.command()
@click.option('--date', '-d', default='', nargs=1)
@pass_config
def new(config, date):
    """ Creates a new day in the lab notebook.
    """
    pynotes.create_day_file() 

@lnote.command()
@click.argument('date', nargs=1, required=True)
@pass_config
def info(config, date):
    """ Prints summarized information of a given date.
    """
    pynotes.print_summary(date)
    
@lnote.command()
#@click.option('--date', '-d', default='', nargs=1, required=True)
@click.argument('date', nargs=1, required=True)
@click.option('--mode', default='md', type=click.Choice(['html', 'md', 'pdf']))
@pass_config
def open(config, date, mode):
    """ Open a given date in mode html, adoc or pdf.
    """
    pynotes.open_day_file(date, mode)

@lnote.command()
def tags():
    """ Prints tags in all days.
    """
    pynotes.print_all_hashtags()

@lnote.command()
@click.argument('tag')
def where(tag):
    """ Where to find a given tag.
    """
    pynotes.print_hashtag_occurrence(tag)

@lnote.command()
@click.argument('tag')
def content(tag):
    """ Where to find a given tag.
    """
    pynotes.print_hashtag_content(tag)

@lnote.command()
def index():
    pynotes.open_template_index()

@lnote.command()
def update():
    """ Convert all ascidocs in html files.
    """
    pynotes.update_asciidocs()
