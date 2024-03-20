from flask import flask

app = Flask(__name__)

@app.route('/')

def hello_geek():
  return '<h1>Alex</h1>'


if __name__="__main__":
  app.run(debug=True)


    
