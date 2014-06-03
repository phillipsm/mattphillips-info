from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def landing():
    return render_template('landing.html')
    
@app.route('/ambient-timer')
def projects_ambient_timer():
    return render_template('projects/ambient-timer.html', project_title="Ambient Timer")
    
@app.route('/awesome-box')
def projects_awesome_box():
    return render_template('projects/awesome-box.html', project_title="Awesome Box")

@app.route('/hovermarks')
def projects_hovermarks():
    return render_template('projects/hovermarks.html', project_title="Hovermarks")

if __name__ == '__main__':
    app.run(debug=True)
    
    