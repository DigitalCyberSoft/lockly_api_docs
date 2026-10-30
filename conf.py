# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Unofficial Lockly API documentation"
copyright = "2022 hacker1024; 2026 contributors (CC BY 4.0 — see CREDITS)"
author = "hacker1024 and contributors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinxcontrib.httpdomain"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.rst", "third_party"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Unofficial Lockly API documentation"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Theme configuration -----------------------------------------------------
html_context = {
    "display_github": True,
    "github_user": "DigitalCyberSoft",
    "github_repo": "lockly_api_docs",
    "github_version": "master/",
}
