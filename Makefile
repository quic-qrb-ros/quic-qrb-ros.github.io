# Makefile for Sphinx documentation

.PHONY: help clean html

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean    to clean the built documentation"
	@echo "  html     to build the HTML documentation"

clean:
	rm -rf build

html:
	sphinx-multiversion source build/html