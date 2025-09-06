from flask import Blueprint

from flask import Flask, render_template, send_file
from libraries.md_util import *
from json import load as j_load
import os

##————————————————————————————————————————————————————————————————————————————##

app_docs = Blueprint('docs', __name__)



config_file = "_config.json"

with open(config_file) as file:
    config = j_load(file)

pages_path = config["pages_path"]

##————————————————————————————————————————————————————————————————————————————##

def render_error(error_msg) -> str :
    return f'<h1>Error</h1><p>{str(error_msg)}</p>'

##————————————————————————————————————————————————————————————————————————————##

@app_docs.route('/<path:filename>')
def web_markdown(filename:str) -> str:

    titlename = f' – {filename}'
    if filename.endswith('.md'):
        filenickname, _ = os.path.splitext(os.path.basename(filename))
        titlename = f' – {filenickname}'
        

    sPath = path.join(pages_path, filename)
    text_file_extensions = [
        '.py', '.sh', '.html', '.css', '.js', '.json', '.txt', 
        ]

    if (not path.isfile(sPath)):
        err = '404 Not Found'
        return render_template(
            'docs_page.html', 
            py_md=render_error(err), py_title=f' – {err}')

    if (not filename.endswith('.md')):
        if not any(filename.endswith(ext) for ext in text_file_extensions):
            return send_file(sPath)  # utile pour les images et les pdf

    try:
        with open(sPath, 'r', encoding='utf-8') as file:
            data = file.read()
    except Exception as e:
        return render_template('docs_page.html', py_md=render_error(e))

    for extension in text_file_extensions:
        if filename.endswith(extension):
            return render_template(
                'docs_page.html', py_md=f'<pre>{data}</pre>'
                )

    data = convert_https_links(data)
    data = convert_strikethrough_text(data)
    data = convert_highlighted_text(data)

    html_data = md_to_html(data)

    return render_template('docs_page.html', 
        py_md=html_data, py_title=titlename)



@app_docs.route('/')
def web_root() -> str:
    return web_markdown('Bienvenue.md')


