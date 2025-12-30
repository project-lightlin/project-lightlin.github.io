# Configuration file for the Sphinx documentation builder.

# -- Project information

project = ''
copyright = '2025-2026, LiGHTLIN'
author = 'LiGHTLIN'

release = ''
version = 'Long-term maintenance'
html_title = "Project LiGHTLIN"

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',  # 添加支持外部链接的扩展
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Logo
html_logo = '_static/lightlin-logo.png'

# Custom CSS and JavaScript
html_static_path = ['_static']  # Ensure static files are copied to output
html_css_files = [
    'custom.css',
]
html_js_files = [
    'custom.js',
]

html_meta = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
