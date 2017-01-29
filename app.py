import click
import flask

from bee_feed import utils
from bee_feed import urls


App = flask.Flask(__name__)


@App.route('/')
def home():
    return flask.render_template('home.html')


@App.route('/silly/')
def silly():
    return flask.render_template('silly.html')


@App.route('/feed/')
@App.route('/feed')
def feed(num=None):
    def ent_to_data(ent):
        return (ent['title'],
                ent['published'],
                flask.Markup(ent['summary']))
    data = list(utils.gen_feed(urls.URLS))[0]['entries']
    data = [ent_to_data(ent) for ent in data]
    if num is not None:
        try:
            data = data[int(num)]
        except:
            data = "No item %s" % num
    return flask.render_template('feed.html', data=data)


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
