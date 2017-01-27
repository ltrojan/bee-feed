import click
import flask

from bee_feed import utils
from bee_feed import urls


App = flask.Flask(__name__)


@App.route('/')
def home():
    return flask.render_template('home.html')


@App.route('/simple/')
@App.route('/simple/<num>')
def simple(num=None):
    data = list(utils.gen_feed(urls.URLS))[0]['entries']
    if num is not None:
        try:
            data = data[int(num)]
        except:
            data = "No item %s" % num
    return str(data)


@click.group()
@click.option('--debug', default=True)
@click.option('--threaded', default=True)
@click.pass_context
def cli(ctx, debug, threaded):
    ctx.obj['DEBUG'] = debug
    ctx.obj['THREADED'] = threaded
    return None


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
