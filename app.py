import feedparser

import click
from flask import Flask

from bee_feed.urls import URLS


App = Flask(__name__)


def gen_feed(urls):
    for url in urls:
        yield feedparser.parse(url)


@App.route('/simple/')
def simple():
    return str(list(gen_feed(URLS)))


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
