import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('index.html')
async def show_message(request):
    return {'text': 'Hello, world!'}


async def add_message(request):
    result = await request.post()

    return web.json_response({
        'ok': True,
    })
