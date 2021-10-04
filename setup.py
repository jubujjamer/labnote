from setuptools import setup, find_packages

setup(
    name='pynotes',
    version='0.1.0',
    pymodules=['clitools', 'pynotes'],
    install_requires=[
        'Click',
        'python-Levenshtein',
        'fuzzywuzzy',
        'flask'
    ],
    entry_points='''
        [console_scripts]
        pynotes = pynotes.clitools:lnote
    ''',
    )
