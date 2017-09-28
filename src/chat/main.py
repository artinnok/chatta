import jinja2
import aiohttp_jinja2
import aiohttp_debugtoolbar
from aiohttp import web

from config.bootstrap import get_config
from chat.routes import set_routes


def setup(app):
    aiohttp_debugtoolbar.setup(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(config['base_path'] + '/templates'))


if __name__ == '__main__':
    config = get_config()

    app = web.Application(
        middlewares=[aiohttp_debugtoolbar.toolbar_middleware_factory],
    )

    set_routes(app.router)

    web.run_app(
        app=app,
        host=config['host'],
        port=config['port'],
    )
