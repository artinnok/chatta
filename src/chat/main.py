import os

import aiohttp
import trafaret as T
from aiohttp import web
from trafaret_config import read_and_validate


TRAFARET = T.Dict({
    T.Key('host'): T.IP,
    T.Key('port'): T.Int()
})


async def websocket_chat(request):
    ws = web.WebSocketResponse()

    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()

            else:
                await ws.send_str(msg.data + '/answer')

        else:
            print(ws.exception())

    return ws


if __name__ == '__main__':
    path = os.getcwd()
    config = read_and_validate(path + '/config.yml', TRAFARET)

    app = web.Application()
    app.router.add_get('/', websocket_chat)

    web.run_app(
        app=app,
        host=config['host'],
        port=config['port'],
    )
