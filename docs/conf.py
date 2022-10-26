import os
import sys
sys.path.insert(0, os.path.abspath('../'))

project = 'Sphinx Docs'
copyright = '2022, Josh Norman'
author = 'Josh Norman'
release = 'v0.6'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = []