# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Project-LiGHTLIN'
copyright = '2025, Project-LiGHTLIN'
author = 'LiGHTLIN'

release = ''
version = 'Official'
html_title = "Project-LiGHTLIN"
# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'pydata_sphinx_theme'

# 添加缓存控制meta标签
html_meta = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
