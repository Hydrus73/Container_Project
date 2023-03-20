from flask import Flask
from flask import send_from_directory
from flask import send_file

app = Flask(__name__, static_folder='')


@app.route('/')
def index():
  return send_from_directory('html/', 'index.html')

@app.route('/path/<file>/<path:path>')
def path(file, path):
  print(path+file)
  return send_from_directory(path, file)

@app.route('/file/<path:path>')
def img(path):
  return send_file(path, mimetype='image')

@app.route('/js/')
def js():
  return send_file('/html/node_modules/chess.js/src/chess.ts')

app.run(host="0.0.0.0",port=80)