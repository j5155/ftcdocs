# Configuration file for the Sphinx documentation builder.

# -- Project information
import os

project = 'ftcdocs'
copyright = '2022, FIRST'
author = 'FIRST'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'sphinx_panels',
]

autosectionlabel_prefix_document = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Credit: https://github.com/wpilibsuite/frc-docs/blob/main/source/conf.py
# -- Options for latex generation --------------------------------------------

latex_engine = "xelatex"

# Disable xindy support
# See: https://github.com/readthedocs/readthedocs.org/issues/5476
latex_use_xindy = False

latex_elements = {
    "fontpkg": r"""
	\setmainfont{DejaVu Serif}
	\setsansfont{DejaVu Sans}
	\setmonofont{DejaVu Sans Mono}""",
    "preamble": r"""
	\usepackage[titles]{tocloft}
	\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
	\setlength{\cftchapnumwidth}{0.75cm}
	\setlength{\cftsecindent}{\cftchapnumwidth}
	\setlength{\cftsecnumwidth}{1.25cm}
	""",
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
    "printindex": r"\footnotesize\raggedright\printindex",
}

suppress_warnings = ["epub.unknown_project_files"]

sphinx_tabs_valid_builders = ["epub", "linkcheck"]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Specify the master doc file, AKA our homepage
master_doc = "index"

def setup(app):
    app.add_css_file("css/ftc-rtd.css")
    #app.add_css_file("css/ftc-rtl.css")
    app.add_js_file("js/external-links-new-tab.js")


if(os.environ.get("DOCS_BUILD") == "true"):
    html_context = dict()
    html_context['display_lower_left'] = True

    html_context['current_version'] = version
    html_context['version'] = version

    html_context['downloads'] = list()  
    html_context['downloads'].append( ('PDF', 'ftcdocs.pdf') )

    html_context['display_github'] = True
    html_context['github_user'] = 'FIRST-Tech-Challenge'
    html_context['github_repo'] = 'ftcdocs'
    html_context['github_version'] = 'main/docs/source/'