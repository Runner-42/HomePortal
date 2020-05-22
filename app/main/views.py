from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('base.html')


@main.route('/domotica')
def domotica():
    return render_template('domotica.html')


@main.route('/kookboek')
def kookboek():
    return render_template('kookboek.html')


@main.route('/runner')
def runner():
    return render_template('runner.html')
