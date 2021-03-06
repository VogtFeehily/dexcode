# coding=utf-8
import os
from app import db, create_app
from app.models import User, Category, Post, Label, Comment, LikePost, LikeComment, DislikeComment
from flask_script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Category=Category, Post=Post, Label=Label, Comment=Comment,
                LikePost=LikePost, LikeComment=LikeComment, DislikeComment=DislikeComment)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()






