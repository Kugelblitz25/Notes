from flask import Flask,render_template,url_for,send_from_directory
import mdtex2html
import os
import re

app = Flask(__name__)

disallow=[r'.*main.py',r'.*/Main.md',]

@app.route('/')
def main():
    return "Welcome"

@app.route('/<path:dir>')
def note(dir):
    if any(re.match(ptr,dir) for ptr in disallow):
        return 'Not Allowed'
    if os.path.isdir(dir):
        paths=os.listdir(dir)
        if 'Main.md' in paths: paths.remove('Main.md')
        if 'attachments' in paths: paths.remove('attachments')
        paths={path: '/'+os.path.join(dir,path) for path in paths}
        return render_template('List.html',paths=paths)
    with open(dir,'r') as f:
        text=f.read()
    return mdtex2html.convert(text,extensions=['meta'])

if __name__=="__main__":
    app.run(debug=True)
