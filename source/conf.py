# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Qualcomm QRB ROS'
copyright = '2024, QUALCOMM'
author = 'Qualcomm'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = 'resources/favicon.ico'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "resources/qrb_ros_logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'collapse_navigation': False
}
html_css_files = ['custom.css']
