from flask import Blueprint
from flask import render_template

# Blueprint Configuration
runner_bp = Blueprint('runner_bp', __name__,
                      template_folder='templates', static_folder='static')


@runner_bp.route('/')
def runner():
    '''homepage'''
    status = "Under construction"
    return render_template('runner/runner.html', runner_site_status=status)
