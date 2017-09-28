from aiohttp import web


async def index(request):
    text = 'Hello, world!'

    return web.Response(text=text)


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', index)

    web.run_app(app, port=7777)
