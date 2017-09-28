import os

from aiohttp import web
import trafaret as T
from trafaret_config import read_and_validate


TRAFARET = T.Dict({
    T.Key('host'): T.IP,
    T.Key('port'): T.Int()
})


async def index(request):
    text = 'Hello, world!'

    return web.Response(text=text)


if __name__ == '__main__':
    path = os.getcwd()
    config = read_and_validate(path + '/config.yml', TRAFARET)

    app = web.Application()
    app['config'] = config
    app.router.add_get('/', index)

    web.run_app(
        app=app,
        host=app['config']['host'],
        port=app['config']['port'],
    )
