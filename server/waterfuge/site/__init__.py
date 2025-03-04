from flask import Blueprint, redirect, render_template, request, url_for

from ..database.db import Sensor

site = Blueprint('site', __name__, template_folder='templates',
                 static_folder='static')


@site.context_processor
def inject_dark():
    dark = request.args.get('dark', "False").lower() in ["true", "1"]
    return dict(dark=dark)


@site.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        try:
            s = Sensor.get_via_id(int(request.form['id']))
            s.set_name(request.form['name'])
        except Exception as e:
            pass
        return redirect(url_for('.index'))

    return render_template('index.html')


@site.get('/overview')
def overview():
    return render_template('overview.html')
