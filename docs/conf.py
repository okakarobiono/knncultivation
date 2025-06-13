import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # sesuaikan jika folder 'docs/' ada di /project-root/docs

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
html_theme = 'sphinx_rtd_theme'
project = 'KNN Cultivation Software'
author = 'Oka Robiono'
release = '1.0'
master_doc = 'index'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
