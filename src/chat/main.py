import os

import trafaret as T
from aiohttp import web
from trafaret_config import read_and_validate


TRAFARET = T.Dict({
    T.Key('host'): T.IP,
    T.Key('port'): T.Int()
})


async def add_message(request):
    return web.Response(text='Hello, world')


if __name__ == '__main__':
    path = os.getcwd()
    config = read_and_validate(path + '/config.yml', TRAFARET)

    app = web.Application()
    app.router.add_get('/add', add_message)

    web.run_app(
        app=app,
        host=config['host'],
        port=config['port'],
    )
