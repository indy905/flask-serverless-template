import os

from application import create_app

env = os.getenv('CONFIG') or 'dev'
app = create_app(env)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['WTF_CSRF_ENABLED'] = False


if __name__ == '__main__':
    app.run()
