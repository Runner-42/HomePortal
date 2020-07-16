#!/usr/bin/env python
import os
import pytest
from flask_script import Manager, Shell
from home_portal import create_app

home_portal = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(home_portal)


@manager.command
def test():
    pytest.main(["", "/home/pi/Projects/HomePortal"])


def make_shell_context():
    return dict(app=home_portal)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
