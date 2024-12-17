# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/masressusage/configuration.html

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Qualcomm QRB ROS'
copyright = f'{datetime.now().year}, QUALCOMM'
author = 'Qualcomm'

# The full version, including alpha/beta/rc tags
release = 'main'  # This will be overridden by sphinx-multiversion

# -- General configuration ---------------------------------------------------

extensions = [
        'sphinx_rtd_theme',
        'sphinx_tabs.tabs',
        'sphinx.ext.autodoc',
        'sphinx.ext.githubpages',
        'sphinx_design',
        'sphinx.ext.napoleon',
        'sphinx_multiversion',
]

templates_path = ['_templates']

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_favicon = 'resources/favicon.ico'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "resources/qrb_ros_logo.png"
html_theme_options = {
            'logo_only': False,
}
html_css_files = ['custom.css']
'''
html_context['current_version'] = 'main'
html_context['version'] = 'main'

html_context['versions'] = list()

versions = [branch.name for branch in repo.branches]
for version in versions:
    html_context['versions'].append(version)
    '''
