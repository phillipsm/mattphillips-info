from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def landing():
    return render_template('landing.html')
    
@app.route('/ambient-timer')
def projects_ambient_timer():
    return render_template('projects/ambient-timer.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    