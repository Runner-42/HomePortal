from flask import Blueprint
from flask import render_template

# Blueprint Configuration
domotica_bp = Blueprint('domotica_bp', __name__,
                        template_folder='templates', static_folder='static')


@domotica_bp.route('/')
def domotica():
    '''homepage'''
    status = "Under construction"
    return render_template('domotica/domotica.html', domotica_site_status=status)
