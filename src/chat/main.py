import jinja2
import aiohttp_jinja2
import aiohttp_debugtoolbar
from aiohttp import web

from bootstrap import get_config


@aiohttp_jinja2.template('index.html')
async def add_message(request):
    return {'text': 'Hello, world!'}


if __name__ == '__main__':
    config = get_config()

    # инициализация приложения
    app = web.Application(middlewares=[aiohttp_debugtoolbar.toolbar_middleware_factory])
    aiohttp_debugtoolbar.setup(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(config['base_path'] + '/templates'))

    # роутинг
    app.router.add_get('/add', add_message)
    app.router.add_static('/static', config['base_path'] + '/static')

    web.run_app(
        app=app,
        host=config['host'],
        port=config['port'],
    )
