from flask import Flask,render_template,url_for,send_from_directory
import mdtex2html
import os
import re

app = Flask(__name__)

disallow=[r'.*(main\.py)',
          r'.*/?(Main\.md)',
          r'.*(requirements\.txt)',
          r'.*(_config\.yml)',
          r'.*(\.note)/?.*',
          r'.*(\.venv)/?.*',
          r'.*(\.git)/?.*',
          r'.*(__pycache__)/?.*',
          r'.*(_templates)/?.*',
          r'.*(templates)/?.*',
          r'.*(static)/?.*']

def validatePath(path: str):
    if any(re.match(ptr,path) for ptr in disallow):
        return False
    return True

@app.route('/')
def main():
    dir='./'
    paths={path: '/'+os.path.join(dir,path) for path in os.listdir(dir) if validatePath(path)}
    return render_template('List.html',paths=paths)

@app.route('/<path:dir>')
def note(dir):
    if not validatePath(dir):
        return 'Not Allowed'
    if os.path.isdir(dir):
        paths={path: '/'+os.path.join(dir,path) for path in os.listdir(dir) if validatePath(path)}
        return render_template('List.html',paths=paths)
    with open(dir,'r') as f:
        text=f.read()
    return mdtex2html.convert(text,extensions=['meta','tables'])

if __name__=="__main__":
    app.run(debug=True)
