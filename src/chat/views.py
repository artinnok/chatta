import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def add_message(request):
    return {'text': 'Hello, world!'}
