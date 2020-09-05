#!/usr/bin/env python
import os
from flask_script import Manager, Shell
from home_portal import create_app

homeportal = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(homeportal)


def make_shell_context():
    return dict(app=homeportal)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
