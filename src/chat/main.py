import os

import trafaret as T
from aiohttp import web
import aiohttp_jinja2
import aiohttp_debugtoolbar
import jinja2
from trafaret_config import read_and_validate


# конфиг
TRAFARET = T.Dict({
    T.Key('host'): T.IP,
    T.Key('port'): T.Int(),
})


@aiohttp_jinja2.template('index.html')
async def add_message(request):
    return {'text': 'Hello, world!'}


if __name__ == '__main__':
    # конфиг
    BASE_PATH = os.getcwd()
    config = read_and_validate(BASE_PATH + '/config.yml', TRAFARET)

    # инициализация приложения
    app = web.Application(middlewares=[aiohttp_debugtoolbar.toolbar_middleware_factory])
    aiohttp_debugtoolbar.setup(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(BASE_PATH + '/templates'))

    # роутинг
    app.router.add_get('/add', add_message)
    app.router.add_static('/static', BASE_PATH + '/static')

    web.run_app(
        app=app,
        host=config['host'],
        port=config['port'],
    )
