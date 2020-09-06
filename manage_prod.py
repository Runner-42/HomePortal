'''
Startup script HomePortal flask application
'''
#!/usr/bin/env python
import os
from flask_script import Manager, Shell
from home_portal import create_app

home_portal = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(home_portal)


def make_shell_context():
    '''
    Run in shell mode
    '''
    return dict(app=home_portal)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
