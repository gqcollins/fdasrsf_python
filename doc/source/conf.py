# -*- coding: utf-8 -*-
#
# fdasrsf documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 20 21:12:55 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
from glob import glob

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath("../../fdasrsf"))
sys.path.append(os.path.abspath("../../src"))
paths = glob("../../build/lib*/", recursive=True)
for i in paths:
    sys.path.append(os.path.abspath(i))
sys.path.append(os.path.abspath("../.."))


# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "3.0"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

autodoc_mock_imports = [
    "optimum_reparamN2",
    "optimum_reparam_N",
    "optimum_reparam_Ng",
    "IPython",
    "cbayesian",
    "fpls_warp",
    "mlogit_warp",
    "cimage",
    "ocmlogit_warp",
    "oclogit_warp",
    "crbfgs",
]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "fdasrsf"
author = "J. Derek Tucker"
copyright = "2024, J. Derek Tucker"
github_url = "https://github.com/jdtuck/fdasrsf_python"
rtd_version = os.environ.get("READTHEDOCS_VERSION")
rtd_version_type = os.environ.get("READTHEDOCS_VERSION_TYPE")

switcher_version = rtd_version
if switcher_version == "latest":
    switcher_version = "dev"
elif rtd_version_type not in {"branch", "tag"}:
    switcher_version = "2.6.0"


nbsphinx_prolog = """
 .. raw:: html
    <style>
        .nbinput .prompt, .nboutput .prompt { display: none; }
    </style>
 .. image:: ../artwork/logo.png
    :width: 200px
    :align: right
"""

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/2.0", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.14.0", None),
    "python": ("http://docs.python.org/3.12", None),
}

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "2.6"
# The full version, including alpha/beta/rc tags.
release = "2.6.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"
html_logo = "../artwork/icon.png"

html_theme_options = {
    "use_edit_page_button": True,
    "github_url": github_url,
    "switcher": {
        "json_url": (
            "https://fdasrsf-python.readthedocs.io/en/latest/_static/switcher.json"
        ),
        "version_match": switcher_version,
    },
    "show_version_warning_banner": False,
    "navbar_start": ["navbar-logo", "version-switcher"],
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/fdasrsf",
            "icon": "https://avatars.githubusercontent.com/u/2964877",
            "type": "url",
        },
        {
            "name": "Anaconda",
            "url": "https://anaconda.org/conda-forge/fdasrsf",
            "icon": "https://avatars.githubusercontent.com/u/3571983",
            "type": "url",
        },
    ],
    "logo": {
        "image_light": html_logo,
        "image_dark": html_logo,
    },
}

html_context = {
    "github_user": "jdtuck",
    "github_repo": "fdasrsf",
    "github_version": "master",
    "doc_path": "docs",
    "default_mode": "light",
}

rtd_branch = os.environ.get(" READTHEDOCS_GIT_IDENTIFIER", "master")
language = "en"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "fdasrsfdoc"


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "letterpaper",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "fdasrsf.tex", "fdasrsf Documentation", "J. Derek Tucker", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "fdasrsf", "fdasrsf Documentation", ["J. Derek Tucker"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "fdasrsf",
        "fdasrsf Documentation",
        "J. Derek Tucker",
        "fdasrsf",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = "fdasrsf"
epub_author = "J. Derek Tucker"
epub_publisher = "J. Derek Tucker"
epub_copyright = "2024, J. Derek Tucker"
