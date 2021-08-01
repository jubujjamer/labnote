from setuptools import setup, find_packages

setup(
    name='pynotes',
    version='0.1.0',
    pymodules=['clitools', 'pynotes'],
    install_requires=[
        'Click',
        'python-Levenshtein',
    ],
    entry_points='''
        [console_scripts]
        lnote=pynotes.clitools:lnote
    ''',
    )
