import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # sesuaikan jika folder 'docs/' ada di /project-root/docs

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
html_theme = 'sphinx_rtd_theme'
project = 'KNN Cultivation Software'
author = 'Oka Robiono'
release = '1.0'
master_doc = 'index'

# Tambahkan pengaturan berikut
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']
