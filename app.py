from contextlib import closing
import click
import flask

import app_conf
from bee_feed import utils
from bee_feed import sql_utils


App = flask.Flask(__name__)
App.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@App.before_request
def before_request():
    flask.g.db = sql_utils.connect_db(app_conf.URL_DB)


@App.teardown_request
def teardown_request(exception):
    db = getattr(flask.g, 'db', None)
    if db is not None:
        db.close()


@App.route('/')
def home():
    return flask.render_template('home.html')


@App.route('/feed/')
def feed(num=None):

    def ent_to_data(ent):
        return (str(ent.title),
                str(ent.date),
                flask.Markup(ent.text))

    data = [ent_to_data(ent)
            for ent in utils.get_entries(
                    db=getattr(flask.g, 'db', None),
                    named_urls=app_conf.Named_Urls)]

    return flask.render_template('feed.html', data=data)


@App.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if 'logged_in' in flask.session and 'username' in flask.session:
        if flask.session['logged_in']:
            flask.flash('You are logged in!')
            return flask.redirect(flask.url_for('feed'))
    if flask.request.method == 'POST':

        if flask.request.form['username'] != 'ltrojan':      # App.config['USERNAME']:
            error = 'Invalid username'
        elif flask.request.form['password'] != 'test1234':   # App.config['PASSWORD']:
            error = 'Invalid password'
        else:
            flask.session['logged_in'] = True
            flask.session['username'] = 'ltrojan'
            flask.flash('You were logged in')
            return flask.redirect(flask.url_for('feed'))
    return flask.render_template('login.html', error=error)


@App.route('/logout')
def logout():
    flask.session.pop('logged_in', None)
    flask.session.pop('username', None)
    flask.flash('You were logged out')
    return flask.redirect(flask.url_for('feed'))


@click.group()
@click.option('--debug', default=True)
@click.option('--threaded', default=True)
@click.option('--url_db', default=app_conf.URL_DB)
@click.pass_context
def cli(ctx, debug, threaded, url_db):
    ctx.obj['DEBUG'] = debug
    ctx.obj['THREADED'] = threaded
    ctx.obj['URL_DB'] = url_db
    return None


@cli.command()
@click.pass_context
def init_db(ctx):
    with closing(sql_utils.connect_db(ctx.obj['URL_DB'])) as db:
        sql_utils.init_db(db)


@cli.command()
@click.option('--host', default='0.0.0.0')
@click.pass_context
def runserver(ctx, host):
    App.run(
        host=host,
        debug=ctx.obj['DEBUG'],
        threaded=ctx.obj['THREADED'])
    return None


if __name__ == '__main__':
    cli(obj={})
