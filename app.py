import re 

from flask import Flask, render_template, redirect

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def landing():
    return render_template('landing.html', num_millisecs=0)

if __name__ == '__main__':
    app.run(debug=True)
    
    