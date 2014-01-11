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

You can view a sample project [here](http://www.github.com/adammacleod/adam.macleod.id.au/).

website/
--------

Contains your website contents. Any number of files, directories and subdirectories are permitted in this folder, they will all be copied to the output directory. Any files with a .md extension will be rendered to HTML.

Source md files should begin with a Title and Template, and then contain the body of the page seperated by a single return.

    Title: Post Title
    Template: templatename

    Contents of page should go here.

You can add any extra meta data you like to the opening section of the page. See the [Markdown Help](http://www.freewisdom.org/projects/python-markdown/Meta-Data) for more information about meta data.

templates/
----------

The templates directory should contain a set of Jinja2 templates in the form templatename.html.

templates/css/
--------------

The css directory is copied file for file into output/css/.

output/
-------

The output directory contains the compiled website. 

**WARNING** all files in this directory will be deleted without any notice.

This directory will be created if it does not exist. It is recommended that you do not check this directory into version control if you are using it.
