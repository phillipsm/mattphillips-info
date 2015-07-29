from flask import Flask, redirect, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/resume')
def resume():
    return redirect('/static/docs/resume.pdf', code=301)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/ambient-timer')
def projects_ambient_timer():
    return render_template('projects/ambient-timer.html', project_title="Ambient Timer")
    
@app.route('/awesome-box')
def projects_awesome_box():
    return render_template('projects/awesome-box.html', project_title="Awesome Box")

@app.route('/hovermarks')
def projects_hovermarks():
    return render_template('projects/hovermarks.html', project_title="Hovermarks")

@app.route('/working-in-widener')
def projects_working_in_widener():
    return render_template('projects/working-in-widener.html', project_title="Working in Widener")

@app.route('/pyfav')
def projects_pyfav():
    return render_template('projects/pyfav.html', project_title="Pyfav")

@app.route('/thelibrary-fm')
def projects_thelibrary_fm():
    return render_template('projects/thelibrary-fm.html', project_title="thelibrary.fm")

@app.route('/360')
def projects_360():
    return render_template('projects/360.html', project_title="360 Portrait")

@app.route('/360/hand')
def projects_360_hand():
    return render_template('projects/360-hand.html')
    
@app.route('/frames')
def projects_frames():
    return render_template('projects/frames.html', project_title="Frames")

@app.route('/stereo-cam')
def projects_stereo():
    return render_template('projects/stereo-cam.html', project_title="Stereo Camera")

if __name__ == '__main__':
    app.run(debug=False)
    
    
