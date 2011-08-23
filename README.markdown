Miniscule
=========

Miniscule is yet another static website generator. It focuses on doing the _bare_ minimum that could possibly get a running website going.

Miniscule uses Markdown and Jinja2.

Miniscule is working well, but has not had extensive testing. 

Requirements
============

Miniscule uses [Jinja2](http://jinja.pocoo.org/) and [Markdown](http://www.freewisdom.org/projects/python-markdown/).

Instructions
============

Miniscule is self contained in the file miniscule.py.

Running Miniscule is as easy as copying miniscule.py to your project directory and running 

    python miniscule.py

This will run Miniscule against the current working directory.

You can also supply a single command line argument to Miniscule containing the path to your project.

Miniscule Projects
==================

Miniscule prefers implicit rather than explicit. A project in Miniscule is simply a directory with a certain folder structure.

    ProjectDir/
    -> website/
    -> templates/
    --> css/
    --> template.html
    -> output/

You can view a sample project [here](http://www.github.com/adammacleod/adam.macleod.id.au/)

website/
--------

Contains your website contents. All files should be in the form source.md. Any number of directories and subdirectories are permitted in this folder, they will all be copied to the output directory.

templates/
----------

The templates directory should contain a set of Jinja2 templates in the form template.html.

templates/css/
--------------

The css directory is copied file for file into output/css/.

output/
-------

The output directory contains the compiled website. **WARNING** all files in this directory will be deleted without any notice.

This directory will be created if it does not exist. It is recommended that you do not check this directory into version control if you are using it.
