import os, sys, shutil, markdown
from jinja2 import Environment, FileSystemLoader

def process_dir(dir):
    for item in os.listdir(dir):
        full_path = os.path.join(dir, item)
        
        if os.path.isfile(full_path):
            process_file(dir, item)
        elif os.path.isdir(full_path):
            process_dir(full_path)
            
def process_file(dir, file):
    [filename, file_ext] = os.path.splitext(file)
    if file_ext != '.md':
        return

    with open(os.path.join(dir, file), 'r') as f:
        page = f.read()
    
    output = render(page)

    write_file(dir, filename, output)

def render(page):
    html = md.convert(page)
    
    template = env.get_template(md.Meta["template"][0] + ".html")
    output = template.render(content = html, meta = md.Meta)

    md.reset() #Clears meta data
    
    return output

def write_file(source_dir, filename, contents):
    output_path = os.path.normpath(
                               os.path.join(
                                        output_dir,
                                        os.path.relpath(source_dir, website_dir)))
                                        
    output_file = os.path.join(output_path, filename + '.html')
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
                    
    with open(output_file, 'w') as f:
        f.write(contents)            

def copy_css_to_output():
    if os.path.exists(css_dir):
        shutil.copytree(css_dir, os.path.join(output_dir, 'css'))

if __name__ == '__main__':
    project_dir = '.'    
    if len(sys.argv) > 1:
        project_dir = os.path.normpath(sys.argv[1])
    
    website_dir = os.path.abspath(os.path.join(project_dir, 'website'))
    output_dir = os.path.join(website_dir, '../output')
    template_dir = os.path.join(website_dir, '../templates')
    css_dir = os.path.join(template_dir, 'css')
    
    shutil.rmtree(output_dir, True)
    
    env = Environment(loader=FileSystemLoader(template_dir))

    md = markdown.Markdown(
        extensions=['meta'], 
        output_format='html4'
    )
    
    process_dir(website_dir)
    
    copy_css_to_output()