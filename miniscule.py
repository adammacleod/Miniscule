import os, sys, shutil, markdown
from jinja2 import Environment, FileSystemLoader

"""Miniscule is a static website generator that makes YOU do all of the work.

It is designed to be as simple as possible.

This project is available at http://www.github.com/adammacleod/Miniscule
"""

def init_constants():
    """Initializes the location of directories used through the remainder of
    the project.
    """
    global PROJECT_DIR, WEBSITE_DIR, OUTPUT_DIR, TEMPLATE_DIR, CSS_DIR
    
    PROJECT_DIR = '.'
    if len(sys.argv) > 1:
        PROJECT_DIR = os.path.normpath(sys.argv[1])

    WEBSITE_DIR = os.path.abspath(os.path.join(PROJECT_DIR, 'website'))
    OUTPUT_DIR = os.path.join(WEBSITE_DIR, '../output')
    TEMPLATE_DIR = os.path.join(WEBSITE_DIR, '../templates')
    CSS_DIR = os.path.join(TEMPLATE_DIR, 'css')

def init_libs():
    """Initializes the Jinja and Markdown libraries."""
    global JINJA_ENV, MARKDOWN
    
    JINJA_ENV = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    MARKDOWN = markdown.Markdown(
        extensions=['meta'], 
        output_format='html4'
    )
    
def process_dir(dir):
    """Recursively searches the website directory for files to process.
    
    Keyword arguments:
    dir -- The first call will be the website directory. 
           Subsequent calls will be the children of previous calls.
    """
    for item in os.listdir(dir):
        full_path = os.path.join(dir, item)
        
        if os.path.isfile(full_path):
            process_file(dir, item)
        elif os.path.isdir(full_path):
            process_dir(full_path)
            
def process_file(dir, file):
    """Reads file from dir, renders it and then writes to the output directory.
    
    Keyword arguments:
    dir -- Directory where file exists.
    file -- Full filename of the file (eg. index.md)
    """
    [filename, file_ext] = os.path.splitext(file)
    if file_ext != '.md':
        return

    with open(os.path.join(dir, file), 'r') as f:
        page = f.read()
    
    output = render(page)

    write_file(dir, filename, output)

def render(page):
    """Renders markdown source into a html format.
    The source is first run through the markdown parser, and then fed into the
    Jinja2 template engine.
    
    Keyword arguments:
    page -- A string containing the markdown source.
    """
    html = MARKDOWN.convert(page)
    
    template = JINJA_ENV.get_template(MARKDOWN.Meta["template"][0] + ".html")
    output = template.render(content = html, meta = MARKDOWN.Meta)

    MARKDOWN.reset() # Clears meta data
    
    return output

def write_file(source_dir, filename, contents):
    """Writes contents into filename.
    
    Keyword arguments:
    source_dir -- The source directory of the original file. This directory
                  will have the website source directory stripped and the
                  output directory prepended.
    filename -- The name of the file to write into. .html is appended to this
                value.
    contents -- The contents of the file to write.
    """
    # rel_path is the position of the file relative to the source website root
    #   This is needed to determine where to write the output file.
    rel_path = os.path.relpath(source_dir, WEBSITE_DIR)
    output_path = os.path.join(OUTPUT_DIR, rel_path)
                                        
    output_file = os.path.join(output_path, filename + '.html')
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
                    
    with open(output_file, 'w') as f:
        f.write(contents)            

def copy_css():
    """Searches for CSS_DIR and copies it into the OUTPUT_DIR/css if it exists.
    """
    if os.path.exists(CSS_DIR):
        shutil.copytree(CSS_DIR, os.path.join(OUTPUT_DIR, 'css'))

if __name__ == '__main__':
    init_constants()
    
    init_libs()
    
    # Clear the output directory.
    shutil.rmtree(OUTPUT_DIR, True)
     
    process_dir(WEBSITE_DIR)
    
    copy_css()