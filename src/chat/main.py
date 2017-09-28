import jinja2
import aiohttp_jinja2
import aiohttp_debugtoolbar
from aiohttp import web

from chat.routes import setup_routes
from config.bootstrap import get_config


def setup_third_party(app):
    aiohttp_debugtoolbar.setup(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(config['base_path'] + '/templates'))


if __name__ == '__main__':
    config = get_config()

    app = web.Application(
        middlewares=[aiohttp_debugtoolbar.toolbar_middleware_factory],
    )

    setup_third_party(app)
    setup_routes(app.router)

    web.run_app(
        app=app,
        host=config['host'],
        port=config['port'],
    )
